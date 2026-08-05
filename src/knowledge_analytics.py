from collections import Counter

from src.knowledge_base import get_policies

# =========================================================
# POLICY USAGE
# =========================================================

def calculate_policy_usage(retrieval_trace_history):
    """Count how often each policy was selected."""

    usage = Counter()

    if not isinstance(retrieval_trace_history, list):
        return {}

    for trace in retrieval_trace_history:

        if not isinstance(trace, dict):
            continue

        selected_policy = trace.get("selected_policy")

        if not isinstance(selected_policy, dict):
            continue

        policy_id = selected_policy.get("policy_id")

        if policy_id:
            usage[policy_id] += 1

    return dict(usage)


# =========================================================
# CATEGORY USAGE
# =========================================================

def calculate_category_usage(retrieval_trace_history):
    """Count retrieval usage by knowledge category."""

    usage = Counter()

    if not isinstance(retrieval_trace_history, list):
        return {}

    for trace in retrieval_trace_history:

        if not isinstance(trace, dict):
            continue

        selected_policy = trace.get("selected_policy")

        if not isinstance(selected_policy, dict):
            continue

        category = selected_policy.get("category")

        if category:
            usage[category] += 1

    return dict(usage)


# =========================================================
# KNOWLEDGE COVERAGE
# =========================================================

def calculate_knowledge_coverage(
    retrieval_trace_history,
):
    """Calculate real knowledge-base usage coverage."""

    policies = get_policies()

    policy_usage = calculate_policy_usage(
        retrieval_trace_history
    )

    total_policies = len(policies)

    valid_policy_ids = {
        policy.get("id")
        for policy in policies
        if policy.get("id")
    }

    used_policy_ids = (
        set(policy_usage.keys())
        & valid_policy_ids
    )

    unused_policy_ids = [
        policy_id
        for policy_id in valid_policy_ids
        if policy_id not in used_policy_ids
    ]

    used_count = len(used_policy_ids)
    unused_count = len(unused_policy_ids)

    coverage_percent = (
        round(
            used_count * 100 / total_policies,
            1,
        )
        if total_policies
        else 0.0
    )

    return {
        "total_policies": total_policies,
        "used_policies": used_count,
        "unused_policies": unused_count,
        "coverage_percent": coverage_percent,
        "unused_policy_ids": sorted(
            unused_policy_ids
        ),
    }


# =========================================================
# KNOWLEDGE SUMMARY
# =========================================================

def generate_knowledge_summary(
    retrieval_trace_history,
):
    """Generate knowledge usage summary."""

    policies = get_policies()

    coverage = calculate_knowledge_coverage(
        retrieval_trace_history
    )

    policy_usage = calculate_policy_usage(
        retrieval_trace_history
    )

    category_usage = calculate_category_usage(
        retrieval_trace_history
    )

    most_used_policy = None
    highest_usage = 0

    for policy in policies:

        policy_id = policy.get("id")

        count = policy_usage.get(
            policy_id,
            0,
        )

        if count > highest_usage:

            highest_usage = count

            most_used_policy = {
                "policy_id": policy_id,
                "title": policy.get("title"),
                "category": policy.get("category"),
                "count": count,
            }

    all_categories = {
        policy.get("category")
        for policy in policies
        if policy.get("category")
    }

    unused_categories = sorted(
        all_categories
        - set(category_usage.keys())
    )

    return {
        "coverage": coverage,
        "policy_usage": policy_usage,
        "category_usage": category_usage,
        "most_used_policy": most_used_policy,
        "unused_policy_ids": coverage[
            "unused_policy_ids"
        ],
        "unused_categories": unused_categories,
    }


# =========================================================
# RETRIEVAL PERFORMANCE
# =========================================================

