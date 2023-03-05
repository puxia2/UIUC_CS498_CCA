#!/usr/bin/env python

#Execution Command: spark-submit PopularityLeagueSpark.py dataset/links/ dataset/league.txt
import sys
from pyspark import SparkConf, SparkContext
import string

conf = SparkConf().setMaster("local").setAppName("PopularityLeague")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf=conf)

lines = sc.textFile(sys.argv[1], 1) 

#TODO
def link_map(page):
    if page.find(":") == -1:
        return (int(page), 1)
    else:
        return (int(page[:-1]), 0)


linkmapRDD = lines.flatMap(lambda line: line.split(" ")).map(link_map)
linkreduceRDD = linkmapRDD.reduceByKey(lambda a,b: a+b)
link_popularity = linkreduceRDD.collect()


leagueIds = sc.textFile(sys.argv[2], 1)

#TODO
league_id = []
for league in leagueIds.collect():
    league_id.append(int(league))

league_popularity = []
for item in link_popularity:
    if int(item[0]) in league_id:
        league_popularity.append([str(item[0]), int(item[1])])

rank = sorted(league_popularity, key=lambda x: x[0])

output = open(sys.argv[3], "w")

#TODO
#write results to output file. Foramt for each line: (key + \t + value +"\n")
for ii in rank:
    rank_id = 0
    for jj in rank:
        if ii[1] > jj[1]:
            rank_id += 1
    output.write(str(ii[0]) + '\t' + str(rank_id) + '\n')

sc.stop()

