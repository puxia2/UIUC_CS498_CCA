#!/usr/bin/env python3
import sys


# for line in sys.stdin: # comment in local test
    # TODO


f1 = open('TTSM_output.txt', 'w', encoding="utf8")

with open('TTM_output.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip('\n')
        title = line.split('\t')[0]
        freq = int(line.split('\t')[1])
        # print('%s\t%s' % (freq, 0)) # comment in local test
        f1.write(str(freq) + '\t' + '0' + '\n')

    # print('%s\t%s' % (  ,  )) pass this output to reducer
