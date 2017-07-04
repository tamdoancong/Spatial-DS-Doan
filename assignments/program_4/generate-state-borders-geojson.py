
import pprint as pp
import os,sys
import json
import collections
f = open("C:\\Users\\QT\\Desktop\\CMPS-5323-Spatial-DS\\Spatial-DS-Doan-master\\assignments\\program_4\\json\\state_borders.json","r")
data = f.read()
data = json.loads(data)
all_states = []

for e in data:
    s = collections.OrderedDict()
    s['type'] = "Feature"
    s['geometry'] = {"type":"Polygon"}
    s['geometry']['coordinates'] =e['borders']
    del e['borders']
    s['properties'] = e
    all_states.append(s)
out = open("C:\\Users\\QT\\Desktop\\CMPS-5323-Spatial-DS\\Spatial-DS-Doan-master\\assignments\\program_4\\geo_json\\state_borders_gj.geojson","w")

out.write(json.dumps(all_states, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()