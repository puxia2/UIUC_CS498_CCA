#!/usr/bin/env python3
import sys

#TODO
link_count = {}
with open('LCM_output.txt') as f: # comment in docker
    lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n').split('\t')
        start = int(line[0])
        end = int(line[1])
        if start != end:
            if end in link_count:
                link_count[end] += 1
            else:
                link_count[end] = 1

f1 = open('LCR_output.txt', 'w') # comment in docker

# input comes from STDIN
# for line in sys.stdin: # comment in local test
    # TODO

# TODO
# print('%s\t%s' % (  ,  )) print as final output
items = list(link_count.items())
for item in items:
    # print('%s\t%s' % (str(item[0]), str(item[1]))) # comment in local test
    f1.write(str(item[0]) + '\t' + str(item[1]) + '\n')