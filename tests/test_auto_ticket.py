from src.ticket import auto_create_ticket

messages = [
    "Where is my package?",
    "I forgot my password.",
    "Someone made an unauthorized payment using my card",
    "I want to speak to a human agent",
]

for message in messages:

    print("=" * 60)
    print(message)

    ticket = auto_create_ticket(message)

    print(ticket)