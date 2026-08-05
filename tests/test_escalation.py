from src.escalation import detect_escalation

tests = [
    "I want to speak to a human agent",
    "Someone made an unauthorized payment",
    "Your service is terrible and I am frustrated",
    "Where is my package?",
]

for message in tests:

    result = detect_escalation(message)

    print("=" * 50)
    print(message)
    print(result)