"""
ResolveAI Premium Navigation Sidebar
"""

import streamlit as st


def initialize_navigation():
    """Initialize active ResolveAI workspace."""

    if "active_page" not in st.session_state:
        st.session_state.active_page = "AI Support"


def navigation_button(label, icon, page_name):
    """Render a navigation button."""

    active = st.session_state.active_page == page_name

    if st.button(
        f"{icon}  {label}",
        key=f"nav_{page_name}",
        use_container_width=True,
        type="primary" if active else "secondary",
    ):
        st.session_state.active_page = page_name
        st.rerun()


def render_sidebar():
    """Render the ResolveAI premium sidebar."""

    initialize_navigation()

    with st.sidebar:

        
        st.markdown(
            '<div class="resolve-brand">'
            '<div class="resolve-logo">✦</div>'
            '<div class="resolve-brand-text">'
            '<div class="resolve-brand-name">ResolveAI</div>'
            '<div class="resolve-brand-subtitle">AI Support Intelligence</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True,
        )        

        # =================================================
        # NEW CONVERSATION
        # =================================================

        if st.button(
            "＋  New Conversation",
            key="sidebar_new_conversation",
            use_container_width=True,
        ):
            st.session_state.active_page = "AI Support"
            st.session_state["request_new_conversation"] = True
            st.rerun()

        # =================================================
        # WORKSPACE
        # =================================================

        st.markdown(
            '<div class="sidebar-section-label">'
            'WORKSPACE'
            '</div>',
            unsafe_allow_html=True,
        )

        navigation_button(
            "AI Support",
            "✦",
            "AI Support",
        )

        navigation_button(
            "Tickets",
            "▣",
            "Tickets",
        )

        navigation_button(
            "Knowledge",
            "◇",
            "Knowledge",
        )

        navigation_button(
            "Analytics",
            "⌁",
            "Analytics",
        )

        # =================================================
        # DIVIDER
        # =================================================

        st.markdown(
            '<div class="sidebar-divider"></div>',
            unsafe_allow_html=True,
        )

        # =================================================
        # SYSTEM
        # =================================================

        st.markdown(
            '<div class="sidebar-section-label">'
            'SYSTEM'
            '</div>',
            unsafe_allow_html=True,
        )

        navigation_button(
            "Settings",
            "⚙",
            "Settings",
        )

        # =================================================
        # FOOTER
        # =================================================

        st.markdown(
            '<div class="sidebar-footer">'
            '<div class="sidebar-status-dot"></div>'
            '<div>'
            '<div class="sidebar-status-title">'
            'ResolveAI'
            '</div>'
            '<div class="sidebar-status-text">'
            'System operational'
            '</div>'
            '</div>'
            '</div>',
            unsafe_allow_html=True,
        )