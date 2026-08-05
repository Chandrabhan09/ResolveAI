from datetime import datetime

import streamlit as st

from src.analytics import (
    generate_analytics,
    generate_support_insights,
    get_analytics_metadata,
)
from src.analytics_export import (
    export_analytics_json,
    export_tickets_csv,
)
from src.executive_kpi import (
    calculate_executive_kpis,
)
from src.knowledge_analytics import (
    calculate_knowledge_coverage,
    calculate_knowledge_health_score,
    calculate_retrieval_performance,
    detect_knowledge_gaps,
    generate_knowledge_recommendations,
)
from src.knowledge_base import get_policies

# =========================================================
# COMPACT DISTRIBUTION
# =========================================================

def render_distribution(title, data):
    """
    Render a compact analytics distribution.
    """

    st.markdown(f"**{title}**")

    if not isinstance(data, dict) or not data:
        st.caption("No data available.")
        return

    cleaned_data = {
        str(key): value
        for key, value in data.items()
        if value
    }

    if not cleaned_data:
        st.caption("No activity recorded.")
        return

    st.bar_chart(
        cleaned_data,
        height=220,
    )


# =========================================================
# EXECUTIVE INTELLIGENCE
# =========================================================

def render_executive_intelligence(
    retrieval_trace_history,
):
    """
    Render executive retrieval and knowledge KPIs.
    """

    if not isinstance(
        retrieval_trace_history,
        list,
    ):
        retrieval_trace_history = []

    policies = get_policies()

    coverage = calculate_knowledge_coverage(
        retrieval_trace_history
    )

    performance = calculate_retrieval_performance(
        retrieval_trace_history
    )

    gaps = detect_knowledge_gaps(
        retrieval_trace_history,
        policies,
    )

    recommendations = (
        generate_knowledge_recommendations(
            gaps
        )
    )

    health = calculate_knowledge_health_score(
        coverage,
        performance,
        recommendations,
    )

    kpis = calculate_executive_kpis(
        performance,
        coverage,
        health,
    )

    st.subheader("Executive Intelligence")

    st.caption(
        "Knowledge retrieval and AI support performance."
    )

    total_requests = kpis.get(
        "total_requests",
        performance.get(
            "total_requests",
            0,
        ),
    )

    if total_requests == 0:
        st.info(
            "No retrieval activity recorded yet. "
            "Use AI Support to generate analytics."
        )

    # -----------------------------------------------------
    # PRIMARY KPIS
    # -----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Support Index",
            f"{kpis.get('executive_support_index', 0):.1f}%",
        )

    with col2:
        st.metric(
            "Knowledge Health",
            f"{kpis.get('support_health_score', 0):.1f}%",
        )

    with col3:
        st.metric(
            "Retrieval Success",
            f"{kpis.get('retrieval_success_rate', 0):.1f}%",
        )

    with col4:
        st.metric(
            "Verified Responses",
            f"{kpis.get('verified_response_rate', 0):.1f}%",
        )

    # -----------------------------------------------------
    # SECONDARY KPIS
    # -----------------------------------------------------

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        st.metric(
            "Knowledge Coverage",
            f"{kpis.get('knowledge_coverage', 0):.1f}%",
        )

    with col6:
        st.metric(
            "Automation Rate",
            f"{kpis.get('automation_rate', 0):.1f}%",
        )

    with col7:
        st.metric(
            "Operational Efficiency",
            f"{kpis.get('operational_efficiency', 0):.1f}%",
        )

    with col8:
        st.metric(
            "Retrieval Reliability",
            f"{kpis.get('retrieval_reliability', 0):.1f}%",
        )

    # -----------------------------------------------------
    # DETAILS
    # -----------------------------------------------------

    with st.expander(
        "Executive diagnostics",
        expanded=False,
    ):

        st.markdown("#### Retrieval Risk")

        risk1, risk2, risk3 = st.columns(3)

        with risk1:
            st.metric(
                "Weak Match Rate",
                f"{kpis.get('weak_match_rate', 0):.1f}%",
            )

        with risk2:
            st.metric(
                "Conflict Rate",
                f"{kpis.get('conflict_rate', 0):.1f}%",
            )

        with risk3:
            st.metric(
                "No-Match Rate",
                f"{kpis.get('no_match_rate', 0):.1f}%",
            )

        st.markdown("#### Knowledge Utilization")

        knowledge1, knowledge2, knowledge3 = (
            st.columns(3)
        )

        with knowledge1:
            st.metric(
                "Total Policies",
                kpis.get(
                    "total_policies",
                    coverage.get(
                        "total_policies",
                        0,
                    ),
                ),
            )

        with knowledge2:
            st.metric(
                "Used Policies",
                kpis.get(
                    "used_policies",
                    coverage.get(
                        "used_policies",
                        0,
                    ),
                ),
            )

        with knowledge3:
            st.metric(
                "Unused Policies",
                kpis.get(
                    "unused_policies",
                    coverage.get(
                        "unused_policies",
                        0,
                    ),
                ),
            )

        st.markdown("#### Executive Status")

        status1, status2, status3 = st.columns(3)

        with status1:
            st.metric(
                "Executive Grade",
                kpis.get(
                    "executive_grade",
                    "N/A",
                ),
            )

        with status2:
            st.metric(
                "Knowledge Grade",
                kpis.get(
                    "knowledge_health_grade",
                    health.get(
                        "grade",
                        "N/A",
                    ),
                ),
            )

        with status3:
            st.metric(
                "Operational Risk",
                kpis.get(
                    "risk_level",
                    "N/A",
                ),
            )

        if recommendations:

            st.markdown(
                "#### Knowledge Improvement"
            )

            for recommendation in recommendations[:3]:

                priority = recommendation.get(
                    "priority",
                    "medium",
                )

                policy = recommendation.get(
                    "policy",
                    "Unknown",
                )

                text = recommendation.get(
                    "recommendation",
                    "",
                )

                if priority == "high":
                    st.warning(
                        f"**{policy}** — {text}"
                    )
                else:
                    st.info(
                        f"**{policy}** — {text}"
                    )


