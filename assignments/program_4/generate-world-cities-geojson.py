
import pprint as pp
import os,sys
import json
import collections

f = open("C:\\Users\\QT\\Desktop\\CMPS-5323-Spatial-DS\\Spatial-DS-Doan-master\\assignments\\program_4\\json\\world_cities_large.json","r")

data = f.read()

data = json.loads(data)

all_cities = []

for m,n in data.items():
    for e in n:
        gj = collections.OrderedDict()
        gj['type'] = "Feature"
        gj['geometry'] = {"type":"Point"}
        #pp.print(e['lon'],e['lat'])
        i=e['lon']
        if i!="":
            i1=float(i)
        j=e['lat']
        if j!="":

            j1=float(j)
        gj['geometry']['coordinates'] =[i1,j1]
        del e['lon']
        del e['lat']
        gj['properties'] = e
        all_cities.append(gj)

out = open("C:\\Users\\QT\\Desktop\\CMPS-5323-Spatial-DS\\Spatial-DS-Doan-master\\assignments\\program_4\\geo_json\\cities_gj.geojson","w")

out.write(json.dumps(all_cities, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()