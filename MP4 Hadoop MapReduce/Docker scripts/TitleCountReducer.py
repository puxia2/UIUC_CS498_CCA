#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
word_sum = {}
# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.rstrip('\n')
    word = line.split('\t')[0]
    if word in word_sum:
        word_sum[word] += 1
    else:
        word_sum[word] = 1

# TODO
# print('%s\t%s' % (  ,  )) print as final output
items = list(word_sum.items())
for item in items:
    print('%s\t%s' % (item[0], item[1])) 