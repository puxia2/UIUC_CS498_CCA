#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TopTitleStatistics")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1)

#TODO
def word_count(line):
    line = line.rstrip('\n')
    count = int(line.split('\t')[1])
    return count

countRDD = lines.map(lambda line: word_count(line))
count_list = [i for i in countRDD.collect()]

word_sum = int(sum(count_list))
word_mean = int(word_sum/10) 
word_min = int(min(count_list))
word_max = int(max(count_list))
word_var = int(sum([((x - word_mean) ** 2) for x in count_list]) / 10) 

outputFile = open(sys.argv[2], "w")
'''
TODO write your output here
write results to output file. Format
outputFile.write('Mean\t%s\n' % ans1)
outputFile.write('Sum\t%s\n' % ans2)
outputFile.write('Min\t%s\n' % ans3)
outputFile.write('Max\t%s\n' % ans4)
outputFile.write('Var\t%s\n' % ans5)
'''
outputFile.write('Mean\t%s\n' % word_mean)
outputFile.write('Sum\t%s\n' % word_sum)
outputFile.write('Min\t%s\n' % word_min)
outputFile.write('Max\t%s\n' % word_max)
outputFile.write('Var\t%s\n' % word_var)

sc.stop()

