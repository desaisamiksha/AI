class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hi": "Hello! How can I assist you today?",
            "hello": "Hello! How can I help you today?",
            "how are you": "I'm just a bot, but I'm here to help you!",
            "store hours": "Our store is open from 9 AM to 9 PM every day.",
            "location": "We are located at 123 Main Street, Springfield.",
            "return policy": "You can return any unopened items within 30 days for a full refund.",
            "shipping": "We offer free shipping for orders over $50!",
            "bye": "Goodbye! Have a great day!"
        }
        self.default_response = "I'm sorry, I don't understand that. Can you rephrase?"

    def get_response(self, user_input):
        
        user_input = user_input.lower()
        
        
        response = self.responses.get(user_input, self.default_response)
        
        return response

def main():
    bot = SimpleChatbot()
    print("Welcome to the Simple Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot:", bot.get_response(user_input))
            break
        response = bot.get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()