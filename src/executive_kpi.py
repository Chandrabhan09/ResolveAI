# =========================================================
# EXECUTIVE KPI ENGINE
# =========================================================

def calculate_executive_kpis(
    performance,
    coverage,
    health,
):
    """
    Generate executive KPIs from real retrieval
    and knowledge analytics.
    """

    if not isinstance(performance, dict):
        performance = {}

    if not isinstance(coverage, dict):
        coverage = {}

    if not isinstance(health, dict):
        health = {}

    # =====================================================
    # BASE METRICS
    # =====================================================

    total_requests = performance.get(
        "total_requests",
        0,
    )

    successful_requests = performance.get(
        "successful_requests",
        0,
    )

    verified_requests = performance.get(
        "verified_requests",
        0,
    )

    success_rate = performance.get(
        "success_rate",
        0.0,
    )

    verified_rate = performance.get(
        "verified_rate",
        0.0,
    )

    weak_rate = performance.get(
        "weak_rate",
        0.0,
    )

    conflict_rate = performance.get(
        "conflict_rate",
        0.0,
    )

    no_match_rate = performance.get(
        "no_match_rate",
        0.0,
    )

    coverage_percent = coverage.get(
        "coverage_percent",
        0.0,
    )

    health_score = health.get(
        "score",
        0.0,
    )

    health_grade = health.get(
        "grade",
        "Unknown",
    )

    # =====================================================
    # DERIVED KPIs
    # =====================================================

    automation_rate = round(
        (
            success_rate
            + verified_rate
        )
        / 2,
        1,
    )

    operational_efficiency = round(
        max(
            0.0,
            100.0
            - weak_rate
            - conflict_rate
            - no_match_rate,
        ),
        1,
    )

    knowledge_utilization = round(
        (
            coverage_percent
            + verified_rate
        )
        / 2,
        1,
    )

    retrieval_reliability = round(
        max(
            0.0,
            100.0
            - conflict_rate
            - no_match_rate,
        ),
        1,
    )

    retrieval_quality_index = round(
        (
            success_rate
            + verified_rate
            + retrieval_reliability
        )
        / 3,
        1,
    )

    executive_support_index = round(
        (
            health_score
            + automation_rate
            + operational_efficiency
            + knowledge_utilization
            + retrieval_quality_index
        )
        / 5,
        1,
    )

    # =====================================================
    # EXECUTIVE GRADE
    # =====================================================

    if total_requests == 0:

        executive_grade = "Insufficient Data"

    elif executive_support_index >= 90:

        executive_grade = "Excellent"

    elif executive_support_index >= 75:

        executive_grade = "Good"

    elif executive_support_index >= 60:

        executive_grade = "Fair"

    else:

        executive_grade = "Needs Improvement"

    # =====================================================
    # OPERATIONAL RISK
    # =====================================================

    if total_requests == 0:

        risk_level = "Unknown"

    else:

        risk_score = (
            weak_rate
            + conflict_rate
            + no_match_rate
        )

        if risk_score >= 60:

            risk_level = "High"

        elif risk_score >= 30:

            risk_level = "Medium"

        else:

            risk_level = "Low"

    # =====================================================
    # RETURN
    # =====================================================

    return {
        "total_requests": total_requests,
        "successful_requests": successful_requests,
        "verified_requests": verified_requests,

        "support_health_score": health_score,
        "knowledge_health_grade": health_grade,

        "total_policies": coverage.get(
            "total_policies",
            0,
        ),
        "used_policies": coverage.get(
            "used_policies",
            0,
        ),
        "unused_policies": coverage.get(
            "unused_policies",
            0,
        ),
        "knowledge_coverage": coverage_percent,

        "retrieval_success_rate": success_rate,
        "verified_response_rate": verified_rate,
        "weak_match_rate": weak_rate,
        "conflict_rate": conflict_rate,
        "no_match_rate": no_match_rate,

        "average_retrieval_score": performance.get(
            "average_score",
            0.0,
        ),

        "average_confidence_score": performance.get(
            "average_confidence_score",
            0.0,
        ),

        "automation_rate": automation_rate,
        "operational_efficiency": operational_efficiency,
        "knowledge_utilization": knowledge_utilization,
        "retrieval_reliability": retrieval_reliability,
        "retrieval_quality_index": retrieval_quality_index,

        "executive_support_index": executive_support_index,
        "executive_grade": executive_grade,
        "risk_level": risk_level,
    }