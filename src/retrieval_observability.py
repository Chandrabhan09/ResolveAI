# =========================================================
# RESOLVEAI RETRIEVAL OBSERVABILITY
# =========================================================


def calculate_retrieval_metrics(
    trace_history,
):
    """
    Calculate retrieval observability metrics from
    ResolveAI decision-trace history.

    This function does not modify retrieval behavior.
    It only analyzes completed retrieval decisions.
    """

    # =====================================================
    # SAFE INPUT
    # =====================================================

    if not isinstance(trace_history, list):

        trace_history = []


    # =====================================================
    # COUNTERS
    # =====================================================

    total_decisions = 0

    verified_decisions = 0

    blocked_conflicts = 0

    ambiguous_decisions = 0

    weak_decisions = 0

    no_match_decisions = 0


    # =====================================================
    # ANALYZE TRACE HISTORY
    # =====================================================

    for trace in trace_history:

        if not isinstance(trace, dict):
            continue

        total_decisions += 1

        decision = trace.get(
            "decision",
            "unknown",
        )

        confidence = trace.get(
            "confidence",
            "none",
        )

        ambiguous = trace.get(
            "ambiguous",
            False,
        )

        verified_eligible = trace.get(
            "verified_eligible",
            False,
        )

        selected_policy = trace.get(
            "selected_policy"
        )


        # -------------------------------------------------
        # VERIFIED
        # -------------------------------------------------

        if verified_eligible:

            verified_decisions += 1


        # -------------------------------------------------
        # AMBIGUITY
        # -------------------------------------------------

        if ambiguous:

            ambiguous_decisions += 1


        # -------------------------------------------------
        # BLOCKED CONFLICT
        # -------------------------------------------------

        if decision == "blocked_conflict":

            blocked_conflicts += 1


        # -------------------------------------------------
        # WEAK RETRIEVAL
        # -------------------------------------------------

        if confidence == "weak":

            weak_decisions += 1


        # -------------------------------------------------
        # NO POLICY MATCH
        # -------------------------------------------------

        if selected_policy is None:

            no_match_decisions += 1


    # =====================================================
    # RATES
    # =====================================================

    if total_decisions:

        verification_rate = (
            verified_decisions
            / total_decisions
        ) * 100

        conflict_rate = (
            blocked_conflicts
            / total_decisions
        ) * 100

        ambiguity_rate = (
            ambiguous_decisions
            / total_decisions
        ) * 100

    else:

        verification_rate = 0.0
        conflict_rate = 0.0
        ambiguity_rate = 0.0


    # =====================================================
    # RETURN OBSERVABILITY SUMMARY
    # =====================================================

    return {
        "total_decisions": total_decisions,

        "verified_decisions": (
            verified_decisions
        ),

        "blocked_conflicts": (
            blocked_conflicts
        ),

        "ambiguous_decisions": (
            ambiguous_decisions
        ),

        "weak_decisions": (
            weak_decisions
        ),

        "no_match_decisions": (
            no_match_decisions
        ),

        "verification_rate": round(
            verification_rate,
            1,
        ),

        "conflict_rate": round(
            conflict_rate,
            1,
        ),

        "ambiguity_rate": round(
            ambiguity_rate,
            1,
        ),
    }