#Written by Malcolm Thorpe message for questions
from flask import Flask
from flask import Response
import NYTIMESparsed

#moduleName = "NYTIMESparsed"
#importlib.import_module(moduleName)
#import pymysql

AllData = NYTIMESparsed.parseData()

#db = pymysql.connect("localhost","testuser","test123","COVIDDB")
#cursor = db.cursor()
app = Flask(__name__)

# e.g. http://127.0.0.1:5000/md-howard/2020-05-01
@app.route('/<date>/<state_id>')
@app.route('/<date>/<state_id>/<countyOrPrison_id>')
def covid(date,state_id, countyOrPrison_id = None, data = AllData):

    # Query for that county/date https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
    # return something like (but now figure out how to return for all counties in MD etc. - maybe query by state?)
    #json = '{"date": "' + date + '", "county": "' + county_id + '", "count": 42}'
    
    Unformated = NYTIMESparsed.findUserSearch(data, date, state_id, countyOrPrison_id)
    if Unformated["type"] == "s":
        json = '{"type": "' + Unformated["type"] + '","date": "' + Unformated["date"] + '","state":"' + Unformated["state"] + '","cases":"' + Unformated["statecases"] + '" , "deaths": "' + Unformated["statedeaths"] + '"}' 
    elif Unformated["type"] == "c":
        json = '{"type": "' + Unformated["type"] + '","date": "' + Unformated["date"] + '","state":"' + Unformated["state"] + '","county": "' + Unformated["county"] + '","cases":"' + Unformated["countycases"] + '" , "deaths": "' + Unformated["countydeaths"] + '"}'
    elif Unformated["type"] == "p":
        json = '{"type": "' + Unformated["type"] + '","date": "' + Unformated["date"] + '","state":"' + Unformated["state"] + '","prison": "' + Unformated["prison"] + '","cases":"' + Unformated["prisoncases"] + '" , "deaths": "' + Unformated["prisondeaths"] + '"}'
    elif Unformated["type"] == "f":
        json = '{"type": "' + Unformated["type"] + '"}'

    response = Response(json, mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response