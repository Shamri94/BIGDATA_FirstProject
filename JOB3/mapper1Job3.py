#!/usr/bin/env python3
"""mapper1Job3.py"""

import sys
import csv

year_2016 = 2016
year_2018 = 2018

dict_ticker_name = {}

# reading from CSV
with open('historical_stocks.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    # ignore first line
    firstLine = True

    for row in csv_reader:
        if not firstLine:
            ticker, _, name, sector, _ = row
            # ignore the tickers witch N/A as sector
            if sector != 'N/A':
                dict_ticker_name[ticker] = name
        else:
            firstLine = False

for line in sys.stdin:
    # turn each row into a list of strings
    dataList = line.strip().split(',')
    if len(dataList) == 8:
        ticker, _, close, _, _, _, _, date = dataList
        # ignore file's first row
        if ticker != 'ticker':
            year = int(date[0:4])

            # check if year is in range year_2016-year_2018
            # check if the ticker has a corresponding sector (we filter out
            if year in range(year_2016, year_2018 + 1) and ticker in dict_ticker_name:
                name = dict_ticker_name[ticker]
                print(name,ticker,date,close, sep='\t')
