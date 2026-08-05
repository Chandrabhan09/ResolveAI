from unittest.mock import patch

from src.chatbot import get_chatbot_response


def test_verified_response():

    with patch(
        "src.chatbot.generate_ai_response",
        return_value=(
            "Approved refunds normally take "
            "5 to 7 business days."
        ),
    ):

        result = get_chatbot_response(
            "My refund is pending and I want my money back."
        )

    print("\n--- VERIFIED TEST ---")
    print("Response:", result["response"])
    print("Verified:", result["verified"])
    print("Source:", result["source"])
    print("Policy ID:", result["policy_id"])
    print("Category:", result["category"])
    print(
        "Confidence:",
        result["retrieval_confidence"],
    )


def test_unverified_response():

    with patch(
        "src.chatbot.generate_ai_response",
        return_value=(
            "This is a mocked AI response."
        ),
    ):

        result = get_chatbot_response(
            "What is the capital of Japan?"
        )

    print("\n--- UNVERIFIED TEST ---")
    print("Response:", result["response"])
    print("Verified:", result["verified"])
    print("Source:", result["source"])
    print("Policy ID:", result["policy_id"])
    print("Category:", result["category"])
    print(
        "Confidence:",
        result["retrieval_confidence"],
    )


if __name__ == "__main__":

    test_verified_response()
    test_unverified_response()