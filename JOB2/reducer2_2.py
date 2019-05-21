#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

current_year = None
current_sector = None
current_date = None
days = None
sector = None
last_day_close = None
first_day_close = None
current_day_close = None
total_volume = None
total_close = None

dict_ticker_initial_current = None

# input comes from STDIN
print('Sector\tYear\tTotal_Volume\tPercent_Variance\tDaily_Average_Close_Price\n')

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    sector_date, volume, close, ticker = line.split('\t', 3)
    # extract sector and date
    sector, date = sector_date.split('_', 1)

    # convert year and volume (currently a string) to int and close to float
    try:
        year = int(date[0:4])
        close = float(close)
        volume = int(volume)
    except ValueError:
        print('Conversion Error')
        continue

    if current_year == year:
        # if the iteration hasn't changed year, keep updating these variables
        if current_date == date:
            # first_day_close += close
            # current_day_close += close
            total_volume += volume
            total_close += close
            # dizionario per memorizzare close iniziale e finale di ogni ticker dell'anno corrente
            if ticker not in dict_ticker_initial_current:
                dict_ticker_initial_current[ticker] = [close,0.0]
            else:
                dict_ticker_initial_current[ticker][1] = close

        # elif (initial_date != date) and (current_date == date):
        #     total_volume += volume
        #     total_close += close
        #     # current_day_close += close
        #     if ticker not in dict_ticker_initial_current:
        #         dict_ticker_initial_current[ticker] = [close,0.0]
        #     else:
        #         dict_ticker_initial_current[ticker][1] = close


        else:
            current_date = date
            total_volume += volume
            total_close += close
            # current_day_close = close
            days += 1
            if ticker not in dict_ticker_initial_current:
                dict_ticker_initial_current[ticker] = [close,0.0]
            else:
                dict_ticker_initial_current[ticker][1] = close

    # write result to STDOUT
    # When a new year is parsed, output the data from the current year
    else:
        if current_year:

            for i in dict_ticker_initial_current:
                first_day_close += dict_ticker_initial_current[i][0]
                last_day_close += dict_ticker_initial_current[i][1]

            perc = (last_day_close - first_day_close)/first_day_close
            if perc < 0:
                print(current_sector, current_year, total_volume, str(perc)+'', total_close/days, sep='\t')
            else:
                print(current_sector, current_year, total_volume, '+'+str(perc)+'', total_close/days, sep='\t')
        # initialization of a new year
        current_year = year
        current_date = date
        # initial_date = date
        total_volume = volume
        first_day_close = 0
        last_day_close = 0
        dict_ticker_initial_current = {}
        # first_day_close = close
        # current_day_close = close
        total_close = close
        days = 1
        current_sector = sector
        dict_ticker_initial_current[ticker] = [close,0.0]

# do not forget to output the last year if needed!
if current_year == year:

    for i in dict_ticker_initial_current:
        first_day_close += dict_ticker_initial_current[i][0]
        last_day_close += dict_ticker_initial_current[i][1]

    perc = (last_day_close - first_day_close)/first_day_close
    if perc < 0:
        print(current_sector, current_year, total_volume, str(perc)+'', total_close/days, sep='\t')
    else:
        print(current_sector, current_year, total_volume, '+'+str(perc)+'', total_close/days, sep='\t')