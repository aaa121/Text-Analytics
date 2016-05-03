'''
The Copora in NLTK_DATA is really useful and contain lots of files and documents like movie review, fiction stories, bible, gutenberg doc etc
To use any file, follow this format
'''
from nltk.corpus import gutenberg, inaugural
from nltk.tokenize import word_tokenize, sent_tokenize

sample=gutenberg.raw('shakespeare-hamlet.txt')
sentence=sent_tokenize(sample)
print(sentence[1:5])

inaugural_lecture=inaugural.raw("1789-Washington.txt")
insent=sent_tokenize(inaugural_lecture)
print(insent[0:6])


