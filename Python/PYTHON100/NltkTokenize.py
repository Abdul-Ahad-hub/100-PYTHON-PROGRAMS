import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "I am learning NLP with NLTK."

tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)
print(tags)
