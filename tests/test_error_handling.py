from unittest.mock import patch

from src.chatbot import get_chatbot_response
from src.openrouter_client import OpenRouterError


def fake_failure(messages):

    raise OpenRouterError(
        "Simulated unexpected failure"
    )


with patch(
    "src.chatbot.generate_ai_response",
    side_effect=fake_failure,
):

    response = get_chatbot_response(
        "Where is my order?"
    )

    print(response)