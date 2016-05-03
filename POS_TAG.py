import nltk
from nltk.corpus import state_union
from nltk import sent_tokenize,word_tokenize,pos_tag
from nltk import PunktSentenceTokenizer as punk # Is a custom and unsupervised tokenizer than can be trained

'''
The Punkt_Sentence_Tokenizer is a better algorithm compare to the default (Peen treebank Tagset) by NLTK if there is text and sample data. The test data
is to train the algorithm, while the sample data is to validate and use it for a specific purpose. In terms of lengths of sentecne list,
Punk has higher of sentence from the state of the union address.
'''
# with open("text","r") as file:
#     text=file.read()

stext=state_union.raw("2006-GWBush.txt")
ttext=state_union.raw('2005-GWBush.txt')

sentence=punk(ttext)
# print(sentence)
punktokenize=sentence.tokenize(stext)
# print(punktokenize)
print(len(punktokenize))

sen=sent_tokenize(stext)
# print(sen)
print(len(sen))

# for w in punktokenize:
#     word=word_tokenize(w)
#     tagged=pos_tag(word)
#     print(tagged)

#Try alternatively:
# def process_pos():
#     try:
#         for w in punktokenize:
#             word = word_tokenize(w)
#             tagged = pos_tag(word)
#             print(tagged)
#     except Exception as e:
#         print(str(e))
#
# process_pos()

'''
Download teh list of the tag from http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html

'''

# CHUNKING
# CHUNKING
# CHUNKING
# CHUNKING
'''
Chunking simply means grouping of things.
Chunking comes handy after split a text into sentence, words and associated category of Part of Speech, to determine the exact named entity.
Like noun. Regular expression is good to be understood to do some chunking
https://www.pythonprogramming.net/regular-expressions-regex-tutorial-python-3/
for example
<RB.?>*
. = any character, except for a new line
? = match 0 or 1 repetitions
* = match 0 or MORE repetitions

It means search for RB (adverb) with any character and 0 or 1 matches with another similar word and match with zero or many repetition
'''
#CHINKING
#CHINKING
#CHINKING
#CHINKING
'''
Chinking is the process of removing things from chunk.
<.*> one or more anything
| = matches either/or. Example x|y = will match either x or y
)( is used to remove i.e.chink
'''

# def process_pos():
#     try:
#         for w in punktokenize[0:5]:
#             word = word_tokenize(w)
#             tagged = pos_tag(word)
#             # print(tagged)
#
#             ChunkGram = r"""Chunk:{<.*>}
#                                 }<VB.?|IN|DT|TO>+{"""
#             ChunkParser = nltk.RegexpParser(ChunkGram)
#             chunked=ChunkParser.parse(tagged)
#             # print(chunked)
#             chunked.draw()
#
#     except Exception as e:
#         print(str(e))
#
# process_pos()


# NAMED ENTITY RECOGNITION
'''
NERecognition can be useful but its error rate and false positive rate is very high. It just reclassify the whole tokens
specific class
It comprises of:
NE Type
ORGANIZATION
PERSON
LOCATION
DATE
TIME
MONEY
PERCENT
FACILITY
GPE

'''
def process_pos():
    try:
        for w in punktokenize:
            word = word_tokenize(w)
            tagged = pos_tag(word)
            namedEnt = nltk.ne_chunk(tagged)
            #namedEnt = nltk.ne_chunk(tagged, binary=True) #When binary is true, it won't classify into any category
            namedEnt.draw()
    except Exception as e:
        print(str(e))
process_pos()

