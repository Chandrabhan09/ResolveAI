import json
from pathlib import Path

# =========================================================
# KNOWLEDGE BASE CONFIGURATION
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

KNOWLEDGE_BASE_PATH = (
    BASE_DIR / "data" / "knowledge_base.json"
)


# =========================================================
# KNOWLEDGE BASE ERROR
# =========================================================

class KnowledgeBaseError(Exception):
    """Controlled knowledge-base error."""



# =========================================================
# LOAD KNOWLEDGE BASE
# =========================================================

def load_knowledge_base():
    """
    Load and validate the ResolveAI knowledge base.
    """

    if not KNOWLEDGE_BASE_PATH.exists():
        raise KnowledgeBaseError(
            "Knowledge-base file was not found."
        )

    try:

        with open(
            KNOWLEDGE_BASE_PATH,
            "r",
            encoding="utf-8",
        ) as file:

            data = json.load(file)

    except json.JSONDecodeError as exc:

        raise KnowledgeBaseError(
            "Knowledge-base JSON is invalid."
        ) from exc

    except OSError as exc:

        raise KnowledgeBaseError(
            "Knowledge base could not be read."
        ) from exc


    # -----------------------------------------------------
    # VALIDATE ROOT STRUCTURE
    # -----------------------------------------------------

    if not isinstance(data, dict):
        raise KnowledgeBaseError(
            "Knowledge base must contain a JSON object."
        )

    if "company" not in data:
        raise KnowledgeBaseError(
            "Knowledge base is missing company information."
        )

    if "policies" not in data:
        raise KnowledgeBaseError(
            "Knowledge base is missing policies."
        )


    policies = data["policies"]

    if not isinstance(policies, list):
        raise KnowledgeBaseError(
            "Policies must be stored as a list."
        )


    # -----------------------------------------------------
    # VALIDATE EACH POLICY
    # -----------------------------------------------------

    required_fields = {
        "id",
        "category",
        "title",
        "keywords",
        "content",
    }


    for policy in policies:

        if not isinstance(policy, dict):
            raise KnowledgeBaseError(
                "Every policy must be an object."
            )

        missing_fields = (
            required_fields - policy.keys()
        )

        if missing_fields:
            raise KnowledgeBaseError(
                "Policy is missing required fields: "
                + ", ".join(sorted(missing_fields))
            )

        if not isinstance(
            policy["keywords"],
            list,
        ):
            raise KnowledgeBaseError(
                f"Policy '{policy['id']}' "
                "has invalid keywords."
            )


    return data

# =========================================================
# KNOWLEDGE BASE HELPERS
# =========================================================

def get_company():
    """Return company information."""

    knowledge_base = load_knowledge_base()

    return knowledge_base["company"]


def get_policies():
    """Return all verified support policies."""

    knowledge_base = load_knowledge_base()

    return knowledge_base["policies"]


def get_policy_by_id(policy_id):
    """Return a policy matching the supplied ID."""

    if not isinstance(policy_id, str):
        return None

    for policy in get_policies():

        if policy["id"] == policy_id:
            return policy

    return None

# =========================================================
# SHARED RETRIEVAL SCORING ENGINE
# =========================================================

SUPPORT_INTENT_PHRASES = (
    "i want",
    "i need",
    "i have",
    "help with",
    "problem with",
    "issue with",
    "having trouble",
    "cannot",
    "can't",
    "unable to",
)


def _confidence_from_score(score):
    """Convert a retrieval score into confidence."""

    if score >= 3:
        return "strong"

    if score == 2:
        return "moderate"

    if score == 1:
        return "weak"

    return "none"


