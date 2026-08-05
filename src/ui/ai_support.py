import html

import streamlit as st
from src.retrieval_observability import calculate_retrieval_metrics
# =========================================================
# AI SUPPORT HERO
# =========================================================

def render_ai_hero():
    """
    Render ResolveAI premium AI assistant hero.
    """

    hero_html = """
<div class="resolve-hero">

<div class="resolve-light-beam"></div>

<div class="resolve-orb">
◇
</div>

<div class="resolve-hero-title">
How can I help you today?
</div>

<div class="resolve-hero-subtitle">
Describe your support issue and ResolveAI will analyze it,
find relevant knowledge, determine priority, and help resolve
the request.
</div>

</div>
"""

    st.markdown(
        hero_html,
        unsafe_allow_html=True,
    )


# =========================================================
# QUICK ACTIONS
# =========================================================

def render_quick_actions():
    """
    Render premium quick action buttons.
    """

    st.markdown(
        '<div class="resolve-label">'
        'QUICK ACTIONS'
        '</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        payment = st.button(
            "Payment issue",
            use_container_width=True,
            key="quick_payment",
        )

    with col2:

        refund = st.button(
            "Request refund",
            use_container_width=True,
            key="quick_refund",
        )

    with col3:

        order = st.button(
            "Track order",
            use_container_width=True,
            key="quick_order",
        )

    with col4:

        account = st.button(
            "Account help",
            use_container_width=True,
            key="quick_account",
        )

    if payment:
        return "I have a payment issue."

    if refund:
        return "I want to request a refund."

    if order:
        return "I want to track my order."

    if account:
        return "I need help with my account."

    return None


# =========================================================
# INTELLIGENCE EMPTY STATE
# =========================================================

def render_intelligence_empty_state():
    """
    Display Support Intelligence before analysis exists.
    """

    intelligence_html = (
        '<div class="resolve-intelligence-empty">'
        '<div class="resolve-intelligence-icon">✦</div>'
        '<div class="resolve-intelligence-content">'
        '<div class="resolve-intelligence-title">'
        'Support Intelligence'
        '</div>'
        '<div class="resolve-intelligence-status">'
        'Waiting for a request'
        '</div>'
        '<div class="resolve-intelligence-description">'
        'Analysis will appear here after you send a message.'
        '</div>'
        '</div>'
        '</div>'
    )

    st.markdown(
        intelligence_html,
        unsafe_allow_html=True,
    )
    
# =========================================================
# SUPPORT INTELLIGENCE PANEL
# =========================================================

