#This Script is supposed to pull all the coordinates from the second line of every state json file in world.geo.json/countries/USA
import os

fileToWrite = "C:\\Users\\Sean\\Desktop\\School\\Senior Year\\CMSC 447\\Covid-MapTracker-T3-Site\\Covid-MapTracker-T3.github.io\\US-Counties.js"

f2 = open(fileToWrite, 'w')

countries = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"]

length = len(countries)

for x in range(length):

    path = "C:\\Users\\Sean\\Desktop\\School\\Senior Year\\CMSC 447\\Covid-MapTracker-T3-Site\\world.geo.json\\countries\\USA\\" + countries[x]

    for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r') as f: # open in read-only mode
                f2.write(f.read() + ',')

f2.close()