import sys
from pathlib import Path

# =========================================================
# PROJECT IMPORT PATH
# =========================================================

PROJECT_ROOT = Path(
    __file__
).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(
        0,
        str(PROJECT_ROOT),
    )


from src.retrieval_observability import (
    calculate_retrieval_metrics,
)

# =========================================================
# TEST HELPERS
# =========================================================

def print_result(
    name,
    metrics,
):
    print()
    print("=" * 70)
    print(f"TEST: {name}")
    print("=" * 70)

    for key, value in metrics.items():
        print(
            f"{key}: {value}"
        )


# =========================================================
# TEST 1 — EMPTY HISTORY
# =========================================================

def test_empty_history():

    metrics = calculate_retrieval_metrics(
        []
    )

    assert metrics[
        "total_decisions"
    ] == 0

    assert metrics[
        "verified_decisions"
    ] == 0

    assert metrics[
        "blocked_conflicts"
    ] == 0

    assert metrics[
        "verification_rate"
    ] == 0.0

    assert metrics[
        "conflict_rate"
    ] == 0.0

    print_result(
        "Empty history",
        metrics,
    )


# =========================================================
# TEST 2 — VERIFIED DECISION
# =========================================================

def test_verified_decision():

    history = [
        {
            "confidence": "strong",
            "ambiguous": False,
            "verified_eligible": True,
            "decision": "verified_policy",
            "selected_policy": {
                "policy_id": "tracking_001",
                "title": "Order Tracking",
            },
        }
    ]

    metrics = calculate_retrieval_metrics(
        history
    )

    assert metrics[
        "total_decisions"
    ] == 1

    assert metrics[
        "verified_decisions"
    ] == 1

    assert metrics[
        "verification_rate"
    ] == 100.0

    assert metrics[
        "blocked_conflicts"
    ] == 0

    print_result(
        "Verified decision",
        metrics,
    )


# =========================================================
# TEST 3 — BLOCKED CONFLICT
# =========================================================

def test_blocked_conflict():

    history = [
        {
            "confidence": "weak",
            "ambiguous": True,
            "verified_eligible": False,
            "decision": "blocked_conflict",
            "selected_policy": {
                "policy_id": "refund_001",
                "title": "Refund Processing",
            },
        }
    ]

    metrics = calculate_retrieval_metrics(
        history
    )

    assert metrics[
        "total_decisions"
    ] == 1

    assert metrics[
        "blocked_conflicts"
    ] == 1

    assert metrics[
        "ambiguous_decisions"
    ] == 1

    assert metrics[
        "weak_decisions"
    ] == 1

    assert metrics[
        "verification_rate"
    ] == 0.0

    assert metrics[
        "conflict_rate"
    ] == 100.0

    assert metrics[
        "ambiguity_rate"
    ] == 100.0

    print_result(
        "Blocked conflict",
        metrics,
    )


# =========================================================
# TEST 4 — NO POLICY MATCH
# =========================================================

def test_no_match():

    history = [
        {
            "confidence": "none",
            "ambiguous": False,
            "verified_eligible": False,
            "decision": "no_verified_policy",
            "selected_policy": None,
        }
    ]

    metrics = calculate_retrieval_metrics(
        history
    )

    assert metrics[
        "total_decisions"
    ] == 1

    assert metrics[
        "no_match_decisions"
    ] == 1

    assert metrics[
        "verified_decisions"
    ] == 0

    assert metrics[
        "weak_decisions"
    ] == 0

    print_result(
        "No policy match",
        metrics,
    )


# =========================================================
# TEST 5 — MIXED HISTORY
# =========================================================

def test_mixed_history():

    history = [
        # Verified
        {
            "confidence": "strong",
            "ambiguous": False,
            "verified_eligible": True,
            "decision": "verified_policy",
            "selected_policy": {
                "policy_id": "tracking_001",
            },
        },

        # Verified
        {
            "confidence": "moderate",
            "ambiguous": False,
            "verified_eligible": True,
            "decision": "verified_policy",
            "selected_policy": {
                "policy_id": "refund_001",
            },
        },

        # Conflict
        {
            "confidence": "weak",
            "ambiguous": True,
            "verified_eligible": False,
            "decision": "blocked_conflict",
            "selected_policy": {
                "policy_id": "payment_001",
            },
        },

        # No match
        {
            "confidence": "none",
            "ambiguous": False,
            "verified_eligible": False,
            "decision": "no_verified_policy",
            "selected_policy": None,
        },
    ]

    metrics = calculate_retrieval_metrics(
        history
    )

    assert metrics[
        "total_decisions"
    ] == 4

    assert metrics[
        "verified_decisions"
    ] == 2

    assert metrics[
        "blocked_conflicts"
    ] == 1

    assert metrics[
        "ambiguous_decisions"
    ] == 1

    assert metrics[
        "weak_decisions"
    ] == 1

    assert metrics[
        "no_match_decisions"
    ] == 1

    assert metrics[
        "verification_rate"
    ] == 50.0

    assert metrics[
        "conflict_rate"
    ] == 25.0

    assert metrics[
        "ambiguity_rate"
    ] == 25.0

    print_result(
        "Mixed retrieval history",
        metrics,
    )


# =========================================================
# TEST 6 — INVALID HISTORY INPUT
# =========================================================

def test_invalid_history():

    metrics = calculate_retrieval_metrics(
        None
    )

    assert metrics[
        "total_decisions"
    ] == 0

    assert metrics[
        "verification_rate"
    ] == 0.0

    print_result(
        "Invalid history input",
        metrics,
    )


# =========================================================
# TEST 7 — INVALID TRACE ITEMS
# =========================================================

def test_invalid_trace_items():

    history = [
        None,
        "invalid",
        123,
        [],
        {
            "confidence": "strong",
            "ambiguous": False,
            "verified_eligible": True,
            "decision": "verified_policy",
            "selected_policy": {
                "policy_id": "tracking_001",
            },
        },
    ]

    metrics = calculate_retrieval_metrics(
        history
    )

    # Only the valid dictionary should count.
    assert metrics[
        "total_decisions"
    ] == 1

    assert metrics[
        "verified_decisions"
    ] == 1

    assert metrics[
        "verification_rate"
    ] == 100.0

    print_result(
        "Invalid trace items",
        metrics,
    )


# =========================================================
# RUN VALIDATION
# =========================================================

if __name__ == "__main__":

    print()
    print("=" * 70)
    print(
        "ResolveAI Retrieval Observability Validation"
    )
    print("=" * 70)

    test_empty_history()

    test_verified_decision()

    test_blocked_conflict()

    test_no_match()

    test_mixed_history()

    test_invalid_history()

    test_invalid_trace_items()

    print()
    print("=" * 70)
    print(
        "All retrieval observability tests passed."
    )
    print("=" * 70)