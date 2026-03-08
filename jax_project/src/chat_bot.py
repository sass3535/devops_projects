"""
Terminal based chatbot leveraging Anthropic API.
All configuration logic is loaded via a .env file, allowing for user customization.
"""
import os
import anthropic
from dotenv import load_dotenv


def load_config() -> dict:
    """Load and return configuration values from .env file."""
    load_dotenv()
    return {
        "model_name": os.getenv("MODEL_NAME"),
        "max_tokens": int(os.getenv("MAX_TOKENS")),
        "system_prompt": os.getenv("SYSTEM"),
    }

def create_client() -> anthropic.Anthropic:
    """Create and return an authenticated Anthropic client."""
    return anthropic.Anthropic()


def get_user_input() -> str | None:
    """Prompt user for input. Returns None if user wants to quit."""
    user_input = input("You: ").strip()
    if user_input.lower() == "quit":
        return None
    return user_input or ""


def receive_response(client: anthropic.Anthropic, config: dict, history: list) -> str:
    """Send conversation history to the API and return the reply text."""
    response = client.messages.create(
        model=config["model_name"],
        max_tokens=config["max_tokens"],
        system=config["system_prompt"],
        messages=history,
    )
    return response.content[0].text


def run_chat_bot():
    """Run the interactive terminal chat loop."""
    config = load_config()
    client = create_client()
    history = []

    print("Chatbot ready. Type 'quit' to exit.\n")

    while True:
        user_input = get_user_input()
        if user_input is None:
            break
        if not user_input:
            continue

        history.append({"role": "user", "content": user_input})
        reply = receive_response(client, config, history)
        history.append({"role": "assistant", "content": reply})
        print(f"Claude: {reply}\n")


if __name__ == "__main__":
    run_chat_bot()
