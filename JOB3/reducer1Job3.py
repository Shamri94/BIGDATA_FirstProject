#!/usr/bin/env python3
"""reducer1Job3.py"""

import sys
import csv


year_2016 = 2016
year_2018 = 2018
from2016_to2018 = list(range(year_2016, year_2018 + 1))


current_name = None
current_ticker = None
current_year = None
current_close = None

# yearToCompanyTrend is data structure used to avoid date comparison
# it stores data for a SINGLE company name
# so it will be resetted on each company name
'''
key: year, value: dictionary {
    closePriceStartingValue: closePriceStartingValue,
    closePriceFinalValue: closePriceFinalValue,
    }
'''
yearToCompanyTrend = {}

dict_name_sector = {}


# *** utility functions ***


# utility function for printing a set of key value pairs
def print_output():
    # First, let's check that a non null value exists for each year
    if all(str(year) in yearToCompanyTrend for year in from2016_to2018):

        yearToCompanyTrendKeys = yearToCompanyTrend.keys()
        # the last two curly brackets are placeholder
        # for company's sector and name
        listOfSquareBrackets = ['{}'] * len(yearToCompanyTrendKeys) + ['{}', '{}']
        
        formattedString = '\t'.join(listOfSquareBrackets)
        # percentChangeMap = {'2016': None, '2017': None, '2018': None}
        # percentChangeMap is a dictionary whose keys are
        # years (taken from the yearToCompanyTrend keys) and
        # values are None (temporary)

        percentChangeMap = {year: None for year in yearToCompanyTrendKeys}

        for year in sorted(yearToCompanyTrend.keys()):
            sectorTrend = yearToCompanyTrend[year]
            closePriceFinalValue = sectorTrend['closePriceFinalValue']
            closePriceStartingValue = sectorTrend['closePriceStartingValue']
            closeDifference = closePriceFinalValue - closePriceStartingValue
            percentChange = closeDifference/closePriceStartingValue
            percentChangeMap[year] = int(round(percentChange*100))

        sortedPercentChangeMapKeys = sorted(percentChangeMap)
        sortedPercentChangeMapValues = [percentChangeMap[year] for year
                                        in sortedPercentChangeMapKeys]
                                        
        if current_name in dict_name_sector:
            sectorList = dict_name_sector[current_name]
            for sector in sectorList:
                valuesToPrint = sortedPercentChangeMapValues + [current_name,
                                                                sector]
                print(formattedString.format(*(valuesToPrint)))


# add or set "value" to yearToCompanyTrend[year]
# dictionary based on key existence
def updateCompanyTrend(dataStructure, year, key, value):
    if year in dataStructure:
        if key in dataStructure[year]:
            dataStructure[year][key] += value
        else:
            dataStructure[year][key] = value
    else:
        dataStructure[year] = {}
        dataStructure[year][key] = value


# parse each value in value list
def parseValues(valueList):
    name = valueList[0].strip()
    ticker = valueList[1].strip()
    year = valueList[2].strip()[0:4]
    close = float(valueList[3].strip())
    return (name, ticker, year, close)


# code section

# reading from CSV
with open('historical_stocks.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    # ignore first line
    firstLine = True

    for row in csv_reader:
        if not firstLine:
            _, _, name, sector, _ = row
            # ignore the tickers witch N/A as sector
            if sector != 'N/A':
                if name in dict_name_sector:
                    if sector not in dict_name_sector[name]:
                        dict_name_sector[name].append(sector)
                else:
                    dict_name_sector[name] = [sector]
        else:
            firstLine = False


# main script
for line in sys.stdin:
    valueList = line.strip().split('\t')

    if len(valueList) == 4:
        name, ticker, year, close = parseValues(valueList)

        if current_name and current_name != name:
            # company name changed.
            # So we set final close price for the previous company
            # (company's ticker) in the previous year, write a new record for
            # the previous company and reset our dictionary
            updateCompanyTrend(yearToCompanyTrend,
                               current_year,
                               'closePriceFinalValue',
                               current_close)
            print_output()

            # reset our dictionary
            yearToCompanyTrend = {}

            # this is the first available date for this new company's record
            # so we update closePriceStartingValue
            updateCompanyTrend(yearToCompanyTrend,
                               year,
                               'closePriceStartingValue',
                               close)

        else:
            # key value unchanged (or this is the first row of the file).

            # Two cases: same ticker or different ticker
            # That is because a same company may have different
            # tickers
            if current_ticker and current_ticker != ticker:
                # Case 1: Different tickers
                # this means that previous close value was the ending
                # close value for the previous ticker in the previous year
                updateCompanyTrend(yearToCompanyTrend,
                                   current_year,
                                   'closePriceFinalValue',
                                   current_close)

                # this also means that the current close value is the first
                # close value for this ticker in this year
                updateCompanyTrend(yearToCompanyTrend,
                                   year,
                                   'closePriceStartingValue',
                                   close)

            else:
                # Case 2: same ticker or first row of the file
                # first row of the file
                
                # Two cases: same year or different year
                if current_year and current_year != year:
                    # Case 1: Different year
                    # this means that previous close value was the ending
                    # close value for the current ticker in the previous year
                    updateCompanyTrend(yearToCompanyTrend,
                                       current_year,
                                       'closePriceFinalValue',
                                       current_close)

                    # this also means that the current close value is the first
                    # close value for this company in this year
                    updateCompanyTrend(yearToCompanyTrend,
                                       year,
                                       'closePriceStartingValue',
                                       close)
                else:
                    # Another case: same year or first row of the file
                    # first row of the file
                    if not current_year:
                        # this also means that the current close value is the
                        # first close value for this company in this year
                        updateCompanyTrend(yearToCompanyTrend,
                                           year,
                                           'closePriceStartingValue',
                                           close)
                                           
        # reset variable values
        current_name = name
        current_ticker = ticker
        current_year = year
        current_close = close

# print last computed key
if current_name:
    # this means that previous close value was the last value
    updateCompanyTrend(yearToCompanyTrend,
                       current_year,
                       'closePriceFinalValue',
                       current_close)
    print_output()