#!/usr/bin/env python3
import sys
#TODO

items = []
# input comes from STDIN
for line in sys.stdin:
    # TODO
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
    print('%s\t%s' % (str(ii[0]), str(rank_id))) # comment in local test