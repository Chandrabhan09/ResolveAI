"""
ResolveAI Conversation Summary
"""

from src.support_intelligence import (
    analyze_customer_message,
)


def generate_summary(customer_message):
    """
    Generate a concise support summary.
    """

    analysis = analyze_customer_message(
        customer_message
    )

    summary = (
        f"Customer contacted support regarding "
        f"{analysis['intent']}. "
        f"Detected sentiment: "
        f"{analysis['sentiment']}. "
        f"Priority: {analysis['priority']}. "
    )

    if analysis["escalation"]:

        summary += (
            "Human escalation required."
        )

    else:

        summary += (
            "No human escalation required."
        )

    return {
        "summary": summary,
        "analysis": analysis,
    }


