#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext
import string

conf = SparkConf().setMaster("local").setAppName("TopPopularLinks")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1) 

#TODO
def link_map(page):
    if page.find(":") == -1:
        return (page, 1)
    else:
        return (page[:-1], 0)



linkmapRDD = lines.flatMap(lambda line: line.split(" ")).map(link_map)
linkreduceRDD = linkmapRDD.reduceByKey(lambda a,b: a+b)
link_ten = linkreduceRDD.takeOrdered(10, key=lambda x: -x[1])
link_sort = sorted(link_ten, key=lambda x: x[0])

output = open(sys.argv[2], "w")

#TODO
#write results to output file. Foramt for each line: (key + \t + value +"\n")
for item in link_sort:
    output.write(str(item[0]) + "\t" + str(item[1]) + "\n")

sc.stop()

