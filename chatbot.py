

from datetime import datetime

print("🤖 Hello! I am ChatBot. Type 'exit' to end the chat.")

while True:
    # Take user input
    user_input = input("You: ").strip().lower()

    
    if user_input in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! Have a great day 👋")
        break

    
    elif user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello there! How can I assist you today?")

    
    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: I am your friendly chatbot built using Python 🐍")

    
    elif "how are you" in user_input:
        print("Bot: I'm doing great, thanks for asking! 🤖 What about you?")

    
    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Bot: The current time is {current_time}")

    
    elif "help" in user_input:
        print("Bot: You can ask me about the time, who I am, or just say hi!")

    else:
        print("Bot: Sorry, I didn't understand that. Try asking something else.")

