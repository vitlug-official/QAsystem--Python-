#! /usr/bin/env python

from nltk import *
import nltk	
import string 


print "Enter your question "

question = raw_input()
question = question.lower()

stopwords = nltk.corpus.stopwords.words('english')
content = nltk.word_tokenize(question)

keywords_analysis = list( set(content) - set(stopwords) )

#print keywords_analysis

# this code can also include the following
	# stemming 
	# stop-word removal
	# lemmatization (necessary for questions that have more than one line)

