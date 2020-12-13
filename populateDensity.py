#This script is going to grab densities from newcounties.csv and populate them into a txt file (US-Counties.js)
#Format to grab from has date,county,state,cases,deaths. This file only pulls cases from each county, and populates 
#US-Counties.js with a new string.
#EDGE CASES TO COVER:
#   -Make sure that correct state is populated. Ex) 2020-11-10,McLean,Kentucky,274,8 must populate where name = Mclean and state = KY
#   -Make sure to skip line 1 of newcounties.csv, as it is just the format
#   -Make sure to only populate one days worth of data. Ex) 2020-11-10, McLean, Kentucky, 274, 8 only refers to the 10th of November. Don't worry about the other days for this county.
#   -Every three lines, add the density field 
#   -Divide the number of cases per state by 2 to normalize (15,043 and 1000 would have the same shade otherwise)

#STEPS:
#   1) Read in all county densities from newcounties.csv, store in dictionary
#   2) Add this string to US-Counties.js on every third line after

import os

def findDensity(stateStr, countyStr, stateInfo):
    
    for i in range(len(stateInfo)):
        
        #if((stateInfo[i][0] == None) or (stateInfo[i][1] == None)):
        #    break
        
        if (stateInfo[i][0] == stateStr) and (countyStr in stateInfo[i][1]):             
            return stateInfo[i][2]


def getAbbr(name, stateArr):


    for i in range(len(stateArr)):

        if name.lower() == stateArr[i]['state'].lower():
            
            return stateArr[i]['abbr']
       
    return name

def getFullName(name, stateArr):

    for i in range(len(stateArr)):
        if name.lower() == stateArr[i]['abbr'].lower():
            return stateArr[i]['state']
        
    return name

fileToRead = "C:\\Users\\Sean\\Desktop\\School\\Senior Year\\CMSC 447\\Covid-MapTracker-T3-Site\\Covid-MapTracker-T3.github.io\\newcounties.csv"

#Use this file to get a dictionary of abbreviations for names of states
f3 = open("abbr-name.csv", 'r')

abbrFile = f3.readlines()
stateAbbr = []

#Create a dictionary entry following the format: state: "maryland", abbr: "MD"
for line in abbrFile:
    line = line.split(',')
    line[0] = line[0].strip('"')
    line[1] = line[1].strip('\n')
    line[1] = line[1].strip('"')
    newDict = {'state': line[1], 'abbr': line[0]}
    stateAbbr.append(newDict)

f1 = open(fileToRead, 'r')

newFile = f1.readlines()[1:]

stateInfo = []

for line in newFile:
    i = 0
    line = line.split(',')
    #Change this date depending on what day you want to display COVID cases for
    #Format: [StateAbbr, County, numCases]
    tempStateInfo = []
    if(line[0] == '2020-12-07'):
        state = getAbbr(line[2], stateAbbr) 
        tempStateInfo.append(state)
        tempStateInfo.append(line[1])
        #Normalize the gradient for display purposes
        if int(line[3]) > 2000:
            numCases = int(line[3]) // 2
        else:
            numCases = int(line[3])

        tempStateInfo.append(str(numCases))
        stateInfo.append(tempStateInfo)

#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   -------------------------------------------------------------------------------
#   This section of the code handles appending stateInfo Densities to US-Counties.js
#   -------------------------------------------------------------------------------
#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

usCountiesJS = "C:\\Users\\Sean\\Desktop\\School\\Senior Year\\CMSC 447\\Covid-MapTracker-T3-Site\\Covid-MapTracker-T3.github.io\\US-Counties.js"

f2 = open(usCountiesJS, 'r')

countyFile = f2.readlines()

newFile = "C:\\Users\\Sean\\Desktop\\School\\Senior Year\\CMSC 447\\Covid-MapTracker-T3-Site\\Covid-MapTracker-T3.github.io\\Final-US-Counties.js"

f4 = open(newFile, 'w')

#Write to newFile line by line, and every line containing 'geometry', add the density for the corresponding state abbr
for i in range(9635):
    
    if('"geometry"' in countyFile[i]):
        newStr = countyFile[i].split('}')
                
        #Search for correct dictionary entry to append
        newStr2 = newStr[0].split('state')
        #Use 2nd index of stateStr for state abbr
        stateStr = newStr2[1].split('"')
        #Use 13th index of countyStr for county name
        countyStr = newStr2[0].split('"')

        newNumCases = findDensity(stateStr[2], countyStr[13], stateInfo)

        if newNumCases == None:
            newNumCases = str(0)
        
        newStr2[1] = ', "density":' + str(newNumCases) + '}'

        strToAdd = newStr[0] + newStr2[1] + newStr[1] + '}}\n'
        
        f4.write(strToAdd)

    else:
        f4.write(countyFile[i])
    

f1.close()
f2.close()
f3.close()
f4.close()