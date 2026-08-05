"""
ResolveAI Ticket Manager
"""

from src.ticket import (
    load_tickets,
    save_tickets,
)

# =========================================================
# TICKET MANAGER
# =========================================================

class TicketManager:

    def __init__(self):
        self.tickets = []
        self.refresh()

    # =====================================================
    # REFRESH
    # =====================================================

    def refresh(self):
        """
        Reload tickets from persistent storage.
        """

        tickets = load_tickets()

        if isinstance(tickets, list):
            self.tickets = tickets
        else:
            self.tickets = []

        return self.tickets

    # =====================================================
    # GET ALL TICKETS
    # =====================================================

    def get_all_tickets(self):
        """
        Return all currently loaded tickets.
        """

        return self.tickets

    # =====================================================
    # GET TICKET
    # =====================================================

    def get_ticket(self, ticket_id):
        """
        Return a ticket matching the supplied ID.
        """

        if not isinstance(ticket_id, str):
            return None

        ticket_id = ticket_id.strip()

        if not ticket_id:
            return None

        for ticket in self.tickets:

            if not isinstance(ticket, dict):
                continue

            if ticket.get("ticket_id") == ticket_id:
                return ticket

        return None

    # =====================================================
    # ADD TICKET
    # =====================================================

    def add_ticket(self, ticket):
        """
        Add and persist a ticket.
        """

        if not isinstance(ticket, dict):
            return None

        ticket_id = ticket.get(
            "ticket_id"
        )

        if (
            not isinstance(ticket_id, str)
            or not ticket_id.strip()
        ):
            return None

        # Prevent duplicate ticket IDs.
        if self.get_ticket(ticket_id):
            return None

        self.tickets.append(ticket)

        save_tickets(
            self.tickets
        )

        return ticket

    # =====================================================
    # UPDATE STATUS
    # =====================================================

    def update_status(
        self,
        ticket_id,
        status,
    ):
        """
        Update and persist a ticket's status.
        """

        allowed_statuses = {
            "Open",
            "In Progress",
            "Resolved",
        }

        if not isinstance(ticket_id, str):
            return None

        if status not in allowed_statuses:
            return None

        ticket_id = ticket_id.strip()

        if not ticket_id:
            return None

        for ticket in self.tickets:

            if not isinstance(ticket, dict):
                continue

            if ticket.get(
                "ticket_id"
            ) != ticket_id:
                continue

            ticket["status"] = status

            save_tickets(
                self.tickets
            )

            return ticket

        return None

    # =====================================================
    # GET TICKET IDS
    # =====================================================

    def get_ticket_ids(self):
        """
        Return all valid ticket IDs.
        """

        ticket_ids = []

        for ticket in self.tickets:

            if not isinstance(ticket, dict):
                continue

            ticket_id = ticket.get(
                "ticket_id"
            )

            if (
                isinstance(ticket_id, str)
                and ticket_id.strip()
            ):
                ticket_ids.append(
                    ticket_id
                )

        return ticket_ids

    # =====================================================
    # SEARCH TICKETS
    # =====================================================

    def search_tickets(self, keyword):
        """
        Search tickets using customer message,
        ticket ID, intent, priority, or status.
        """

        if keyword is None:
            return self.tickets

        keyword = str(
            keyword
        ).lower().strip()

        if not keyword:
            return self.tickets

        results = []

        for ticket in self.tickets:

            if not isinstance(ticket, dict):
                continue

            searchable_text = " ".join(
                [
                    str(
                        ticket.get(
                            "ticket_id",
                            "",
                        )
                    ),
                    str(
                        ticket.get(
                            "customer_message",
                            "",
                        )
                    ),
                    str(
                        ticket.get(
                            "intent",
                            "",
                        )
                    ),
                    str(
                        ticket.get(
                            "priority",
                            "",
                        )
                    ),
                    str(
                        ticket.get(
                            "status",
                            "",
                        )
                    ),
                ]
            ).lower()

            if keyword in searchable_text:

                results.append(
                    ticket
                )

        return results