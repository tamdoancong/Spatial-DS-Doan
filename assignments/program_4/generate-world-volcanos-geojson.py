# reference from Dr.Griffin code
import pprint as pp
import os,sys
import json
import collections


f = open("C:\\Users\\QT\\Desktop\\CMPS-5323-Spatial-DS\\Spatial-DS-Doan-master\\assignments\\program_4\\json\\world_volcanos.json","r")

data = f.read()

data = json.loads(data)

all_volcanos = []

"""
mongoimport --db world_data --collection volcanos --type json --file world_volcanos.geojson --jsonArray
db.volcanos.find( { loc: { $geoWithin: { $centerSphere: [ [140.8, 39.76 ] , 50 / 3963.2 ] } } } )
"""


for v in data:
    gj = collections.OrderedDict()
    gj['type'] = "Feature"
    gj['properties'] = v
    if not v['Lat'] and not v['Lon']:
        continue

    lat = float(v['Lat'])
    lon = float(v['Lon'])
    
    del gj['properties']['Lat']
    del gj['properties']['Lon']
    gj["geometry"] = {}
    gj["geometry"]["type"]="Point"
    gj["geometry"]["coordinates"] = [
          lon,
          lat
        ]
    all_volcanos.append(gj)


out = open("C:\\Users\\QT\\Desktop\\CMPS-5323-Spatial-DS\\Spatial-DS-Doan-master\\assignments\\program_4\\geo_json\\volcanos_gj.geojson","w")

out.write(json.dumps(all_volcanos, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()