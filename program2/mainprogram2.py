import pygame
import random
from dbscan import *
import sys,os
import pprint as pp

Resolution = 2000

def calculate_mbrs(points, epsilon, min_pts):
    """
    Find clusters using DBscan and then create a list of bounding rectangles
    to return.
    """
    mbrs = []
    clusters =  dbscan(points, epsilon, min_pts)
    """
    Using list index value to iterate over the clusters dictionary
    Does same as above
    """
    for id in range(len(clusters)-1):
        xs = []
        ys = []
        for p in clusters[id]:
            xs.append(p[0])
            ys.append(p[1])
        max_x = max(xs) 
        max_y = max(ys)
        min_x = min(xs)
        min_y = min(ys)
        mbrs.append([(min_x,min_y),(max_x,min_y),(max_x,max_y),(min_x,max_y),(min_x,min_y)])
    return mbrs


def clean_area(screen,origin,width,height,color):
    """
    Prints a color rectangle (typically white) to "erase" an area on the screen.
    Could be used to erase a small area, or the entire screen.
    """
    ox,oy = origin
    points = [(ox,oy),(ox+width,oy),(ox+width,oy+height),(ox,oy+height),(ox,oy)]
    pygame.draw.polygon(screen, color, points, 0)

background_colour = (255,255,255)
black = (0,0,0)

Manhatten = (194,35,38)
Queens = (243,115,56)
StatenIsland = (253,182,50)
Bronx = (2,120,120)
Brooklyn = (128,22,56)

(width, height) = (Resolution , Resolution)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Line')
screen.fill(background_colour)

pygame.display.flip()

epsilon = 20
min_pts = 5.0

points = []

num_points = 500

for i in range(num_points):
    x = random.randint(10,width-10)
    y = random.randint(10,height-10)
    points.append((x,y))

mbrs = calculate_mbrs(points, epsilon, min_pts)

running = True
DIRPATH = os.path.dirname(os.path.realpath(__file__))
keys = []
crimes = []
MaxX = 1067226
MaxY = 271820
MinX = 913357
MinY = 121250
got_keys = False
with open(DIRPATH+'/'+'filtered_crimes_bronx.csv') as f:
    for line in f:
        line = ''.join(x if i % 2 == 0 else x.replace(',', ':') for i, x in enumerate(line.split('"')))
        line = line.strip().split(',')
        if not got_keys:
            keys = line
            got_keys = True
            continue
        crimes.append(line)
        
pointListBronx = []

for crime in crimes:
    if (crime[19] != "") and (crime[20] != "" ):
        x1 = int ( ( int(crime[19]) - MinX ) / ( MaxX - MinX ) * Resolution  ) 
        y1 = Resolution - int ( ( int(crime[20]) - MinY ) / ( MaxY - MinY ) * Resolution )
        p = (x1,y1)
        pointListBronx.append(p)
#######################################################3

got_keys = False
crimes.clear()
with open(DIRPATH+'/'+'filtered_crimes_brooklyn.csv') as f:
    for line in f:
        line = ''.join(x if i % 2 == 0 else x.replace(',', ':') for i, x in enumerate(line.split('"')))
        line = line.strip().split(',')
        if not got_keys:
            keys = line
            got_keys = True
            continue
        crimes.append(line)
        
pointListBrooklyn = []

for crime in crimes:
    if (crime[19] != "") and (crime[20] != "" ):
        x1 = int ( ( int(crime[19]) - MinX ) / ( MaxX - MinX ) * Resolution  ) 
        y1 = Resolution - int ( ( int(crime[20]) - MinY ) / ( MaxY - MinY ) * Resolution )
        p = (x1,y1)
        pointListBrooklyn.append(p)
#########################################################

got_keys = False
crimes.clear()
with open(DIRPATH+'/'+'filtered_crimes_manhattan.csv') as f:
    for line in f:
        line = ''.join(x if i % 2 == 0 else x.replace(',', ':') for i, x in enumerate(line.split('"')))
        line = line.strip().split(',')
        if not got_keys:
            keys = line
            got_keys = True
            continue
        crimes.append(line)
        
pointListManhattan = []

for crime in crimes:
    if (crime[19] != "") and (crime[20] != "" ):
        x1 = int ( ( int(crime[19]) - MinX ) / ( MaxX - MinX ) * Resolution  ) 
        y1 = Resolution - int ( ( int(crime[20]) - MinY ) / ( MaxY - MinY ) * Resolution )
        p = (x1,y1)
        pointListManhattan.append(p)
######################################################


got_keys = False
crimes.clear()
with open(DIRPATH+'/'+'filtered_crimes_queens.csv') as f:
    for line in f:
        line = ''.join(x if i % 2 == 0 else x.replace(',', ':') for i, x in enumerate(line.split('"')))
        line = line.strip().split(',')
        if not got_keys:
            keys = line
            got_keys = True
            continue
        crimes.append(line)
        
pointListQueens = []

for crime in crimes:
    if (crime[19] != "") and (crime[20] != "" ):
        x1 = int ( ( int(crime[19]) - MinX ) / ( MaxX - MinX ) * Resolution  ) 
        y1 = Resolution - int ( ( int(crime[20]) - MinY ) / ( MaxY - MinY ) * Resolution )
        p = (x1,y1)
        pointListQueens.append(p)
######################################################

got_keys = False
crimes.clear()
with open(DIRPATH+'/'+'filtered_crimes_staten_island.csv') as f:
    for line in f:
        line = ''.join(x if i % 2 == 0 else x.replace(',', ':') for i, x in enumerate(line.split('"')))
        line = line.strip().split(',')
        if not got_keys:
            keys = line
            got_keys = True
            continue
        crimes.append(line)

        
pointListStatenIsland = []

for crime in crimes:
    if (crime[19] != "") and (crime[20] != "" ):
        x1 = int ( ( int(crime[19]) - MinX ) / ( MaxX - MinX ) * Resolution  ) 
        y1 = Resolution - int ( ( int(crime[20]) - MinY ) / ( MaxY - MinY ) * Resolution )
        p = (x1,y1)
        pointListStatenIsland.append(p)
######################################################


for point in pointListBronx:
    pygame.draw.circle(screen, Bronx, point, 3, 0)

for point in pointListBrooklyn:
    pygame.draw.circle(screen, Brooklyn, point, 3, 0)

for point in pointListManhattan:
    pygame.draw.circle(screen, Manhatten, point, 3, 0)

for point in pointListQueens:
    pygame.draw.circle(screen, Queens, point, 3, 0)

for point in pointListStatenIsland:
    pygame.draw.circle(screen, StatenIsland, point, 3, 0)



for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        clean_area(screen,(0,0),width,height,(255,255,255))
        points.append(event.pos)
        mbrs = calculate_mbrs(points, epsilon, min_pts)

pygame.image.save(screen , "temp.png")
#pygame.display.flip()