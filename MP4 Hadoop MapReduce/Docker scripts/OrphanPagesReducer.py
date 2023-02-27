#!/usr/bin/env python3
import sys


#TODO

book = {}
orphan_id = []
for line in sys.stdin:
    # TODO
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
    print('%s' % (str(orphan))) 
    

#TODO
# print(xx) print as final output
