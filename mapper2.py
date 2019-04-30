#!/usr/bin/env python
"""mapper.py"""

import sys
firstline = True
# input comes from STDIN (standard input)
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()
    # use this split to get all the data
    ticker, openn, close, adj_close, lowThe, highThe, volume, date, exchange, name_sector_industry = line.split(',', 9)

    # take exactly the sector (because there are some commas inside the names)
    if (name_sector_industry[0] == '\"'):
    	name1, name2, sector, industry = name_sector_industry.split(',', 3)
    else:
    	name, sector, industry = name_sector_industry.split(',', 2)

    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    # select ony sectors between 2004 and 2018, date, volume and close_price
    if (int(date[0:4]) in range(2004,2019)): 
    	print '%s\t%s\t%s' % (sector+'_'+date,volume,close)