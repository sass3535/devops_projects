"""
Terminal based chatbot leveraging Anthropic API. 
All configuration logic is loaded via a .env file, allowing for user customization.

"""
import os
import anthropic
from dotenv import load_dotenv

#Load and return configuration values, uses .env via load_dotenv()
def load_config():
    
    load_dotenv()
    
    return {

    "model_name" : os.getenv("MODEL_NAME"),
    "max_tokens": int(os.getenv("MAX_TOKENS")) ,
    "system_prompt": os.getenv("SYSTEM")
    
    }

#Client function for calling Anthropic SDK and authenticating
def create_client():
    return anthropic.Anthropic()

def get_input():
    return input("You: ").strip()
    or 
    return None if input =='quit'

# #Single conversational history stored in list object
# history = []

# #Global environment variables utilizing .env
# model_name = os.getenv("MODEL_NAME")
# max_tokens = int(os.getenv("MAX_TOKENS"))
# system_prompt = os.getenv("SYSTEM")

#Print statement for user input prompt
print("Chatbot ready. Type 'quit' to exit.\n")

#While loop, calls Anthropic messages API, if user inputs 'quit' chatbot closes
while True:
    user_input = input("You: ").strip()
    if user_input.lower() == 'quit':
        break
    if not user_input:
        continue

    history.append({"role": "user", "content": user_input})

    response = client.messages.create(
    model=model_name,
    max_tokens=max_tokens,
    system=system_prompt,
    messages=history
    )

    text = response.content[0].text
    history.append({"role": "assistant", "content": text})

    print(f"Claude: {text}\n")