import streamlit as st

from src.chatbot import get_chatbot_response
from src.components.analytics_dashboard import (
    render_analytics_dashboard,
)
from src.components.knowledge_dashboard import (
    render_knowledge_dashboard,
)
from src.components.settings_dashboard import render_settings_dashboard
from src.components.ticket_dashboard import (
    render_ticket_dashboard,
)
from src.memory import (
    add_message,
    clear_memory,
    get_messages,
    initialize_memory,
)
from src.support_intelligence import (
    analyze_customer_message,
)
from src.ui.ai_support import (
    render_ai_hero,
    render_conversation_header,
    render_intelligence_empty_state,
    render_intelligence_panel,
    render_quick_actions,
)
from src.ui.sidebar import render_sidebar
from src.ui.theme import apply_resolve_theme

# =========================================================
# RETRIEVAL OBSERVABILITY
# =========================================================

MAX_RETRIEVAL_TRACE_HISTORY = 10


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="ResolveAI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# INITIALIZATION
# =========================================================

apply_resolve_theme()

initialize_memory()

render_sidebar()


# =========================================================
# NEW CONVERSATION
# =========================================================

if st.session_state.pop(
    "request_new_conversation",
    False,
):

    clear_memory()

    keys_to_clear = [
        "last_support_data",
        "last_verified",
        "last_source",
        "last_retrieval_confidence",
        "last_retrieval_ambiguous",
        "last_conflict_type",
        "last_competing_policies",
        "last_retrieval_trace",
    ]

    for key in keys_to_clear:
        st.session_state.pop(
            key,
            None,
        )

    # Retrieval history is intentionally preserved
    # because Analytics uses it across conversations.

    st.rerun()


# =========================================================
# ACTIVE PAGE
# =========================================================

active_page = st.session_state.get(
    "active_page",
    "AI Support",
)


# =========================================================
# AI SUPPORT
# =========================================================

if active_page == "AI Support":

    messages = get_messages()

    support_data = st.session_state.get(
        "last_support_data"
    )

    verified = st.session_state.get(
        "last_verified",
        False,
    )

    source = st.session_state.get(
        "last_source"
    )

    retrieval_confidence = st.session_state.get(
        "last_retrieval_confidence",
        "none",
    )

    retrieval_ambiguous = st.session_state.get(
        "last_retrieval_ambiguous",
        False,
    )

    conflict_type = st.session_state.get(
        "last_conflict_type",
        "none",
    )

    competing_policies = st.session_state.get(
        "last_competing_policies",
        [],
    )

    retrieval_trace = st.session_state.get(
        "last_retrieval_trace",
        {},
    )

    retrieval_trace_history = st.session_state.get(
        "retrieval_trace_history",
        [],
    )

    if not isinstance(
        retrieval_trace_history,
        list,
    ):
        retrieval_trace_history = []

    quick_message = None
    user_message = None

    # =====================================================
    # EMPTY CONVERSATION
    # =====================================================

    if not messages:

        render_ai_hero()

        quick_message = render_quick_actions()

        st.markdown(
            '<div class="resolve-composer-space"></div>',
            unsafe_allow_html=True,
        )

        user_message = st.chat_input(
            "What do you want to know?"
        )

        st.markdown(
            "<br>",
            unsafe_allow_html=True,
        )

        render_intelligence_empty_state()

    # =====================================================
    # ACTIVE CONVERSATION
    # =====================================================

    else:

        render_conversation_header(
            verified=verified,
            source=source,
        )

        chat_col, intelligence_col = st.columns(
            [2.7, 1],
            gap="large",
        )

        # -------------------------------------------------
        # CHAT
        # -------------------------------------------------

        with chat_col:

            for message in messages:

                if not isinstance(
                    message,
                    dict,
                ):
                    continue

                role = message.get(
                    "role",
                    "assistant",
                )

                content = message.get(
                    "content",
                    "",
                )

                with st.chat_message(
                    role
                ):

                    if role == "assistant":

                        st.markdown(
                            """
<div class="resolve-message-label">
◇ RESOLVEAI
</div>
""",
                            unsafe_allow_html=True,
                        )

                    else:

                        st.markdown(
                            """
<div class="resolve-message-label">
YOU
</div>
""",
                            unsafe_allow_html=True,
                        )

                    st.markdown(
                        content
                    )

        # -------------------------------------------------
        # SUPPORT INTELLIGENCE
        # -------------------------------------------------

        with intelligence_col:

            if support_data:

                render_intelligence_panel(
                    support_data=support_data,
                    verified=verified,
                    source=source,
                    retrieval_confidence=(
                        retrieval_confidence
                    ),
                    retrieval_ambiguous=(
                        retrieval_ambiguous
                    ),
                    conflict_type=(
                        conflict_type
                    ),
                    competing_policies=(
                        competing_policies
                    ),
                    retrieval_trace=(
                        retrieval_trace
                    ),
                    retrieval_trace_history=(
                        retrieval_trace_history
                    ),
                )

            else:

                render_intelligence_empty_state()

        user_message = st.chat_input(
            "Ask a follow-up question..."
        )

    # =====================================================
    # QUICK ACTION
    # =====================================================

    if (
        quick_message
        and not user_message
    ):

        user_message = quick_message

    # =====================================================
    # PROCESS MESSAGE
    # =====================================================

    if user_message:

        support_data = (
            analyze_customer_message(
                user_message
            )
        )

        add_message(
            "user",
            user_message,
        )

        with st.spinner(
            "ResolveAI is analyzing your request..."
        ):

            chatbot_result = (
                get_chatbot_response(
                    user_message,
                    get_messages(),
                )
            )

        if not isinstance(
            chatbot_result,
            dict,
        ):
            chatbot_result = {}

        assistant_text = chatbot_result.get(
            "response",
            "Unable to generate a response.",
        )

        verified = chatbot_result.get(
            "verified",
            False,
        )

        source = chatbot_result.get(
            "source"
        )

        retrieval_confidence = chatbot_result.get(
            "retrieval_confidence",
            "none",
        )

        retrieval_ambiguous = chatbot_result.get(
            "retrieval_ambiguous",
            False,
        )

        conflict_type = chatbot_result.get(
            "conflict_type",
            "none",
        )

        competing_policies = chatbot_result.get(
            "competing_policies",
            [],
        )

        retrieval_trace = chatbot_result.get(
            "retrieval_trace",
            {},
        )

        if not isinstance(
            competing_policies,
            list,
        ):
            competing_policies = []

        if not isinstance(
            retrieval_trace,
            dict,
        ):
            retrieval_trace = {}

        # -------------------------------------------------
        # STORE RESPONSE
        # -------------------------------------------------

        add_message(
            "assistant",
            assistant_text,
        )

        # -------------------------------------------------
        # STORE CURRENT INTELLIGENCE
        # -------------------------------------------------

        st.session_state[
            "last_support_data"
        ] = support_data

        st.session_state[
            "last_verified"
        ] = verified

        st.session_state[
            "last_source"
        ] = source

        st.session_state[
            "last_retrieval_confidence"
        ] = retrieval_confidence

        st.session_state[
            "last_retrieval_ambiguous"
        ] = retrieval_ambiguous

        st.session_state[
            "last_conflict_type"
        ] = conflict_type

        st.session_state[
            "last_competing_policies"
        ] = competing_policies

        st.session_state[
            "last_retrieval_trace"
        ] = retrieval_trace

        # -------------------------------------------------
        # STORE RETRIEVAL HISTORY
        # -------------------------------------------------

        if retrieval_trace:

            trace_history = st.session_state.get(
                "retrieval_trace_history",
                [],
            )

            if not isinstance(
                trace_history,
                list,
            ):
                trace_history = []

            trace_history.append(
                retrieval_trace
            )

            st.session_state[
                "retrieval_trace_history"
            ] = trace_history[
                -MAX_RETRIEVAL_TRACE_HISTORY:
            ]

        st.rerun()


