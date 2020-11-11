from flask import Flask
from flask import Response
#import pymysql

#db = pymysql.connect("localhost","testuser","test123","COVIDDB")
#cursor = db.cursor()
app = Flask(__name__)

# e.g. http://127.0.0.1:5000/md-howard/2020-05-01
@app.route('/<date>/<state_id>')
@app.route('/<date>/<state_id>/<county_id>')
@app.route('/<date>/<state_id>/<county_id>/<prison_id>')
def covid(date,state_id, county_id = None, prison_id = None ):
#def covid(date,state_id,county_id):
    Counties = []
    Baltimore ={"state":"Maryland","county": "Baltimore","cases": "67","deaths":"5"}
    Howard ={"state":"Maryland","county": "Howard","cases": "500","deaths":"25"}
    Allegany ={"state":"Maryland","county": "Allegany","cases": "17","deaths":"2"}
    Counties.append(Baltimore)
    Counties.append(Howard)
    Counties.append(Allegany)
    Prisons =[]
    Jessup = {"county": "Allegany","prison":"Jessup Correctional Institution","cases": "3","deaths":"1"}
    BaltP = {"county": "Baltimore","prison":"Baltimore City Correctional Center","cases": "5","deaths":"0"}
    Prisons.append(Jessup)
    Prisons.append(BaltP)
    chosenCounty = 0
    chosenPrison = 0
    statedeaths = 0
    statecases = 0
    for county in Counties:
        if county_id != None:
            if county["state"].lower() == state_id.lower() and county["county"].lower() == county_id.lower():
                chosenCounty = county
        statecases += int(county["cases"])
        statedeaths += int(county["deaths"])
    for prison in Prisons:
        if prison_id != None:
            if prison["county"].lower() == county_id.lower() and prison["prison"].lower() == prison_id.lower():
                chosenPrison = prison
    # Query for that county/date https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
    # return something like (but now figure out how to return for all counties in MD etc. - maybe query by state?)
    #json = '{"date": "' + date + '", "county": "' + county_id + '", "count": 42}'
    if(county_id == None and prison_id == None):
        json = '{"date": "' + date + '","state":"' + state_id + '","cases":"' + str(statecases) + '" , "deaths": "' + str(statedeaths) + '"}' 
    elif(prison_id == None):

        json = '{"date": "' + date + '","state":"' + state_id + '","county": "' + county_id + '", "cases":"' + chosenCounty["cases"] + '" , "deaths": "' + chosenCounty["deaths"] + '"}' #"' + date + '"
    else:
        json = '{"date": "' + date + '","state":"' + state_id + '","county": "' + county_id + '","prison": "' + prison_id + '", "cases":"' + chosenPrison["cases"] + '" , "deaths": "' + chosenPrison["deaths"] + '"}'
    
    response = Response(json, mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response