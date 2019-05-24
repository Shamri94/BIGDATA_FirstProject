#!/usr/bin/env python3
"""mapperJob2.py"""

import sys
import csv

year_2004 = 2004
year_2018 = 2018

dict_ticker_sector = {}

# reading from CSV
with open('historical_stocks.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    # ignore first line
    firstLine = True

    for row in csv_reader:
        if not firstLine:
            ticker, _, _, sector, _ = row
            # ignore the tickers witch N/A as sector
            if sector != 'N/A':
                dict_ticker_sector[ticker] = sector
        else:
            firstLine = False

for line in sys.stdin:
    # turn each row into a list of strings
    dataList = line.strip().split(',') 
    if len(dataList) == 8:
        ticker, _, close, _, _, _, volume, date = dataList
        # ignore file's first row
        if ticker != 'ticker':
            year = int(date[0:4])

            # check if year is in range year_2004-year_2018
            # check if the ticker has a corresponding sector
            if year in range(year_2004, year_2018 + 1) and ticker in dict_ticker_sector:
                sector = dict_ticker_sector[ticker]
                print(sector,date,ticker,close,volume, sep='\t')
