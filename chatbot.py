import nltk
# Uncomment the following line if you haven't downloaded NLTK data
# nltk.download('punkt')
from nltk.tokenize import word_tokenize
responses = {
    "hi": "Hello!",
    "how are you": "I'm good, thank you!",
    "what's your name": "I'm a chatbot!",
    # Add more predefined responses
}
def chat():
    user_input = input("You: ").lower()
    response = responses.get(user_input, "I'm sorry, I don't understand.")
    print("Bot:", response)
if __name__ == "__main__":
    print("Bot: Hi, I'm a simple chatbot. You can start talking to me!")
    while True:
        chat()
