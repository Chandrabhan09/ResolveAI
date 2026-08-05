"""
ResolveAI Analytics Export
"""

import csv
import io
import json

from src.analytics import (
    generate_analytics,
    generate_support_insights,
)
from src.ticket import load_tickets


def export_tickets_csv():
    """
    Convert stored tickets into CSV text.
    """

    tickets = load_tickets()

    if not tickets:
        return ""

    fields = [
        "ticket_id",
        "created_at",
        "status",
        "priority",
        "intent",
        "sentiment",
        "customer_message",
        "summary",
        "escalation_reason",
    ]

    output = io.StringIO()

    writer = csv.DictWriter(
        output,
        fieldnames=fields,
        extrasaction="ignore",
    )

    writer.writeheader()

    for ticket in tickets:
        writer.writerow({
            field: ticket.get(field, "")
            for field in fields
        })

    return output.getvalue()


def export_analytics_json():
    """
    Export analytics and support insights as JSON.
    """

    data = {
        "analytics": generate_analytics(),
        "support_insights": generate_support_insights(),
    }

    return json.dumps(
        data,
        indent=4,
    )