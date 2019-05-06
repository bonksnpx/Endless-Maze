import arcade
import TextButton
import Orb
import var
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# class for individual rooms
class MazeRoom:
    # trap_room : boolean for whether current room is a trap or not
    def __init__(self, trap_room):

        arcade.set_background_color(arcade.color.GRAY)

        self.created = False
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.rectangle_list = []
        self.button_list = []
        self.trap_room = trap_room
        self.orb = None
        self.slot = None

        # visual objects for open entrances
        self.leftrect = arcade.buffered_draw_commands.create_rectangle_filled(10, 300, 20, 100, arcade.color.WHITE)
        self.rightrect = arcade.buffered_draw_commands.create_rectangle_filled(790, 300, 20, 100, arcade.color.WHITE)
        self.downrect = arcade.buffered_draw_commands.create_rectangle_filled(400, 590, 100, 20, arcade.color.WHITE)
        self.uprect = arcade.buffered_draw_commands.create_rectangle_filled(400, 10, 100, 20, arcade.color.WHITE)

    def set_orb(self, orb):
        self.orb = orb

    def set_slot(self, slot):
        self.slot = slot

    # creates a left entrance: visual object and a button
    def createleft(self):
        left_button = TextButton.CreateButton(100, 300, var.game_window.move_left, 70, 30, "Left")
        self.button_list.append(left_button)
        self.rectangle_list.append(self.leftrect)
        self.left = True
        self.created = True

    # creates a right entrance
    def createright(self):
        right_button = TextButton.CreateButton(700, 300, var.game_window.move_right, 70, 30, "Right")
        self.button_list.append(right_button)
        self.rectangle_list.append(self.rightrect)
        self.right = True
        self.created = True

    # creates a down entrance
    def createdown(self):
        down_button = TextButton.CreateButton(400, 50, var.game_window.move_down, 70, 30, "Down")
        self.button_list.append(down_button)
        self.rectangle_list.append(self.uprect)
        self.down = True
        self.created = True

    # creates an up entrance
    def createup(self):
        up_button = TextButton.CreateButton(400, 550, var.game_window.move_up, 70, 30, "Up")
        self.button_list.append(up_button)
        self.rectangle_list.append(self.downrect)
        self.up = True
        self.created = True

    # creates orb object for a room
    def create_orb(self, color, x, y):
        orb = Orb.CreateOrb(400, 300, 20, color, x, y)
        self.set_orb(orb)
        var.game_window.orb_list.append(orb)

    # creates an orb slot
    def create_orb_slot(self, color, x, y):
        slot = Orb.CreateOrbSlot(400, 300, 20, color, x, y)
        self.set_slot(slot)
        var.game_window.slot_list.append(slot)


# method to create room objects
def CreateRoom(trap_room):
    room = MazeRoom(trap_room)
    return room

