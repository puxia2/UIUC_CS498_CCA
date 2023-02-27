#!/usr/bin/env python3
import sys
#TODO

# input comes from STDIN
# for line in sys.stdin: # comment in local test
    # TODO

items = []
with open('PLM_output.txt') as f:
       lines = f.readlines()
       for line in lines:
              line = line.rstrip('\n').split('\t')
              page = int(line[0])
              count = int(line[1])
              items.append([page, count])

#TODO
# print('%s\t%s' % (  ,  )) print as final output
rank = sorted(items, key=lambda x:(-x[0]))

for ii in rank:
    rank_id = 0
    for jj in rank:
        if ii[1] > jj[1]:
            rank_id += 1
    print(str(ii[0]) + '\t' + str(rank_id) + '\n')       
                      
    # print('%s\t%s' % (str(ii[0]), str(rank_id))) # comment in local test