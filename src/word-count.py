# This program takes two arguments - the input file name and the threshold
# it prints out the words whoes occurrence exceeds the threshold
# To submit the program to a local standlone Apache Spark:
# $/usr/local/spark/bin/submit-spark word-count.py ../data/external/jay.txt 10

import sys
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
   # create Spark context with Spark configuration
   conf = SparkConf().setAppName("Spark Count")
   sc = SparkContext(conf=conf)
   # get threshold
   threshold = int(sys.argv[2])
   # read in text file and split each document into words
   tokenized = sc.textFile(sys.argv[1]).flatMap(lambda line: line.split(" "))
   # count the occurrence of each word
   wordCounts = tokenized.map(lambda word: (word, 1)).reduceByKey(lambda v1,v2:v1 +v2)
   # filter out words with fewer than threshold occurrences
   filtered = wordCounts.filter(lambda pair:pair[1] >= threshold)
   print(filtered.take(10))
   # count characters
   # charCounts = filtered.flatMap(lambda pair:pair[0]).map(lambda c: c).map(lambda c: (c, 1)).reduceByKey(lambda v1,v2:v1 +v2)
   #list = charCounts.collect()
   #print repr(list)[1:-1]
