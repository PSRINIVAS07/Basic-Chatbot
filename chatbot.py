import random
import re
import spacy

# Load spaCy's English NLP model with a fallback installation check
def load_spacy_model():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        print("The spaCy model 'en_core_web_sm' is not installed. Installing now...")
        from spacy.cli import download
        download("en_core_web_sm")
        return spacy.load("en_core_web_sm")

nlp = load_spacy_model()

class AdvancedChatBot:
    def __init__(self):
        self.default_responses = [
            "That's interesting! Tell me more.",
            "I'm not sure I understand. Could you elaborate?",
            "Can you explain that in more detail?"
        ]
        self.greetings = ["hello", "hi", "hey", "good morning", "good evening"]
        self.farewells = ["bye", "goodbye", "see you", "take care"]
        self.fallback_response = "I'm sorry, I didn't quite understand that."

    def generate_response(self, user_input):
        # Preprocess user input
        doc = nlp(user_input.lower())

        # Check for greetings
        if any(token.text in self.greetings for token in doc):
            return random.choice(["Hello! How can I assist you today?", "Hi there! What's on your mind?", "Hey! What can I do for you?"])

        # Check for farewells
        if any(token.text in self.farewells for token in doc):
            return random.choice(["Goodbye! Have a great day!", "Bye! Take care!", "See you later!"])

        # Check for specific intents
        if "weather" in user_input:
            return "I'm not sure about the weather, but you can check a weather app for the latest updates."

        if "help" in user_input:
            return "Of course! Let me know how I can assist you."

        if "name" in user_input:
            return "I'm an advanced chatbot powered by spaCy! What's your name?"

        # Check for more complex intents using spaCy
        if "joke" in user_input:
            return random.choice([
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the bicycle fall over? It was two-tired!",
                "What do you call fake spaghetti? An impasta!"
            ])

        # Use fallback responses for unrecognized input
        return random.choice(self.default_responses)

    def start(self):
        print("Hello! I'm your advanced chatbot. Type 'bye' to exit the chat.")
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in self.farewells:
                print("Chatbot: Goodbye! Have a nice day!")
                break

            response = self.generate_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot = AdvancedChatBot()
    chatbot.start()
