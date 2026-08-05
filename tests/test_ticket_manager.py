from src.ticket_manager import TicketManager

tm = TicketManager()

print("=" * 50)
print("All Tickets")
print(tm.get_all_tickets())

print("=" * 50)
print("Single Ticket")
print(tm.get_ticket("RES-20260803-0001"))

print("=" * 50)
print("Status Update")
print(
    tm.update_status(
        "RES-20260803-0001",
        "Resolved",
    )
)