#!/usr/bin/env python3
import sys


# TODO

link_count = []

# for line in sys.stdin: # comment in local test

       #TODO
with open('LCR_output.txt') as f: # comment in docker
       lines = f.readlines()
       for line in lines:
            line = line.rstrip('\n').split('\t')
            page = str(line[0])
            count = int(line[1])
            link_count.append([page, count])

link_sort = sorted(link_count, key=lambda x:(x[1], x[0]))
top_link =link_sort[-10:]
        

#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer
for link in top_link:
       # print('%s\t%s' % (str(link[0]), str(link[1]))) # comment in local test
       print(str(link[0]) + '\t' + str(link[1]) + '\n')