def _score_policy(user_message, policy):
    """
    Score one verified policy against a customer message.

    Single-word keyword = 1 point.
    Multi-word keyword = 2 points.
    Explicit support intent + existing keyword evidence = +1.

    The support-intent bonus is applied at most once and
    cannot create a policy match without keyword evidence.
    """

    empty_result = {
        "score": 0,
        "confidence": "none",
        "matched_keywords": [],
        "matched_keyword_count": 0,
        "intent_bonus": 0,
    }

    if not isinstance(user_message, str):
        return empty_result

    if not isinstance(policy, dict):
        return empty_result

    cleaned_message = user_message.lower().strip()

    if not cleaned_message:
        return empty_result

    score = 0
    matched_keywords = []

    for keyword in policy.get("keywords", []):
        cleaned_keyword = str(keyword).lower().strip()

        if not cleaned_keyword:
            continue

        if cleaned_keyword in cleaned_message:
            weight = 2 if " " in cleaned_keyword else 1
            score += weight

            matched_keywords.append(
                {
                    "keyword": str(keyword),
                    "weight": weight,
                }
            )

    intent_bonus = 0

    if matched_keywords and any(
        phrase in cleaned_message
        for phrase in SUPPORT_INTENT_PHRASES
    ):
        intent_bonus = 1
        score += intent_bonus

    return {
        "score": score,
        "confidence": _confidence_from_score(score),
        "matched_keywords": matched_keywords,
        "matched_keyword_count": len(matched_keywords),
        "intent_bonus": intent_bonus,
    }


# =========================================================
# KNOWLEDGE RETRIEVAL
# =========================================================

def find_relevant_policy(user_message):
    """
    Find the most relevant policy using keyword matching.

    Returns the best matching policy or None.
    """

    if not isinstance(user_message, str):
        return None

    cleaned_message = user_message.lower().strip()

    if not cleaned_message:
        return None

    best_policy = None
    best_score = 0

    for policy in get_policies():

        score = 0

        for keyword in policy["keywords"]:

            keyword = keyword.lower().strip()

            if keyword and keyword in cleaned_message:
                score += 1

        if score > best_score:
            best_score = score
            best_policy = policy

    return best_policy

# =========================================================
# KNOWLEDGE RELEVANCE SCORING
# =========================================================

def retrieve_policy_with_confidence(user_message):
    """
    Retrieve the highest-scoring verified policy using
    the shared ResolveAI retrieval scoring engine.
    """

    if not isinstance(user_message, str):
        return {
            "policy": None,
            "score": 0,
            "confidence": "none",
        }

    cleaned_message = user_message.lower().strip()

    if not cleaned_message:
        return {
            "policy": None,
            "score": 0,
            "confidence": "none",
        }

    best_policy = None
    best_score = 0
    best_confidence = "none"

    for policy in get_policies():
        scoring = _score_policy(cleaned_message, policy)
        score = scoring["score"]

        if score > best_score:
            best_score = score
            best_policy = policy
            best_confidence = scoring["confidence"]

    return {
        "policy": best_policy,
        "score": best_score,
        "confidence": best_confidence,
    }

# =========================================================
# KNOWLEDGE RETRIEVAL DIAGNOSTICS
# =========================================================

def get_retrieval_diagnostics(
    user_message,
    policy,
):
    """
    Explain exactly how the shared retrieval scorer
    evaluated a policy.
    """

    scoring = _score_policy(
        user_message,
        policy,
    )

    return {
        "matched_keywords": scoring["matched_keywords"],
        "matched_keyword_count": scoring[
            "matched_keyword_count"
        ],
        "intent_bonus": scoring["intent_bonus"],
        "calculated_score": scoring["score"],
        "confidence": scoring["confidence"],
    }

# =========================================================
# KNOWLEDGE HEALTH ANALYTICS
# =========================================================

