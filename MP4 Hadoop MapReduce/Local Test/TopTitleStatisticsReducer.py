#!/usr/bin/env python3
import sys
import math


#TODO
word_count = [] # a list to store counts of each top titiles


# for line in sys.stdin: # comment in local test
    # TODO
with open('TTSM_output.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n')
        count = int(line.split('\t')[0])
        word_count.append(count)

word_sum = int(sum(word_count))
word_mean = int(word_sum/10) 
word_min = int(min(word_count))
word_max = int(max(word_count))
word_var = int(sum([((x - word_mean) ** 2) for x in word_count]) / 10)
#TODO
# print('%s\t%s' % (  ,  )) print as final output
print('%s\t%s' % ('Mean', word_mean))
print('%s\t%s' % ('Sum', word_sum))
print('%s\t%s' % ('Min', word_min))
print('%s\t%s' % ('Max', word_max))
print('%s\t%s' % ('Var', word_var))