# =========================================================
# TICKETS
# =========================================================

elif active_page == "Tickets":

    st.markdown(
        '<div class="resolve-label">'
        'SUPPORT OPERATIONS'
        '</div>',
        unsafe_allow_html=True,
    )

    st.title("Tickets")

    st.caption(
        "Review and manage customer support tickets."
    )

    st.divider()

    render_ticket_dashboard()


# =========================================================
# KNOWLEDGE
# =========================================================

elif active_page == "Knowledge":

    st.markdown(
        '<div class="resolve-label">'
        'VERIFIED KNOWLEDGE'
        '</div>',
        unsafe_allow_html=True,
    )

    st.title("Knowledge")

    st.caption(
        "Browse, inspect, and test the verified "
        "support policies used by ResolveAI."
    )

    st.divider()

    retrieval_trace_history = (
        st.session_state.get(
            "retrieval_trace_history",
            [],
        )
    )

    if not isinstance(
        retrieval_trace_history,
        list,
    ):
        retrieval_trace_history = []

    render_knowledge_dashboard(
        retrieval_trace_history=(
            retrieval_trace_history
        )
    )


# =========================================================
# ANALYTICS
# =========================================================

elif active_page == "Analytics":

    st.markdown(
        '<div class="resolve-label">'
        'SUPPORT INTELLIGENCE'
        '</div>',
        unsafe_allow_html=True,
    )

    st.title("Analytics")

    st.caption(
        "Monitor support operations, knowledge quality, "
        "and retrieval performance."
    )

    st.divider()

    retrieval_trace_history = (
        st.session_state.get(
            "retrieval_trace_history",
            [],
        )
    )

    if not isinstance(
        retrieval_trace_history,
        list,
    ):
        retrieval_trace_history = []

    render_analytics_dashboard(
        retrieval_trace_history=(
            retrieval_trace_history
        )
    )



# =========================================================
# SETTINGS
# =========================================================

elif active_page == "Settings":

    st.markdown(
        '<div class="resolve-label">'
        'SYSTEM'
        '</div>',
        unsafe_allow_html=True,
    )

    st.title(
        "Settings"
    )

    st.caption(
        "Review ResolveAI system configuration "
        "and service status."
    )

    st.divider()

    render_settings_dashboard()
# =========================================================
# FALLBACK
# =========================================================

else:

    st.error(
        "Unknown ResolveAI workspace."
    )