import nltk
from nltk.corpus import wordnet

# Download WordNet data if not already downloaded
nltk.download('wordnet')

# Function to explore word meanings
def explore_word_meanings(word):
    # Get synsets for the word
    synsets = wordnet.synsets(word)
    
    if synsets:
        print(f"Synsets for '{word}':")
        for synset in synsets:
            print(f" - Definition: {synset.definition()}")
            print(f" - Examples: {synset.examples()}")
            print()
    else:
        print(f"No synsets found for '{word}'")

# Example word to explore
word_to_explore = "play"

# Explore meanings of the word
explore_word_meanings(word_to_explore)
