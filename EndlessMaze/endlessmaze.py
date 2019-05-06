import arcade
import TextButton
import Room
import Orb
import random
import var
import Setup


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# main menu class
class MainMenu(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, "Main Menu")

        arcade.set_background_color(arcade.color.DARK_GRAY)

        self.button_list = None

    def setup(self):
        # creates buttons in main menu
        self.button_list = []

        easy_button = TextButton.EasyTextButton(250, 300, self.set_easy_diff)
        self.button_list.append(easy_button)

        medium_button = TextButton.MedTextButton(400, 300, self.set_med_diff)
        self.button_list.append(medium_button)

        hard_button = TextButton.HardTextButton(550, 300, self.set_hard_diff)
        self.button_list.append(hard_button)

        start_button = TextButton.StartButton(400, 200, self.start_game)
        self.button_list.append(start_button)

        help_button = TextButton.CreateButton(400, 100, self.help, 100, 40, "How To Play")
        self.button_list.append(help_button)

    # draws objects to window
    def on_draw(self):
        arcade.start_render()

        arcade.draw_text("Endless Maze", 212, 400, arcade.color.WHITE, 36, font_name="Copperplate Gothic Bold")

        # Draw the buttons
        for button in self.button_list:
            button.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        TextButton.check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        TextButton.check_mouse_release_for_buttons(x, y, self.button_list)

    @staticmethod  # sets difficulty to easy
    def set_easy_diff():
        var.difficulty = "Easy"
        var.print_difficulty()

    @staticmethod  # sets difficulty to medium
    def set_med_diff():
        var.difficulty = "Medium"
        var.print_difficulty()

    @staticmethod  # sets difficulty to hard
    def set_hard_diff():
        var.difficulty = "Hard"
        var.print_difficulty()

    @staticmethod # how to play the game
    def help():
        HelpWindow(600, 1800)

    @staticmethod  # starts the game
    def start_game():
        arcade.finish_render()
        arcade.close_window()
        Setup.on_start()
        var.game_window.setup()
        arcade.run()


# window displayed when player clicks on "help" button
class HelpWindow(arcade.Window):
    def __init__(self, height, width):
        super().__init__(width, height, "How To Play")
        arcade.set_background_color(arcade.color.DARK_GRAY)

        # text to be drawn
        self.title = "How To Play"
        self.par1 = "Welcome to the Endless Maze! The objective of the game is to match a set number, depending on " \
                    "difficulty, of colored orbs to their slots, both of which are randomly distributed throughout " \
                    "the maze."
        self.par2 = "The 'maze' is actually a grid of individual rooms, each of which will have entrances to other rooms." \
                    "The player only sees one room at a time (the room they are currently in) and are able to choose" \
                    "a direction to move in from the room. Each room can contain only one orb or slot - there can not be" \
                    " two orbs or slots in one room."
        self.par3 = "To move the orbs, a player may click on an orb to pick it up. Once you pick an orb up, you cannot" \
                    "put it back down until you find the corresponding slot! Once you find the corresponding slot and " \
                    "you have the correct orb in your possession, you can click on the slot and the orb and slot both" \
                    "will disappear. The game is over once all of the orbs have been slotted correctly."
        self.par4 = "On easy difficulty, the grid of rooms is 4x4, and there is only one orb. On medium, the grid is 6x6" \
                    "with 3 orbs, and hard is 8x8 with 5 orbs. On medium and hard difficulty, there will be one randomly " \
                    "generated 'trap room' which, when entered, will teleport you to a random room in the maze! Be cautious, " \
                    "as there is no indication that you have been teleported. Also beware of rooms on the edges of the " \
                    "grid - entering an entrance on any of the edges of the maze will wrap around to the opposite side!"

    def on_draw(self):
        arcade.draw_text(self.title, 275, 550, arcade.color.BLACK, 28, font_name="Copperplate Gothic Bold")
        arcade.draw_text(self.par1, 50, 400, arcade.color.BLACK, 10, font_name="Bahnschrift Bold")
        arcade.draw_text(self.par2, 50, 300, arcade.color.BLACK, 10, font_name="Bahnschrift Bold")
        arcade.draw_text(self.par3, 50, 200, arcade.color.BLACK, 10, font_name="Bahnschrift Bold")
        arcade.draw_text(self.par4, 50, 100, arcade.color.BLACK, 10, font_name="Bahnschrift Bold")