def generate_knowledge_health():
    """
    Generate measurable health and coverage information
    from the real ResolveAI knowledge base.
    """

    policies = get_policies()

    if not policies:
        return {
            "total_policies": 0,
            "total_categories": 0,
            "total_keywords": 0,
            "average_keywords": 0.0,
            "category_distribution": {},
            "low_keyword_policies": [],
            "duplicate_keywords": {},
        }

    category_distribution = {}

    total_keywords = 0

    keyword_usage = {}

    low_keyword_policies = []

    # -----------------------------------------------------
    # ANALYZE POLICIES
    # -----------------------------------------------------

    for policy in policies:

        category = str(
            policy.get(
                "category",
                "Unknown",
            )
        ).strip()

        category_distribution[
            category
        ] = (
            category_distribution.get(
                category,
                0,
            )
            + 1
        )

        keywords = policy.get(
            "keywords",
            [],
        )

        clean_keywords = [
            str(keyword).strip()
            for keyword in keywords
            if str(keyword).strip()
        ]

        keyword_count = len(
            clean_keywords
        )

        total_keywords += keyword_count

        # ---------------------------------------------
        # FLAG LOW KEYWORD COVERAGE
        # ---------------------------------------------

        if keyword_count < 3:

            low_keyword_policies.append(
                {
                    "id": policy.get(
                        "id",
                        "Unknown",
                    ),
                    "title": policy.get(
                        "title",
                        "Unknown",
                    ),
                    "category": category,
                    "keyword_count": keyword_count,
                }
            )

        # ---------------------------------------------
        # TRACK KEYWORD USAGE
        # ---------------------------------------------

        for keyword in clean_keywords:

            normalized_keyword = (
                keyword.lower()
            )

            if normalized_keyword not in keyword_usage:

                keyword_usage[
                    normalized_keyword
                ] = []

            keyword_usage[
                normalized_keyword
            ].append(
                policy.get(
                    "id",
                    "Unknown",
                )
            )

    # -----------------------------------------------------
    # DUPLICATE / SHARED KEYWORDS
    # -----------------------------------------------------

    duplicate_keywords = {
        keyword: policy_ids
        for keyword, policy_ids
        in keyword_usage.items()
        if len(
            set(policy_ids)
        ) > 1
    }

    # -----------------------------------------------------
    # AVERAGE KEYWORD COVERAGE
    # -----------------------------------------------------

    average_keywords = (
        total_keywords / len(policies)
        if policies
        else 0.0
    )

    return {
        "total_policies": len(
            policies
        ),
        "total_categories": len(
            category_distribution
        ),
        "total_keywords": total_keywords,
        "average_keywords": average_keywords,
        "category_distribution": (
            category_distribution
        ),
        "low_keyword_policies": (
            low_keyword_policies
        ),
        "duplicate_keywords": (
            duplicate_keywords
        ),
    }

# =========================================================
# RETRIEVAL CANDIDATE & CONFLICT ENGINE
# =========================================================

