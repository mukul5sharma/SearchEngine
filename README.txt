Mukul Sharma
mukul@ccs.neu.edu

Files Included: 

Indexer.py   |Used to create inverted index from the tccorpus.txt file
BM25.py      |Used to calculate BM25 score and returns a sorted lst of 
	      documents for the provided queries
Report.txt   |A brief explanation of solution
index.out    |Output of indexer.py file (inverted list)
results.eval |Final result 

**Note:The python version used - 2.7

Running the program - 
1. First run indexer.py file 
For Indexing      "python27 indexer.py <input filename> <output filename>"
**input = tccorpus.txt


2. Then run BM25.py file
For BM25 analysis "python27 BM25.py index.out queries.txt 100 > <output filename>"
**input = index.out file and queries.txt file 
  
