# Simple Python Chatbot

A basic conversational chatbot built with Python that uses pattern matching to respond to user inputs.

## Features

- **Greeting responses**: Responds to various greetings (hi, hello, hey)
- **Personal questions**: Answers questions about itself (name, age, capabilities)
- **Weather inquiries**: Acknowledges weather questions (though can't provide actual weather data)
- **Gratitude handling**: Responds to thanks and appreciation
- **Help functionality**: Explains its capabilities when asked
- **Graceful exits**: Multiple ways to end the conversation
- **Default responses**: Handles unexpected inputs with engaging fallback responses

## How to Run

1. Make sure you have Python installed on your system
2. Run the chatbot:
   ```bash
   python simple_chatbot.py
   ```

## How to Use

Once the chatbot starts, you can:
- Say hello: "hi", "hello", "hey"
- Ask about the bot: "what is your name?", "how are you?", "how old are you?"
- Ask for help: "what can you do?", "help"
- Thank the bot: "thanks", "thank you"
- Ask about weather: "how's the weather?"
- Have general conversation - the bot will respond to most inputs
- Exit the conversation: "quit", "exit", "bye", or "goodbye"

## Example Conversation

```
Hello! I'm ChatBot, your simple chatbot.
Type 'quit', 'exit', or 'bye' to end our conversation.
--------------------------------------------------
You: hello
ChatBot: Hello! How can I help you today?
You: what is your name?
ChatBot: I'm ChatBot, your friendly chatbot!
You: how are you?
ChatBot: I'm doing great! Thanks for asking. How are you?
You: what can you do?
ChatBot: I can have simple conversations with you! Try asking me about myself, say hello, or just chat!
You: bye
ChatBot: Goodbye! It was nice chatting with you!
```

## Customization

You can easily customize the chatbot by:

1. **Adding new patterns**: Add new regex patterns and responses in the `self.patterns` dictionary
2. **Modifying responses**: Change existing responses to match your preferred tone or style
3. **Changing the bot name**: Update `self.name` in the `__init__` method
4. **Adding new functionality**: Extend the `SimpleChatbot` class with additional methods

## Technical Details

- **Language**: Python 3.x
- **Dependencies**: Only built-in Python modules (`re`, `random`)
- **Pattern matching**: Uses regular expressions for input recognition
- **Response selection**: Randomly selects from predefined responses for variety
- **Error handling**: Gracefully handles Ctrl+C and other interruptions

## Future Enhancements

This is a basic chatbot that could be enhanced with:
- Integration with external APIs (weather, news, etc.)
- Machine learning for better response generation
- Conversation history and context awareness
- More sophisticated natural language processing
- Database integration for persistent conversations
- Web interface using Flask or Django
