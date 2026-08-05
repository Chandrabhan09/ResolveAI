from src.sentiment import detect_sentiment

tests = {
    "Thank you, your support was excellent": "positive",
    "I am very frustrated": "negative",
    "Where is my package?": "neutral",
    "My refund is delayed and I am angry": "negative",
    "Hello": "neutral",
}

for message, expected in tests.items():

    result = detect_sentiment(message)

    print("=" * 40)
    print(message)
    print("Expected :", expected)
    print("Detected :", result)