import Room
import endlessmaze
import random
import arcade
import Orb

# variables to be accessed across all files
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
difficulty = "Easy"
array_length = 0
num_orbs = 0
red = None
yellow = None
green = None
purple = None
blue = arcade.color.BRANDEIS_BLUE
red_slot = None
yellow_slot = None
green_slot = None
purple_slot = None
blue_slot = None
rooms = []
game_window = endlessmaze.GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)


def print_difficulty():
    print(difficulty)

