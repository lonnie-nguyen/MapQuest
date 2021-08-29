'''
Created on Aug 24, 2021

@author: lon
'''
class STEPS: 
    '''
    Parses through json dictionary object to get values for line by line directions
    '''
    def info(self, jobj):  
        print('\nDIRECTIONS')
        
        for i in jobj['route']['legs']:
            for j in i['maneuvers']:
                #print(j['narrative'])
                yield j['narrative']
                
class TOTALDISTANCE:            
    '''
    Parses through json dictionary object to get value for distance
    '''
    def info(self, jobj):
        miles = int(round(jobj['route']['distance']))
        
        if miles <= 1:
            yield '\nTOTAL DISTANCE: ' + str(miles) + ' mile'
        else:
            yield '\nTOTAL DISTANCE: ' + str(miles) + ' miles '
            
class TOTALTIME:
    '''
    Parses through json dictionary object to get value for time
    '''
    def info(self, jobj):
        minutes = int(round(jobj['route']['time'] / 60))
        
        if minutes <= 1:
            yield '\nTOTAL TIME: ' + str(minutes) + ' minute'
        else:
            yield '\nTOTAL TIME: ' + str(minutes) + ' minutes'

class LATLONG:
    '''
    Parses through json dictionary object to get values for latitude and
    longitude.
    Separate function (latlnglist) for parsing through json latitude and
    longitude values. Values are appended to a list that will be passed in
    to a function to create the url for elevation.
    '''
    def info(self, jobj):
        print('\nLATLONGS')
        
        for i in jobj['route']['locations']:
            lat = i['latLng']['lat']
            
            if str(lat).startswith('-'):
                #yield str(format(abs(lat), '.2f')) + 'S ' #can't use end=''
                lat = str(format(abs(lat), ',2f')) + 'S '
            else:
                #yield str(format(lat, '.2f')) + 'N ' #can't use end=''
                lat = str(format(lat, '.2f')) + 'S '
                
            lng = i['latLng']['lng']
            
            if str(lng).startswith('-'):
                #yield str(format(abs(lng), '.2f')) + 'W'
                lng = str(format(abs(lng), '.2f')) + 'W'
            else:
                #yield str(format(lng, '.2f')) + 'E'
                lng = str(format(lng, '.2f')) + 'E'
            
            yield lat + lng #concatenates lat and lng strings so they print on the same line
            
    def latlnglist(self, jobj):
        lllist = []
        
        for i in jobj['route']['locations']:
            lat = i['latLng']['lat']
            lllist.append(lat)
            
            lng = i['latLng']['lng']
            lllist.append(lng)
            
        return lllist
    
class ELEVATION:
    '''
    Parse through json dictionary object to get value for elevation
    '''
    def info(self, eobj):
        print('\nELEVATIONS')
        
        for i in eobj['elevationProfile']:
            yield i['height']
                