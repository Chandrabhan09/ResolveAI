import streamlit as st

# =========================================================
# CONFIGURATION
# =========================================================

ALLOWED_ROLES = {
    "user",
    "assistant",
}


# =========================================================
# INITIALIZE MEMORY
# =========================================================

def initialize_memory():
    """
    Initialize conversation memory safely.
    """

    messages = st.session_state.get(
        "messages"
    )

    if not isinstance(messages, list):

        st.session_state[
            "messages"
        ] = []


# =========================================================
# GET MESSAGES
# =========================================================

def get_messages():
    """
    Return the current conversation safely.
    """

    initialize_memory()

    return st.session_state[
        "messages"
    ]


# =========================================================
# ADD MESSAGE
# =========================================================

def add_message(
    role,
    content,
):
    """
    Add a valid message to conversation memory.
    """

    initialize_memory()

    if role not in ALLOWED_ROLES:
        return False

    if not isinstance(content, str):
        return False

    cleaned_content = content.strip()

    if not cleaned_content:
        return False

    st.session_state[
        "messages"
    ].append(
        {
            "role": role,
            "content": cleaned_content,
        }
    )

    return True


# =========================================================
# CLEAR MEMORY
# =========================================================

def clear_memory():
    """
    Clear the current conversation.
    """

    st.session_state[
        "messages"
    ] = []