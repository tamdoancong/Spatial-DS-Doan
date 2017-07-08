import numpy as np
import matplotlib.pyplot as plt
import pygame
import math
from pprint import pprint 
import os,sys
import json
import collections
from numpy  import array
import statistics
"""
Program:
--------
    Program 6 - Terrorists attack map heap

Description:
------------
    This program read terrorsist's attack data from attacks.json and create map heat.
Name: Tam Doan
Date: jul 7 2017
"""


def median(lst):
    """
    This function return median of list
    """
    return numpy.median(numpy.array(lst))

def mercX(lon):
    """
    Mercator projection from longitude to X coord
    """
    zoom = 1.0
    lon = math.radians(lon)
    a = (256.0 / math.pi) * pow(2.0, zoom)
    b = lon + math.pi
    return int(a * b)


def mercY(lat):
    """
    Mercator projection from latitude to Y coord
    """
    zoom = 1.0
    lat = math.radians(lat)
    a = (256.0 / math.pi) * pow(2.0, zoom)
    b = math.tan(math.pi / 4 + lat / 2)
    c = math.pi - math.log(b)
    return int(a * c)

def adjust_location_coords(extremes,points,width,height):
    """
    Adjust your point data to fit in the screen. 
    Input:
        extremes: dictionary with all maxes and mins
        points: list of points
        width: width of screen to plot to
        height: height of screen to plot to
    """
    maxx = float(extremes['max_x']) # The max coords from bounding rectangles
    minx = float(extremes['min_x'])
    maxy = float(extremes['max_y'])
    miny = float(extremes['min_y'])
    deltax = float(maxx) - float(minx)
    deltay = float(maxy) - float(miny)

    adjusted = []

    for p in points:
        x,y = p
        x = float(x)
        y = float(y)
        xprime = (x - minx) / deltax         
        yprime = ((y - miny) / deltay) 
        adjx = int(xprime*width)
        adjy = int(yprime*height)
        adjusted.append((adjx,adjy))
    return adjusted
#open attacks.json file
f = open("C:\\Users\\QT\\Desktop\\CMPS-5323-Spatial-DS\\Spatial-DS-Doan-master\\assignments\\program_6\\attacks.json","r")

data = f.read()
data = json.loads(data)
#create array to store all x coordinate
allx = []
#create array to store all y coordinate
ally = []
#create array to store all number attack in  associate city
c=[]
# for loop to get which data we need
for m,n in data.items():
    for k,j in n.items():
        c1=j['count']
        lon,lat=j['geometry']['coordinates']
        # adjust coordinate
        x,y = (mercX(lon),mercY(lat))
        #store x into array
        allx.append(x)
        #store y into array
        ally.append(y)
        #store number of attack each city into array
        c.append(c1)
#tranfer x to numpy array
x = array(allx)
#tranfer y to numpy array
y = array(ally)
#tranfer number of attack each city to numpy array
z=array(c)
#insert background image
img = plt.imread("/Users/QT/Desktop/CMPS-5323-Spatial-DS/Spatial-DS-Doan-master/assignments/program_6/world_map.png")
implot = plt.imshow(img,zorder=0, extent=[-100, 1024, -100, 700])
#color will change from cool to warm base on this variable
scaled_z = (z -z.min())/20
colors = plt.cm.coolwarm(scaled_z)
plt.scatter(x, y, marker='.', edgecolors=colors, s=100, linewidths=4)
plt.title('Terrorist attack  heatmap ')
plt.ylabel('y')
plt.xlabel('x')
plt.show()
