import html

import streamlit as st

from src.knowledge_analytics import (
    calculate_category_performance,
    calculate_knowledge_health_score,
    calculate_retrieval_performance,
    detect_knowledge_gaps,
    generate_knowledge_recommendations,
    generate_knowledge_summary,
)
from src.knowledge_base import (
    KnowledgeBaseError,
    analyze_retrieval_candidates,
    generate_knowledge_health,
    get_company,
    get_policies,
    get_retrieval_diagnostics,
    retrieve_policy_with_confidence,
)


def _safe_text(value, fallback="Unknown"):
    """
    Convert knowledge-base values into safe display text.
    """

    if value is None:
        return fallback

    value = str(value).strip()

    if not value:
        return fallback

    return value


def render_knowledge_dashboard(
    retrieval_trace_history = None,
):
    """
    Render the ResolveAI verified knowledge workspace.
    """

    # =====================================================
    # LOAD REAL KNOWLEDGE BASE
    # =====================================================

    try:
        company = get_company()
        policies = get_policies()

    except KnowledgeBaseError as exc:

        st.error(
            f"Unable to load verified knowledge: {exc}"
        )

        return
    
    retrieval_trace_history = (retrieval_trace_history or []    )
    analytics = generate_knowledge_summary(
        retrieval_trace_history
    )
    performance = calculate_retrieval_performance(
        retrieval_trace_history
    )
    category_performance = calculate_category_performance(
        retrieval_trace_history
    )
    gap_analysis = detect_knowledge_gaps(
        retrieval_trace_history,
        policies,
    )
    recommendations = generate_knowledge_recommendations(gap_analysis)
    
    unused_policies = gap_analysis[
        "unused_policies"
    ]

    weak_policies = gap_analysis[
        "weak_policies"
    ]

    conflict_policies = gap_analysis[
        "conflict_policies"
    ]
    coverage = analytics["coverage"]

    

    category_usage = analytics[
        "category_usage"
    ]

    most_used_policy = analytics[
        "most_used_policy"
    ]

    unused_policy_ids = analytics[
        "unused_policy_ids"
    ]

    unused_categories = analytics[
        "unused_categories"
    ]
    verified_rate = performance[
        "verified_rate"
    ]

    weak_rate = performance[
        "weak_rate"
    ]

    conflict_rate = performance[
        "conflict_rate"
    ]

    no_match_rate = performance[
        "no_match_rate"
    ]

    average_score = performance[
        "average_score"
    ]

    average_confidence = performance[
        "average_confidence_score"
    ]

    success_rate = performance[
        "success_rate"
    ]
    health = calculate_knowledge_health_score(
            coverage,
            performance,
            recommendations,
        )

    st.markdown(
        '<div class="resolve-label">'
        'RETRIEVAL PERFORMANCE'
        '</div>',
        unsafe_allow_html=True,
    )

    perf1, perf2, perf3, perf4 = st.columns(4)

    with perf1:
        st.metric(
            "Verified",
            f"{verified_rate}%",
        )

    with perf2:
        st.metric(
            "Weak",
            f"{weak_rate}%",
        )

    with perf3:
        st.metric(
            "Conflict",
            f"{conflict_rate}%",
        )

    with perf4:
        st.metric(
            "No Match",
            f"{no_match_rate}%",
        )

    perf5, perf6, perf7 = st.columns(3)

    with perf5:
        st.metric(
            "Avg Score",
            average_score,
        )

    with perf6:
        st.metric(
            "Avg Confidence",
            average_confidence,
        )

    with perf7:
        st.metric(
            "Success",
            f"{success_rate}%",
        )

    if success_rate >= 90:

        st.success(
            "Retrieval performance is excellent. "
            "Most customer requests produce reliable "
            "knowledge retrieval."
        )

    elif success_rate >= 70:

        st.info(
            "Retrieval performance is good, but "
            "there is still room to improve knowledge "
            "coverage and retrieval quality."
        )

    else:

        st.warning(
            "Retrieval performance needs improvement. "
            "Consider expanding keywords or adding "
            "new support policies."
        )

    st.markdown(
        '<div class="resolve-label">'
        'CATEGORY PERFORMANCE'
        '</div>',
        unsafe_allow_html=True,
    )
    if not category_performance:

        st.info(
            "No category performance data available."
        )

    else:

        header = st.columns(
            [2.2, 1, 1, 1, 1, 1]
        )

        header[0].markdown("**Category**")
        header[1].markdown("**Requests**")
        header[2].markdown("**Verified**")
        header[3].markdown("**Weak**")
        header[4].markdown("**Avg Score**")
        header[5].markdown("**Rate**")

        st.divider()

    for stats in category_performance.values():

            row = st.columns(
                [2.2, 1, 1, 1, 1, 1]
            )

            row[0].write(
                stats["category"].title()
            )

            row[1].write(
                stats["requests"]
            )

            row[2].write(
                stats["verified"]
            )

            row[3].write(
                stats["weak"]
            )

            row[4].write(
                stats["average_score"]
            )

            row[5].write(
                f"{stats['verification_rate']}%"
            )

    st.markdown(
        '<div class="resolve-label">'
        'KNOWLEDGE GAP DETECTION'
        '</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="resolve-label">'
        'KNOWLEDGE GAP DETECTION'
        '</div>',
        unsafe_allow_html=True,
    )
    if unused_policies:

        st.subheader("Unused Policies")

        for policy in unused_policies:

            st.warning(
                f"{policy['title']} "
                f"({policy['category']}) "
                "- never retrieved."
            )
    if weak_policies:

        st.subheader("Weak Retrieval Policies")

        for policy in weak_policies:

            st.info(
                f"{policy['title']} "
                f"- Weak Rate: "
                f"{policy['weak_rate']}%"
            )

    if conflict_policies:

        st.subheader("Conflict Policies")

        for policy in conflict_policies:

            st.error(
                f"{policy['title']} "
                f"- Conflict Rate: "
                f"{policy['conflict_rate']}%"
            )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Unused Policies",
            len(unused_policies),
        )

    with col2:
        st.metric(
            "Weak Policies",
            len(weak_policies),
        )

    with col3:
        st.metric(
            "Conflict Policies",
            len(conflict_policies),
        )
    st.markdown(
        '<div class="resolve-label">'
        'KNOWLEDGE IMPROVEMENT RECOMMENDATIONS'
        '</div>',
        unsafe_allow_html=True,
    )
    if not recommendations:

        st.success(
            "No improvement recommendations at this time. "
            "The knowledge base is performing well."
        )
    else:

        for recommendation in recommendations:

            priority = recommendation["priority"]
            recommendation_type = recommendation["type"]
            policy = recommendation["policy"]
            text = recommendation["recommendation"]

            if priority == "high":

                st.error(
                    f"🔴 {recommendation_type}\n\n"
                    f"Policy: {policy}\n\n"
                    f"{text}"
                )

            elif priority == "medium":

                st.warning(
                    f"🟡 {recommendation_type}\n\n"
                    f"Policy: {policy}\n\n"
                    f"{text}"
                )

            else:

                st.info(
                    f"🔵 {recommendation_type}\n\n"
                    f"Policy: {policy}\n\n"
                    f"{text}"
                )
    high_count = sum(
        1
        for recommendation in recommendations
        if recommendation["priority"] == "high"
    )

    medium_count = sum(
        1
        for recommendation in recommendations
        if recommendation["priority"] == "medium"
    )

    low_count = sum(
        1
        for recommendation in recommendations
        if recommendation["priority"] == "low"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "High Priority",
            high_count,
        )

    with col2:
        st.metric(
            "Medium Priority",
            medium_count,
        )

    with col3:
        st.metric(
            "Low Priority",
            low_count,
        )

    st.markdown(
        '<div class="resolve-label">'
        'KNOWLEDGE PERFORMANCE DASHBOARD'
        '</div>',
        unsafe_allow_html=True,
    )
    row1 = st.columns(4)

    with row1[0]:
        st.metric(
            "Health Score",
            f"{health['score']}/100",
        )

    with row1[1]:
        st.metric(
            "Coverage",
            f"{coverage['coverage_percent']}%",
        )

    with row1[2]:
        st.metric(
            "Success",
            f"{performance['success_rate']}%",
        )

    with row1[3]:
        st.metric(
            "Verified",
            f"{performance['verified_rate']}%",
        )
    row2 = st.columns(4)

    with row2[0]:
        st.metric(
            "Weak",
            f"{performance['weak_rate']}%",
        )

    with row2[1]:
        st.metric(
            "Conflicts",
            f"{performance['conflict_rate']}%",
        )

    with row2[2]:
        st.metric(
            "No Match",
            f"{performance['no_match_rate']}%",
        )

    with row2[3]:
        st.metric(
            "Recommendations",
            len(recommendations),
        )


    st.markdown(
        '<div class="resolve-label">'
        'EXECUTIVE SUMMARY'
        '</div>',
        unsafe_allow_html=True,
    )

    if health["grade"] == "Excellent":

        st.success(
            "Knowledge health is excellent. "
            "Retrieval quality is consistently high with "
            "minimal conflicts and strong coverage."
        )

    elif health["grade"] == "Good":

        st.info(
            "Knowledge health is good. "
            "Minor improvements can increase retrieval "
            "quality and reduce weak matches."
        )

    elif health["grade"] == "Fair":

        st.warning(
            "Knowledge health is fair. "
            "Several policies would benefit from "
            "keyword expansion and conflict reduction."
        )

    else:

        st.error(
            "Knowledge health requires attention. "
            "Significant knowledge improvements are "
            "recommended."
        )

    # =====================================================
    # CATEGORY SUMMARY
    # =====================================================

    if category_performance:

        best = max(
            category_performance.values(),
            key=lambda x: (
                x["verification_rate"],
                x["requests"],
            ),
        )

        st.success(
            f"Best performing category: "
            f"{best['category'].title()} "
            f"({best['verification_rate']}% verified)"
        )

        worst = min(
            category_performance.values(),
            key=lambda x: (
                x["verification_rate"],
                -x["requests"],
            ),
        )

        if worst["verification_rate"] < 60:

            st.warning(
                f"Category needing improvement: "
                f"{worst['category'].title()} "
                f"({worst['verification_rate']}% verified)"
            )

    else:

        st.info(
            "Category performance analytics will appear after "
            "ResolveAI retrieves verified knowledge."
        )



    # =====================================================
    # KNOWLEDGE STATISTICS
    # =====================================================

    total_policies = len(policies)

    categories = sorted(
        {
            _safe_text(
                policy.get("category")
            )
            for policy in policies
        }
    )

    total_categories = len(categories)

    st.markdown(
        '<div class="resolve-label">'
        'KNOWLEDGE OVERVIEW'
        '</div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Verified Policies",
            total_policies,
        )

    with col2:
        st.metric(
            "Categories",
            total_categories,
        )

    with col3:
        st.metric(
            "Knowledge Status",
            "Verified",
        )

    # =====================================================
    # COMPANY CONTEXT
    # =====================================================

    if isinstance(company, dict):

        company_name = (
            company.get("name")
            or company.get("company_name")
            or "Support Knowledge"
        )

    else:

        company_name = str(company)

    company_name = html.escape(
        _safe_text(company_name)
    )

    st.markdown(
        f"""
<div class="resolve-knowledge-company">
<div class="resolve-knowledge-company-icon">
◇
</div>

<div>
<div class="resolve-knowledge-company-title">
{company_name}
</div>

<div class="resolve-knowledge-company-caption">
Verified support knowledge used by ResolveAI
</div>
</div>

<div class="resolve-knowledge-verified">
✓ Verified
</div>
</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # EMPTY KNOWLEDGE BASE
    # =====================================================

    if not policies:

        st.info(
            "No verified policies are currently available."
        )

        return

    # =====================================================
    # SEARCH + CATEGORY FILTER
    # =====================================================

    st.markdown(
        '<div class="resolve-label">'
        'POLICY LIBRARY'
        '</div>',
        unsafe_allow_html=True,
    )

    search_col, category_col = st.columns(
        [3, 1],
        gap="small",
    )

    with search_col:

        search = st.text_input(
            "Search policies",
            placeholder=(
                "Search title, category, "
                "keyword or policy content..."
            ),
            label_visibility="collapsed",
            key="knowledge_search",
        )

    with category_col:

        category_filter = st.selectbox(
            "Category",
            ["All categories"] + categories,
            label_visibility="collapsed",
            key="knowledge_category_filter",
        )

    # =====================================================
    # FILTER POLICIES
    # =====================================================

    filtered_policies = []

    search_term = search.lower().strip()

    for policy in policies:

        category = _safe_text(
            policy.get("category")
        )

        if (
            category_filter != "All categories"
            and category != category_filter
        ):
            continue

        if search_term:

            keywords = policy.get(
                "keywords",
                [],
            )

            searchable_text = " ".join(
                [
                    _safe_text(
                        policy.get("id"),
                        "",
                    ),
                    _safe_text(
                        policy.get("title"),
                        "",
                    ),
                    category,
                    _safe_text(
                        policy.get("content"),
                        "",
                    ),
                    " ".join(
                        str(keyword)
                        for keyword in keywords
                    ),
                ]
            ).lower()

            if search_term not in searchable_text:
                continue

        filtered_policies.append(policy)

    # =====================================================
    # RESULT SUMMARY
    # =====================================================

    st.markdown(
        f"""
<div class="resolve-queue-summary">

<div>
<span class="resolve-queue-count">
{len(filtered_policies)}
</span>
policies shown
</div>

<div class="resolve-queue-total">
{total_policies} verified policies
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    if not filtered_policies:

        st.info(
            "No verified policies match your search."
        )

        return


    st.markdown(
        '<div class="resolve-label">'
        'KNOWLEDGE ANALYTICS'
        '</div>',
        unsafe_allow_html=True,
    )

    metric1, metric2, metric3, metric4 = st.columns(4)

    with metric1:
        st.metric(
            "Coverage",
            f"{coverage['coverage_percent']}%",
        )

    with metric2:
        st.metric(
            "Policies Used",
            coverage["used_policies"],
        )

    with metric3:
        st.metric(
            "Unused",
            coverage["unused_policies"],
        )

    with metric4:
        st.metric(
            "Categories Used",
            len(category_usage),
        )
    if unused_policy_ids:

        st.warning(
            "Unused policies: "
            + ", ".join(unused_policy_ids)
        )

    if unused_categories:

        st.info(
            "Unused categories: "
            + ", ".join(unused_categories)
        )

    if most_used_policy:

        st.success(
            f"Most used policy: "
            f"{most_used_policy['title']} "
            f"({most_used_policy['count']} retrievals)"
        )

    else:

        st.info(
            "No policy has been retrieved yet."
        )
    # =====================================================
    # POLICY LIBRARY
    # =====================================================

    header1, header2, header3 = st.columns(
        [1.3, 3, 1.6],
    )

    with header1:
        st.markdown(
            '<div class="resolve-queue-header">'
            'POLICY ID'
            '</div>',
            unsafe_allow_html=True,
        )

    with header2:
        st.markdown(
            '<div class="resolve-queue-header">'
            'POLICY'
            '</div>',
            unsafe_allow_html=True,
        )

    with header3:
        st.markdown(
            '<div class="resolve-queue-header">'
            'CATEGORY'
            '</div>',
            unsafe_allow_html=True,
        )

    for policy in filtered_policies:

        policy_id = html.escape(
            _safe_text(
                policy.get("id")
            )
        )

        title = html.escape(
            _safe_text(
                policy.get("title")
            )
        )

        category = html.escape(
            _safe_text(
                policy.get("category")
            )
        )

        row1, row2, row3 = st.columns(
            [1.3, 3, 1.6],
        )

        with row1:
            st.markdown(
                f"""
<div class="resolve-knowledge-policy-id">
{policy_id}
</div>
""",
                unsafe_allow_html=True,
            )

        with row2:
            st.markdown(
                f"""
<div class="resolve-knowledge-policy-title">
{title}
</div>
""",
                unsafe_allow_html=True,
            )

        with row3:
            st.markdown(
                f"""
<div class="resolve-knowledge-category">
{category}
</div>
""",
                unsafe_allow_html=True,
            )

        st.markdown(
            '<div class="resolve-queue-divider"></div>',
            unsafe_allow_html=True,
        )

    # =====================================================
    # POLICY SELECTOR
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="resolve-label">'
        'OPEN POLICY'
        '</div>',
        unsafe_allow_html=True,
    )

    policy_lookup = {
        policy["id"]: policy
        for policy in filtered_policies
    }

    policy_ids = list(
        policy_lookup.keys()
    )

    selected_policy_id = st.selectbox(
        "Open Policy",
        policy_ids,
        label_visibility="collapsed",
        key="selected_knowledge_policy",
    )

    selected_policy = policy_lookup[
        selected_policy_id
    ]

    # =====================================================
    # SELECTED POLICY DATA
    # =====================================================

    policy_id = html.escape(
        _safe_text(
            selected_policy.get("id")
        )
    )

    title = html.escape(
        _safe_text(
            selected_policy.get("title")
        )
    )

    category = html.escape(
        _safe_text(
            selected_policy.get("category")
        )
    )

    content = html.escape(
        _safe_text(
            selected_policy.get("content"),
            "No policy content available.",
        )
    )

    keywords = selected_policy.get(
        "keywords",
        [],
    )

    # =====================================================
    # POLICY HEADER
    # =====================================================

    st.markdown(
        f"""
<div class="resolve-knowledge-detail-header">

<div>
<div class="resolve-knowledge-detail-id">
{policy_id}
</div>

<div class="resolve-knowledge-detail-title">
{title}
</div>
</div>

<div class="resolve-knowledge-verified">
✓ Verified
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # POLICY METADATA
    # =====================================================

    meta1, meta2 = st.columns(2)

    with meta1:

        st.markdown(
            '<div class="resolve-ticket-meta-label">'
            'CATEGORY'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div class="resolve-ticket-meta-value">'
            f'{category}'
            f'</div>',
            unsafe_allow_html=True,
        )

    with meta2:

        st.markdown(
            '<div class="resolve-ticket-meta-label">'
            'KNOWLEDGE TYPE'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="resolve-ticket-meta-value">'
            'Verified Support Policy'
            '</div>',
            unsafe_allow_html=True,
        )

    # =====================================================
    # POLICY CONTENT
    # =====================================================

    st.markdown(
        f"""
<div class="resolve-detail-card">

<div class="resolve-detail-card-header">

<div class="resolve-detail-icon">
◇
</div>

<div>
<div class="resolve-detail-title">
Verified Policy
</div>

<div class="resolve-detail-caption">
Approved support information available to ResolveAI
</div>
</div>

</div>

<div class="resolve-detail-content">
{content}
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # KEYWORDS
    # =====================================================

    keyword_html = ""

    for keyword in keywords:

        safe_keyword = html.escape(
            str(keyword)
        )

        keyword_html += (
            '<span class="resolve-knowledge-keyword">'
            f'{safe_keyword}'
            '</span>'
        )

    st.markdown(
        f"""
<div class="resolve-detail-card">

<div class="resolve-detail-card-header">

<div class="resolve-detail-icon">
⌕
</div>

<div>
<div class="resolve-detail-title">
Retrieval Keywords
</div>

<div class="resolve-detail-caption">
Terms used by ResolveAI policy retrieval
</div>
</div>

</div>

<div class="resolve-knowledge-keywords">
{keyword_html}
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # RETRIEVAL INFORMATION
    # =====================================================

    st.markdown(
        """
<div class="resolve-knowledge-note">

<div class="resolve-knowledge-note-title">
How ResolveAI uses this policy
</div>

<div class="resolve-knowledge-note-text">
ResolveAI matches customer messages against the policy
keywords. Strong and moderate matches may be used as
verified knowledge. Weak matches are not treated as
verified policy answers.
</div>

</div>
""",
        unsafe_allow_html=True,
    )

# =====================================================
    # RETRIEVAL TESTER
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.divider()

    st.markdown(
        '<div class="resolve-label">'
        'RETRIEVAL TESTER'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="resolve-retrieval-heading">
Test ResolveAI Knowledge Retrieval
</div>

<div class="resolve-retrieval-description">
Enter a sample customer message to inspect which policy
ResolveAI retrieves, its relevance score, confidence,
and the exact keywords responsible for the match.
</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # TEST MESSAGE
    # =====================================================

    test_message = st.text_area(
        "Customer message",
        placeholder=(
            "Example: I want a refund for my order..."
        ),
        label_visibility="collapsed",
        key="knowledge_retrieval_message",
        height=100,
    )

    test_clicked = st.button(
        "Analyze Knowledge Match",
        use_container_width=True,
        key="knowledge_retrieval_test",
    )

    # =====================================================
    # RUN RETRIEVAL
    # =====================================================

    if test_clicked:

        cleaned_test_message = (
            test_message.strip()
            if isinstance(test_message, str)
            else ""
        )

        if not cleaned_test_message:

            st.warning(
                "Enter a customer message before "
                "running the retrieval test."
            )

        else:

            retrieval = (
                retrieve_policy_with_confidence(
                    cleaned_test_message
                )
            )

            st.session_state[
                "knowledge_retrieval_result"
            ] = {
                "policy": retrieval.get(
                    "policy"
                ),
                "score": retrieval.get(
                    "score",
                    0,
                ),
                "confidence": retrieval.get(
                    "confidence",
                    "none",
                ),
                "message": cleaned_test_message,
            }

    # =====================================================
    # DISPLAY RETRIEVAL RESULT
    # =====================================================

    retrieval_result = st.session_state.get(
        "knowledge_retrieval_result"
    )

    if retrieval_result:

        matched_policy = retrieval_result.get(
            "policy"
        )

        score = retrieval_result.get(
            "score",
            0,
        )

        confidence = retrieval_result.get(
            "confidence",
            "none",
        )

        tested_message = retrieval_result.get(
            "message",
            "",
        )

        verification_eligible = (
            matched_policy is not None
            and confidence in {
                "strong",
                "moderate",
            }
        )

        # =================================================
        # RESULT HEADER
        # =================================================

        confidence_display = html.escape(
            str(confidence).title()
        )

        if confidence == "strong":

            confidence_class = (
                "resolve-confidence-strong"
            )

        elif confidence == "moderate":

            confidence_class = (
                "resolve-confidence-moderate"
            )

        elif confidence == "weak":

            confidence_class = (
                "resolve-confidence-weak"
            )

        else:

            confidence_class = (
                "resolve-confidence-none"
            )

        st.markdown(
            '<div class="resolve-label">'
            'RETRIEVAL RESULT'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
<div class="resolve-retrieval-result-header">

<div>

<div class="resolve-retrieval-result-title">
Knowledge Match Analysis
</div>

<div class="resolve-retrieval-result-caption">
Result from ResolveAI keyword retrieval
</div>

</div>

<span class="resolve-confidence-badge {confidence_class}">
{confidence_display}
</span>

</div>
""",
            unsafe_allow_html=True,
        )

        # =================================================
        # RESULT METRICS
        # =================================================

        metric1, metric2, metric3 = st.columns(3)

        with metric1:

            st.metric(
                "Relevance Score",
                score,
            )

        with metric2:

            st.metric(
                "Confidence",
                confidence_display,
            )

        with metric3:

            st.metric(
                "Verified Use",
                (
                    "Eligible"
                    if verification_eligible
                    else "Not Eligible"
                ),
            )

        # =================================================
        # NO MATCH
        # =================================================

        if matched_policy is None:

            st.markdown(
                """
<div class="resolve-retrieval-no-match">

<div class="resolve-retrieval-no-match-icon">
⌕
</div>

<div>

<div class="resolve-retrieval-no-match-title">
No policy matched
</div>

<div class="resolve-retrieval-no-match-text">
ResolveAI did not find a policy keyword matching
this customer message.
</div>

</div>

</div>
""",
                unsafe_allow_html=True,
            )

        # =================================================
        # MATCHED POLICY
        # =================================================

        else:

            # =============================================
            # STEP 7.5.3 — DIAGNOSTICS
            # =============================================

            diagnostics = get_retrieval_diagnostics(
                tested_message,
                matched_policy,
            )

            matched_keywords = diagnostics.get(
                "matched_keywords",
                [],
            )

            matched_keyword_count = diagnostics.get(
                "matched_keyword_count",
                0,
            )

            calculated_score = diagnostics.get(
                "calculated_score",
                0,
            )

            # =============================================
            # SAFE POLICY DATA
            # =============================================

            matched_id = html.escape(
                _safe_text(
                    matched_policy.get("id")
                )
            )

            matched_title = html.escape(
                _safe_text(
                    matched_policy.get("title")
                )
            )

            matched_category = html.escape(
                _safe_text(
                    matched_policy.get(
                        "category"
                    )
                )
            )

            matched_content = html.escape(
                _safe_text(
                    matched_policy.get(
                        "content"
                    ),
                    "No policy content available.",
                )
            )

            # =============================================
            # MATCHED POLICY CARD
            # =============================================

            st.markdown(
                f"""
<div class="resolve-retrieval-policy">

<div class="resolve-retrieval-policy-top">

<div>

<div class="resolve-retrieval-policy-id">
{matched_id}
</div>

<div class="resolve-retrieval-policy-title">
{matched_title}
</div>

</div>

<div class="resolve-knowledge-category">
{matched_category}
</div>

</div>

<div class="resolve-retrieval-policy-content">
{matched_content}
</div>

</div>
""",
                unsafe_allow_html=True,
            )

            # =============================================
            # VERIFICATION STATUS
            # =============================================

            if verification_eligible:

                st.markdown(
                    """
<div class="resolve-verification-result
resolve-verification-eligible">

<div class="resolve-verification-symbol">
✓
</div>

<div>

<div class="resolve-verification-title">
Eligible for verified AI response
</div>

<div class="resolve-verification-text">
This policy has strong or moderate retrieval
confidence and may be supplied to ResolveAI as
verified support knowledge.
</div>

</div>

</div>
""",
                    unsafe_allow_html=True,
                )

            elif confidence == "weak":

                st.markdown(
                    """
<div class="resolve-verification-result">

<div class="resolve-verification-symbol">
!
</div>

<div>

<div class="resolve-verification-title">
Weak match — verification blocked
</div>

<div class="resolve-verification-text">
A possible policy was found, but weak confidence
is not sufficient for verified use.
</div>

</div>

</div>
""",
                    unsafe_allow_html=True,
                )

            # =============================================
            # MATCH DIAGNOSTICS
            # =============================================

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(
                '<div class="resolve-label">'
                'MATCH DIAGNOSTICS'
                '</div>',
                unsafe_allow_html=True,
            )

            diagnostic_col1, diagnostic_col2 = (
                st.columns(
                    [2, 1],
                    gap="large",
                )
            )

            # ---------------------------------------------
            # MATCHED KEYWORDS
            # ---------------------------------------------

            with diagnostic_col1:

                st.markdown(
                    """
<div class="resolve-diagnostic-card">

<div class="resolve-diagnostic-title">
Matched Keywords
</div>

<div class="resolve-diagnostic-caption">
Keywords detected in the customer message
</div>
""",
                    unsafe_allow_html=True,
                )

                if matched_keywords:

                    keyword_rows = ""

                    for match in matched_keywords:

                        keyword = html.escape(
                            str(
                                match.get(
                                    "keyword",
                                    "",
                                )
                            )
                        )

                        weight = match.get(
                            "weight",
                            0,
                        )

                        keyword_rows += f"""
<div class="resolve-diagnostic-keyword-row">

<div class="resolve-diagnostic-keyword">
{keyword}
</div>

<div class="resolve-diagnostic-weight">
+{weight}
</div>

</div>
"""

                    st.markdown(
                        keyword_rows,
                        unsafe_allow_html=True,
                    )

                else:

                    st.markdown(
                        """
<div class="resolve-diagnostic-empty">
No matching keywords detected.
</div>
""",
                        unsafe_allow_html=True,
                    )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True,
                )

            # ---------------------------------------------
            # SCORE BREAKDOWN
            # ---------------------------------------------

            with diagnostic_col2:

                st.markdown(
                    f"""
<div class="resolve-diagnostic-card">

<div class="resolve-diagnostic-title">
Score Breakdown
</div>

<div class="resolve-diagnostic-caption">
Current retrieval calculation
</div>

<div class="resolve-diagnostic-stat">
<span>Matched keywords</span>
<strong>{matched_keyword_count}</strong>
</div>

<div class="resolve-diagnostic-stat">
<span>Calculated score</span>
<strong>{calculated_score}</strong>
</div>

<div class="resolve-diagnostic-stat">
<span>Retrieval score</span>
<strong>{score}</strong>
</div>

<div class="resolve-diagnostic-stat">
<span>Confidence</span>
<strong>{confidence_display}</strong>
</div>

</div>
""",
                    unsafe_allow_html=True,
                )

            # =============================================
            # SCORE CONSISTENCY CHECK
            # =============================================

            if calculated_score == score:

                st.markdown(
                    """
<div class="resolve-verification-result
resolve-verification-eligible">

<div class="resolve-verification-symbol">
✓
</div>

<div>

<div class="resolve-verification-title">
Retrieval calculation verified
</div>

<div class="resolve-verification-text">
The diagnostic score matches the score returned
by the production retrieval engine.
</div>

</div>

</div>
""",
                    unsafe_allow_html=True,
                )

            else:

                st.error(
                    "Retrieval diagnostic mismatch: "
                    f"engine score = {score}, "
                    f"diagnostic score = "
                    f"{calculated_score}."
                )

            # =============================================
            # CONFIDENCE THRESHOLD
            # =============================================

            if score >= 3:

                threshold_title = (
                    "Strong verification threshold reached"
                )

                threshold_description = (
                    "The relevance score is 3 or higher, "
                    "so this policy has strong retrieval "
                    "confidence."
                )

            elif score == 2:

                threshold_title = (
                    "Moderate verification threshold reached"
                )

                threshold_description = (
                    "The relevance score is 2. "
                    "ResolveAI permits moderate matches "
                    "to be used as verified knowledge."
                )

            elif score == 1:

                threshold_title = (
                    "Verification threshold not reached"
                )

                threshold_description = (
                    "The relevance score is 1. "
                    "This is a weak match and must not "
                    "be treated as verified knowledge."
                )

            else:

                threshold_title = (
                    "No retrieval confidence"
                )

                threshold_description = (
                    "No matching retrieval evidence "
                    "was detected."
                )

            st.markdown(
                f"""
<div class="resolve-threshold-card">

<div class="resolve-threshold-symbol">
◇
</div>

<div>

<div class="resolve-threshold-title">
{threshold_title}
</div>

<div class="resolve-threshold-description">
{threshold_description}
</div>

</div>

</div>
""",
                unsafe_allow_html=True,
            )

        # =================================================
        # TESTED MESSAGE
        # =================================================

        safe_tested_message = html.escape(
            tested_message
        )

        st.markdown(
            f"""
<div class="resolve-retrieval-tested-message">

<div class="resolve-ticket-meta-label">
TESTED CUSTOMER MESSAGE
</div>

<div>
{safe_tested_message}
</div>

</div>
""",
            unsafe_allow_html=True,
        )