def calculate_retrieval_performance(
    retrieval_trace_history,
):
    """Calculate retrieval performance metrics."""

    if not isinstance(
        retrieval_trace_history,
        list,
    ):
        retrieval_trace_history = []

    traces = [
        trace
        for trace in retrieval_trace_history
        if isinstance(trace, dict)
    ]

    total = len(traces)

    if total == 0:

        return {
            "total_requests": 0,
            "successful_requests": 0,
            "verified_requests": 0,
            "weak_requests": 0,
            "conflict_requests": 0,
            "no_match_requests": 0,
            "verified_rate": 0.0,
            "weak_rate": 0.0,
            "conflict_rate": 0.0,
            "no_match_rate": 0.0,
            "average_score": 0.0,
            "average_confidence_score": 0.0,
            "success_rate": 0.0,
        }

    verified = 0
    weak = 0
    conflicts = 0
    no_match = 0
    successful = 0

    score_sum = 0.0
    confidence_sum = 0

    confidence_map = {
        "none": 0,
        "weak": 1,
        "moderate": 2,
        "strong": 3,
    }

    for trace in traces:

        try:
            score_sum += float(
                trace.get("score", 0) or 0
            )
        except (TypeError, ValueError):
            pass

        confidence = str(
            trace.get(
                "confidence",
                "none",
            )
        ).lower()

        confidence_sum += confidence_map.get(
            confidence,
            0,
        )

        selected_policy = trace.get(
            "selected_policy"
        )

        ambiguous = bool(
            trace.get(
                "ambiguous",
                False,
            )
        )

        verified_eligible = bool(
            trace.get(
                "verified_eligible",
                False,
            )
        )

        if selected_policy is None:
            no_match += 1

        if ambiguous:
            conflicts += 1

        if confidence == "weak":
            weak += 1

        if verified_eligible:
            verified += 1

        # A retrieval succeeds when a policy was found
        # and the result was not ambiguous.
        if (
            isinstance(selected_policy, dict)
            and not ambiguous
        ):
            successful += 1

    return {
        "total_requests": total,

        "successful_requests": successful,

        "verified_requests": verified,

        "weak_requests": weak,

        "conflict_requests": conflicts,

        "no_match_requests": no_match,

        "verified_rate": round(
            verified * 100 / total,
            1,
        ),

        "weak_rate": round(
            weak * 100 / total,
            1,
        ),

        "conflict_rate": round(
            conflicts * 100 / total,
            1,
        ),

        "no_match_rate": round(
            no_match * 100 / total,
            1,
        ),

        "average_score": round(
            score_sum / total,
            2,
        ),

        "average_confidence_score": round(
            confidence_sum / total,
            2,
        ),

        "success_rate": round(
            successful * 100 / total,
            1,
        ),
    }


# =========================================================
# CATEGORY PERFORMANCE
# =========================================================

def calculate_category_performance(
    retrieval_trace_history,
):
    """Calculate retrieval quality by category."""

    if not isinstance(
        retrieval_trace_history,
        list,
    ):
        return {}

    categories = {}

    for trace in retrieval_trace_history:

        if not isinstance(trace, dict):
            continue

        selected_policy = trace.get(
            "selected_policy"
        )

        if not isinstance(
            selected_policy,
            dict,
        ):
            continue

        category = selected_policy.get(
            "category"
        )

        if not category:
            continue

        if category not in categories:

            categories[category] = {
                "category": category,
                "requests": 0,
                "verified": 0,
                "weak": 0,
                "conflicts": 0,
                "score_total": 0.0,
            }

        row = categories[category]

        row["requests"] += 1

        try:

            row["score_total"] += float(
                trace.get("score", 0) or 0
            )

        except (TypeError, ValueError):

            pass

        if trace.get(
            "verified_eligible",
            False,
        ):
            row["verified"] += 1

        if (
            trace.get("confidence")
            == "weak"
        ):
            row["weak"] += 1

        if trace.get(
            "ambiguous",
            False,
        ):
            row["conflicts"] += 1

    for row in categories.values():

        requests = row["requests"]

        row["verification_rate"] = round(
            row["verified"]
            * 100
            / requests,
            1,
        )

        row["weak_rate"] = round(
            row["weak"]
            * 100
            / requests,
            1,
        )

        row["conflict_rate"] = round(
            row["conflicts"]
            * 100
            / requests,
            1,
        )

        row["average_score"] = round(
            row["score_total"]
            / requests,
            2,
        )

    return dict(
        sorted(
            categories.items(),
            key=lambda item: (
                item[1]["requests"],
                item[1]["verification_rate"],
            ),
            reverse=True,
        )
    )


# =========================================================
# KNOWLEDGE GAP DETECTION
# =========================================================

