from nltk.stem import PorterStemmer
words = ["running", "jumps", "better", "writing", "written"]
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]

print("Original Words:", words)
print("Stemmed Words:", stemmed_words)