# game window class - opened when player clicks "start"
class GameWindow(arcade.Window):
    def __init__(self, width, height):
        self.window_width = width
        self.window_height = height
        self.button_list = []
        self.orb_list = []
        self.slot_list = []
        self.won = False

        self.current_orb = None
        self.current_room = {'x': 0, 'y': 0}

    def setup(self):
        super().__init__(self.window_width, self.window_height, "Endless Maze")

    # draws objects to window
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.GRAY)
        self.button_list = var.rooms[self.current_room['x']][self.current_room['y']].button_list

        # draws rectangles for open rooms
        for rectangle in var.rooms[self.current_room['x']][self.current_room['y']].rectangle_list:
            arcade.buffered_draw_commands.render(rectangle)

        # draws buttons
        for button in var.rooms[self.current_room['x']][self.current_room['y']].button_list:
            button.draw()

        # renders orb(s)
        if var.rooms[self.current_room['x']][self.current_room['y']].orb is not None:
            arcade.buffered_draw_commands.render(var.rooms[self.current_room['x']][self.current_room['y']].orb.shape)

        # renders slot(s)
        if var.rooms[self.current_room['x']][self.current_room['y']].slot is not None:
            arcade.buffered_draw_commands.render(var.rooms[self.current_room['x']][self.current_room['y']].slot.shape)

        # if holding an orb, displays in the top right corner
        if self.current_orb is not None:
            arcade.draw_text("Current Orb: ", 600, 550, arcade.color.WHITE, 10, font_name="Bahnschrift Bold")
            shape = arcade.buffered_draw_commands.create_ellipse(700, 555, 10, 10, self.current_orb.color)
        else:
            shape = arcade.buffered_draw_commands.create_rectangle_filled(750, 550, 30, 30, arcade.color.GRAY)
        arcade.buffered_draw_commands.render(shape)

        # displays win text
        if self.won:
            arcade.draw_text("You win!", 183, 275, arcade.color.BLACK, 72, font_name="Copperplate Gothic Bold")

    # called when mouse is clicked
    def on_mouse_press(self, x, y, button, key_modifiers):
        # checks if mouse press is on a button
        TextButton.check_mouse_press_for_buttons(x, y, self.button_list)
        Orb.check_mouse_press_for_orbs(x, y, self.orb_list)
        Orb.check_mouse_press_for_slots(x, y, self.slot_list)
        print(self.current_room)

    # called when click is released
    def on_mouse_release(self, x, y, button, key_modifiers):
        TextButton.check_mouse_release_for_buttons(x, y, self.button_list)

    @staticmethod
    # returns coordinates of room 'above' the room at (x,y)
    def get_up(x, y):
        room = {'x': x, 'y': y}
        # if at the top row, going 'up' will return you to the bottom
        if room['y'] == var.array_length-1:
            room['y'] = 0
            # when returning to the bottom, the x coordinate is moved across the grid
            # e.g. going up when at (0,3) will return you to (2,0) on easy
            if room['x'] < int(var.array_length / 2):
                room['x'] = room['x'] + int(var.array_length / 2)
            else:
                room['x'] = room['x'] - int(var.array_length / 2)
        else:
            room['y'] = room['y'] + 1
        return room

    @staticmethod
    # returns coordinates of room 'below' (x,y)
    def get_down(x, y):
        room = {'x': x, 'y': y}
        # if at the bottom row, going 'down' will return you to the top
        if room['y'] == 0:
            room['y'] = var.array_length-1
            # when going to the top, x coordinate is moved across the grid
            if room['x'] < int(var.array_length / 2):
                room['x'] = room['x'] + int(var.array_length / 2)
            else:
                room['x'] = room['x'] - int(var.array_length / 2)
        else:
            room['y'] = room['y'] - 1

        return room

    @staticmethod
    # returns coordinates of room to the left of (x,y)
    def get_left(x, y):
        room = {'x': x, 'y': y}
        # if already at the far left side, moving left will take you to the right side
        if room['x'] == 0:
            room['x'] = var.array_length-1
            # similar to x distortion in get_down() and get_up(), y coordinate is moved across the grid
            if room['y'] < int(var.array_length / 2):
                room['y'] = room['y'] + int(var.array_length / 2)
            else:
                room['y'] = room['y'] - int(var.array_length / 2)
        else:
            room['x'] = room['x'] - 1

        return room

    @staticmethod
    # returns coordinates of room to the right of (x,y)
    def get_right(x, y):
        room = {'x': x, 'y': y}
        # if already at the far right side, moving right will take you to the left side
        if room['x'] == var.array_length-1:
            room['x'] = 0
            # same y distortion as above
            if room['y'] < int(var.array_length / 2):
                room['y'] = room['y'] + int(var.array_length / 2)
            else:
                room['y'] = room['y'] - int(var.array_length / 2)
        else:
            room['x'] = room['x'] + 1

        return room

    # move the player up
    def move_up(self):
        # checks if the player has won - win message will be displayed after moving one more time
        self.check_win()
        up_xy = self.get_up(self.current_room['x'], self.current_room['y'])
        # on medium and hard difficulties, there is a random (x,y) set as a trap room
        # entering this room will teleport the player to a random (x,y)
        if var.rooms[up_xy['x']][up_xy['y']].trap_room:
            self.current_room['x'] = random.randint(0, var.array_length)
            self.current_room['y'] = random.randint(0, var.array_length)
        else:
            self.current_room = up_xy

    # move the player down
    def move_down(self):
        self.check_win()
        down_xy = self.get_down(self.current_room['x'], self.current_room['y'])
        if var.rooms[down_xy['x']][down_xy['y']].trap_room:
            self.current_room['x'] = random.randint(0, var.array_length)
            self.current_room['y'] = random.randint(0, var.array_length)
        else:
            self.current_room = down_xy

    # move player left
    def move_left(self):
        self.check_win()
        left_xy = self.get_left(self.current_room['x'], self.current_room['y'])
        if var.rooms[left_xy['x']][left_xy['y']].trap_room:
            self.current_room['x'] = random.randint(0, var.array_length)
            self.current_room['y'] = random.randint(0, var.array_length)
        else:
            self.current_room = left_xy

    # move player right
    def move_right(self):
        self.check_win()
        right_xy = self.get_right(self.current_room['x'], self.current_room['y'])
        if var.rooms[right_xy['x']][right_xy['y']].trap_room:
            self.current_room['x'] = random.randint(0, var.array_length)
            self.current_room['y'] = random.randint(0, var.array_length)
        else:
            self.current_room = right_xy

    # picks orb up when clicked on
    def pick_up_orb(self, orb):
        self.current_orb = orb
        # makes orb "disappear"
        orb.set_color(arcade.color.GRAY)
        self.orb_list.remove(orb)

    # places orb in a slot
    def place_orb(self, slot):
        self.current_orb = None
        slot.set_color(arcade.color.GRAY)
        self.slot_list.remove(slot)

    def check_win(self):
        # checks if every orb has been placed
        if len(self.orb_list) == 0 and len(self.slot_list) == 0:
            self.won = True


# runs main window
def main():
    game = MainMenu(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
