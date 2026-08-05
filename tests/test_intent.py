from src.intent import detect_intent

tests = {
    "I want my money back": "refund",
    "Where is my package": "tracking",
    "I forgot my password": "account",
    "Cancel my order": "cancellation",
    "Your service is terrible": "complaint",
    "Hello": "general",
}

for message, expected in tests.items():

    result = detect_intent(message)

    print("=" * 40)
    print(message)
    print("Expected :", expected)
    print("Detected :", result)