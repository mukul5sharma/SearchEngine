__author__ = 'mukul'

'''
Retrieve all inverted lists corresponding to terms in a query.
Compute BM25 scores for documents in the lists.
Make a score list for documents in the inverted lists.
Accumulate scores for each term in a query on the score list.
Assume that no relevance information is available.
For parameters, use k1=1.2, b=0.75, k2=100.
Sort the documents by the BM25 scores.
'''

import sys
import math

# User inputs
index = open(sys.argv[1], "r")
queries = open(sys.argv[2], "r")
max_num = int(sys.argv[3])
#result = open(sys.argv[4], "w")

# All lists
allWords = {}
queryDict = {}
bm25Score = {}
lengthOfEachDoc = {}

#BM25 constants
k1 = 1.2
b = 0.75
k2 = 100
r = 0
R = 0

# To represent Query ID
sq = 0


# Create a list of words with their docid and frequency
# Add values from file to data structure
for line in index:
    line = line.strip().split("->")
    word = line[0]
    wordInfo = line[1]

    allWords[word] = {}
    docs = wordInfo.split(";")

    for elem in docs:
        elem = elem.replace("(", "")
        elem = elem.replace(")", "")
        docInfo = elem.split(",")
        docId = docInfo[0]
        docFreq = docInfo[1]
        allWords[word][docId] = docFreq


for w in allWords:
    # All docs for the word
    docDictionary = allWords[w]

    # Access frequency of each word in each
    for doc in docDictionary:
        if doc not in lengthOfEachDoc:
            lengthOfEachDoc[doc] = float(docDictionary[doc])
        else:
            lengthOfEachDoc[doc] += float(docDictionary[doc])

# print lengthOfEachDoc.__len__()

# Length of all docs
totalLength = 0.0
for val in lengthOfEachDoc:
    # print val
    totalLength += float(lengthOfEachDoc[val])
    # print lengthOfEachDoc[val]

# Average Document Length
avdl = totalLength/lengthOfEachDoc.__len__()

#print avdl

# Function to calculate the BM25 score for each document
def computeBM25Score(query, qFreq):

    qFreq = float(qFreq)
    if query in allWords:
        for doc in allWords[query]:
            K = k1*((1-b)+b*(float(lengthOfEachDoc[doc])/avdl))

            # Terms for calculation
            t1 = (math.log(((r+0.5)/(R-r+0.5))/((len(allWords[query])-r+0.5)/(len(lengthOfEachDoc)-len(allWords[query])-R+r+0.5))))
            t2 = ((k1 + 1) * float(allWords[query][doc]))/(K + float(allWords[query][doc]))
            t3 = ((k2+1)*qFreq)/(k2+qFreq)
            # Score
            score = t1 * t2 * t3

            if doc in bm25Score:
                bm25Score[doc] += score
            else:
                bm25Score[doc] = score


print "Format : query_id Q0 doc_id rank BM25_score system_name"

# Process each query
for line in queries:
    sq += 1
    queryDict = {}
    bm25Score = {}
    query = line
    queryWords = line.strip().split(" ")
    for q in queryWords:
        if q in queryDict:
            queryDict[q] += 1
        else:
            queryDict[q] = 1

    for q in queryDict:
        # print "q before compute function call"
        #print q
        # compute the score
        computeBM25Score(q, queryDict[q])

    # Sort the Scores
    sortedBm25 = sorted(bm25Score, key = bm25Score.get, reverse=True)

    i = 0
    # Write Items to file
    for item in sortedBm25:
        if i in range(0,max_num):
            # print sortedBm25[item]
            # query_id Q0 doc_id rank BM25_score system_name
            print str(sq) + " " + "Q0" + " " + str(item) +" " + str(i+1) + " " + str(bm25Score[item]) + " " + "MK"
            #print "\n"

            i += 1
    print "\n"


