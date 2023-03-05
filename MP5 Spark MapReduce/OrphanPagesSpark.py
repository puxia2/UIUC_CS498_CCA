#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext
import string

conf = SparkConf().setMaster("local").setAppName("OrphanPages")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1) 

#TODO
def orphan_page(page):
    if page.find(":") == -1: # no : found -> page_end
        return (int(page), 1)
    else:
        return (int(page[:-1]), 0)


bookmapRDD = lines.flatMap(lambda line: line.split(" ")).map(orphan_page)
bookreduceRDD = bookmapRDD.reduceByKey(lambda a, b: a+b)
orphanRDD = bookreduceRDD.filter(lambda page: int(page[1]) == 0)

output = open(sys.argv[2], "w")

#TODO
#write results to output file. Foramt for each line: (line + "\n")
for item in orphanRDD.sortBy(lambda page: str(page[0])).collect():
    output.write(str(item[0]) + '\n')

sc.stop()