# =====================================================
    # KNOWLEDGE HEALTH & COVERAGE
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.divider()

    st.markdown(
        '<div class="resolve-label">'
        'KNOWLEDGE HEALTH'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="resolve-health-heading">
Knowledge Health & Coverage
</div>

<div class="resolve-health-description">
Inspect the structure and retrieval coverage of the
verified ResolveAI knowledge base.
</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # GENERATE HEALTH DATA
    # =====================================================

    health = generate_knowledge_health()

    total_keywords = health[
        "total_keywords"
    ]

    average_keywords = health[
        "average_keywords"
    ]

    category_distribution = health[
        "category_distribution"
    ]

    low_keyword_policies = health[
        "low_keyword_policies"
    ]

    duplicate_keywords = health[
        "duplicate_keywords"
    ]

    # =====================================================
    # HEALTH METRICS
    # =====================================================

    health_col1, health_col2, health_col3, health_col4 = (
        st.columns(4)
    )

    with health_col1:

        st.metric(
            "Policies",
            health["total_policies"],
        )

    with health_col2:

        st.metric(
            "Categories",
            health["total_categories"],
        )

    with health_col3:

        st.metric(
            "Retrieval Keywords",
            total_keywords,
        )

    with health_col4:

        st.metric(
            "Avg. Keywords / Policy",
            f"{average_keywords:.1f}",
        )

    # =====================================================
    # CATEGORY COVERAGE
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    coverage_col, quality_col = st.columns(
        [1.4, 1],
        gap="large",
    )

    with coverage_col:

        st.markdown(
            """
<div class="resolve-health-card-title">
Category Coverage
</div>

<div class="resolve-health-card-caption">
Number of verified policies available in each category
</div>
""",
            unsafe_allow_html=True,
        )

        if category_distribution:

            st.bar_chart(
                category_distribution
            )

        else:

            st.info(
                "No category data available."
            )

    # =====================================================
    # COVERAGE SUMMARY
    # =====================================================

    with quality_col:

        st.markdown(
            """
<div class="resolve-health-card-title">
Retrieval Coverage
</div>

<div class="resolve-health-card-caption">
Structural checks based on available policy keywords
</div>
""",
            unsafe_allow_html=True,
        )

        policies_needing_keywords = len(
            low_keyword_policies
        )

        shared_keyword_count = len(
            duplicate_keywords
        )

        st.markdown(
            f"""
<div class="resolve-health-summary-card">

<div class="resolve-health-stat">

<div>
Policies with limited keywords
</div>

<strong>
{policies_needing_keywords}
</strong>

</div>


<div class="resolve-health-stat">

<div>
Shared keywords
</div>

<strong>
{shared_keyword_count}
</strong>

</div>


<div class="resolve-health-stat">

<div>
Total retrieval terms
</div>

<strong>
{total_keywords}
</strong>

</div>


<div class="resolve-health-stat">

<div>
Average terms per policy
</div>

<strong>
{average_keywords:.1f}
</strong>

</div>

</div>
""",
            unsafe_allow_html=True,
        )

    # =====================================================
    # POLICIES NEEDING KEYWORD REVIEW
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="resolve-label">'
        'COVERAGE REVIEW'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="resolve-health-card-title">
Policies With Limited Retrieval Keywords
</div>

<div class="resolve-health-card-caption">
Policies containing fewer than three retrieval keywords
</div>
""",
        unsafe_allow_html=True,
    )

    if low_keyword_policies:

        for policy in low_keyword_policies:

            safe_id = html.escape(
                _safe_text(
                    policy.get("id")
                )
            )

            safe_title = html.escape(
                _safe_text(
                    policy.get("title")
                )
            )

            safe_category = html.escape(
                _safe_text(
                    policy.get("category")
                )
            )

            keyword_count = policy.get(
                "keyword_count",
                0,
            )

            st.markdown(
                f"""
<div class="resolve-health-policy-row">

<div>

<div class="resolve-health-policy-id">
{safe_id}
</div>

<div class="resolve-health-policy-title">
{safe_title}
</div>

<div class="resolve-health-policy-category">
{safe_category}
</div>

</div>

<div class="resolve-health-keyword-count">
{keyword_count} keywords
</div>

</div>
""",
                unsafe_allow_html=True,
            )

    else:

        st.markdown(
            """
<div class="resolve-health-good">

<div class="resolve-health-good-symbol">
✓
</div>

<div>

<div class="resolve-health-good-title">
No limited-keyword policies detected
</div>

<div class="resolve-health-good-text">
Every verified policy currently contains at least
three retrieval keywords.
</div>

</div>

</div>
""",
            unsafe_allow_html=True,
        )

    # =====================================================
    # SHARED KEYWORDS
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
<div class="resolve-health-card-title">
Shared Retrieval Keywords
</div>

<div class="resolve-health-card-caption">
Keywords appearing in more than one verified policy.
Shared terms may make keyword-only retrieval less specific.
</div>
""",
        unsafe_allow_html=True,
    )

    if duplicate_keywords:

        for keyword, policy_ids in (
            duplicate_keywords.items()
        ):

            safe_keyword = html.escape(
                str(keyword)
            )

            safe_policy_ids = html.escape(
                ", ".join(
                    str(policy_id)
                    for policy_id
                    in policy_ids
                )
            )

            st.markdown(
                f"""
<div class="resolve-shared-keyword-row">

<div class="resolve-shared-keyword">
{safe_keyword}
</div>

<div class="resolve-shared-policy">
{safe_policy_ids}
</div>

</div>
""",
                unsafe_allow_html=True,
            )

    else:

        st.markdown(
            """
<div class="resolve-health-good">

<div class="resolve-health-good-symbol">
✓
</div>

<div>

<div class="resolve-health-good-title">
No shared retrieval keywords
</div>

<div class="resolve-health-good-text">
No keyword currently appears across multiple policies.
</div>

</div>

</div>
""",
            unsafe_allow_html=True,
        )

