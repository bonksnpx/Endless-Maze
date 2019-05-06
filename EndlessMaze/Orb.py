import arcade
import TextButton
import endlessmaze
import var
import random


class Orb:
    def __init__(self, center_x, center_y, diameter, color, x, y):
        self.center_x = center_x
        self.center_y = center_y
        self.diameter = diameter
        self.color = color
        self.shape = arcade.buffered_draw_commands.create_ellipse(center_x, center_y, diameter, diameter, color)
        self.x = x
        self.y = y

    def set_color(self, color):
        self.shape = arcade.buffered_draw_commands.create_ellipse(self.center_x, self.center_y, self.diameter,
                                                                  self.diameter, color)


class CreateOrb(Orb):
    def __init__(self, center_x, center_y, radius, color, x, y):
        super().__init__(center_x, center_y, radius, color, x, y)


class OrbSlot:
    def __init__(self, center_x, center_y, diameter, color, x, y):
        self.center_x = center_x
        self.center_y = center_y
        self.diameter = diameter
        self.color = color
        self.shape = arcade.buffered_draw_commands.create_ellipse(center_x, center_y, diameter, diameter, color,
                                                                  filled=False, border_width=5)
        self.x = x
        self.y = y

    def set_color(self, color):
        self.shape = arcade.buffered_draw_commands.create_ellipse(self.center_x, self.center_y, self.diameter,
                                                                  self.diameter, color, filled=False, border_width=5)

    @staticmethod
    def delete(slot):
        del slot


class CreateOrbSlot(OrbSlot):
    def __init__(self, center_x, center_y, radius, color, x, y):
        super().__init__(center_x, center_y, radius, color, x, y)


# checks if mouse press is on an orb
def check_mouse_press_for_orbs(x, y, orb_list):
    # pick up orb if mouse press is on the orb
    for orb in orb_list:
        if orb.x == var.game_window.current_room['x'] and orb.y == var.game_window.current_room['y']:
            if var.game_window.current_orb is None:
                if x > orb.center_x + orb.diameter:
                    continue
                if x < orb.center_x - orb.diameter:
                    continue
                if y > orb.center_y + orb.diameter:
                    continue
                if y < orb.center_y - orb.diameter:
                    continue
                var.game_window.pick_up_orb(orb)


# checks if mouse press is on a slot
def check_mouse_press_for_slots(x, y, slot_list):
    for slot in slot_list:
        if slot.x == var.game_window.current_room['x'] and slot.y == var.game_window.current_room['y'] \
                and var.game_window.current_orb is not None:
            if x > slot.center_x + slot.diameter:
                continue
            if x < slot.center_x - slot.diameter:
                continue
            if y > slot.center_y + slot.diameter:
                continue
            if y < slot.center_y - slot.diameter:
                continue
            # check if player is holding the same color orb as the slot
            if slot.color == var.game_window.current_orb.color:
                var.game_window.place_orb(slot)


# logic for creating and placing orbs in room(s)
def generate_orbs(difficulty):
    # 1 orb for easy, 3 for medium, 5 for hard
    if difficulty == "Easy":
        iterations = 1
    if difficulty == "Medium":
        iterations = 3
    if difficulty == "Hard":
        iterations = 5

    # colors for individual orbs
    colors = [arcade.color.BRANDEIS_BLUE, arcade.color.RED, arcade.color.ELECTRIC_YELLOW, arcade.color.ELECTRIC_GREEN,
              arcade.color.PSYCHEDELIC_PURPLE]

    coordinate_array = []

    for c in range(iterations):
        while True:
            slot_rand_x = random.randint(0, var.array_length - 1)
            slot_rand_y = random.randint(0, var.array_length - 1)
            # ensures room is accessible
            if not (var.rooms[slot_rand_x][slot_rand_y].down or var.rooms[slot_rand_x][slot_rand_y].up or
               var.rooms[slot_rand_x][slot_rand_y].left or var.rooms[slot_rand_x][slot_rand_y].right):
                continue

            # ensures it's not placed in the same room as any other slot/orb
            if len(coordinate_array) != 0:
                for coord in coordinate_array:
                    if slot_rand_x != coord['x'] and slot_rand_y != coord['y']:
                        continue
                    continue

            var.rooms[slot_rand_x][slot_rand_y].create_orb_slot(colors[c], slot_rand_x, slot_rand_y)
            print(slot_rand_x, slot_rand_y, colors[c], "slot")
            coordinate_array.append({'x': slot_rand_x, 'y': slot_rand_y})
            break

    for c in range(iterations):
        while True:
            orb_rand_x = random.randint(0, var.array_length - 1)
            orb_rand_y = random.randint(0, var.array_length - 1)
            # ensures room is accessible
            if not (var.rooms[orb_rand_x][orb_rand_y].down or var.rooms[orb_rand_x][orb_rand_y].up or
                    var.rooms[orb_rand_x][orb_rand_y].left or var.rooms[orb_rand_x][orb_rand_y].right):
                continue

            # ensures it's not placed in the same room as any other slot/orb
            if len(coordinate_array) != 0:
                for coord in coordinate_array:
                    if orb_rand_x != coord['x'] and orb_rand_y != coord['y']:
                        continue
                    continue

            var.rooms[orb_rand_x][orb_rand_y].create_orb(colors[c], orb_rand_x, orb_rand_y)
            print(orb_rand_x, orb_rand_y, colors[c], "orb")
            coordinate_array.append({'x': orb_rand_x, 'y': orb_rand_y})
            break
