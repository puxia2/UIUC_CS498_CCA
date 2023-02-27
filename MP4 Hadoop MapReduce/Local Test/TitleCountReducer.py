#!/usr/bin/env python3
from operator import itemgetter
import sys

#TODO
word_sum = {}
with open('TCM_output.txt', encoding='utf8') as f: # replace this block in docker with stdin below
    lines = f.readlines()
    for line in lines: # key1\t1\n
        line = line.rstrip('\n')
        word = line.split('\t')[0]
        if word in word_sum:
            word_sum[word] += 1
        else:
            word_sum[word] = 1



# input comes from STDIN
# for line in sys.stdin: # key1\t1\n # comment in local test
    # TODO

# create a txt file to store reduce function output
# comment in docker
f1 = open('TCR_output.txt', 'w', encoding="utf8")

# TODO
# print('%s\t%s' % (  ,  )) print as final output
items = list(word_sum.items())
for item in items:
    # print('%s\t%s' % (item[0], item[1])) # comment in local test
    f1.write(item[0] + '\t' + str(item[1]) + '\n')
