#!/usr/bin/env python3

import sys
import string
import re


stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

stop_words = []
delimiters = []
word_count = {}

# TODO
with open(stopWordsPath) as f:
    # TODO
    lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n') # get rid of \n
        stop_words.append(line)



#TODO 
# with open(delimitersPath) as f:
# TODO
delimiters = "[\t,;\.\?\!\-\:@\[\]\(\)\{\}_\*/]+" 
    
    

for line in sys.stdin:
  
    # TODO
    line = re.sub('\n', '', line) # get rid of \n at the end of each line
    line = line.strip()
    sep_line = re.split(delimiters, line)
    sep_line = [i.lower() for i in sep_line]

    sep_line = [i for i in sep_line if i] # remove empty string from the list

    for word in sep_line:
        if word not in stop_words:
            to_reduce = word + '\t' + '1'
            print(to_reduce) # comment in local test
    # print('%s\t%s' % (  ,  )) pass this output to reducer


