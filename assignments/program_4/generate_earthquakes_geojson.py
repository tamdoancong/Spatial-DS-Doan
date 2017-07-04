# reference Dr.Griffin code
import pprint as pp
import os,sys
import json
import collections
f = open("C:\\Users\\QT\\Desktop\\CMPS-5323-Spatial-DS\\Spatial-DS-Doan-master\\assignments\\program_4\\json\\earthquakes-1960-2017.json","r")
data = f.read()
data = json.loads(data)
all_quakes = []
for k,quakes in data.items():
    for e in quakes:
        eq = collections.OrderedDict()
        eq['type'] = "Feature"
        eq['geometry'] = {"type":"Point"}
        eq['geometry']['coordinates'] = [e['geometry']['coordinates'][0],e['geometry']['coordinates'][1]]
        depth = e['geometry']['coordinates'][2]
        del e['geometry']
        eq['properties'] = e
        eq['properties']['depth'] = depth
        eq['properties']['year'] = k
        all_quakes.append(eq)
out = open("C:\\Users\\QT\\Desktop\\CMPS-5323-Spatial-DS\\Spatial-DS-Doan-master\\assignments\\program_4\\geo_json\\earthquakes_gj.geojson","w")

out.write(json.dumps(all_quakes, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()