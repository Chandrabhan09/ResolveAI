from src.knowledge_base import (
    build_retrieval_decision_trace,
    get_policy_by_id,
)
from src.openrouter_client import (
    OpenRouterError,
    generate_ai_response,
)
from src.prompts import (
    RESOLVEAI_SYSTEM_PROMPT,
)

# =========================================================
# CONFIGURATION
# =========================================================

MAX_CONTEXT_MESSAGES = 6


# =========================================================
# RESULT BUILDER
# =========================================================

def build_result(
    response,
    verified=False,
    source=None,
    policy_id=None,
    category=None,
    retrieval_confidence="none",
    retrieval_ambiguous=False,
    conflict_type="none",
    competing_policies=None,
    retrieval_trace=None,
):
    """
    Build a consistent ResolveAI chatbot result.
    """

    if not isinstance(response, str):
        response = str(response)

    if not isinstance(competing_policies, list):
        competing_policies = []

    if not isinstance(retrieval_trace, dict):
        retrieval_trace = {}

    return {
        "response": response,
        "verified": bool(verified),
        "source": source,
        "policy_id": policy_id,
        "category": category,
        "retrieval_confidence": retrieval_confidence,
        "retrieval_ambiguous": bool(
            retrieval_ambiguous
        ),
        "conflict_type": conflict_type,
        "competing_policies": competing_policies,
        "retrieval_trace": retrieval_trace,
    }


# =========================================================
# CONVERSATION HISTORY
# =========================================================

def _prepare_conversation_history(
    conversation_history,
):
    """
    Return a safe bounded conversation history.
    """

    if not isinstance(
        conversation_history,
        list,
    ):
        return []

    valid_messages = []

    for message in conversation_history:

        if not isinstance(message, dict):
            continue

        role = message.get("role")
        content = message.get("content")

        if role not in {
            "user",
            "assistant",
        }:
            continue

        if (
            not isinstance(content, str)
            or not content.strip()
        ):
            continue

        valid_messages.append(
            {
                "role": role,
                "content": content.strip(),
            }
        )

    return valid_messages[
        -MAX_CONTEXT_MESSAGES:
    ]


# =========================================================
# CHATBOT RESPONSE
# =========================================================