def detect_knowledge_gaps(
    retrieval_trace_history,
    policies=None,
):
    """Detect unused, weak, and conflicting policies."""

    if not isinstance(
        retrieval_trace_history,
        list,
    ):
        retrieval_trace_history = []

    if policies is None:
        policies = get_policies()

    if not isinstance(policies, list):
        policies = []

    policy_stats = {}

    for policy in policies:

        policy_id = policy.get("id")

        if not policy_id:
            continue

        policy_stats[policy_id] = {
            "policy_id": policy_id,
            "title": policy.get(
                "title",
                "Unknown",
            ),
            "category": policy.get(
                "category",
                "Unknown",
            ),
            "retrievals": 0,
            "weak": 0,
            "conflicts": 0,
        }

    for trace in retrieval_trace_history:

        if not isinstance(trace, dict):
            continue

        selected = trace.get(
            "selected_policy"
        )

        if not isinstance(selected, dict):
            continue

        policy_id = selected.get(
            "policy_id"
        )

        stats = policy_stats.get(
            policy_id
        )

        if not stats:
            continue

        stats["retrievals"] += 1

        if trace.get(
            "confidence"
        ) == "weak":
            stats["weak"] += 1

        if trace.get(
            "ambiguous",
            False,
        ):
            stats["conflicts"] += 1

    unused = []
    weak = []
    conflicts = []

    for stats in policy_stats.values():

        retrievals = stats["retrievals"]

        if retrievals == 0:

            unused.append(
                stats.copy()
            )

            continue

        weak_rate = (
            stats["weak"]
            * 100
            / retrievals
        )

        conflict_rate = (
            stats["conflicts"]
            * 100
            / retrievals
        )

        if weak_rate >= 50:

            weak.append(
                {
                    **stats,
                    "weak_rate": round(
                        weak_rate,
                        1,
                    ),
                }
            )

        if conflict_rate >= 30:

            conflicts.append(
                {
                    **stats,
                    "conflict_rate": round(
                        conflict_rate,
                        1,
                    ),
                }
            )

    return {
        "unused_policies": sorted(
            unused,
            key=lambda item: item["title"],
        ),

        "weak_policies": sorted(
            weak,
            key=lambda item: item["weak_rate"],
            reverse=True,
        ),

        "conflict_policies": sorted(
            conflicts,
            key=lambda item: item[
                "conflict_rate"
            ],
            reverse=True,
        ),
    }


# =========================================================
# KNOWLEDGE RECOMMENDATIONS
# =========================================================

def generate_knowledge_recommendations(
    gap_analysis,
):
    """Generate actionable knowledge recommendations."""

    if not isinstance(gap_analysis, dict):
        return []

    recommendations = []

    for policy in gap_analysis.get(
        "weak_policies",
        [],
    ):

        recommendations.append(
            {
                "priority": "high",
                "type": "Weak Retrieval",
                "policy": policy.get(
                    "title",
                    "Unknown",
                ),
                "recommendation": (
                    "Add more customer-facing keywords "
                    "and phrases to improve retrieval "
                    "confidence."
                ),
            }
        )

    for policy in gap_analysis.get(
        "conflict_policies",
        [],
    ):

        recommendations.append(
            {
                "priority": "high",
                "type": "Retrieval Conflict",
                "policy": policy.get(
                    "title",
                    "Unknown",
                ),
                "recommendation": (
                    "Refine overlapping keywords to "
                    "improve retrieval precision."
                ),
            }
        )

    for policy in gap_analysis.get(
        "unused_policies",
        [],
    ):

        recommendations.append(
            {
                "priority": "medium",
                "type": "Unused Policy",
                "policy": policy.get(
                    "title",
                    "Unknown",
                ),
                "recommendation": (
                    "Review this policy's keywords or "
                    "confirm whether the policy is still "
                    "required."
                ),
            }
        )

    priority_order = {
        "high": 0,
        "medium": 1,
        "low": 2,
    }

    recommendations.sort(
        key=lambda item: (
            priority_order.get(
                item["priority"],
                3,
            ),
            item["policy"],
        )
    )

    return recommendations

# =========================================================
# KNOWLEDGE HEALTH SCORE
# =========================================================

def calculate_knowledge_health_score(
    coverage,
    performance,
    recommendations,
):
    """Calculate overall knowledge health from 0–100."""

    if not isinstance(coverage, dict):
        coverage = {}

    if not isinstance(performance, dict):
        performance = {}

    if not isinstance(recommendations, list):
        recommendations = []

    coverage_percent = float(
        coverage.get(
            "coverage_percent",
            0,
        )
        or 0
    )

    weak_rate = float(
        performance.get(
            "weak_rate",
            0,
        )
        or 0
    )

    conflict_rate = float(
        performance.get(
            "conflict_rate",
            0,
        )
        or 0
    )

    no_match_rate = float(
        performance.get(
            "no_match_rate",
            0,
        )
        or 0
    )

    score = 100.0

    score -= (
        100 - coverage_percent
    ) * 0.20

    score -= weak_rate * 0.20

    score -= conflict_rate * 0.30

    score -= no_match_rate * 0.20

    high_priority = sum(
        1
        for item in recommendations
        if isinstance(item, dict)
        and item.get("priority") == "high"
    )

    medium_priority = sum(
        1
        for item in recommendations
        if isinstance(item, dict)
        and item.get("priority") == "medium"
    )

    score -= high_priority * 3
    score -= medium_priority

    score = round(
        max(
            0.0,
            min(score, 100.0),
        ),
        1,
    )

    if score >= 90:
        grade = "Excellent"

    elif score >= 75:
        grade = "Good"

    elif score >= 60:
        grade = "Fair"

    else:
        grade = "Needs Improvement"

    return {
        "score": score,
        "grade": grade,
    }