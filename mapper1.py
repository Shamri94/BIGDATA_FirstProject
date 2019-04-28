#!/usr/bin/env python
"""mapper.py"""

import sys
firstline = True
# input comes from STDIN (standard input)
for line in sys.stdin:
    if firstline:    #skip first line
    	firstline = False
    	continue

    # remove leading and trailing whitespace
    line = line.strip()
    # use this split to get all the data
    ticker, openn, close, adj_close, lowThe, highThe, volume, date = line.split(',', 7)	

    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    # select ony the ticker between 1998 and 2018
    if (int(date[0:4]) in range(1998,2019)): 
    	print '%s\t%s\t%s\t%s\t%s' % (ticker+'_'+date,close,lowThe,highThe,volume)
