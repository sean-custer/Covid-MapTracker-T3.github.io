#Written by Malcolm Thorpe message for questions

import requests
import json
from bs4 import BeautifulSoup

#class will store all the data that occurs on a day
class Date:
    def __init__(self,name):
        self.name = name
        self.states = []
#class will store all The data of what happens in a state
class State:
    def __init__(self,name):
        self.name = name
        self.counties = []
        self.prisons = []
        self.cases = -1
        self.deaths = -1

#class will store all The data of what happens in a county
class County:
    def __init__(self,name):
        self.name = name
        self.cases = -1
        self.deaths = -1

#class will store all The data of what happens in a prison
class Prison:
    def __init__(self,name):
        self.name = name
        self.cases = -1
        self.deaths = -1

#used to quickly search through an array and find a specific elements index
def index_of(elem, a):

    for i in range(len(a)):
        if(a[i].name.lower() == elem.lower()):
            return i
    return -1

#function is used to return the data that was asked by the user from the web page
#takes in all the parsed data, date, state, county or prison
#returns none
def findUserSearch(AllDates, date, state, countyOrPrison = None):
    UserValue = {}
    a = index_of(date,AllDates)
    if a == -1:
        UserValue["type"] = "f"
        return UserValue
    b = index_of(state,AllDates[a].states)
    if b == -1:
        UserValue["type"] = "f"
        return UserValue
    c = -1
    choicePrison = False
    choiceCounty = False
    if countyOrPrison != None:

        c = index_of(countyOrPrison,AllDates[a].states[b].counties)
        if c >= 0:
            choiceCounty = True
        else:    
            c = index_of(countyOrPrison,AllDates[a].states[b].prisons)
            if c >= 0:
                choicePrison = True
        if c == -1:
            UserValue["type"] = "f"
            return UserValue
    
    if countyOrPrison == None:
        UserValue["type"] = "s"
        UserValue["date"] = AllDates[a].name
        UserValue["state"] = AllDates[a].states[b].name
        UserValue["statecases"] = AllDates[a].states[b].cases
        UserValue["statedeaths"] = AllDates[a].states[b].deaths
    elif choiceCounty:
        UserValue["type"] = "c"
        UserValue["date"] = AllDates[a].name
        UserValue["state"] = AllDates[a].states[b].name
        UserValue["county"] = AllDates[a].states[b].counties[c].name
        UserValue["countycases"] = AllDates[a].states[b].counties[c].cases
        UserValue["countydeaths"] = AllDates[a].states[b].counties[c].deaths
    elif choicePrison:
        UserValue["type"] = "p"
        UserValue["date"] = AllDates[a].name
        UserValue["state"] = AllDates[a].states[b].name
        UserValue["prison"] = AllDates[a].states[b].prisons[c].name
        UserValue["prisoncases"] = AllDates[a].states[b].prisons[c].cases
        UserValue["prisondeaths"] = AllDates[a].states[b].prisons[c].deaths
    else:
        UserValue["type"] = "f"
        return UserValue
        
    return UserValue

#function is used to test the data that was parsed through the console
#takes in all the parsed data
#returns none
def testSearch(AllDates):
    user = input("Please enter a date and state(enter 'exit' to stop): ")
    

    if user == 'exit':
        return True
    
    allinput = user.split("/")
    num = len(allinput)
    if len(allinput) < 2:
        print("You entered wrong format 1")
        return False

    a = index_of(allinput[0],AllDates)
    if a == -1 and num >= 2 :
        print("You entered wrong format 2")
        return False
    b = index_of(allinput[1],AllDates[a].states)
    if b == -1 and num >= 2:
        print("You entered the wrong format 3")
        return False
    c = -1
    choicePrison = False
    choiceCounty = False
    if num >= 3:

        c = index_of(allinput[2],AllDates[a].states[b].counties)
        if c >= 0:
            choiceCounty = True
        else:    
            c = index_of(allinput[2],AllDates[a].states[b].prisons)
            if c >= 0:
                choicePrison = True
    if num == 2:    
        print("On", AllDates[a].name,"in",AllDates[a].states[b].name, "there were", AllDates[a].states[b].cases, "cases and", 
            AllDates[a].states[b].deaths, "deaths")
        
    elif num == 3 and choiceCounty:
        print("On", AllDates[a].name,"in",AllDates[a].states[b].counties[c].name,"County,",AllDates[a].states[b].name, "there were", AllDates[a].states[b].counties[c].cases, "cases and", 
            AllDates[a].states[b].counties[c].deaths, "deaths")
    elif num == 3 and choicePrison:
        print("On", AllDates[a].name,"in",AllDates[a].states[b].prisons[c].name,",",AllDates[a].states[b].name, "there were", AllDates[a].states[b].prisons[c].cases, "cases and", 
            AllDates[a].states[b].prisons[c].deaths, "deaths")
    return False



