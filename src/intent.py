"""
ResolveAI Intent Detection
"""

INTENT_KEYWORDS = {
    "refund": [
        "refund",
        "money back",
        "refunded",
        "refund pending",
    ],

    "return": [
        "return",
        "send back",
        "replace",
        "exchange",
    ],

    "tracking": [
        "track",
        "tracking",
        "where is my order",
        "package",
        "shipment",
        "delivery",
    ],

    "payment": [
        "payment",
        "charged",
        "transaction",
        "card",
        "billing",
    ],

    "account": [
        "login",
        "password",
        "account",
        "sign in",
        "forgot password",
    ],

    "warranty": [
        "warranty",
        "guarantee",
        "defect",
    ],

    "cancellation": [
        "cancel",
        "cancel order",
        "cancellation",
    ],

    "complaint": [
        "complaint",
        "poor service",
        "bad experience",
        "angry",
        "frustrated",
    ],
}

def detect_intent(user_message):
    """
    Detect the primary customer intent.
    """

    if not isinstance(user_message, str):
        return "general"

    message = user_message.lower().strip()

    if not message:
        return "general"

    best_intent = "general"
    best_score = 0

    for intent, keywords in INTENT_KEYWORDS.items():

        score = 0

        for keyword in keywords:

            if keyword in message:
                score += 1

        if score > best_score:
            best_score = score
            best_intent = intent

    return best_intent