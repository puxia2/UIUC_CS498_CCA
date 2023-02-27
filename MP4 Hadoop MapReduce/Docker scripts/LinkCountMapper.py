#!/usr/bin/env python3
import sys

id_link = []
for line in sys.stdin:
  #TODO
  line = line.rstrip('\n')
  page_id = line.split(': ')[0]
  id_link = line.split(': ')[1].split()

  for link in id_link:
    print('%s\t%s' % (page_id, link)) 

  # print('%s\t%s' % (  ,  )) pass this output to reducer