def render_intelligence_panel(
    support_data,
    verified=False,
    source=None,
    retrieval_confidence="none",
    retrieval_ambiguous=False,
    conflict_type="none",
    competing_policies=None,
    retrieval_trace=None,
    retrieval_trace_history=None,
):
    competing_policies = (
        competing_policies or []
    )

    retrieval_trace = (
        retrieval_trace or {}
    )

    retrieval_trace_history = (
        retrieval_trace_history or []
    )

    retrieval_metrics = (
        calculate_retrieval_metrics(
            retrieval_trace_history
        )
    )
    """
    Render premium Support Intelligence analysis panel.

    Includes:
    - Intent
    - Sentiment
    - Priority
    - Escalation
    - Knowledge verification
    - Retrieval confidence
    - Retrieval conflict detection
    - Competing policies
    """
    competing_policies = (competing_policies or [])
    retrieval_trace = (retrieval_trace or {})
    retrieval_trace_history = (retrieval_trace_history or [])
    # -----------------------------------------------------
    # SAFE DEFAULTS
    # -----------------------------------------------------

    if not isinstance(
        support_data,
        dict,
    ):
        support_data = {}

    if not isinstance(
        competing_policies,
        list,
    ):
        competing_policies = []

    # -----------------------------------------------------
    # REQUEST ANALYSIS DATA
    # -----------------------------------------------------

    intent = str(
        support_data.get(
            "intent",
            "Unknown",
        )
    ).title()

    sentiment = str(
        support_data.get(
            "sentiment",
            "Unknown",
        )
    ).title()

    priority = str(
        support_data.get(
            "priority",
            "Unknown",
        )
    ).title()

    escalation = bool(
        support_data.get(
            "escalation",
            False,
        )
    )

    escalation_reason = (
        support_data.get(
            "escalation_reason",
            "",
        )
    )

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown(
        """
<div class="resolve-intelligence-header">

<div class="resolve-intelligence-symbol">
◇
</div>

<div>

<div class="resolve-intelligence-heading">
Support Intelligence
</div>

<div class="resolve-intelligence-caption">
Live request analysis
</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # REQUEST ANALYSIS
    # =====================================================

    st.markdown(
        '<div class="resolve-label">'
        'REQUEST ANALYSIS'
        '</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Intent",
            intent,
        )

    with col2:

        st.metric(
            "Sentiment",
            sentiment,
        )

    st.metric(
        "Priority",
        priority,
    )

    # =====================================================
    # ESCALATION
    # =====================================================

    st.markdown(
        '<div class="resolve-label">'
        'ESCALATION'
        '</div>',
        unsafe_allow_html=True,
    )

    if escalation:

        st.error(
            "Human escalation required"
        )

        if escalation_reason:

            st.caption(
                str(
                    escalation_reason
                )
            )

    else:

        st.success(
            "No escalation required"
        )

    # =====================================================
    # KNOWLEDGE VERIFICATION
    # =====================================================

    st.markdown(
        '<div class="resolve-label">'
        'KNOWLEDGE'
        '</div>',
        unsafe_allow_html=True,
    )

    if verified and source:

        safe_source = html.escape(
            str(source)
        )

        st.markdown(
            f"""
<div class="resolve-live-retrieval">

<div class="resolve-live-retrieval-icon">
✓
</div>

<div>

<div class="resolve-live-retrieval-title">
Verified Knowledge
</div>

<div class="resolve-live-retrieval-text">
{safe_source}
</div>

</div>

</div>
""",
            unsafe_allow_html=True,
        )

    elif retrieval_ambiguous:

        st.markdown(
            """
<div class="resolve-live-conflict">

<div class="resolve-live-conflict-icon">
!
</div>

<div>

<div class="resolve-live-conflict-title">
Verified knowledge blocked
</div>

<div class="resolve-live-conflict-text">
A retrieval conflict must be resolved before
verified policy information can be used.
</div>

</div>

</div>
""",
            unsafe_allow_html=True,
        )

    else:

        st.info(
            "No verified policy used."
        )

    # =====================================================
    # RETRIEVAL RELIABILITY
    # =====================================================

    st.markdown(
        '<div class="resolve-label">'
        'RETRIEVAL RELIABILITY'
        '</div>',
        unsafe_allow_html=True,
    )

    confidence_display = str(
        retrieval_confidence
    ).replace(
        "_",
        " ",
    ).title()

    # -----------------------------------------------------
    # RETRIEVAL CONFLICT
    # -----------------------------------------------------

    if retrieval_ambiguous:

        if conflict_type == "tie":

            conflict_display = (
                "Policy Tie"
            )

        elif conflict_type == "close_match":

            conflict_display = (
                "Close Match"
            )

        else:

            conflict_display = (
                "Ambiguous Match"
            )

        st.markdown(
            f"""
<div class="resolve-live-conflict">

<div class="resolve-live-conflict-icon">
!
</div>

<div>

<div class="resolve-live-conflict-title">
Retrieval Conflict
</div>

<div class="resolve-live-conflict-text">
{conflict_display} detected.<br>
Verified policy use has been blocked.
</div>

</div>

</div>
""",
            unsafe_allow_html=True,
        )

    # -----------------------------------------------------
    # CLEAR RETRIEVAL
    # -----------------------------------------------------

    else:

        if retrieval_confidence == "none":

            retrieval_title = (
                "No Policy Match"
            )

            retrieval_text = (
                "No verified knowledge candidate "
                "matched this request."
            )

            retrieval_symbol = "◇"

        elif retrieval_confidence == "weak":

            retrieval_title = (
                "Weak Retrieval"
            )

            retrieval_text = (
                "Confidence: Weak · "
                "Not eligible for verified use."
            )

            retrieval_symbol = "!"

        else:

            retrieval_title = (
                "Retrieval Clear"
            )

            retrieval_text = (
                f"Confidence: "
                f"{confidence_display}"
            )

            retrieval_symbol = "✓"

        st.markdown(
            f"""
<div class="resolve-live-retrieval">

<div class="resolve-live-retrieval-icon">
{retrieval_symbol}
</div>

<div>

<div class="resolve-live-retrieval-title">
{retrieval_title}
</div>

<div class="resolve-live-retrieval-text">
{retrieval_text}
</div>

</div>

</div>
""",
            unsafe_allow_html=True,
        )

    # =====================================================
    # COMPETING POLICIES
    # =====================================================

    if (
        retrieval_ambiguous
        and competing_policies
    ):

        st.markdown(
            """
<div class="resolve-live-competitor-label">
COMPETING POLICIES
</div>
""",
            unsafe_allow_html=True,
        )

        for policy in competing_policies:

            if not isinstance(
                policy,
                dict,
            ):
                continue

            title = html.escape(
                str(
                    policy.get(
                        "title",
                        "Unknown Policy",
                    )
                )
            )

            category = html.escape(
                str(
                    policy.get(
                        "category",
                        "Unknown",
                    )
                )
            )

            score = policy.get(
                "score",
                0,
            )

            confidence = html.escape(
                str(
                    policy.get(
                        "confidence",
                        "none",
                    )
                ).title()
            )

            st.markdown(
                f"""
<div class="resolve-live-competitor">

<div class="resolve-live-competitor-title">
{title}
</div>

<div class="resolve-live-competitor-meta">
{category} · Score {score} · {confidence}
</div>

</div>
""",
                unsafe_allow_html=True,
            )

        st.caption(
            "ResolveAI requested clarification "
            "instead of selecting a conflicting policy."
        )

# =====================================================
    # RETRIEVAL DECISION TRACE
    # =====================================================

    if retrieval_trace:

        st.markdown(
            '<div class="resolve-label">'
            'DECISION TRACE'
            '</div>',
            unsafe_allow_html=True,
        )

        # -------------------------------------------------
        # READ TRACE
        # -------------------------------------------------

        decision = retrieval_trace.get(
            "decision",
            "unknown",
        )

        decision_reason = retrieval_trace.get(
            "decision_reason",
            "No decision explanation available.",
        )

        trace_score = retrieval_trace.get(
            "score",
            0,
        )

        trace_confidence = retrieval_trace.get(
            "confidence",
            "none",
        )

        matched_keywords = retrieval_trace.get(
            "matched_keywords",
            [],
        )

        matched_keyword_count = retrieval_trace.get(
            "matched_keyword_count",
            0,
        )

        intent_bonus = retrieval_trace.get(
            "intent_bonus",
            0,
        )

        verified_eligible = retrieval_trace.get(
            "verified_eligible",
            False,
        )

        score_gap = retrieval_trace.get(
            "score_gap"
        )

        selected_policy = retrieval_trace.get(
            "selected_policy"
        )

        # -------------------------------------------------
        # SAFE DISPLAY VALUES
        # -------------------------------------------------

        decision_display = (
            str(decision)
            .replace("_", " ")
            .title()
        )

        confidence_display = (
            str(trace_confidence)
            .replace("_", " ")
            .title()
        )

        safe_decision = html.escape(
            decision_display
        )

        safe_reason = html.escape(
            str(decision_reason)
        )

        # -------------------------------------------------
        # DECISION STATUS
        # -------------------------------------------------

        if verified_eligible:

            decision_icon = "✓"
            decision_status = (
                "Verified Knowledge Eligible"
            )

            decision_class = (
                "resolve-trace-eligible"
            )

        elif retrieval_ambiguous:

            decision_icon = "!"

            decision_status = (
                "Verification Blocked"
            )

            decision_class = (
                "resolve-trace-blocked"
            )

        else:

            decision_icon = "◇"

            decision_status = (
                "AI Assistance"
            )

            decision_class = (
                "resolve-trace-neutral"
            )

        st.markdown(
            f"""
<div class="resolve-trace-card {decision_class}">

<div class="resolve-trace-top">

<div class="resolve-trace-icon">
{decision_icon}
</div>

<div>

<div class="resolve-trace-title">
{safe_decision}
</div>

<div class="resolve-trace-status">
{decision_status}
</div>

</div>

</div>

<div class="resolve-trace-reason">
{safe_reason}
</div>

</div>
""",
            unsafe_allow_html=True,
        )

        # -------------------------------------------------
        # DECISION METRICS
        # -------------------------------------------------

        trace_col1, trace_col2 = st.columns(
            2
        )

        with trace_col1:

            st.metric(
                "Score",
                trace_score,
            )

        with trace_col2:

            st.metric(
                "Evidence",
                matched_keyword_count,
            )

        trace_col3, trace_col4 = st.columns(
            2
        )

        with trace_col3:

            st.metric(
                "Confidence",
                confidence_display,
            )

        with trace_col4:

            st.metric(
                "Intent Bonus",
                intent_bonus,
            )

        # -------------------------------------------------
        # SELECTED POLICY
        # -------------------------------------------------

        if isinstance(
            selected_policy,
            dict,
        ):

            selected_title = html.escape(
                str(
                    selected_policy.get(
                        "title",
                        "Unknown",
                    )
                )
            )

            selected_category = html.escape(
                str(
                    selected_policy.get(
                        "category",
                        "Unknown",
                    )
                ).title()
            )

            selected_policy_id = html.escape(
                str(
                    selected_policy.get(
                        "policy_id",
                        "Unknown",
                    )
                )
            )

            st.markdown(
                f"""
<div class="resolve-trace-policy">

<div class="resolve-trace-small-label">
SELECTED POLICY
</div>

<div class="resolve-trace-policy-title">
{selected_title}
</div>

<div class="resolve-trace-policy-meta">
{selected_policy_id} · {selected_category}
</div>

</div>
""",
                unsafe_allow_html=True,
            )

        # -------------------------------------------------
        # MATCHED RETRIEVAL EVIDENCE
        # -------------------------------------------------

        if matched_keywords:

            st.markdown(
                """
<div class="resolve-trace-small-label">
MATCHED EVIDENCE
</div>
""",
                unsafe_allow_html=True,
            )

            evidence_html = ""

            for item in matched_keywords:

                if not isinstance(
                    item,
                    dict,
                ):
                    continue

                keyword = html.escape(
                    str(
                        item.get(
                            "keyword",
                            "Unknown",
                        )
                    )
                )

                weight = item.get(
                    "weight",
                    0,
                )

                evidence_html += (
                    '<div class="resolve-trace-evidence">'
                    '<span>'
                    f'{keyword}'
                    '</span>'
                    '<span class="resolve-trace-weight">'
                    f'+{weight}'
                    '</span>'
                    '</div>'
                )

            st.markdown(
                f"""
<div class="resolve-trace-evidence-list">
{evidence_html}
</div>
""",
                unsafe_allow_html=True,
            )

        # -------------------------------------------------
        # SCORE GAP
        # -------------------------------------------------

        if score_gap is not None:

            st.markdown(
                f"""
<div class="resolve-trace-score-gap">

<span>
Candidate score gap
</span>

<strong>
{html.escape(str(score_gap))}
</strong>

</div>
""",
                unsafe_allow_html=True,
            )

    # =====================================================
    # RETRIEVAL TRACE HISTORY
    # =====================================================

    if retrieval_trace_history:

        st.markdown(
            '<div class="resolve-label">'
            'TRACE HISTORY'
            '</div>',
            unsafe_allow_html=True,
        )

        st.caption(
            f"{len(retrieval_trace_history)} "
            "retrieval decisions retained"
        )

        # Show newest decision first.
        recent_traces = list(
            reversed(
                retrieval_trace_history
            )
        )

        for index, trace in enumerate(
            recent_traces,
            start=1,
        ):

            if not isinstance(
                trace,
                dict,
            ):
                continue

            decision = str(
                trace.get(
                    "decision",
                    "unknown",
                )
            )

            confidence = str(
                trace.get(
                    "confidence",
                    "none",
                )
            )

            score = trace.get(
                "score",
                0,
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

            message = str(
                trace.get(
                    "message",
                    "",
                )
            )

            # ---------------------------------------------
            # SAFE DISPLAY VALUES
            # ---------------------------------------------

            decision_display = html.escape(
                decision
                .replace("_", " ")
                .title()
            )

            confidence_display = html.escape(
                confidence
                .replace("_", " ")
                .title()
            )

            safe_message = html.escape(
                message
            )

            # Keep long messages compact.
            if len(safe_message) > 90:

                safe_message = (
                    safe_message[:87]
                    + "..."
                )

            policy_title = (
                "No policy selected"
            )

            if isinstance(
                selected_policy,
                dict,
            ):

                policy_title = html.escape(
                    str(
                        selected_policy.get(
                            "title",
                            "Unknown",
                        )
                    )
                )

            # ---------------------------------------------
            # STATUS
            # ---------------------------------------------

            if ambiguous:

                status_symbol = "!"

                status_text = (
                    "Conflict"
                )

            elif verified_eligible:

                status_symbol = "✓"

                status_text = (
                    "Verified"
                )

            else:

                status_symbol = "◇"

                status_text = (
                    "AI"
                )

            # ---------------------------------------------
            # RENDER HISTORY ITEM
            # ---------------------------------------------

            st.markdown(
                f"""
<div class="resolve-trace-history-item">

<div class="resolve-trace-history-top">

<div class="resolve-trace-history-status">
{status_symbol}
</div>

<div class="resolve-trace-history-main">

<div class="resolve-trace-history-policy">
{policy_title}
</div>

<div class="resolve-trace-history-message">
{safe_message}
</div>

</div>

<div class="resolve-trace-history-type">
{status_text}
</div>

</div>

<div class="resolve-trace-history-meta">
<span>
{decision_display}
</span>

<span>
Score {score}
</span>

<span>
{confidence_display}
</span>
</div>

</div>
""",
                unsafe_allow_html=True,
            )


    # =====================================================
    # RETRIEVAL HEALTH
    # =====================================================

    if retrieval_trace_history:

        st.markdown(
            '<div class="resolve-label">'
            'RETRIEVAL HEALTH'
            '</div>',
            unsafe_allow_html=True,
        )

        total_decisions = (
            retrieval_metrics.get(
                "total_decisions",
                0,
            )
        )

        verified_decisions = (
            retrieval_metrics.get(
                "verified_decisions",
                0,
            )
        )

        blocked_conflicts = (
            retrieval_metrics.get(
                "blocked_conflicts",
                0,
            )
        )

        ambiguous_decisions = (
            retrieval_metrics.get(
                "ambiguous_decisions",
                0,
            )
        )

        weak_decisions = (
            retrieval_metrics.get(
                "weak_decisions",
                0,
            )
        )

        no_match_decisions = (
            retrieval_metrics.get(
                "no_match_decisions",
                0,
            )
        )

        verification_rate = (
            retrieval_metrics.get(
                "verification_rate",
                0.0,
            )
        )

        conflict_rate = (
            retrieval_metrics.get(
                "conflict_rate",
                0.0,
            )
        )

        ambiguity_rate = (
            retrieval_metrics.get(
                "ambiguity_rate",
                0.0,
            )
        )

        # -------------------------------------------------
        # PRIMARY METRICS
        # -------------------------------------------------

        health_col1, health_col2 = (
            st.columns(2)
        )

        with health_col1:

            st.metric(
                "Decisions",
                total_decisions,
            )

        with health_col2:

            st.metric(
                "Verified",
                verified_decisions,
            )

        # -------------------------------------------------
        # VERIFICATION RATE
        # -------------------------------------------------

        st.metric(
            "Verification Rate",
            f"{verification_rate:.1f}%",
        )

        # -------------------------------------------------
        # HEALTH STATUS
        # -------------------------------------------------

        if conflict_rate >= 40:

            health_status = (
                "Needs attention"
            )

            health_description = (
                "A high percentage of retrieval "
                "decisions are being blocked by "
                "policy conflicts."
            )

            health_symbol = "!"

        elif ambiguity_rate >= 30:

            health_status = (
                "Ambiguity detected"
            )

            health_description = (
                "Several customer requests are "
                "matching multiple support policies."
            )

            health_symbol = "!"

        elif verification_rate >= 60:

            health_status = (
                "Healthy retrieval"
            )

            health_description = (
                "Most recent retrieval decisions "
                "are producing verified policy "
                "matches."
            )

            health_symbol = "✓"

        else:

            health_status = (
                "Developing coverage"
            )

            health_description = (
                "Retrieval is operational, but "
                "knowledge coverage can still "
                "be improved."
            )

            health_symbol = "◇"

        st.markdown(
            f"""
<div class="resolve-retrieval-health">

<div class="resolve-retrieval-health-icon">
{health_symbol}
</div>

<div>

<div class="resolve-retrieval-health-title">
{health_status}
</div>

<div class="resolve-retrieval-health-text">
{health_description}
</div>

</div>

</div>
""",
            unsafe_allow_html=True,
        )

        # -------------------------------------------------
        # SECONDARY STATISTICS
        # -------------------------------------------------

        st.markdown(
            f"""
<div class="resolve-retrieval-health-grid">

<div class="resolve-retrieval-health-stat">
<div class="resolve-retrieval-health-value">
{blocked_conflicts}
</div>
<div class="resolve-retrieval-health-label">
Blocked
</div>
</div>

<div class="resolve-retrieval-health-stat">
<div class="resolve-retrieval-health-value">
{ambiguous_decisions}
</div>
<div class="resolve-retrieval-health-label">
Ambiguous
</div>
</div>

<div class="resolve-retrieval-health-stat">
<div class="resolve-retrieval-health-value">
{weak_decisions}
</div>
<div class="resolve-retrieval-health-label">
Weak
</div>
</div>

<div class="resolve-retrieval-health-stat">
<div class="resolve-retrieval-health-value">
{no_match_decisions}
</div>
<div class="resolve-retrieval-health-label">
No Match
</div>
</div>

</div>
""",
            unsafe_allow_html=True,
        )


# =========================================================
# CONVERSATION HEADER
# =========================================================

def render_conversation_header(
    verified=False,
    source=None,
):
    """
    Render premium active conversation header.
    """

    if verified and source:

        status = (
            "Verified knowledge"
        )

        status_class = (
            "resolve-status-verified"
        )

    else:

        status = (
            "AI assistance"
        )

        status_class = (
            "resolve-status-ai"
        )

    header_html = f"""
<div class="resolve-conversation-topbar">

<div class="resolve-conversation-identity">

<div class="resolve-conversation-avatar">
◇
</div>

<div>

<div class="resolve-conversation-name">
ResolveAI Support
</div>

<div class="resolve-conversation-state">
<span class="resolve-live-dot"></span>
Active conversation
</div>

</div>

</div>

<div class="{status_class}">
{status}
</div>

</div>
"""

    st.markdown(
        header_html,
        unsafe_allow_html=True,
    )