import os

import requests
from dotenv import load_dotenv

# =========================================================
# ENVIRONMENT CONFIGURATION
# =========================================================

load_dotenv()

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)

OPENROUTER_URL = (
    "https://openrouter.ai/api/v1/chat/completions"
)

OPENROUTER_MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "openrouter/free",
)

DEFAULT_TIMEOUT = 30

try:
    OPENROUTER_TIMEOUT = int(
        os.getenv(
            "OPENROUTER_TIMEOUT",
            str(DEFAULT_TIMEOUT),
        )
    )

except (TypeError, ValueError):
    OPENROUTER_TIMEOUT = DEFAULT_TIMEOUT

if OPENROUTER_TIMEOUT <= 0:
    OPENROUTER_TIMEOUT = DEFAULT_TIMEOUT


# =========================================================
# CUSTOM EXCEPTION
# =========================================================

class OpenRouterError(Exception):
    """Controlled OpenRouter service error."""



# =========================================================
# MESSAGE VALIDATION
# =========================================================

def _validate_messages(messages):
    """
    Validate messages before sending them
    to the external AI service.
    """

    if not isinstance(messages, list):
        raise OpenRouterError(
            "Messages must be provided as a list."
        )

    if not messages:
        raise OpenRouterError(
            "Messages cannot be empty."
        )

    allowed_roles = {
        "system",
        "user",
        "assistant",
    }

    for message in messages:

        if not isinstance(message, dict):
            raise OpenRouterError(
                "AI message format is invalid."
            )

        role = message.get("role")
        content = message.get("content")

        if role not in allowed_roles:
            raise OpenRouterError(
                "AI message role is invalid."
            )

        if (
            not isinstance(content, str)
            or not content.strip()
        ):
            raise OpenRouterError(
                "AI message content is invalid."
            )


# =========================================================
# OPENROUTER CLIENT
# =========================================================

def generate_ai_response(messages):
    """
    Send validated messages to OpenRouter and
    return the assistant response.

    External-service failures are converted into
    controlled OpenRouterError exceptions.
    """

    # -----------------------------------------------------
    # CONFIGURATION VALIDATION
    # -----------------------------------------------------

    if (
        not isinstance(OPENROUTER_API_KEY, str)
        or not OPENROUTER_API_KEY.strip()
    ):
        raise OpenRouterError(
            "API key is not configured."
        )

    # -----------------------------------------------------
    # MESSAGE VALIDATION
    # -----------------------------------------------------

    _validate_messages(messages)

    # -----------------------------------------------------
    # REQUEST
    # -----------------------------------------------------

    headers = {
        "Authorization": (
            f"Bearer {OPENROUTER_API_KEY.strip()}"
        ),
        "Content-Type": "application/json",
    }

    payload = {
        "model": OPENROUTER_MODEL,
        "messages": messages,
    }

    try:

        response = requests.post(
            OPENROUTER_URL,
            headers=headers,
            json=payload,
            timeout=OPENROUTER_TIMEOUT,
        )

    except requests.Timeout as exc:

        raise OpenRouterError(
            "AI service request timed out."
        ) from exc

    except requests.ConnectionError as exc:

        raise OpenRouterError(
            "Unable to connect to the AI service."
        ) from exc

    except requests.RequestException as exc:

        raise OpenRouterError(
            "AI service request failed."
        ) from exc

    # =====================================================
    # HTTP STATUS HANDLING
    # =====================================================

    if response.status_code == 400:

        raise OpenRouterError(
            "AI service rejected the request."
        )

    if response.status_code in {
        401,
        403,
    }:

        raise OpenRouterError(
            "AI authentication failed."
        )

    if response.status_code == 408:

        raise OpenRouterError(
            "AI service request timed out."
        )

    if response.status_code == 429:

        raise OpenRouterError(
            "AI service rate limit reached."
        )

    if response.status_code >= 500:

        raise OpenRouterError(
            "AI service is temporarily unavailable."
        )

    if not response.ok:

        raise OpenRouterError(
            "AI service returned an unexpected error."
        )

    # =====================================================
    # RESPONSE VALIDATION
    # =====================================================

    try:

        data = response.json()

    except ValueError as exc:

        raise OpenRouterError(
            "AI service returned invalid data."
        ) from exc

    if not isinstance(data, dict):

        raise OpenRouterError(
            "AI service returned invalid data."
        )

    choices = data.get("choices")

    if (
        not isinstance(choices, list)
        or not choices
    ):

        raise OpenRouterError(
            "AI service returned no response."
        )

    first_choice = choices[0]

    if not isinstance(first_choice, dict):

        raise OpenRouterError(
            "AI service returned an invalid response."
        )

    message = first_choice.get("message")

    if not isinstance(message, dict):

        raise OpenRouterError(
            "AI service returned an invalid message."
        )

    content = message.get("content")

    if (
        not isinstance(content, str)
        or not content.strip()
    ):

        raise OpenRouterError(
            "AI service returned an empty response."
        )

    return content.strip()