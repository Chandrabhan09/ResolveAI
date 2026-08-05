"""
ResolveAI Support Intelligence Pipeline
"""

from src.escalation import detect_escalation
from src.intent import detect_intent
from src.priority import detect_priority
from src.sentiment import detect_sentiment


def analyze_customer_message(user_message):
    """
    Analyze a customer message and return
    support intelligence.
    """

    intent = detect_intent(user_message)

    sentiment = detect_sentiment(user_message)

    priority = detect_priority(user_message)

    escalation = detect_escalation(user_message)

    return {
        "intent": intent,
        "sentiment": sentiment,
        "priority": priority,
        "escalation": escalation["escalate"],
        "escalation_reason": escalation["reason"],
    }