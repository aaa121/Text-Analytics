Donald_Trump_News=open('Donald_Trump_News.txt', 'r') #Recall to put the file format at the end of the name i.e. txt
news=Donald_Trump_News.read()
'''
print(news)

'''
DTN_split=news.split()
count1=news.split().count('Trump')
print(count1)
count2=news.count('Trump')
print(count2)

import word_occurence_counter_program as wc
count3=wc.word_counter(news,'','Trump')
print(count3)

Donald_Trump_News.close()
