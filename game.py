import math
import random
import pygame
import tkinter as tk 
from tkinter import messagebox

#Define cube class
class cube(object):
    rows = 0
    w = 0
    #pass is used when a statement is required syntactically but you do not want any command or code to execute
    #we are using pass as placeholders 
    def __init__( self,start,dirnx=1, dirny=0, color=(255,0,0) ) :
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


#Define snake class
class snake(object):
    
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):
    # divides w by rows and receives an int 
    sizeBtwn = w // rows

    x = 0
    y = 0

    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        #this function draws lines across the board
        #arguments => place where it is drawn, color, which value, and range
        #vertical lines
        pygame.draw.line(surface , (255,255,255), (x, 0), (x,w))
        #horizontal lines
        pygame.draw.line(surface , (255,255,255), (0, y), (x,w))

def redrawWindow(surface):
    # gets the global variables rows, and width from the main function
    global rows, width
    #rgb color?
    win.fill((0,0,0))
    
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    #turns width and rows into global variables
    global width, rows

    # create variables to be used in the window object in PyGame
    width = 500

    #define what the row size is going to be
    rows = 20
    #this sets the x,y but since it is a square we use the same variable
    win = pygame.display.set_mode((width, width))
    
    #create a snake with first color and starting position
    s = snake((255,0,0), (10,10))
    flag = True

    #built in object in pygame
    clock = pygame.time.Clock()

    while flag:

        #create this to set a speed for the game // lower this int goes the faster it moves
        pygame.time.delay(50)

        #set so it doesnt run more than 10 frames per second //the lower this int the slower
        clock.tick(10)

        #redraws window this time win is the surface we are redrawing
        redrawWindow(win)
    pass


# rows =
# w =
# h = 

# cube.rows = rows
# cube.w = = w

main()