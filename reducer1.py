#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

#this function is needed to order by the second element
def takeSecond(elem):
    return elem[1]

current_ticker = None
first_year = None
current_year = None
close_1998 = None
min_lowThe = None
max_highThe = None
sum_volume = None
count_volume = None
ticker = None

list_ticker = []


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    ticker_date, close, lowThe, highThe, volume = line.split('\t', 4)
    # extract the ticker and the date by separating ticker_date
    ticker, date = ticker_date.split('_', 1)

    # print '%s\t%s\t%s\t%s\t%s\t%s\t' % (ticker, date, close, lowThe, highThe, volume)

    # convert in int and float
    try:
        year = int(date[0:4])
        close = float(close)
        lowThe = float(lowThe)
        highThe = float(highThe)
        volume = int(volume)
        # print 'br1'
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
        print 'errore'

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: ticker_date) before it is passed to the reducer
    if current_ticker == ticker:
        current_year = year
        min_lowThe = min(min_lowThe,lowThe)
        max_highThe = max(max_highThe,highThe)
        sum_volume += volume
        count_volume += 1
        # print 'br3'
    else:
        if (current_ticker) and (first_year == 1998) and (current_year == 2018):
            # write result to STDOUT
            delta = close - close_1998
            # percentage
            perc = delta/close_1998*100
            avg_volume = sum_volume/count_volume
            # list_ticker.append((current_ticker,perc,min_lowThe,max_highThe,avg_volume))
            list_ticker.append((current_ticker,perc,min_lowThe,max_highThe,avg_volume,str(first_year)+'-'+str(current_year)))
            # print 'br4'

        first_year = year
        current_ticker = ticker
        # close price value in 1998
        close_1998 = close
        current_year = year
        min_lowThe = lowThe
        max_highThe = highThe
        sum_volume = volume
        count_volume = 1
        # print 'br2'

# do not forget to output the last ticker if needed!
if current_ticker == ticker and (first_year == 1998) and (current_year == 2018):
    delta = close - close_1998
    perc = delta/close_1998*100
    avg_volume = sum_volume/count_volume
    # list_ticker.append((current_ticker,perc,min_lowThe,max_highThe,avg_volume))
    list_ticker.append((current_ticker,perc,min_lowThe,max_highThe,avg_volume,str(first_year)+'-'+str(current_year)))
    # print 'br5'

# sort the list by close price 
list_ticker.sort(key=takeSecond,reverse=True)

# write result to STDOUT
# print 'Ticker\tClose_Price_Variance\tLowest_Price\tHighest_Price\tDaily_Average_Volume\n'
print 'Ticker\tClose_Price_Variance\tLowest_Price\tHighest_Price\tDaily_Average_Volume\tPeriod\n'
for elem in list_ticker:
    # print 'br6'
    if elem[1] < 0:
        print '%s\t%s\t%s\t%s\t%s\t%s' % (elem[0], str(elem[1])+'%', elem[2], elem[3], elem[4], elem[5])
    else:
        print '%s\t%s\t%s\t%s\t%s\t%s' % (elem[0], '+'+str(elem[1])+'%', elem[2], elem[3], elem[4], elem[5])