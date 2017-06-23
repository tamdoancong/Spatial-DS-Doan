import requests
import json
import sys,os
import glob
import math
import pygame
DIRPATH = os.path.dirname(os.path.realpath(__file__))

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
        xprime = (x - minx) / deltax         # val (0,1)
        yprime = ((y - miny) / deltay) # val (0,1)
        adjx = int(xprime*width)
        adjy = int(yprime*height)
        adjusted.append((adjx,adjy))
    return adjusted
def clean_area(screen,origin,width,height,color):
    """
    Prints a color rectangle (typically white) to "erase" an area on the screen.
    Could be used to erase a small area, or the entire screen.
    """
    ox,oy = origin
    points = [(ox,oy),(ox+width,oy),(ox+width,oy+height),(ox,oy+height),(ox,oy)]
    pygame.draw.polygon(screen, color, points, 0)



if __name__=='__main__':

    # Open our condensed json file to extract points
   
    with open(DIRPATH+'/'+'quake-condensed.json') as f:
    #f = open('\Users\QT\Desktop\CMPS-5323-Spatial-DS\quake.json.json','r')
      
        data = json.loads(f.read())
     
    
    allx = []
    ally = []
    points = []

    # Loop through converting lat/lon to x/y and saving extreme values. 
    for quake in data:
        #st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        lon = quake['geometry']['coordinates'][0]
        lat = quake['geometry']['coordinates'][1]
        x,y = (mercX(lon),mercY(lat))
        allx.append(x)
        ally.append(y)
        points.append((x,y))

    # Create dictionary to send to adjust method
    extremes = {}
    extremes['max_x'] = max(allx)
    extremes['min_x'] = min(allx)
    extremes['max_y'] = max(ally)
    extremes['min_y'] = min(ally)

    # Get adjusted points
    screen_width = 1024
    screen_height = 512
    adj = adjust_location_coords(extremes,points,screen_width,screen_height)

    # Save adjusted points
    f = open('quake-adjusted.json','w')
    f.write(json.dumps(adj, sort_keys=True,indent=4, separators=(',', ': ')))
    f.close()
    ##############################################################
    background_colour = (255,255,255)
    black = (0,0,0)
    (width, height) = (1024, 512)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('MBRs')
    screen.fill(background_colour)
    pygame.init() 
    bg = pygame.image.load("/Users/QT/Desktop/CMPS-5323-Spatial-DS/Spatial-DS-Doan-master/assignments/program3/world_map.png")
    pygame.image.save(screen,DIRPATH+'/'+'screen_shot.png')
    pygame.display.flip()
    
    with open(DIRPATH+'/'+'quake-adjusted.json') as f:
    #f = open('quake-2017-adjusted.json','r')
        points = json.loads(f.read())
    running = True
    while running:
        for p in points:
            pygame.draw.circle(screen,(255,0,0), p, 1,0)
        for event in pygame.event.get():
            screen.blit(bg, (0, 0))
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clean_area(screen,(0,0),width,height,(255,255,255))
        pygame.display.flip()