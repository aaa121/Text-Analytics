'''
http://textminingonline.com/dive-into-nltk-part-i-getting-started-with-nltk
'''

import nltk
from nltk.corpus import treebank

with open('text.txt','r') as text:
    content=text.read()
    sen=nltk.sent_tokenize(content) # split text into sentences
    #print(sen)
    token=nltk.word_tokenize(content) # Split text into words
    #print(token)
    tagged_token = nltk.pos_tag(token) # Classification of words into their part of speech
    print(tagged_token)
    print(len(tagged_token))
    '''
    entity=nltk.chunk.ne_chunk(tagged_token)
    print(entity)
    t= treebank.parsed_sents("wsj_0001.mrg")
    print(t)
    '''

