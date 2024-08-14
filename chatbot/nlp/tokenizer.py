from nltk.tokenize import word_tokenize
import nltk
nltk.data.path.append(r'C:\Users\Rohit Sharma\AppData\Roaming\nltk_data')

# Ensure punkt is downloaded
nltk.download('punkt')

from nltk.tokenize import word_tokenize


def process_input(user_input):
    tokens = word_tokenize(user_input)
    return tokens
# tokenizer.py

def process_input(user_input):
    # Use str.split() to tokenize the input text by spaces
    tokens = user_input.split()  # Simple tokenization by splitting on spaces
    return tokens

