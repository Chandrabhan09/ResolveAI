from pathlib import Path

"""
ResolveAI Analytics Engine
"""

from collections import Counter

from src.ticket import load_tickets

BASE_DIR = Path(__file__).resolve().parent.parent
TICKET_FILE = BASE_DIR / "data" / "tickets.json"


def generate_analytics():
    """
    Generate ticket analytics.
    """

    tickets = load_tickets()

    status_counter = Counter()
    priority_counter = Counter()
    intent_counter = Counter()

    for ticket in tickets:

        status_counter[ticket.get("status", "Unknown")] += 1
        priority_counter[ticket.get("priority", "Unknown")] += 1
        intent_counter[ticket.get("intent", "Unknown")] += 1

    analytics = {
        "total_tickets": len(tickets),
        "status": dict(status_counter),
        "priority": dict(priority_counter),
        "intent": dict(intent_counter),
    }

    return analytics

def generate_support_insights():
    """
    Generate useful support insights from ticket data.
    """

    tickets = load_tickets()

    if not tickets:
        return {
            "most_common_intent": "N/A",
            "most_common_priority": "N/A",
            "escalated_tickets": 0,
            "escalation_rate": 0.0,
        }

    intent_counter = Counter()
    priority_counter = Counter()
    escalated_tickets = 0

    for ticket in tickets:

        intent = ticket.get("intent", "Unknown")
        priority = ticket.get("priority", "Unknown")

        intent_counter[intent] += 1
        priority_counter[priority] += 1

        if ticket.get("escalation_reason"):
            escalated_tickets += 1

    most_common_intent = intent_counter.most_common(1)[0][0]

    most_common_priority = priority_counter.most_common(1)[0][0]

    escalation_rate = (
        escalated_tickets / len(tickets)
    ) * 100

    return {
        "most_common_intent": most_common_intent,
        "most_common_priority": most_common_priority,
        "escalated_tickets": escalated_tickets,
        "escalation_rate": escalation_rate,
    }

def get_analytics_metadata():
    """
    Return metadata about the analytics data source.
    """

    if not TICKET_FILE.exists():
        return {
            "last_updated": None,
        }

    modified_time = TICKET_FILE.stat().st_mtime

    return {
        "last_updated": modified_time,
    }