#!/usr/bin/env python3
# import sys



# # input comes from STDIN
# for line in sys.stdin:
#     # TODO
    
#     # print('%s\t%s' % (  ,  )) print as final output
import sys


# TODO
word_count = []


for line in sys.stdin:
       line = line.rstrip('\n')
       title = line.split('\t')[0]
       freq = int(line.split('\t')[1])
       word_count.append([title, freq])

word_sort = sorted(word_count, key=lambda x:(x[1], x[0]))
top_titles =word_sort[-10:]

       #TODO


#TODO
# print('%s\t%s' % (  ,  )) pass this output to reducer
for title in top_titles:
       print('%s\t%s' % (title[0], title[1])) 
       