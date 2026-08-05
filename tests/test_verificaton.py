from src.knowledge_base import retrieve_policy_with_confidence

tests = [
    "My refund is pending.",
    "I forgot my password.",
    "Someone used my card.",
    "What is the capital of Japan?"
]

for text in tests:

    result = retrieve_policy_with_confidence(text)

    print("=" * 50)
    print(text)
    print(result)