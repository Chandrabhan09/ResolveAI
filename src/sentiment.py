"""
ResolveAI Sentiment Analysis
"""

POSITIVE_KEYWORDS = [
    "thanks",
    "thank you",
    "great",
    "good",
    "excellent",
    "awesome",
    "love",
    "happy",
    "perfect",
    "resolved",
]

NEGATIVE_KEYWORDS = [
    "bad",
    "terrible",
    "angry",
    "frustrated",
    "refund",
    "complaint",
    "poor",
    "issue",
    "problem",
    "delay",
    "late",
    "broken",
    "worst",
    "hate",
    "unacceptable",
]
def detect_sentiment(user_message):
    """
    Detect customer sentiment.
    """

    if not isinstance(user_message, str):
        return "neutral"

    message = user_message.lower().strip()

    if not message:
        return "neutral"

    positive_score = 0
    negative_score = 0

    for keyword in POSITIVE_KEYWORDS:

        if keyword in message:
            positive_score += 1

    for keyword in NEGATIVE_KEYWORDS:

        if keyword in message:
            negative_score += 1

    if positive_score > negative_score:
        return "positive"

    if negative_score > positive_score:
        return "negative"

    return "neutral"