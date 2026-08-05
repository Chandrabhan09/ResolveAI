import os

import streamlit as st

# =========================================================
# SETTINGS DASHBOARD
# =========================================================

def render_settings_dashboard():
    """
    Render ResolveAI system configuration and status.
    """

    api_configured = bool(
        os.getenv("OPENROUTER_API_KEY")
    )

    # =====================================================
    # SYSTEM STATUS
    # =====================================================

    st.subheader("System Status")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Application",
            "Operational",
        )

    with col2:
        st.metric(
            "AI Service",
            (
                "Configured"
                if api_configured
                else "Not Configured"
            ),
        )

    with col3:
        st.metric(
            "Knowledge System",
            "Active",
        )

    # =====================================================
    # AI CONFIGURATION
    # =====================================================

    st.divider()

    st.subheader("AI Configuration")

    st.caption(
        "AI provider configuration used by "
        "ResolveAI customer support."
    )

    ai_col1, ai_col2 = st.columns(2)

    with ai_col1:
        st.markdown("**Provider**")
        st.write("OpenRouter")

    with ai_col2:
        st.markdown("**API Key**")

        if api_configured:
            st.success(
                "Configured"
                
            )
        else:
            st.warning(
                "OPENROUTER_API_KEY is not configured."
            )

    # =====================================================
    # KNOWLEDGE CONFIGURATION
    # =====================================================

    st.divider()

    st.subheader("Knowledge Configuration")

    st.caption(
        "Verified company knowledge used to ground "
        "ResolveAI responses."
    )

    knowledge_col1, knowledge_col2 = st.columns(2)

    with knowledge_col1:
        st.markdown("**Knowledge Mode**")
        st.write("Verified policy retrieval")

    with knowledge_col2:
        st.markdown("**Verification**")
        st.write("Enabled")

    # =====================================================
    # RETRIEVAL CONFIGURATION
    # =====================================================

    st.divider()

    st.subheader("Retrieval Configuration")

    st.caption(
        "ResolveAI evaluates local verified knowledge "
        "before generating AI responses."
    )

    retrieval_col1, retrieval_col2 = st.columns(2)

    with retrieval_col1:
        st.markdown("**Decision Tracing**")
        st.write("Enabled")

    with retrieval_col2:
        st.markdown("**Conflict Detection**")
        st.write("Enabled")

    # =====================================================
    # DATA & PRIVACY
    # =====================================================

    st.divider()

    st.subheader("Data & Privacy")

    st.caption(
        "Operational information about local "
        "ResolveAI data."
    )

    st.info(
        "Support tickets and verified knowledge are "
        "stored locally by this ResolveAI deployment."
    )

    # =====================================================
    # APPLICATION
    # =====================================================

    st.divider()

    st.subheader("Application")

    app_col1, app_col2 = st.columns(2)

    with app_col1:
        st.markdown("**Product**")
        st.write("ResolveAI")

    with app_col2:
        st.markdown("**Workspace**")
        st.write("Support Intelligence")

    st.caption(
        "ResolveAI — AI-powered customer support "
        "intelligence platform."
    )