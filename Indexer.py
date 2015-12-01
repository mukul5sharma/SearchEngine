__author__ = 'mukul'

import sys

# Open input file
corpus = open(sys.argv[1], "r")
indexed = open(sys.argv[2], "w")
finalDict = {}
documentId = 0

for line in corpus:

    if line.startswith("#"):
        documentId = int(line.split(" ")[1])
    else:
        # print line
        words = line.strip().split(" ")
        # print words
        for w in words:

            if not w.isdigit():
            #if w not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                # print w
                if w in finalDict:
                    # print "true"
                    if documentId in finalDict[w]:
                        finalDict[w][documentId] += 1
                        # print finalDict[w]
                    else:
                        finalDict[w][documentId] = 1
                        # print finalDict[w]
                else:
                    # print "false"
                    finalDict[w] = {}
                    finalDict[w][documentId] = 1
                    # print finalDict[w][documentId]


# print finalDict
count = 0
for key in finalDict:
    newLine = str(key) + "->"
    flag = 0
    for innerKey in finalDict[key]:
        if flag != 0:
            newLine = newLine + ";" + "(" + str(innerKey) + "," + str(finalDict[key][innerKey]) + ")"
        else:
            newLine = newLine + "(" + str(innerKey) + "," + str(finalDict[key][innerKey]) + ")"
            flag = 1

    count += 1
    print count
    indexed.write(newLine + "\n")

indexed.close()
