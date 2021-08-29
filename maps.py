'''
Created on Aug 24, 2021

@author: lon
'''
import requests
import json
import sys
import config
'''
Takes a list of user input locations to build the directions url.
Creates json file that will be parsed through to retrieve values.
'''
def directurl(addresslist):
    startloc = addresslist[0:1]
    endloc = addresslist[1:len(addresslist)]
    
    durldict = {"key": config.api_key, 'from': '', 'to': ''}
    durldict['from'] = startloc
    durldict['to'] = endloc
    
    directreq = requests.get('http://open.mapquestapi.com/directions/v2/route', params = durldict)
    json_data = requests.get(directreq.url).json()
    
    with open('json_data.json', 'w') as outfile1:
        json.dump(json_data, outfile1)
        
    with open('json_data.json') as data_file1:
        return json.load(data_file1)
    
'''
Checks to see if an appropriate json response is created from urls.
If the json is successful, will return the passed in json. Otherwise,
an error will print out depending on the error source.
'''
def checkjson(jsondata):
    if jsondata['info']['statuscode'] == 0:
        return jsondata
        pass
    elif jsondata['info']['statuscode'] != 0:
        print('\nNo Route Found!') #can also be seen with an elevation error in mapquest
        sys.exit(1)
    elif jsondata['info']['statuscode'] == 500:
        print('\nMAPQUEST ERROR') #typically seen with elevation error when mapquest thinks it is in canada
        pass
    else:
        print('\nMAPQUEST ERROR')
        sys,exit(1)
        
'''
Takes a list of latitudes and longitudes to build the elevation url.
Creates json file that will be parsed through to retrieve elevation values.
'''
def elevurl(latlonglist):
    eurldict = {'key': config.api_key, 'shapeFormat': 'raw', 'latlngCollection': ''}
    elist = latlonglist #coord.latlnglist(data) #lllist
    estring = ','.join(map(str, elist))
    eurldict['latlngCollection'] = estring
    
    elevreq = requests.get('http://open.mapquestapi.com/elevation/v1/profile', params = eurldict)
    ejson_data = requests.get(elevreq.url).json()
    ejson_data = checkjson(ejson_data)
    
    with open('ejson_data.json', 'w') as outfile2:
        json.dump(ejson_data, outfile2)
        
    with open('ejson_data.json') as data_file2:
        return json.load(data_file2)