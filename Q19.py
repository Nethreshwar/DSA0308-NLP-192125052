from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

def lesk_algorithm(word, sentence):
    best_sense = None
    max_overlap = 0
    sentence_tokens = set(word_tokenize(sentence))
    sentence_tokens = sentence_tokens.difference(set(stopwords.words('english'))) # Removing stopwords

    for sense in wordnet.synsets(word):
        definition = set(word_tokenize(sense.definition()))
        definition = definition.difference(set(stopwords.words('english'))) # Removing stopwords
        overlap = len(sentence_tokens.intersection(definition))
        for example in sense.examples():
            example_tokens = set(word_tokenize(example))
            example_tokens = example_tokens.difference(set(stopwords.words('english'))) # Removing stopwords
            overlap += len(sentence_tokens.intersection(example_tokens))
        
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense
    
    return best_sense

# Get input from the user
word = input("Enter the target word for word sense disambiguation: ")
sentence = input("Enter the sentence containing the target word: ")

sense = lesk_algorithm(word, sentence)
if sense:
    print("Best sense:", sense.name())
    print("Definition:", sense.definition())
else:
    print("No sense found for the word in the given context.")
