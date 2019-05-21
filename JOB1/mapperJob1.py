#!/usr/bin/env python3
"""mapperJob1.py"""

import sys

firstLine = True
year_1998 = 1998
year_2018 = 2018

# input comes from STDIN (standard input)
for line in sys.stdin:
	#skip first line
	if firstLine:
		firstLine = False
		continue

	# remove leading and trailing whitespace and insert the data in dataList
	dataList = line.strip().split(',')

	if len(dataList) == 8:
		# get the relevant data
		ticker, _, close, _, lowThe, highThe, volume, date = dataList
		year = int(date[0:4])
		# select ony the ticker between 1998 and 2018
		if (year in range(year_1998,year_2018 + 1)): 
			print(ticker,date,close,lowThe,highThe,volume, sep='\t')