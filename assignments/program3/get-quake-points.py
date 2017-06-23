import requests
import json
import sys,os
import glob

"""
This class helps read earthquake data.

"""
#this function create a small jasion file to store what data we need
def condense_file(data):
    condensed_data = []  
    for quake in data['features']:
        keep={}  
        keep['geometry'] = quake['geometry']
        keep['mag'] = quake["properties"]["mag"]
        keep['magType'] = quake["properties"]["magType"]
        keep ['time'] = quake["properties"]["time"]
        keep['place'] = quake["properties"]["place"]
        keep['types'] = quake["properties"]["types"]
        keep['rms'] = quake["properties"]["rms"]
        keep['sig'] = quake["properties"]["sig"]
        condensed_data.append(keep)
    return condensed_data

##########################################################################################
# This function read earthquake data year by year and write in 2 file: quake-condensed.json
# and quake.json 
def get_earth_quake_data(year,month=[1,12],minmag=None,maxmag=7,query=True):
    start_month = month[0]
    end_month = month[1]

    if not maxmag is None:
        maxmag = '&maxmagnitude='+str(maxmag)
    else:
        maxmag = ''

    if not minmag is None:
        minmag = '&minmagnitude='+str(minmag)
    else:
        minmag = '&minmagnitude='+str(1.0)

    if query:
        type = 'query'

    else:
        type = 'count'

    url = 'https://earthquake.usgs.gov/fdsnws/event/1/'+type+'?format=geojson&starttime='+str(year)+'-'+str(start_month)+'-01&endtime='+str(year)+'-'+str(end_month)+'-01'+minmag+maxmag

    r = requests.get(url).json()

    if type == 'count':
        return r['count']
    else:
        return r

path = '/Volumes/1TBHDD/code/repos/0courses/4553-Spatial-DS/Resources/EarthquakeData'
years = [x for x in range(1960,2017)]
months = [x for x in range(1,13)]
f1 = open('./quake'+ '.json','w')
f2 = open('./quake-'+ 'condensed'+'.json','w')
rc1=[]
r1=[]
for y in years:
    print("Year:%s" % (y))
    #get data of earthquake which has mag>7
    r = get_earth_quake_data(y,[1,12],7,None,True)
    r1.append(r)
    rc=condense_file(r)
    #ad data from 1960 to 2017 to one list
    rc1=rc1+rc   
f1.write(json.dumps(r1, sort_keys=True,indent=4, separators=(',', ': '))) 
#write data from 1960 to 2017 in one file 
f2.write(json.dumps(rc1, sort_keys=True,indent=4, separators=(',', ': ')))
    
f1.close()
f1.close()