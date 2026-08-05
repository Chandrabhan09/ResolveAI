from src.support_intelligence import analyze_customer_message

tests = [
    "I want my refund",
    "Where is my package?",
    "I forgot my password",
    "Someone made an unauthorized payment",
    "Your service is terrible",
]

for message in tests:

    print("=" * 60)
    print(message)
    print(analyze_customer_message(message))