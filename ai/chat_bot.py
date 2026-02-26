import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()
history = []

print("Chatbot ready. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() == 'quit':
        break
    if not user_input:
        continue

    history.append({"role": "user", "content": user_input})

    response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=history
    )

    text = response.content[0].text
    history.append({"role": "assistant", "content": text})

    print(f"Claude: {text}\n")