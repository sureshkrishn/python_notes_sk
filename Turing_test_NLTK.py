import nltk
import random

nltk.download("punkt")

# Define a simple chatbot
def chatbot_response(user_input):
    responses = [
        "Hello, how can I help you?",
        "What can I assist you with today?",
        "Nice to meet you! How can I assist?",
    ]
    return random.choice(responses)

# Simulate a conversation
def simulate_conversation():
    print("Welcome to the Turing Test simulation!")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Simulation ended.")
            break

        chatbot_reply = chatbot_response(user_input)
        print("Chatbot:", chatbot_reply)

# Start the conversation simulation
if __name__ == "__main__":
    simulate_conversation()

