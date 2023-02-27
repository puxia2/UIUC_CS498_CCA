#!/usr/bin/env python3
import sys


#TODO
f1 = open('OPR_output.txt','w') # comment in docker

# for line in sys.stdin: # comment in local test
  # TODO
book = {}
orphan_id = []
with open('OPM_output.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n').split('\t')
        start_id = str(line[0])
        end_id = str(line[1])
        if start_id != end_id:
            if start_id not in book:
                book[start_id] = 0
            book[end_id] = 1

for page_id in book.keys():
    if book[page_id] == 0:
        orphan_id.append(int(page_id))

orphan_id.sort()
for orphan in orphan_id:
    f1.write(str(orphan) + '\n')
    # print(str(orphan)) # comment in local test
            
        
        

        

#TODO
# print(xx) print as final output