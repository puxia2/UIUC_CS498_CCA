#!/usr/bin/env python3
import sys


leaguePath = sys.argv[1]
#TODO

league_id = []
with open(leaguePath) as f:
	#TODO
       lines = f.readlines()
       for line in lines:
              line = line.rstrip('\n')
              league_id.append(str(line))


popularity = {}
for line in sys.stdin:
       #TODO
       line = line.rstrip('\n').split('\t')
       page = int(line[0])
       count = int(line[1])
       if str(page) in league_id:
              popularity[page] = count


# print('%s\t%s' % (  ,  )) pass this output to reducer
items = list(popularity.items())
for item in items:
       print('%s\t%s' % (str(item[0]), str(item[1]))) 