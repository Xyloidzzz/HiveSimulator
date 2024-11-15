##################################################################################################################################
#
# Name: hive.py
# Author: Alfredo Pena
# CSCI 6370 - Hive Final Project
# Purpose: Create a clickable board game application for the game Hive
# Last Modified: 11/15/2024
#
##################################################################################################################################

from tkinter import Menu
from graphics import *
import math

# global variables  
BOARD_SIZE = 10
PIECE_COLOR = "black"
CENTERS = []
CLICKABLE_AREAS = []

# create the board
def draw_board(window):
    # draw the hexagons
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if i % 2 == 0:
                draw_hexagon(window, 50 + 50 * i, 50 + 50 * j)
            else:
                draw_hexagon(window, 50 + 50 * i, 75 + 50 * j)
    
            
# draw a hexagon
def draw_hexagon(window, x, y):
    centers = []
    radius = 25  # control the size of hex
    for i in range(6):
      angle_deg = 60 * i
      angle_rad = math.radians(angle_deg)
      x_center = x + radius * math.cos(angle_rad)
      y_center = y + radius * math.sin(angle_rad)
      centers.append(Point(x_center, y_center))
    # draw the hexagon
    for i in range(6):
      j = (i + 1) % 6
      Line(centers[i], centers[j]).draw(window)
    # save the clickable areas
    CENTERS.append(centers)
    CLICKABLE_AREAS.append([x - radius, y - radius, x + radius, y + radius])
    
    
# add actions on click
def play_game(window):
  while True:
        # get the first click
        click1 = window.getMouse()
        # TODO: place a piece... maybe make a menu to select which piece
        
        
# draw a piece
def draw_piece(window, x, y):
    center = Point(x, y)
    Circle(center, 20).draw(window)


# main
def main():
    # create the window
    window = GraphWin("Hive", 800, 800)
    window.setCoords(0, 0, BOARD_SIZE * 56, BOARD_SIZE * 56)
    window.setBackground("white")

    draw_board(window)
    play_game(window)
    
if __name__ == "__main__":
    main()