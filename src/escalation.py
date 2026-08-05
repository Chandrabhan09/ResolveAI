"""
ResolveAI Escalation Engine
"""

from src.intent import detect_intent
from src.priority import detect_priority
from src.sentiment import detect_sentiment

ESCALATION_KEYWORDS = [
    "human",
    "agent",
    "representative",
    "manager",
    "supervisor",
    "fraud",
    "unauthorized",
    "security",
    "legal",
    "lawyer",
    "court",
    "police",
]

def detect_escalation(user_message):
    """
    Determine whether a conversation should be
    escalated to a human support agent.
    """

    if not isinstance(user_message, str):
        return {
            "escalate": False,
            "reason": None,
        }

    message = user_message.lower().strip()

    if not message:
        return {
            "escalate": False,
            "reason": None,
        }

    # -------------------------------------
    # Customer explicitly asks for a human
    # -------------------------------------

    human_requests = [
        "human",
        "talk to a person",
        "real person",
        "customer representative",
        "support agent",
    ]

    for phrase in human_requests:

        if phrase in message:
            return {
                "escalate": True,
                "reason": "Customer requested a human agent.",
            }

    # -------------------------------------
    # High-risk keywords
    # -------------------------------------

    for keyword in ESCALATION_KEYWORDS:

        if keyword in message:
            return {
                "escalate": True,
                "reason": f"High-risk keyword detected: {keyword}",
            }

    intent = detect_intent(message)
    sentiment = detect_sentiment(message)
    priority = detect_priority(message)

    # -------------------------------------
    # Critical priority
    # -------------------------------------

    if priority == "critical":
        return {
            "escalate": True,
            "reason": "Critical priority issue.",
        }

    # -------------------------------------
    # Complaint + Negative
    # -------------------------------------

    if (
        intent == "complaint"
        and sentiment == "negative"
    ):
        return {
            "escalate": True,
            "reason": "Negative customer complaint.",
        }

    return {
        "escalate": False,
        "reason": None,
    }