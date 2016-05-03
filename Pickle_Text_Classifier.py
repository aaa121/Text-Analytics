
import nltk
from nltk.corpus import movie_reviews
import random
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
import pickle

'''
The objectives are: (1) construct a training and testing datasets for extracting words in a particular category either
positive or negative; (2) use the words classification to examine a review being postive or negative.
Also, a database of all words are contructed to compile all the words in the review; find the most common words in the list;
classify the words into positive or negative

'''
documents = []
for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents+=[(list(movie_reviews.words(fileid)),category)] # The document is a tuple

#Alternanatively, you can use one-liner append command as follows:

# documents=[(list(movie_reviews.words(fileid)), category)
#            for catgory in movie_reviews.categories()
#            for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
# print(documents)
# print(documents[1])
# for j in documents:
#     print(j)
# print(set(documents)) #It won't work. Return: TypeError: unhashable type: 'list' because document
# is in the format [(['u','g','h'],'pos'), (['u','g','h'],'neg')] i.e. (review, category)
# for j in documents:
#     print(j)
unique_documents=[]
for j in documents:
    # print(j[0])
    for k in j[0]:
        unique_documents +=[k]
# print(unique_documents)


all_words=[]
for w in movie_reviews.words():
    all_words+=[w.lower()]
# print(all_words)
# NLTK FREQUENCY DISTRIBUTION
# top_all_words=nltk.FreqDist(all_words)
# print(top_all_words)
# print(top_all_words.most_common(200))
# print(top_all_words["awesome"])
# print(top_all_words["awesome","interesting"])

# The next thing is to match the common words in training and testing dataset with all the compiled words set i.e. finding the features
'''
If the all_words list is equated to top_all_words by using the same name. the list will turn to dictionary then use:
word_features = list(all_words.keys())[:3000]. That will find the keys instead of values i.e. all_words={"keys":values}
Otherwise use the following:
'''

# word_features = []
# # word_features = [w[0] for w in sorted(all_words,key=lambda k_v:k_v[1], reverse=True)[:3000]]
# for w in sorted(all_words,key=lambda k_v:k_v[1], reverse=True)[:3000]:
#     word_features += [w[0]]
# print(word_features)

# word_features =sorted(list(set(all_words)),reverse=True)[:3000]
word_features = list(set(all_words))[:3000]
# print(word_features)

'''
The function 'find_features' is to look for common words in the document parsed in say "cv000_29416.txt" relative to a set of
all_words database named word_features
'''

def find_features(documents):
    words=set(documents)
    features ={}
    for w in word_features:
        features[w] = (w in words) # This is a dictionary thar will return the word in word_feature and boolean (against of the same word is in words)
    return features

# print(find_features(movie_reviews.words('neg/cv000_29416.txt')))
'''
What the above print function does is that, it parsed in text file in the negative sub-folder of the movie_reviews
file in nltk_data/corpora then compare the words generated from it with the database, all_words without repetition,
i.e. word_features (though, it can be either a list or tuple depending on using the command list)
'''

featuressets=[]
for (rev,category) in documents:
    featuressets +=[((find_features(rev)),category)]
    # featuressets += [(set(find_features(rev)), category)] # This will shrink the list and turn the review into dictionary since find_features returns a dictionary
# print(featuressets[1]) # This returns list of dictionary and quoted category i.e. {'word1': True, 'word2': False},"pos"


#NAIVE BAYES ALGORITHM FOR TEXT CLASSIFIER
'''
The machine learning algorithm requires TRAINING and TESTING SET data. The training set is used to train the algorithm. The set
is to check how many times the word appears in neg or pos category. The more appearance in a particular category indicates the
importance of the category. The testing set on the other hand is to validate the accuracy of the algorithm. It is used as a feed
for the algorithm to return the category of the word without specifying it. The outcome is compare with known category of the word.
Then test the accuracy of the algorithm.
'''

training_set = featuressets[:1900]
testing_set = featuressets[1900:]
classifier = NaiveBayesClassifier.train(training_set)
accuracy = nltk.classify.util.accuracy(classifier,testing_set)
print("Naive Bayes Algorithm Accuracy Rate: ",accuracy*100,"%")
classifier.show_most_informative_features(15)

save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

