#!/usr/bin/env python3
"""reducer2Job3.py"""

import sys


# global variables
current_percentChangeTriplet = None

companyList = []


# *** utility functions ***

# utility function for printing a set of key value pairs
def writeRecord():
    listLength = len(companyList)
    for i in range(listLength - 1):
        for j in range(i, listLength):
            firstCompany = companyList[i]
            firstCompanyName = firstCompany['name']
            firstCompanySector = firstCompany['sector']
            secondCompany = companyList[j]
            secondCompanyName = secondCompany['name']
            secondCompanySector = secondCompany['sector']
            if firstCompanySector != secondCompanySector and firstCompanyName != secondCompanyName:
                percentChange_2016 = None 
                percentChange_2017 = None 
                percentChange_2018 = None
                if current_percentChangeTriplet[0][0] == '-':
                    percentChange_2016 = '2016: '+current_percentChangeTriplet[0]+'%'
                else:
                    percentChange_2016 = '2016: +'+current_percentChangeTriplet[0]+'%'
                if current_percentChangeTriplet[1][0] == '-':
                    percentChange_2017 = '2017: '+current_percentChangeTriplet[1]+'%'
                else:
                    percentChange_2017 = '2017: +'+current_percentChangeTriplet[1]+'%'
                if current_percentChangeTriplet[2][0] == '-':
                    percentChange_2018 = '2018: '+current_percentChangeTriplet[2]+'%'
                else:
                    percentChange_2018 = '2018: +'+current_percentChangeTriplet[2]+'%'
                print(firstCompanyName,firstCompanySector,secondCompanyName,secondCompanySector,percentChange_2016,percentChange_2017,percentChange_2018,sep='\t')



# add a new entry in companyList global variable
def addItemToList(sector, name):
    entry = {'sector': sector, 'name': name}
    companyList.append(entry)



# parse each value in value list
def parseValues(valueList):
    percentChange2016 = valueList[0].strip()
    percentChange2017 = valueList[1].strip()
    percentChange2018 = valueList[2].strip()
    name = valueList[3].strip()
    sector = valueList[4].strip()
    return ((percentChange2016, percentChange2017, percentChange2018),
            name,
            sector)



print('Company\tSector\tCompany\tSector\tTrend 2016\tTrend 2017\tTrend 2018')
# main script
for line in sys.stdin:
    valueList = line.strip().split('\t')

    if len(valueList) == 5:
        percentChangeTriplet, name, sector = parseValues(valueList)

        if current_percentChangeTriplet and (current_percentChangeTriplet != percentChangeTriplet):
            # triplet changed.
            # So we write a new record for the previous company,
            # update global variables for the new company
            # and finally update company list for the new triplet
            writeRecord()
            # reset variable values
            current_percentChangeTriplet = percentChangeTriplet
            # reset our list
            companyList = []
            # add a new entry in companyList
            addItemToList(sector, name)

        else:
            # key value unchanged (or this is the first row of the file).
            current_percentChangeTriplet = percentChangeTriplet
            # add a new entry in companyList
            addItemToList(sector, name)

# print last computed key
if current_percentChangeTriplet:
    writeRecord()