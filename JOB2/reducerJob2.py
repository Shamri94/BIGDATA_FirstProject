#!/usr/bin/env python3
"""reducerJob2.py"""

from operator import itemgetter
import sys

current_year = None
current_sector = None
current_date = None
days = None
sector = None
last_day_close = None
total_volume = None
total_close = None

dict_ticker_InitialCurrent_close = None



# data structure to keep track of the initial close and final close in the year
# This structure is needed beacause the dates for the first occurrence
# of a ticker in a year may change
def update_dict(dict_ticker_InitialCurrent_close,ticker,clo):
    if ticker not in dict_ticker_InitialCurrent_close:
        dict_ticker_InitialCurrent_close[ticker] = {}
        dict_ticker_InitialCurrent_close[ticker]['initial'] = clo
        dict_ticker_InitialCurrent_close[ticker]['current'] = 0.0
    else:
        dict_ticker_InitialCurrent_close[ticker]['current'] = clo



# function for output the result
def write_output():
    first_day_close = 0
    last_day_close = 0
    for ticker in dict_ticker_InitialCurrent_close:
        first_day_close += dict_ticker_InitialCurrent_close[ticker]['initial']
        last_day_close += dict_ticker_InitialCurrent_close[ticker]['current']
    # compute the trend percentage
    perc = (last_day_close - first_day_close)/first_day_close*100
    if perc < 0:
        print(current_sector, current_year, total_volume, str(perc)+'%', total_close/days, sep='\t')
    else:
        print(current_sector, current_year, total_volume, '+'+str(perc)+'%', total_close/days, sep='\t')




print('Sector\tYear\tTotal_Volume\tPercent_Variance\tDaily_Average_Close_Price\n')
# input comes from STDIN
for line in sys.stdin:
     # remove leading and trailing whitespace and insert the data in valueList
    dataValue = line.strip().split('\t')

    if len(dataValue) == 5:
        # parse the input we got from mapperJob2.py
        sector, date, ticker, close, volume = dataValue

        # convert year and volume (currently a string) to int and close to float
        try:
            year = int(date[0:4])
            close = float(close)
            volume = int(volume)
        except ValueError:
            print('Conversion Error')
            continue

        # if the iteration hasn't changed year, keep updating these variables
        if current_year == year:
            if current_date == date:
                total_volume += volume
                total_close += close
                update_dict(dict_ticker_InitialCurrent_close,ticker,close)

            else:
                current_date = date
                total_volume += volume
                total_close += close
                days += 1
                update_dict(dict_ticker_InitialCurrent_close,ticker,close)

        # write result to STDOUT
        # When a new year is parsed, output the data from the current year
        else:
            if current_year:
                write_output()

            # initialization of a new year
            current_year = year
            current_date = date
            # initial_date = date
            total_volume = volume
            # initializr a new structure
            dict_ticker_InitialCurrent_close = {}
            total_close = close
            days = 1
            current_sector = sector
            update_dict(dict_ticker_InitialCurrent_close,ticker,close)

# do not forget to output the last year
if current_year == year:
    write_output()