def get_chatbot_response(
    user_message,
    conversation_history=None,
):
    """
    Generate a context-aware and knowledge-grounded
    ResolveAI customer-support response.

    Retrieval decisions are produced locally before
    any external AI request is made.
    """

    # =====================================================
    # INPUT VALIDATION
    # =====================================================

    if not isinstance(user_message, str):

        return build_result(
            response=(
                "I'm unable to process that message. "
                "Please enter a valid support request."
            )
        )

    cleaned_message = user_message.strip()

    if not cleaned_message:

        return build_result(
            response=(
                "Please enter a message so I can "
                "assist you."
            )
        )

    # =====================================================
    # RETRIEVAL DECISION
    # =====================================================

    try:

        retrieval_trace = (
            build_retrieval_decision_trace(
                cleaned_message
            )
        )

    except Exception:

        # Retrieval failure must not expose internal
        # application details to the customer.

        return build_result(
            response=(
                "I'm temporarily unable to access "
                "verified support information. "
                "Please try again shortly."
            )
        )

    if not isinstance(
        retrieval_trace,
        dict,
    ):
        retrieval_trace = {}

    selected_policy = retrieval_trace.get(
        "selected_policy"
    )

    confidence = retrieval_trace.get(
        "confidence",
        "none",
    )

    if confidence not in {
        "none",
        "weak",
        "moderate",
        "strong",
    }:
        confidence = "none"

    retrieval_ambiguous = bool(
        retrieval_trace.get(
            "ambiguous",
            False,
        )
    )

    conflict_type = retrieval_trace.get(
        "conflict_type",
        "none",
    )

    competing_policies = retrieval_trace.get(
        "competing_policies",
        [],
    )

    if not isinstance(
        competing_policies,
        list,
    ):
        competing_policies = []

    verified_eligible = bool(
        retrieval_trace.get(
            "verified_eligible",
            False,
        )
    )

    # =====================================================
    # LOAD SELECTED POLICY
    # =====================================================

    policy = None

    if isinstance(selected_policy, dict):

        selected_policy_id = (
            selected_policy.get(
                "policy_id"
            )
        )

        if isinstance(
            selected_policy_id,
            str,
        ) and selected_policy_id.strip():

            try:

                policy = get_policy_by_id(
                    selected_policy_id
                )

            except Exception:

                policy = None

    # =====================================================
    # AMBIGUITY SAFETY GATE
    # =====================================================

    if retrieval_ambiguous:

        policy_names = []

        if isinstance(
            selected_policy,
            dict,
        ):

            selected_title = (
                selected_policy.get(
                    "title"
                )
            )

            if (
                isinstance(
                    selected_title,
                    str,
                )
                and selected_title.strip()
            ):

                policy_names.append(
                    selected_title.strip()
                )

        for candidate in competing_policies:

            if not isinstance(
                candidate,
                dict,
            ):
                continue

            title = candidate.get(
                "title"
            )

            if (
                isinstance(title, str)
                and title.strip()
                and title.strip()
                not in policy_names
            ):

                policy_names.append(
                    title.strip()
                )

        if len(policy_names) >= 2:

            if len(policy_names) == 2:

                readable_policies = (
                    f"{policy_names[0]} or "
                    f"{policy_names[1]}"
                )

            else:

                readable_policies = (
                    ", ".join(
                        policy_names[:-1]
                    )
                    + ", or "
                    + policy_names[-1]
                )

            clarification = (
                "I found more than one relevant "
                "support policy for your request "
                f"({readable_policies}). "
                "Could you clarify which issue you "
                "need help with so I can give you "
                "the correct verified information?"
            )

        else:

            clarification = (
                "Your request appears to match more "
                "than one support issue. Could you "
                "clarify what you need help with so "
                "I can use the correct verified "
                "support policy?"
            )

        return build_result(
            response=clarification,
            verified=False,
            source=None,
            policy_id=None,
            category=None,
            retrieval_confidence=confidence,
            retrieval_ambiguous=True,
            conflict_type=conflict_type,
            competing_policies=(
                competing_policies
            ),
            retrieval_trace=(
                retrieval_trace
            ),
        )

    # =====================================================
    # VERIFIED KNOWLEDGE CONTEXT
    # =====================================================

    knowledge_context = None
    verified = False

    if (
        isinstance(policy, dict)
        and verified_eligible
        and confidence
        in {
            "moderate",
            "strong",
        }
    ):

        policy_title = str(
            policy.get(
                "title",
                "Verified Policy",
            )
        )

        policy_category = str(
            policy.get(
                "category",
                "support",
            )
        )

        policy_content = str(
            policy.get(
                "content",
                "",
            )
        ).strip()

        if policy_content:

            verified = True

            knowledge_context = (
                "VERIFIED NOVASTORE SUPPORT POLICY\n\n"
                f"Policy: {policy_title}\n"
                f"Category: {policy_category}\n"
                "Policy information: "
                f"{policy_content}\n\n"
                "Use ONLY this verified policy when "
                "answering the customer's request. "
                "Do not invent additional company "
                "policy."
            )

    elif (
        isinstance(policy, dict)
        and confidence == "weak"
    ):

        knowledge_context = (
            "A weak knowledge-base match was found.\n"
            "Do NOT treat this policy as verified "
            "knowledge.\n"
            "Do NOT state uncertain policy information "
            "as company fact.\n"
            "Ask the customer for clarification when "
            "necessary."
        )

    # =====================================================
    # CONVERSATION CONTEXT
    # =====================================================

    recent_history = (
        _prepare_conversation_history(
            conversation_history
        )
    )

    messages = [
        {
            "role": "system",
            "content": (
                RESOLVEAI_SYSTEM_PROMPT
            ),
        }
    ]

    if knowledge_context:

        messages.append(
            {
                "role": "system",
                "content": knowledge_context,
            }
        )

    for message in recent_history:

        messages.append(message)

    # -----------------------------------------------------
    # CURRENT USER MESSAGE
    # -----------------------------------------------------

    current_message_already_present = (
        bool(messages)
        and messages[-1].get("role")
        == "user"
        and messages[-1].get("content")
        == cleaned_message
    )

    if not current_message_already_present:

        messages.append(
            {
                "role": "user",
                "content": cleaned_message,
            }
        )

    # =====================================================
    # AI RESPONSE
    # =====================================================

    try:

        response = generate_ai_response(
            messages
        )

    except OpenRouterError:

        return build_result(
            response=(
                "I'm temporarily unable to access "
                "AI-powered support. "
                "Please try again shortly."
            ),
            verified=False,
            retrieval_confidence=confidence,
            retrieval_ambiguous=(
                retrieval_ambiguous
            ),
            conflict_type=conflict_type,
            competing_policies=(
                competing_policies
            ),
            retrieval_trace=(
                retrieval_trace
            ),
        )

    except Exception:

        return build_result(
            response=(
                "Something went wrong while processing "
                "your request. Please try again."
            ),
            verified=False,
            retrieval_confidence=confidence,
            retrieval_ambiguous=(
                retrieval_ambiguous
            ),
            conflict_type=conflict_type,
            competing_policies=(
                competing_policies
            ),
            retrieval_trace=(
                retrieval_trace
            ),
        )

    # =====================================================
    # VERIFIED RESPONSE
    # =====================================================

    if (
        verified
        and isinstance(policy, dict)
    ):

        return build_result(
            response=response,
            verified=True,
            source=policy.get(
                "title"
            ),
            policy_id=policy.get(
                "id"
            ),
            category=policy.get(
                "category"
            ),
            retrieval_confidence=confidence,
            retrieval_ambiguous=False,
            conflict_type=conflict_type,
            competing_policies=(
                competing_policies
            ),
            retrieval_trace=(
                retrieval_trace
            ),
        )

    # =====================================================
    # NON-VERIFIED RESPONSE
    # =====================================================

    return build_result(
        response=response,
        verified=False,
        source=None,
        policy_id=None,
        category=None,
        retrieval_confidence=confidence,
        retrieval_ambiguous=False,
        conflict_type=conflict_type,
        competing_policies=(
            competing_policies
        ),
        retrieval_trace=(
            retrieval_trace
        ),
    )