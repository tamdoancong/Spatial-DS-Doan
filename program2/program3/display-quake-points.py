import pygame
import sys,os
import json
DIRPATH = os.path.dirname(os.path.realpath(__file__))
def clean_area(screen,origin,width,height,color):
    """
    Prints a color rectangle (typically white) to "erase" an area on the screen.
    Could be used to erase a small area, or the entire screen.
    """
    ox,oy = origin
    points = [(ox,oy),(ox+width,oy),(ox+width,oy+height),(ox,oy+height),(ox,oy)]
    pygame.draw.polygon(screen, color, points, 0)

if __name__=='__main__':

    background_colour = (255,255,255)
    black = (0,0,0)
    (width, height) = (1024, 512)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('MBRs')
    screen.fill(background_colour)
    pygame.init() 
    bg = pygame.image.load("/Users/QT/Desktop/CMPS-5323-Spatial-DS/Spatial-DS-Doan-master/assignments/program3/world_map.png")
    




    pygame.display.flip()
    DIRPATH = os.path.dirname(os.path.realpath(__file__))
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
            pygame.image.save(screen,DIRPATH+'/'+'screen_shot.png')
        pygame.display.flip()