def analyze_retrieval_candidates(user_message):
    """
    Analyze a customer message against every verified
    policy in the ResolveAI knowledge base.

    The function uses the shared production scoring rules:

    Single-word keyword = 1 point
    Multi-word phrase   = 2 points
    Explicit support intent with keyword evidence = +1 point

    It returns ranked policy candidates together with
    ambiguity and conflict information.

    The candidate engine and production retriever therefore
    remain score-consistent.
    """

    # -----------------------------------------------------
    # VALIDATE MESSAGE
    # -----------------------------------------------------

    if not isinstance(user_message, str):

        return {
            "candidates": [],
            "best_candidate": None,
            "competing_candidates": [],
            "ambiguous": False,
            "conflict_type": "none",
            "score_gap": None,
        }

    cleaned_message = (
        user_message
        .lower()
        .strip()
    )

    if not cleaned_message:

        return {
            "candidates": [],
            "best_candidate": None,
            "competing_candidates": [],
            "ambiguous": False,
            "conflict_type": "none",
            "score_gap": None,
        }

    # -----------------------------------------------------
    # LOAD VERIFIED POLICIES
    # -----------------------------------------------------

    policies = get_policies()

    candidates = []

    # -----------------------------------------------------
    # SCORE EVERY POLICY
    # -----------------------------------------------------

    for policy in policies:
        scoring = _score_policy(
            cleaned_message,
            policy,
        )

        score = scoring["score"]

        # -------------------------------------------------
        # IGNORE ZERO-SCORE POLICIES
        # -------------------------------------------------

        if score == 0:
            continue

        candidates.append(
            {
                "policy": policy,
                "policy_id": policy.get("id"),
                "title": policy.get("title"),
                "category": policy.get("category"),
                "score": score,
                "confidence": scoring["confidence"],
                "matched_keywords": scoring[
                    "matched_keywords"
                ],
                "matched_keyword_count": scoring[
                    "matched_keyword_count"
                ],
                "intent_bonus": scoring["intent_bonus"],
            }
        )

    # -----------------------------------------------------
    # NO MATCH
    # -----------------------------------------------------

    if not candidates:

        return {
            "candidates": [],
            "best_candidate": None,
            "competing_candidates": [],
            "ambiguous": False,
            "conflict_type": "none",
            "score_gap": None,
        }

    # -----------------------------------------------------
    # RANK CANDIDATES
    # -----------------------------------------------------

    candidates.sort(
        key=lambda candidate: (
            candidate["score"],
            candidate[
                "matched_keyword_count"
            ],
        ),
        reverse=True,
    )

    best_candidate = candidates[0]

    # -----------------------------------------------------
    # FIND COMPETING CANDIDATES
    # -----------------------------------------------------

    competing_candidates = []

    best_score = best_candidate[
        "score"
    ]

    for candidate in candidates[1:]:

        score_gap = (
            best_score
            - candidate["score"]
        )

        # A candidate is considered competitive when:
        #
        # 1. It ties the best score, OR
        # 2. It is only one point behind AND has at least
        #    moderate confidence.
        #
        # Weak candidates are therefore not treated as
        # serious competitors merely because they matched
        # one generic keyword.

        is_competing = (
            score_gap == 0
            or (
                score_gap == 1
                and candidate[
                    "confidence"
                ]
                in {
                    "strong",
                    "moderate",
                }
            )
        )

        if is_competing:

            competing_candidates.append(
                candidate
            )

    # -----------------------------------------------------
    # DETERMINE AMBIGUITY
    # -----------------------------------------------------

    ambiguous = bool(
        competing_candidates
    )

    # -----------------------------------------------------
    # DETERMINE CONFLICT TYPE
    # -----------------------------------------------------

    conflict_type = "none"

    score_gap = None

    if len(candidates) > 1:

        second_candidate = candidates[1]

        score_gap = (
            best_candidate["score"]
            - second_candidate["score"]
        )

        if (
            second_candidate["score"]
            == best_candidate["score"]
        ):

            conflict_type = "tie"

        elif competing_candidates:

            conflict_type = (
                "close_match"
            )

        else:

            conflict_type = (
                "clear_winner"
            )

    # -----------------------------------------------------
    # RETURN ANALYSIS
    # -----------------------------------------------------

    return {
        "candidates": candidates,
        "best_candidate": best_candidate,
        "competing_candidates": (
            competing_candidates
        ),
        "ambiguous": ambiguous,
        "conflict_type": conflict_type,
        "score_gap": score_gap,
    }
# =========================================================
# RETRIEVAL DECISION TRACE
# =========================================================

