from nltk.tokenize import sent_tokenize, word_tokenize
with open("text", "r") as file:
    text=file.read()
    sentence=sent_tokenize(text)
    word=word_tokenize(text)
# print(sentence)
# print(word)
# for i in word:
#     print(i)
print(len(word))

#STOP WORDS: It helps to determine common words for seperation or classification in a particular language. the default has 20 word

from nltk.corpus import stopwords
# print(stopwords.words("english"))
#The list can be expanded depending on the project ypu are working on
stop_words_built=set(stopwords.words('english'))
# filtered_words=[]
# for w in word:
#     if w not in stop_words_built:
#         filtered_words +=[w]
# print(filtered_words)
# print(len(filtered_words))

# #ALTERNATIVELY
#
# filtered_sentence=[w for w in word if w not in stop_words_built]
# print(filtered_sentence)



### STEMMING
### STEMMING
### STEMMING
### STEMMING
'''
Stemming is teh process of reducing inflated (or sometimes derived) words to their word stem, base or root form. Such as
organizes, organizing, organize ---> organize
Lemmatisation is the process of grouping together different inflected forms of a word so they can be analyzed as a single
item. The reduced form must have meaning that is exist in the dictionary. such root word or single item is called lemma for the wors.
The best algorithm under computational linguistics is Porter's (1980) framework.
'''

from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag
stemmer= PorterStemmer()
wordsets1=["loving", "lovingly", "lovely","love","lover"]
wordsets2= ["organize", "organise", "organizin", "organisaton", "organises"]
# for w in wordsets1:
#     print(stemmer.stem(w))
#
# stemmed_text_file=[]
# with open('text',"r") as file:
#     text=file.read()
#     word=word_tokenize(text)
#     tagged=pos_tag(word)
#     for (w,tag) in tagged:
#         stemmered=stemmer.stem(w)
#         # print(stemmered)
#         stemmed_text_file+=[stemmered]
# print(stemmed_text_file)
# print(len(stemmed_text_file))

lemmatizer = WordNetLemmatizer()
# for h in wordsets2:
#     print(lemmatizer.lemmatize(h))
print(lemmatizer.lemmatize("great",pos="a"))
print(lemmatizer.lemmatize("goose", "v"))
print(lemmatizer.lemmatize("better", "a"))
print(lemmatizer.lemmatize("better"))