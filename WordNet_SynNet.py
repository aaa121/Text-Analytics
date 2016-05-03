'''
Is a very good module for search for synonyms and antonyms of words. Also chossing the right definition of a word
'''

from nltk.corpus import wordnet
from nltk.tokenize import sent_tokenize, word_tokenize
syns = wordnet.synsets("course")

# #print(syns)
#
# #Pick the exact meaning based on your interest
# print(syns[4])
#
# #Synonyms of the chosen word
# # print(syns[4].lemmas())
# # print(syns[4].lemmas()[2])
# print(syns[4].lemmas()[2].name())
#
# # definition of the word
# print(syns[4].definition())
#
# #Examples in statemenet
# print(syns[4].examples())

# Synonyms and Antonyms
synonyms=[]
antonyms = []
for syn in wordnet.synsets("good"):
    # print(syn.name())
    # print(syn.definition())
    for s in syn.lemmas():
        synonyms +=[s.name()]
        # print(s.name())
        if s.antonyms():
            antonyms+=[s.antonyms()]
            # print(s.antonyms()[0].name())

# print()
# print(synonyms)
# print()
# print(antonyms)

# Similarity Index (words such as TurnitIn)
wd1=wordnet.synset("boat.n.01")
wd2=wordnet.synset("ship.n.01")
si1=wd1.wup_similarity(wd2)
print(si1*100)

wd1=wordnet.synset("boat.n.01")
wd2=wordnet.synset("car.n.01")
si1=wd1.wup_similarity(wd2)
print(si1*100)

wd1=wordnet.synset("boat.n.01")
wd2=wordnet.synset("cat.n.01")
si1=wd1.wup_similarity(wd2)
print(si1*100)
