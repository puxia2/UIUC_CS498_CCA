#!/usr/bin/env python3
import sys


# leaguePath = sys.argv[1] # comment in local test
#TODO
leaguePath = 'dataset/league.txt' # comment in docker
f1 = open('PLM_output.txt', 'w') # comment in docker

league_id = []
with open(leaguePath) as f:
	#TODO
       lines = f.readlines()
       for line in lines:
              line = line.rstrip('\n')
              league_id.append(str(line))


# for line in sys.stdin: # comment in local test

       #TODO

popularity = {}
with open('LCR_output.txt') as f:
       lines = f.readlines()
       for line in lines:
              line = line.rstrip('\n').split('\t')
              page = int(line[0])
              count = int(line[1])
              if str(page) in league_id:
                     popularity[page] = count


items = list(popularity.items())
for item in items:
       # print('%s\t%s' % (str(item[0]), str(item[1]))) # comment in local test
       f1.write(str(item[0]) + '\t' + str(item[1]) + '\n')





       # print('%s\t%s' % (  ,  )) pass this output to reducer
