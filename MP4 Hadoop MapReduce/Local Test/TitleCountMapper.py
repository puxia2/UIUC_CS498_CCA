#!/usr/bin/env python3

import sys
import string
import re



# stopWordsPath = sys.argv[1] # comment in local test
# delimitersPath = sys.argv[2] # comment in local test

stopWordsPath = "stopwords.txt" # comment in docker
delimitersPath = "delimiters.txt" # comment in docker

stop_words = []
delimiters = []
word_count = {}

text = [] # comment in docker

# TODO
with open(stopWordsPath) as f:
    # TODO
    lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n') # get rid of \n
        stop_words.append(line)


# comment in docker
with open('input.txt', encoding='utf8') as f:
    text = f.readlines()


#TODO 
# with open(delimitersPath) as f:
    # TODO
delimiters = "[\t,;\.\?\!\-\:@\[\]\(\)\{\}_\*/]+" 


# create a txt file to store map function output
# comment in docker
f1 = open('TCM_output.txt', 'w', encoding="utf8")

for line in text:  # sys.stdin in docker
  
    # TODO
    line = re.sub('\n', '', line) # get rid of \n at the end of each line
    line = line.strip()
    sep_line = re.split(delimiters, line)
    sep_line = [i.lower() for i in sep_line]

    sep_line = [i for i in sep_line if i] # remove empty string from the list

    # remove word from stopWord list
    # map function will return output in the following key-pair format:
    # first line: billy 1
    # second line: reeves 1
    # ...... (word and 1 is seperated by tab)
    # above key-pair outputs will be passed to reducer
    for word in sep_line:
        if word not in stop_words:
            to_reduce = word + '\t' + '1'
            # print(to_reduce) # comment in local test
            f1.write(to_reduce + '\n')
    

    # print('%s\t%s' % (  ,  )) pass this output to reducer