# =====================================================
    # STEP 7.5.5.2 — RETRIEVAL CONFLICT ANALYSIS
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.divider()

    st.markdown(
        '<div class="resolve-label">'
        'RETRIEVAL RELIABILITY'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="resolve-conflict-heading">
Retrieval Conflict Analysis
</div>

<div class="resolve-conflict-description">
Test whether the same customer request strongly matches
multiple verified support policies.
</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # CONFLICT TEST INPUT
    # =====================================================

    conflict_message = st.text_area(
        "Conflict analysis message",
        placeholder=(
            "Example: I was charged twice and "
            "I want a refund..."
        ),
        label_visibility="collapsed",
        key="knowledge_conflict_message",
        height=100,
    )

    conflict_clicked = st.button(
        "Analyze Retrieval Conflict",
        use_container_width=True,
        key="knowledge_conflict_test",
    )

    # =====================================================
    # RUN CONFLICT ANALYSIS
    # =====================================================

    if conflict_clicked:

        cleaned_conflict_message = (
            conflict_message.strip()
            if isinstance(
                conflict_message,
                str,
            )
            else ""
        )

        if not cleaned_conflict_message:

            st.warning(
                "Enter a customer message before "
                "running conflict analysis."
            )

        else:

            conflict_result = (
                analyze_retrieval_candidates(
                    cleaned_conflict_message
                )
            )

            # Store result because Streamlit reruns
            # after future widget interactions.
            st.session_state[
                "knowledge_conflict_result"
            ] = {
                "message": (
                    cleaned_conflict_message
                ),
                "analysis": conflict_result,
            }

    # =====================================================
    # LOAD STORED RESULT
    # =====================================================

    stored_conflict_result = (
        st.session_state.get(
            "knowledge_conflict_result"
        )
    )

    if stored_conflict_result:

        tested_conflict_message = (
            stored_conflict_result.get(
                "message",
                "",
            )
        )

        conflict_analysis = (
            stored_conflict_result.get(
                "analysis",
                {},
            )
        )

        candidates = (
            conflict_analysis.get(
                "candidates",
                [],
            )
        )

        best_candidate = (
            conflict_analysis.get(
                "best_candidate"
            )
        )

        competing_candidates = (
            conflict_analysis.get(
                "competing_candidates",
                [],
            )
        )

        ambiguous = conflict_analysis.get(
            "ambiguous",
            False,
        )

        conflict_type = (
            conflict_analysis.get(
                "conflict_type",
                "none",
            )
        )

        score_gap = (
            conflict_analysis.get(
                "score_gap"
            )
        )

        # =================================================
        # NO CANDIDATES
        # =================================================

        if best_candidate is None:

            st.markdown(
                """
<div class="resolve-conflict-empty">

<div class="resolve-conflict-empty-symbol">
⌕
</div>

<div>

<div class="resolve-conflict-empty-title">
No retrieval candidates
</div>

<div class="resolve-conflict-empty-text">
No verified policy received a retrieval score
for this customer message.
</div>

</div>

</div>
""",
                unsafe_allow_html=True,
            )

        else:

            # =================================================
            # SAFE BEST-CANDIDATE VALUES
            # =================================================

            best_title = html.escape(
                _safe_text(
                    best_candidate.get(
                        "title"
                    )
                )
            )

            best_policy_id = html.escape(
                _safe_text(
                    best_candidate.get(
                        "policy_id"
                    )
                )
            )

            best_category = html.escape(
                _safe_text(
                    best_candidate.get(
                        "category"
                    )
                )
            )

            best_score = best_candidate.get(
                "score",
                0,
            )

            best_confidence = html.escape(
                str(
                    best_candidate.get(
                        "confidence",
                        "none",
                    )
                ).title()
            )

            # =================================================
            # CONFLICT STATUS
            # =================================================

            if conflict_type == "tie":

                conflict_label = (
                    "Score Tie"
                )

                conflict_class = (
                    "resolve-conflict-danger"
                )

                conflict_symbol = "!"

            elif conflict_type == "close_match":

                conflict_label = (
                    "Close Match"
                )

                conflict_class = (
                    "resolve-conflict-warning"
                )

                conflict_symbol = "!"

            elif conflict_type == "clear_winner":

                conflict_label = (
                    "Clear Winner"
                )

                conflict_class = (
                    "resolve-conflict-clear"
                )

                conflict_symbol = "✓"

            else:

                conflict_label = (
                    "Single Match"
                )

                conflict_class = (
                    "resolve-conflict-clear"
                )

                conflict_symbol = "✓"

            # =================================================
            # SUMMARY
            # =================================================

            st.markdown(
                '<div class="resolve-label">'
                'ANALYSIS RESULT'
                '</div>',
                unsafe_allow_html=True,
            )

            summary1, summary2, summary3, summary4 = (
                st.columns(4)
            )

            with summary1:

                st.metric(
                    "Candidates",
                    len(candidates),
                )

            with summary2:

                st.metric(
                    "Best Score",
                    best_score,
                )

            with summary3:

                st.metric(
                    "Score Gap",
                    (
                        score_gap
                        if score_gap is not None
                        else "—"
                    ),
                )

            with summary4:

                st.metric(
                    "Competing",
                    len(
                        competing_candidates
                    ),
                )

            # =================================================
            # STATUS BANNER
            # =================================================

            st.markdown(
                f"""
<div class="resolve-conflict-status {conflict_class}">

<div class="resolve-conflict-status-symbol">
{conflict_symbol}
</div>

<div>

<div class="resolve-conflict-status-title">
{conflict_label}
</div>

<div class="resolve-conflict-status-text">
{
    "Multiple policies are competing for this customer request."
    if ambiguous
    else
    "The retrieval engine has a sufficiently distinct leading policy."
}
</div>

</div>

</div>
""",
                unsafe_allow_html=True,
            )

            # =================================================
            # BEST MATCH
            # =================================================

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(
                '<div class="resolve-label">'
                'BEST MATCH'
                '</div>',
                unsafe_allow_html=True,
            )

            st.markdown(
                f"""
<div class="resolve-conflict-best">

<div class="resolve-conflict-best-top">

<div>

<div class="resolve-conflict-policy-id">
{best_policy_id}
</div>

<div class="resolve-conflict-policy-title">
{best_title}
</div>

<div class="resolve-conflict-policy-category">
{best_category}
</div>

</div>

<div class="resolve-conflict-score">
{best_score}
<span>score</span>
</div>

</div>

<div class="resolve-conflict-confidence">
Confidence: {best_confidence}
</div>

</div>
""",
                unsafe_allow_html=True,
            )

            # =================================================
            # BEST MATCH KEYWORDS
            # =================================================

            best_keywords = (
                best_candidate.get(
                    "matched_keywords",
                    [],
                )
            )

            st.markdown(
                """
<div class="resolve-conflict-subheading">
Matched Keywords
</div>
""",
                unsafe_allow_html=True,
            )

            if best_keywords:

                best_keyword_html = ""

                for keyword_data in (
                    best_keywords
                ):

                    safe_keyword = html.escape(
                        str(
                            keyword_data.get(
                                "keyword",
                                "",
                            )
                        )
                    )

                    weight = keyword_data.get(
                        "weight",
                        0,
                    )

                    best_keyword_html += f"""
<div class="resolve-conflict-keyword">
<span>{safe_keyword}</span>
<strong>+{weight}</strong>
</div>
"""

                st.markdown(
                    f"""
<div class="resolve-conflict-keywords">
{best_keyword_html}
</div>
""",
                    unsafe_allow_html=True,
                )

            else:

                st.caption(
                    "No matched keywords recorded."
                )

            # =================================================
            # COMPETING CANDIDATES
            # =================================================

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(
                '<div class="resolve-label">'
                'COMPETING MATCHES'
                '</div>',
                unsafe_allow_html=True,
            )

            if competing_candidates:

                for candidate in (
                    competing_candidates
                ):

                    candidate_title = html.escape(
                        _safe_text(
                            candidate.get(
                                "title"
                            )
                        )
                    )

                    candidate_id = html.escape(
                        _safe_text(
                            candidate.get(
                                "policy_id"
                            )
                        )
                    )

                    candidate_category = (
                        html.escape(
                            _safe_text(
                                candidate.get(
                                    "category"
                                )
                            )
                        )
                    )

                    candidate_score = (
                        candidate.get(
                            "score",
                            0,
                        )
                    )

                    candidate_confidence = (
                        html.escape(
                            str(
                                candidate.get(
                                    "confidence",
                                    "none",
                                )
                            ).title()
                        )
                    )

                    candidate_keywords = (
                        candidate.get(
                            "matched_keywords",
                            [],
                        )
                    )

                    candidate_keyword_html = ""

                    for keyword_data in (
                        candidate_keywords
                    ):

                        safe_keyword = (
                            html.escape(
                                str(
                                    keyword_data.get(
                                        "keyword",
                                        "",
                                    )
                                )
                            )
                        )

                        weight = (
                            keyword_data.get(
                                "weight",
                                0,
                            )
                        )

                        candidate_keyword_html += f"""
<span class="resolve-conflict-mini-keyword">
{safe_keyword} +{weight}
</span>
"""

                    st.markdown(
                        f"""
<div class="resolve-conflict-candidate">

<div class="resolve-conflict-candidate-main">

<div>

<div class="resolve-conflict-policy-id">
{candidate_id}
</div>

<div class="resolve-conflict-candidate-title">
{candidate_title}
</div>

<div class="resolve-conflict-policy-category">
{candidate_category}
</div>

</div>

<div class="resolve-conflict-candidate-score">
{candidate_score}
</div>

</div>

<div class="resolve-conflict-candidate-meta">
{candidate_confidence} confidence
</div>

<div class="resolve-conflict-mini-keywords">
{candidate_keyword_html}
</div>

</div>
""",
                        unsafe_allow_html=True,
                    )

            else:

                st.markdown(
                    """
<div class="resolve-conflict-clear-card">

<div class="resolve-conflict-clear-symbol">
✓
</div>

<div>

<div class="resolve-conflict-clear-title">
No meaningful competing policy
</div>

<div class="resolve-conflict-clear-text">
Other matching policies are not close enough to
the leading policy to be classified as retrieval
competitors.
</div>

</div>

</div>
""",
                    unsafe_allow_html=True,
                )

            # =================================================
            # ALL MATCHING CANDIDATES
            # =================================================

            if len(candidates) > 1:

                with st.expander(
                    "View all matching candidates"
                ):

                    for index, candidate in enumerate(
                        candidates,
                        start=1,
                    ):

                        candidate_title = (
                            _safe_text(
                                candidate.get(
                                    "title"
                                )
                            )
                        )

                        candidate_score = (
                            candidate.get(
                                "score",
                                0,
                            )
                        )

                        candidate_confidence = (
                            str(
                                candidate.get(
                                    "confidence",
                                    "none",
                                )
                            ).title()
                        )

                        st.write(
                            f"**{index}. "
                            f"{candidate_title}**"
                        )

                        st.caption(
                            f"Score: "
                            f"{candidate_score} · "
                            f"Confidence: "
                            f"{candidate_confidence}"
                        )

            # =================================================
            # SAFETY INTERPRETATION
            # =================================================

            st.markdown("<br>", unsafe_allow_html=True)

            if ambiguous:

                st.markdown(
                    """
<div class="resolve-conflict-guidance">

<div class="resolve-conflict-guidance-symbol">
!
</div>

<div>

<div class="resolve-conflict-guidance-title">
Clarification recommended
</div>

<div class="resolve-conflict-guidance-text">
This request has more than one competitive policy match.
The production chatbot should not automatically assume
that the highest-scoring policy represents the customer's
exact intent until the conflict is resolved.
</div>

</div>

</div>
""",
                    unsafe_allow_html=True,
                )

            else:

                st.markdown(
                    """
<div class="resolve-conflict-clear-card">

<div class="resolve-conflict-clear-symbol">
✓
</div>

<div>

<div class="resolve-conflict-clear-title">
Retrieval is sufficiently distinct
</div>

<div class="resolve-conflict-clear-text">
No meaningful policy conflict was detected for this
customer message.
</div>

</div>

</div>
""",
                    unsafe_allow_html=True,
                )

        # =================================================
        # TESTED MESSAGE
        # =================================================

        safe_conflict_message = html.escape(
            tested_conflict_message
        )

        st.markdown(
            f"""
<div class="resolve-retrieval-tested-message">

<div class="resolve-ticket-meta-label">
TESTED CUSTOMER MESSAGE
</div>

<div>
{safe_conflict_message}
</div>

</div>
""",
            unsafe_allow_html=True,
        )