#function takes all covid data parses it and puts it in there respecitive object
#array is return populated with date objects, each date will store the states,county,prison covid information
def parseData():

    states = requests.get("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")
    counties = requests.get("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")
    
    states = BeautifulSoup(states.content, 'html.parser')
    counties = BeautifulSoup(counties.content, 'html.parser')
    

    states = states.prettify().split('\n')
    del states[0]
    del states[len(states) - 1]
    AllDates = []
    
    for line in range(len(states)):
        
        data = states[line].split(",")
        date = data[0]
        statename = data[1]
        statecase = data[3]
        statedeath = data[4]

        #check if date is in all dates
    
        i = index_of(date, AllDates)
        if i < 0:
            AllDates.append(Date(date))
            i = len(AllDates) - 1
        
        j = index_of(statename, AllDates[i].states)
        if j < 0:
        
            AllDates[i].states.append(State(statename))
            j = len(AllDates[i].states) - 1
        
        AllDates[i].states[j].cases = statecase
        AllDates[i].states[j].deaths = statedeath
    
    counties = counties.prettify().split('\n')
    del counties[0]
    del counties[len(counties) - 1]

    for line in range(len(counties)):
        data = counties[line].split(",")
        
        date = data[0]
        countyname = data[1]
        statename = data[2]
        countycase = data[4]
        countydeath = data[5]
        i = index_of(date, AllDates)
        j = index_of(statename, AllDates[i].states)
        k = index_of(countyname, AllDates[i].states[j].counties)
        if k < 0:
            AllDates[i].states[j].counties.append(County(countyname))
            k = len(AllDates[i].states[j].counties) - 1

        AllDates[i].states[j].counties[k].cases = countycase
        AllDates[i].states[j].counties[k].deaths = countydeath

    prisonsfile = open("C:\\Users\\Sean\\Desktop\\School\\Senior Year\\CMSC 447\\Covid-MapTracker-T3-Site\\Covid-MapTracker-T3.github.io\\prisonformated.txt", "r")
    prisons = prisonsfile.readlines()[1:]
    #prisonsfile.close()

    for line in prisons:
        date = ""
        statename = ""
        prisonname = ""
        prisoncase = ""
        prisondeath = ""

        comma = 0
        quote = 0

        for letter in line:
            if letter == '"':
                quote += 1
        
            if letter == "," and quote % 2 == 0:
                comma += 1
            elif comma == 0:
                date += letter
            elif comma == 1:
                prisonname += letter
            elif comma == 2:
                statename += letter
            elif comma == 3:
                prisoncase += letter
            elif comma == 4:
                prisondeath += letter

        prisonname = prisonname.strip('"')
        prisondeath = prisondeath.strip()
        
        i = index_of(date, AllDates)
        j = index_of(statename, AllDates[i].states)
        k = index_of(prisonname, AllDates[i].states[j].prisons)
        if k < 0:
            AllDates[i].states[j].prisons.append(Prison(prisonname))
            k = len(AllDates[i].states[j].prisons) - 1

        AllDates[i].states[j].prisons[k].cases = prisoncase
        AllDates[i].states[j].prisons[k].deaths = prisondeath
        #print(prisonname)    
    return AllDates


#data = parseData()
#while not testSearch(data):
 #   pass
