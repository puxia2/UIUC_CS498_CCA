#!/usr/bin/env python3
import sys

#TODO
link_count = {}
# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.rstrip('\n').split('\t')
    start = int(line[0])
    end = int(line[1])
    if start != end:
        if end in link_count:
            link_count[end] += 1
        else:
            link_count[end] = 1
# TODO
# print('%s\t%s' % (  ,  )) print as final output
items = list(link_count.items())
for item in items:
    print('%s\t%s' % (str(item[0]), str(item[1]))) # comment in local test