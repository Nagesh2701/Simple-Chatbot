import re
import random

class SimpleChatbot:
    def __init__(self):
        self.name = "ChatBot"
        
        # Define patterns and responses
        self.patterns = {
            # Greetings
            r'(hi|hello|hey|greetings).*': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! Nice to meet you!",
                "Hello! I'm here to chat with you."
            ],
            
            # How are you
            r'how are you.*': [
                "I'm doing great! Thanks for asking. How are you?",
                "I'm fine, thank you! How about you?",
                "I'm having a wonderful day! What about you?"
            ],
            
            # Name questions
            r'(what is your name|who are you).*': [
                f"I'm {self.name}, your friendly chatbot!",
                f"My name is {self.name}. I'm here to chat with you!",
                f"I'm {self.name}, nice to meet you!"
            ],
            
            # Age questions
            r'how old are you.*': [
                "I'm timeless! I exist in the digital realm.",
                "Age is just a number for AI like me!",
                "I was born when you started this conversation!"
            ],
            
            # Weather
            r'.*(weather|temperature).*': [
                "I wish I could check the weather for you, but I don't have access to weather data.",
                "I can't check the weather, but I hope it's nice where you are!",
                "You might want to check a weather app for that information."
            ],
            
            # Thanks
            r'.*(thank|thanks).*': [
                "You're welcome! Happy to help!",
                "No problem at all!",
                "My pleasure! Anything else I can help with?"
            ],
            
            # Goodbye
            r'.*(bye|goodbye|see you|farewell).*': [
                "Goodbye! It was nice chatting with you!",
                "See you later! Have a great day!",
                "Farewell! Come back anytime!"
            ],
            
            # Help
            r'.*(help|what can you do).*': [
                "I can have simple conversations with you! Try asking me about myself, say hello, or just chat!",
                "I'm a simple chatbot. I can respond to greetings, questions about myself, and general conversation!",
                "Just talk to me! I can discuss various topics and answer simple questions."
            ],
            
            # Default responses for unmatched input
            'default': [
                "That's interesting! Tell me more.",
                "I see! What else would you like to talk about?",
                "Hmm, that's something to think about!",
                "I'm not sure I understand completely, but I'm listening!",
                "Can you tell me more about that?",
                "That's a good point! What do you think about it?"
            ]
        }
    
    def get_response(self, user_input):
        """
        Find the best response based on user input using pattern matching
        """
        user_input = user_input.lower().strip()
        
        # Check each pattern
        for pattern, responses in self.patterns.items():
            if pattern == 'default':
                continue
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        # If no pattern matches, return default response
        return random.choice(self.patterns['default'])
    
    def chat(self):
        """
        Main chat loop
        """
        print(f"Hello! I'm {self.name}, your simple chatbot.")
        print("Type 'quit', 'exit', or 'bye' to end our conversation.")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                # Check for exit commands
                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    print(f"{self.name}: Goodbye! It was nice chatting with you!")
                    break
                
                # Skip empty input
                if not user_input:
                    print(f"{self.name}: I'm still here! Say something.")
                    continue
                
                # Generate and print response
                response = self.get_response(user_input)
                print(f"{self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n{self.name}: Goodbye! Thanks for chatting!")
                break
            except EOFError:
                print(f"\n{self.name}: Goodbye! Thanks for chatting!")
                break

def main():
    """
    Main function to start the chatbot
    """
    chatbot = SimpleChatbot()
    chatbot.chat()

if __name__ == "__main__":
    main()
