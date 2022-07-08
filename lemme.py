from nltk.stem import WordNetLemmatizer
import nltk
# nltk.download()
# RUNS ONLY ONCE
lemmatizer = WordNetLemmatizer()
sentence = 'Mine grandmas are inside  grocery shop'
sentence_tokens = nltk.word_tokenize(sentence.lower())

pos_tags = nltk.pos_tag(sentence_tokens)
# print(pos_tags)
# For sentence we use tokens


def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)
    print(sentence_lemmas)
    return sentence_lemmas


sent = input("Please Enter Sentence\n")
lemma_me(sent)
# lemma2 = lemmatizer.lemmatize('fruit', 'n')