# =========================================================
# MAIN ANALYTICS DASHBOARD
# =========================================================

def render_analytics_dashboard(
    retrieval_trace_history=None,
):
    """
    Render ResolveAI analytics dashboard.
    """

    if not isinstance(
        retrieval_trace_history,
        list,
    ):
        retrieval_trace_history = []

    # =====================================================
    # REFRESH
    # =====================================================

    if st.button(
        "Refresh Analytics",
        key="refresh_analytics",
    ):
        st.rerun()

    # =====================================================
    # EXECUTIVE INTELLIGENCE
    # =====================================================

    render_executive_intelligence(
        retrieval_trace_history
    )

    st.divider()

    # =====================================================
    # LOAD SUPPORT ANALYTICS
    # =====================================================

    analytics = generate_analytics()
    insights = generate_support_insights()
    metadata = get_analytics_metadata()

    if not isinstance(analytics, dict):
        analytics = {}

    if not isinstance(insights, dict):
        insights = {}

    if not isinstance(metadata, dict):
        metadata = {}

    total_tickets = analytics.get(
        "total_tickets",
        0,
    )

    status_data = analytics.get(
        "status",
        {},
    )

    priority_data = analytics.get(
        "priority",
        {},
    )

    intent_data = analytics.get(
        "intent",
        {},
    )

    if not isinstance(status_data, dict):
        status_data = {}

    if not isinstance(priority_data, dict):
        priority_data = {}

    if not isinstance(intent_data, dict):
        intent_data = {}

    # =====================================================
    # SUPPORT OPERATIONS
    # =====================================================

    open_tickets = (
        status_data.get("Open", 0)
        + status_data.get("open", 0)
    )

    resolved_tickets = (
        status_data.get("Resolved", 0)
        + status_data.get("resolved", 0)
    )

    critical_tickets = (
        priority_data.get("Critical", 0)
        + priority_data.get("critical", 0)
    )

    resolution_rate = (
        resolved_tickets
        * 100
        / total_tickets
        if total_tickets
        else 0.0
    )

    st.subheader("Support Operations")

    last_updated = metadata.get(
        "last_updated"
    )

    if last_updated:

        try:
            formatted_time = (
                datetime.fromtimestamp(
                    last_updated
                ).strftime(
                    "%d %b %Y, %I:%M:%S %p"
                )
            )

            st.caption(
                f"Data last updated: {formatted_time}"
            )

        except (
            TypeError,
            ValueError,
            OSError,
        ):
            pass

    col1, col2, col3, col4, col5 = (
        st.columns(5)
    )

    with col1:
        st.metric(
            "Total Tickets",
            total_tickets,
        )

    with col2:
        st.metric(
            "Open",
            open_tickets,
        )

    with col3:
        st.metric(
            "Resolved",
            resolved_tickets,
        )

    with col4:
        st.metric(
            "Critical",
            critical_tickets,
        )

    with col5:
        st.metric(
            "Resolution Rate",
            f"{resolution_rate:.1f}%",
        )

    # =====================================================
    # DISTRIBUTIONS
    # =====================================================

    st.divider()

    st.subheader("Ticket Distribution")

    chart1, chart2, chart3 = st.columns(3)

    with chart1:
        render_distribution(
            "Status",
            status_data,
        )

    with chart2:
        render_distribution(
            "Priority",
            priority_data,
        )

    with chart3:
        render_distribution(
            "Customer Intent",
            intent_data,
        )

    # =====================================================
    # SUPPORT INSIGHTS
    # =====================================================

    st.divider()

    st.subheader("Support Insights")

    most_common_intent = insights.get(
        "most_common_intent",
        "N/A",
    )

    most_common_priority = insights.get(
        "most_common_priority",
        "N/A",
    )

    escalated_tickets = insights.get(
        "escalated_tickets",
        0,
    )

    escalation_rate = insights.get(
        "escalation_rate",
        0.0,
    )

    insight1, insight2, insight3, insight4 = (
        st.columns(4)
    )

    with insight1:
        st.metric(
            "Most Common Issue",
            str(
                most_common_intent
            ).title(),
        )

    with insight2:
        st.metric(
            "Common Priority",
            str(
                most_common_priority
            ).title(),
        )

    with insight3:
        st.metric(
            "Escalated Tickets",
            escalated_tickets,
        )

    with insight4:
        st.metric(
            "Escalation Rate",
            f"{escalation_rate:.1f}%",
        )

    # =====================================================
    # EXPORT
    # =====================================================

    st.divider()

    st.subheader("Export Analytics")

    csv_data = export_tickets_csv()
    json_data = export_analytics_json()

    export1, export2 = st.columns(2)

    with export1:
        st.download_button(
            label="Download Tickets CSV",
            data=csv_data,
            file_name="resolveai_tickets.csv",
            mime="text/csv",
            disabled=not bool(csv_data),
            key="download_tickets_csv",
            use_container_width=True,
        )

    with export2:
        st.download_button(
            label="Download Analytics JSON",
            data=json_data,
            file_name="resolveai_analytics.json",
            mime="application/json",
            disabled=not bool(json_data),
            key="download_analytics_json",
            use_container_width=True,
        )