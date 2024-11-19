import openai
from openai import OpenAI
import os

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Act as a master algorithm solver."},
        {
            "role": "user",
            "content": """
import openai
from openai import OpenAI
import os

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

# Start the conversation with an empty messages list
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]

while True:
    # Get user input and add it to the conversation history
    user_message = input("You: ")
    messages.append({"role": "user", "content": user_message})

    # Generate response
    completion_response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Make sure to use a currently available model
        messages=messages
    )
    response_message = completion_response.choices[0].message.content
    print("Bot: ", response_message)

    # Ask if you want to add the response to the conversation history
    confirm_input = input("Add to history? (yes/no): ")

    if confirm_input.lower() == "yes":
        # Add bot's response to the conversation history if confirmed
        messages.append({"role": "assistant", "content": response_message})
###

This is my current code. This works generally okay, but there is a problem. If i say no to the gpt response, it will only add my input, which makes it weird. make it so that it will also remove my message from the history too. I know that this might make a big change.
"""
        }
    ]
)

print(completion.choices[0].message.content)