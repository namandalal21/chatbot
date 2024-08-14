import nltk
from nltk.tokenize import word_tokenize

# Print the path where NLTK looks for data
print(nltk.data.path)

# Try to load a specific file to ensure access
try:
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    print("Punkt tokenizer loaded successfully.")
except Exception as e:
    print(f"An error occurred while loading Punkt tokenizer: {e}")
