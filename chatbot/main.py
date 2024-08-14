from nlp.tokenizer import process_input
from nlp.entity_recognition import recognize_entities
from conversation.intent_detection import determine_intent
from conversation.response_generator import chatbot_response
import nltk

nltk.data.path.append('C:\\Users\\Rohit Sharma\\AppData\Roaming\\nltk_data\\tokenizers\\punkt')

def main():
    print("Welcome to the Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        tokens = process_input(user_input)
        intent = determine_intent(tokens)
        entities = recognize_entities(user_input)

        response = chatbot_response(intent, entities)
        print("Bot:", response)

if __name__ == "__main__":
    main()
# main.py

def main():
    print("Welcome to the Chatbot! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            break
        
        tokens = process_input(user_input)
        print("Tokens:", tokens)  # Just to check the tokens
        
        # Here you can process the tokens further as needed

if __name__ == "__main__":
    main()

