#!/usr/bin/env python3
import sys


# for line in sys.stdin: # comment in local test
  # TODO

link_name = ['links-a', 'links-b', 'links-c', 'links-d', 'links-e'] # comment in docker
link_path = 'dataset/links/' # comment in docker

f1 = open('OPM_output.txt', 'w') # comment in docker

id_link = [] # store all the links an id link to

for i in range(len(link_name)): # comment in docker
    with open(link_path + link_name[i]) as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip('\n')
            page_id = line.split(': ')[0]
            id_link = line.split(': ')[1].split()

            for link in id_link:
                f1.write(page_id + '\t' + link + '\n')
                # print('%s\t%s' % (page_id, link)) # comment in local test
  
  # print('%s\t%s' % (  ,  )) pass this output to reducer
