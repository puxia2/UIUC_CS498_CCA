#!/usr/bin/env python3
import sys


for line in sys.stdin:
    # TODO
    line = line.rstrip('\n')
    title = line.split('\t')[0]
    freq = int(line.split('\t')[1])
    print('%s\t%s' % (freq, 0))
    
    # print('%s\t%s' % (  ,  )) pass this output to reducer
