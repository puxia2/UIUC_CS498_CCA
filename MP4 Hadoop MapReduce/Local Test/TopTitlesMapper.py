#!/usr/bin/env python3
import sys


# TODO
word_count = []

# create a txt file to store reduce function output
# comment in docker
f1 = open('TTM_output.txt', 'w', encoding="utf8")
# for line in sys.stdin: # comment in local test # key\t\number\n

       #TODO

with open('TCR_output.txt', encoding='utf8') as f: # replace this block in docker with stdin below
       lines = f.readlines()
       for line in lines: # key1\t1\n
              line = line.rstrip('\n')
              title = line.split('\t')[0]
              freq = int(line.split('\t')[1])
              word_count.append([title, freq])
       
       word_sort = sorted(word_count, key=lambda x:(x[1], x[0]))
       top_titles =word_sort[-10:]




#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer
for title in top_titles:
       # print('%s\t%s' % (title[0], title[1])) # comment in local test
       f1.write(title[0] + '\t' + str(title[1]) + '\n')
