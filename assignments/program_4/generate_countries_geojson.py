import pprint as pp
import os,sys
import json
import collections
f = open("C:\\Users\\QT\\Desktop\\CMPS-5323-Spatial-DS\\Spatial-DS-Doan-master\\assignments\\program_4\\json\\countries.json","r")
data = f.read()
data = json.loads(data)
all_countries = []
for e in data:
    c = collections.OrderedDict()
    i=e['id']
    del e['id']
    c=e
    c['properties']['id']=i
    all_countries.append(c)
out = open("C:\\Users\\QT\\Desktop\\CMPS-5323-Spatial-DS\\Spatial-DS-Doan-master\\assignments\\program_4\\geo_json\\countries_gj.geojson","w")
out.write(json.dumps(all_countries, sort_keys=False,indent=4, separators=(',', ': ')))
out.close()