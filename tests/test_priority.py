from src.priority import detect_priority

tests = {
    "I want my refund": "high",
    "Where is my package?": "medium",
    "I forgot my password": "medium",
    "Someone made an unauthorized payment": "critical",
    "I am very frustrated": "high",
    "Hello": "low",
}

for message, expected in tests.items():

    result = detect_priority(message)

    print("=" * 40)
    print(message)
    print("Expected :", expected)
    print("Detected :", result)