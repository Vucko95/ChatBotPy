from nltk.stem import WordNetLemmatizer
import nltk
# nltk.download()
# RUNS ONLY ONCE


lemmatizer = WordNetLemmatizer()
lemma1 = lemmatizer.lemmatize('fruits', 'n')
lemma2 = lemmatizer.lemmatize('fruit', 'n')
print(lemma1)
print(lemma2)
