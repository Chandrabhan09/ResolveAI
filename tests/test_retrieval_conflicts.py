from src.knowledge_base import (
    analyze_retrieval_candidates,
    retrieve_policy_with_confidence,
)

# =========================================================
# TEST CASES
# =========================================================

TEST_CASES = [
    {
        "name": "Payment request",
        "message": "I have a payment issue.",
    },
    {
        "name": "Refund request",
        "message": "I want a refund for my order.",
    },
    {
        "name": "Order tracking",
        "message": "Where is my order? I want to track it.",
    },
    {
        "name": "Account help",
        "message": "I need help with my account.",
    },
    {
        "name": "Mixed payment and refund",
        "message": (
            "I was charged twice and I also "
            "want a refund."
        ),
    },
    {
        "name": "Mixed refund and delivery",
        "message": (
            "My order has not arrived and "
            "I want a refund."
        ),
    },
    {
        "name": "Weak generic request",
        "message": "I have a problem.",
    },
    {
        "name": "Completely unrelated request",
        "message": (
            "What is the weather like today?"
        ),
    },
]


# =========================================================
# DISPLAY HELPERS
# =========================================================

def divider():
    print(
        "\n"
        + "=" * 70
    )


def safe_policy_name(policy):
    if not policy:
        return "None"

    return policy.get(
        "title",
        "Unknown Policy",
    )


# =========================================================
# RUN VALIDATION
# =========================================================

def run_validation():

    print(
        "\nResolveAI Retrieval Validation"
    )

    print(
        "=" * 70
    )

    for test in TEST_CASES:

        message = test["message"]

        retrieval = (
            retrieve_policy_with_confidence(
                message
            )
        )

        candidate_analysis = (
            analyze_retrieval_candidates(
                message
            )
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

        ambiguous = (
            candidate_analysis.get(
                "ambiguous",
                False,
            )
        )

        conflict_type = (
            candidate_analysis.get(
                "conflict_type",
                "none",
            )
        )

        best_candidate = (
            candidate_analysis.get(
                "best_candidate"
            )
        )

        competing = (
            candidate_analysis.get(
                "competing_candidates",
                [],
            )
        )

        divider()

        print(
            f"TEST: {test['name']}"
        )

        print(
            f"MESSAGE: {message}"
        )

        print(
            "\nPRIMARY RETRIEVAL"
        )

        print(
            "Policy:",
            safe_policy_name(
                policy
            ),
        )

        print(
            "Score:",
            score,
        )

        print(
            "Confidence:",
            confidence,
        )

        print(
            "\nCONFLICT ANALYSIS"
        )

        print(
            "Ambiguous:",
            ambiguous,
        )

        print(
            "Conflict Type:",
            conflict_type,
        )

        if best_candidate:

            print(
                "Best Candidate:",
                best_candidate.get(
                    "title",
                    "Unknown",
                ),
            )

            print(
                "Best Score:",
                best_candidate.get(
                    "score",
                    0,
                ),
            )

        else:

            print(
                "Best Candidate: None"
            )

        print(
            "\nCOMPETING POLICIES"
        )

        if competing:

            for candidate in competing:

                print(
                    "-",
                    candidate.get(
                        "title",
                        "Unknown",
                    ),
                    "| score:",
                    candidate.get(
                        "score",
                        0,
                    ),
                    "| confidence:",
                    candidate.get(
                        "confidence",
                        "none",
                    ),
                )

        else:

            print(
                "None"
            )

    divider()

    print(
        "Validation completed."
    )


# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":
    run_validation()