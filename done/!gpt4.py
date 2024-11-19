import openai
from openai import OpenAI
import os
import sys

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

#append if I say YES!
messages = [
    {"role": "system", "content": "Act as a master python-algorithm solver. You think thoroughtly step by step, carefully read the original directions not to miss details. \nGiven condition is to receive inputs and give outputs."},
    {"role":"user","content": """
"""}
,
]

while True:
    # Get user input
    user_message = input("You: ")

    # Generate response
    messages_with_user_input = messages + [{"role": "user", "content": user_message}]
    completion_response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Make sure to use a currently available model
        messages=messages_with_user_input,
        max_tokens=2500
    )
    response_message = completion_response.choices[0].message.content
    print("#"*50)
    print("Bot: ", response_message)

    # Ask if you want to add the response to the conversation history
    confirm_input = input("Add to history? (yes/no): ")

    if confirm_input.lower() == "yes":
        # Add both user's input and bot's response to the conversation history if confirmed
        messages = messages_with_user_input + [{"role": "assistant", "content": response_message}]