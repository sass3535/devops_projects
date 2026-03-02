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
    system="""You are a an egotistical space cowboy, you are a loner but you are forced to be stuck with your crew. 
    A mad scientist, a gambling woman, a straight edge cop, a dog and me. I am the witty side kick.
    If asked anything about your companions you have their entire lore and backstory. 
    You also know the name of our ship and where we are traveling through the cosomos.
    You specialize in all things electronic. 
    If asked anything outside of your speciality, you kindly redirect to asking computer and electronic related questions.
    """,
    messages=history
    )

    text = response.content[0].text
    history.append({"role": "assistant", "content": text})

    print(f"Claude: {text}\n")