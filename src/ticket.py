"""
ResolveAI Ticket System
"""

import json
from datetime import datetime
from pathlib import Path

from src.summary import generate_summary

# =========================================================
# CONFIGURATION
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

TICKET_FILE = DATA_DIR / "tickets.json"


# =========================================================
# TICKET STORAGE ERROR
# =========================================================

class TicketStorageError(Exception):
    """Controlled ticket persistence error."""



# =========================================================
# LOAD TICKETS
# =========================================================

def load_tickets():
    """
    Load support tickets from persistent storage.

    Missing files return an empty ticket list.
    Invalid storage raises a controlled error.
    """

    if not TICKET_FILE.exists():
        return []

    try:

        with open(
            TICKET_FILE,
            "r",
            encoding="utf-8",
        ) as file:

            tickets = json.load(file)

    except json.JSONDecodeError as exc:

        raise TicketStorageError(
            "Ticket storage contains invalid JSON."
        ) from exc

    except OSError as exc:

        raise TicketStorageError(
            "Ticket storage could not be read."
        ) from exc

    if not isinstance(tickets, list):

        raise TicketStorageError(
            "Ticket storage must contain a list."
        )

    return [
        ticket
        for ticket in tickets
        if isinstance(ticket, dict)
    ]


# =========================================================
# SAVE TICKETS
# =========================================================

def save_tickets(tickets):
    """
    Safely save tickets to disk.

    Data is first written to a temporary file and then
    atomically moved into the real ticket file.
    """

    if not isinstance(tickets, list):

        raise TicketStorageError(
            "Tickets must be provided as a list."
        )

    clean_tickets = [
        ticket
        for ticket in tickets
        if isinstance(ticket, dict)
    ]

    try:

        DATA_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        temporary_file = TICKET_FILE.with_suffix(
            ".json.tmp"
        )

        with open(
            temporary_file,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                clean_tickets,
                file,
                indent=4,
                ensure_ascii=False,
            )

            file.flush()

        temporary_file.replace(
            TICKET_FILE
        )

    except (
        OSError,
        TypeError,
        ValueError,
    ) as exc:

        raise TicketStorageError(
            "Tickets could not be saved."
        ) from exc


# =========================================================
# GENERATE TICKET ID
# =========================================================

def generate_ticket_id(
    tickets=None,
):
    """
    Generate a unique support ticket ID.

    Format:
    RES-YYYYMMDD-0001
    """

    if tickets is None:
        tickets = load_tickets()

    if not isinstance(tickets, list):
        tickets = []

    today = datetime.now().strftime(
        "%Y%m%d"
    )

    prefix = f"RES-{today}-"

    highest_sequence = 0

    for ticket in tickets:

        if not isinstance(ticket, dict):
            continue

        ticket_id = ticket.get(
            "ticket_id"
        )

        if not isinstance(
            ticket_id,
            str,
        ):
            continue

        if not ticket_id.startswith(
            prefix
        ):
            continue

        sequence_text = ticket_id[
            len(prefix):
        ]

        try:

            sequence = int(
                sequence_text
            )

        except ValueError:

            continue

        highest_sequence = max(
            highest_sequence,
            sequence,
        )

    next_sequence = (
        highest_sequence + 1
    )

    return (
        f"{prefix}"
        f"{next_sequence:04d}"
    )


# =========================================================
# CREATE TICKET
# =========================================================

def create_ticket(
    customer_message,
    intent,
    sentiment,
    priority,
    escalation_reason,
    summary=None,
):
    """
    Create and persist a new support ticket.
    """

    if not isinstance(
        customer_message,
        str,
    ) or not customer_message.strip():

        raise ValueError(
            "Customer message is required."
        )

    tickets = load_tickets()

    ticket = {
        "ticket_id": generate_ticket_id(
            tickets
        ),
        "created_at": (
            datetime.now().isoformat()
        ),
        "status": "Open",
        "customer_message": (
            customer_message.strip()
        ),
        "intent": intent,
        "sentiment": sentiment,
        "priority": priority,
        "escalation_reason": (
            escalation_reason
        ),
    }

    if (
        isinstance(summary, str)
        and summary.strip()
    ):

        ticket["summary"] = (
            summary.strip()
        )

    tickets.append(ticket)

    save_tickets(tickets)

    return ticket


# =========================================================
# AUTO CREATE TICKET
# =========================================================

def auto_create_ticket(
    customer_message,
):
    """
    Automatically create a ticket when
    escalation is required.
    """

    if not isinstance(
        customer_message,
        str,
    ) or not customer_message.strip():

        return None

    summary_data = generate_summary(
        customer_message.strip()
    )

    if not isinstance(
        summary_data,
        dict,
    ):
        return None

    analysis = summary_data.get(
        "analysis"
    )

    if not isinstance(
        analysis,
        dict,
    ):
        return None

    if not analysis.get(
        "escalation",
        False,
    ):
        return None

    summary = summary_data.get(
        "summary"
    )

    return create_ticket(
        customer_message=(
            customer_message
        ),
        intent=analysis.get(
            "intent",
            "unknown",
        ),
        sentiment=analysis.get(
            "sentiment",
            "neutral",
        ),
        priority=analysis.get(
            "priority",
            "Medium",
        ),
        escalation_reason=analysis.get(
            "escalation_reason"
        ),
        summary=summary,
    )