#!/usr/bin/env python

'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''

import sys
from pyspark import SparkConf, SparkContext
import re

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

stop_words = []
delimiters = []
word_count = {}

with open(stopWordsPath) as f:
	#TODO
    lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n') # get rid of \n
        stop_words.append(line)

# with open(delimitersPath) as f:
#     #TODO
delimiters = "[\t,;\.\?\!\-\:@\[\]\(\)\{\}_\*/]+" 


def line_processing(line):
    global delimiters
    global stop_words
    line = re.sub('\n', '', line)
    sep_line = re.split(delimiters, line)
    sep_line = [i.lower() for i in sep_line]

    sep_line = [i for i in sep_line if i]

    final_line = []
    for word in sep_line:
        if word not in stop_words:
            final_line.append(word)

    return final_line



conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[3], 1)
#TODO
titlesRDD = lines.flatMap(lambda line: line_processing(line)).map(lambda word: (word, 1))
titleCountRDD = titlesRDD.reduceByKey(lambda a, b: a+b)
title_sort = titleCountRDD.collect()
title_sort = sorted(title_sort, key=lambda x:x[1])
title_ten = title_sort[-10:]
title_ten = sorted(title_ten, key=lambda x:x[0])

outputFile = open(sys.argv[4],"w")

#TODO
#write results to output file. Foramt for each line: (line +"\n")
for item in title_ten:
    outputFile.write(item[0] + "\t" + str(item[1]) + "\n")

sc.stop()
