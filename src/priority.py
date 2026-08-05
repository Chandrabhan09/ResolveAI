"""
ResolveAI Priority Detection
"""

from src.intent import detect_intent
from src.sentiment import detect_sentiment

CRITICAL_INTENTS = {
    "payment",
}

HIGH_INTENTS = {
    "refund",
    "complaint",
}

MEDIUM_INTENTS = {
    "tracking",
    "return",
    "warranty",
    "account",
    "cancellation",
}


CRITICAL_KEYWORDS = [
    "fraud",
    "stolen",
    "unauthorized",
    "scam",
    "security",
    "hack",
]


def detect_priority(user_message):
    """
    Determine the support priority of a customer message.
    """

    if not isinstance(user_message, str):
        return "low"

    message = user_message.lower().strip()

    if not message:
        return "low"

    # ---------------------------------------
    # Critical keywords
    # ---------------------------------------

    for keyword in CRITICAL_KEYWORDS:

        if keyword in message:
            return "critical"

    intent = detect_intent(message)
    sentiment = detect_sentiment(message)

    # ---------------------------------------
    # Critical
    # ---------------------------------------

    if intent in CRITICAL_INTENTS:
        return "critical"

    # ---------------------------------------
    # High
    # ---------------------------------------

    if (
        intent in HIGH_INTENTS
        or sentiment == "negative"
    ):
        return "high"

    # ---------------------------------------
    # Medium
    # ---------------------------------------

    if intent in MEDIUM_INTENTS:
        return "medium"

    # ---------------------------------------
    # Default
    # ---------------------------------------

    return "low"