def build_retrieval_decision_trace(user_message):
    """
    Build an explainable trace of ResolveAI's knowledge
    retrieval decision.

    This function performs no AI/API calls. It uses the
    deterministic local retrieval engine only.
    """

    empty_trace = {
        "message": "",
        "selected_policy": None,
        "score": 0,
        "confidence": "none",
        "matched_keywords": [],
        "matched_keyword_count": 0,
        "intent_bonus": 0,
        "ambiguous": False,
        "conflict_type": "none",
        "score_gap": None,
        "competing_policies": [],
        "verified_eligible": False,
        "decision": "no_match",
        "decision_reason": (
            "No usable customer message was provided."
        ),
    }

    # -----------------------------------------------------
    # VALIDATE INPUT
    # -----------------------------------------------------

    if not isinstance(user_message, str):
        return empty_trace

    cleaned_message = user_message.strip()

    if not cleaned_message:
        return empty_trace

    # -----------------------------------------------------
    # PRIMARY RETRIEVAL
    # -----------------------------------------------------

    retrieval = retrieve_policy_with_confidence(
        cleaned_message
    )

    policy = retrieval.get(
        "policy"
    )

    score = retrieval.get(
        "score",
        0,
    )

    confidence = retrieval.get(
        "confidence",
        "none",
    )

    # -----------------------------------------------------
    # CANDIDATE / CONFLICT ANALYSIS
    # -----------------------------------------------------

    candidate_analysis = (
        analyze_retrieval_candidates(
            cleaned_message
        )
    )

    ambiguous = candidate_analysis.get(
        "ambiguous",
        False,
    )

    conflict_type = candidate_analysis.get(
        "conflict_type",
        "none",
    )

    score_gap = candidate_analysis.get(
        "score_gap"
    )

    # -----------------------------------------------------
    # PRIMARY POLICY DIAGNOSTICS
    # -----------------------------------------------------

    matched_keywords = []
    matched_keyword_count = 0
    intent_bonus = 0

    if policy is not None:

        diagnostics = (
            get_retrieval_diagnostics(
                cleaned_message,
                policy,
            )
        )

        matched_keywords = diagnostics.get(
            "matched_keywords",
            [],
        )

        matched_keyword_count = diagnostics.get(
            "matched_keyword_count",
            0,
        )

        intent_bonus = diagnostics.get(
            "intent_bonus",
            0,
        )

    # -----------------------------------------------------
    # COMPETING POLICIES
    # -----------------------------------------------------

    competing_policies = []

    for candidate in candidate_analysis.get(
        "competing_candidates",
        [],
    ):

        competing_policies.append(
            {
                "policy_id": candidate.get(
                    "policy_id"
                ),
                "title": candidate.get(
                    "title"
                ),
                "category": candidate.get(
                    "category"
                ),
                "score": candidate.get(
                    "score",
                    0,
                ),
                "confidence": candidate.get(
                    "confidence",
                    "none",
                ),
                "matched_keywords": candidate.get(
                    "matched_keywords",
                    [],
                ),
                "intent_bonus": candidate.get(
                    "intent_bonus",
                    0,
                ),
            }
        )

    # -----------------------------------------------------
    # VERIFIED KNOWLEDGE DECISION
    # -----------------------------------------------------

    verified_eligible = (
        policy is not None
        and confidence in {
            "strong",
            "moderate",
        }
        and not ambiguous
    )

    # -----------------------------------------------------
    # DECISION CLASSIFICATION
    # -----------------------------------------------------

    if policy is None:

        decision = "no_match"

        decision_reason = (
            "No verified support policy matched "
            "the customer message."
        )

    elif ambiguous:

        decision = "blocked_conflict"

        decision_reason = (
            "Multiple policies produced competing "
            "retrieval evidence. Verified policy use "
            "was blocked to prevent an ambiguous answer."
        )

    elif confidence == "weak":

        decision = "blocked_low_confidence"

        decision_reason = (
            "A policy matched, but retrieval confidence "
            "was too weak for verified knowledge use."
        )

    elif verified_eligible:

        decision = "verified_policy_selected"

        decision_reason = (
            "A clear policy matched with sufficient "
            "confidence and no retrieval conflict."
        )

    else:

        decision = "blocked"

        decision_reason = (
            "The retrieval result was not eligible "
            "for verified knowledge use."
        )

    # -----------------------------------------------------
    # SELECTED POLICY SUMMARY
    # -----------------------------------------------------

    selected_policy = None

    if policy is not None:

        selected_policy = {
            "policy_id": policy.get(
                "id"
            ),
            "title": policy.get(
                "title"
            ),
            "category": policy.get(
                "category"
            ),
        }

    # -----------------------------------------------------
    # RETURN TRACE
    # -----------------------------------------------------

    return {
        "message": cleaned_message,
        "selected_policy": selected_policy,
        "score": score,
        "confidence": confidence,
        "matched_keywords": matched_keywords,
        "matched_keyword_count": (
            matched_keyword_count
        ),
        "intent_bonus": intent_bonus,
        "ambiguous": ambiguous,
        "conflict_type": conflict_type,
        "score_gap": score_gap,
        "competing_policies": (
            competing_policies
        ),
        "verified_eligible": (
            verified_eligible
        ),
        "decision": decision,
        "decision_reason": decision_reason,
    }