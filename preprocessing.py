#! /usr/bin/env python

import string

f = open('knowledge_base.txt','r')

list_tuples = f.readlines()

tuples = []

for i in range(len(list_tuples)):
	if(list_tuples != "\n"):
		tuples.append(list_tuples[i])	

#the knowledge base consists of many noisy data like \n  \t and so on . First , these have to be removed 


for i in range(len(tuples)):
	tuples[i] = tuples[i].replace("\n","")
	tuples[i] = tuples[i].replace("\t","")    # note :(this can be modified) you can try replacing all these statements using a regular expression 
	tuples[i] = tuples[i].replace("\t1","")
	tuples[i] = tuples[i].replace("\t2","")
	tuples[i] = tuples[i].replace("\t3","")
	tuples[i] = tuples[i].replace("\t4","")
	tuples[i] = tuples[i].replace("\t5","")
	tuples[i] = tuples[i].replace("\t6","")
	tuples[i] = tuples[i].replace("\t7","")
	tuples[i] = tuples[i].replace(", ",",")


actual_tuples = []

# this step is just for the beginning stage . I am eliminating the relationship between the concepts . When we build a full-fledged system, the relations have to be taken into account .

for i in range(len(tuples)):
	myString = tuples[i]
	actual_tuples.append(myString[myString.find("(")+1:myString.find(")")])


#there are so many tuples that dont have the first entry in the tuple . they must be eliminated .

for i in range(len(actual_tuples)):
	if(actual_tuples[i].startswith(" ,")):
		del(actual_tuples[i])


#print len(actual_tuples)




