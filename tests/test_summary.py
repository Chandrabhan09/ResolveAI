from src.summary import generate_summary

tests = [
    "I want my refund.",
    "Where is my package?",
    "I forgot my password.",
    "Someone made an unauthorized payment.",
]

for message in tests:

    print("=" * 60)
    print(message)
    print(generate_summary(message))