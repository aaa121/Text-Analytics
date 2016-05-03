from nltk.stem.porter import PorterStemmer
from nltk import pos_tag, word_tokenize, sent_tokenize
with open('text.txt','r') as text:
    content=text.read()
    word=word_tokenize(content)
    sent=sent_tokenize(content)
    tagged=pos_tag(word)