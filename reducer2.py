#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_year = None
current_sector = None
current_date = None
days = None
sector = None
current_day_close = None
first_day_close = None
current_day_close = None

# input comes from STDIN
print 'Sector\tYear\tTotal_Volume\tPercent_Variance\tDaily_Average_Close_Price\n'

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    sector_date, volume, close = line.split('\t', 2)
    # extract sector and date
    sector, date = sector_date.split('_', 1)

    # convert count (currently a string) to int
    try:
        year = int(date[0:4])
        close = float(close)
        volume = int(volume)
    except ValueError:
        print 'Conversion Error'
        continue

    # if the iteration has changed year, keep updating these variables
    if current_year == year:

        if initial_date == date:
            first_day_close += close
            current_day_close += close
            total_volume += volume
            total_close += close

        elif (initial_date != date) and (current_date == date):
            total_volume += volume
            total_close += close
            current_day_close += close

        elif current_date != date:
            current_date = date
            total_volume += volume
            total_close += close
            current_day_close = close
            days += 1

    # write result to STDOUT
    # When a new year is parsed, output the data from the current year
    else:
        if current_year:
            perc = (current_day_close - first_day_close)/first_day_close*100
            if perc < 0:
                print '%s\t%s\t%s\t%s\t%s' % (current_sector, current_year, total_volume, str(round(perc))+'%', total_close/days)
            else:
                print '%s\t%s\t%s\t%s\t%s' % (current_sector, current_year, total_volume, '+'+str(round(perc))+'%', total_close/days)
        # initialization of a new year
        current_year = year
        current_date = date
        initial_date = date
        total_volume = volume
        first_day_close = close
        current_day_close = close
        total_close = close
        days = 1
        current_sector = sector

# do not forget to output the last year if needed!
if current_year == year:
    perc = (current_day_close - first_day_close)/first_day_close*100
    if perc < 0:
        print '%s\t%s\t%s\t%s\t%s' % (current_sector, current_year, total_volume, str(round(perc))+'%', total_close/days)
    else:
        print '%s\t%s\t%s\t%s\t%s' % (current_sector, current_year, total_volume, '+'+str(round(perc))+'%', total_close/days)