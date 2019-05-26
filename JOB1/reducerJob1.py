#!/usr/bin/env python3
"""reducerJob1.py"""

import sys

current_ticker = None
first_year = None
current_year = None
close_1998 = None
current_close = None
min_lowThe = None
max_highThe = None
sum_volume = None
count_volume = None
ticker = None

list_ticker = []

print('Ticker\tClose_Price_Percentage_Change\tLowest_Price\tHighest_Price\tDaily_Average_Volume\n')
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace and insert the data in valueList
    valueList = line.strip().split('\t')

    # parse the input we got from mapperJob1.py
    ticker, date, close, lowThe, highThe, volume = valueList

    # convert the fields in int and float
    try:
        year = int(date[0:4].strip())
        close = float(close.strip())
        lowThe = float(lowThe.strip())
        highThe = float(highThe.strip())
        volume = int(volume.strip())
    except ValueError:
        print ('ValueError')
        continue

    if current_ticker == ticker:
        current_year = year
        current_close = close
        min_lowThe = min(min_lowThe,lowThe)
        max_highThe = max(max_highThe,highThe)
        sum_volume += volume
        count_volume += 1
    else:
        # take only the ticker who appears in 1998 and in 2018
        if (current_ticker) and (first_year == 1998) and (current_year == 2018):
            # write result to STDOUT
            delta = current_close - close_1998
            # percentage
            perc = (delta/close_1998)*100
            avg_volume = sum_volume/count_volume
            list_ticker.append((current_ticker,perc,min_lowThe,max_highThe,avg_volume))

        first_year = year
        current_ticker = ticker
        # close price value in 1998
        close_1998 = close
        # current close price
        current_close = close
        current_year = year
        min_lowThe = lowThe
        max_highThe = highThe
        sum_volume = volume
        count_volume = 1

# do not forget to output the last ticker!
if current_ticker == ticker and (first_year == 1998) and (current_year == 2018):
    delta = current_close - close_1998
    perc = (delta/close_1998)*100
    avg_volume = sum_volume/count_volume
    list_ticker.append((current_ticker,perc,min_lowThe,max_highThe,avg_volume))

# sort the list by close price- The key for the sorting is set with a lambda function
list_ticker.sort(key=lambda elem: elem[1], reverse=True)

# print the top 10
for elem in list_ticker[:10]:
    if elem[1] < 0:
        print(elem[0], str(elem[1])+'%', elem[2], elem[3], elem[4], sep='\t')
    else:
        print(elem[0], '+'+str(elem[1])+'%', elem[2], elem[3], elem[4], sep='\t')
