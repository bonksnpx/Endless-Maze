import Room
import endlessmaze
import random
import arcade
import Orb
import var


# called when player clicks start
def on_start():
    if var.difficulty == "Easy":
        create_easy_rooms()
        var.num_orbs = 1
    elif var.difficulty == "Medium":
        create_med_rooms()
        var.array_length = 6
        var.num_orbs = 3
    elif var.difficulty == "Hard":
        create_hard_rooms()
        var.array_length = 8
        var.num_orbs = 5


# creates 2d array of room objects - this is the 'grid'
# on easy difficulty, the grid is 4x4 with 1 orb object
def create_easy_rooms():
    var.array_length = 4

    for y in range(4):  # create rows
        var.rooms.append([])
        for x in range(4):  # create columns
            room = Room.CreateRoom(False)
            var.rooms[y].append(room)

    # logic for creating entrances between rooms - pathing
    for y in range(4):
        for x in range(4):
            up_xy = var.game_window.get_up(x, y)
            down_xy = var.game_window.get_down(x, y)
            left_xy = var.game_window.get_left(x, y)
            right_xy = var.game_window.get_right(x, y)
            if var.rooms[up_xy['x']][up_xy['y']].down:
                up = True
            else:
                if var.rooms[up_xy['x']][up_xy['y']].created:
                    up = False
                else:
                    up = bool(random.getrandbits(1))

            if var.rooms[down_xy['x']][down_xy['y']].up:
                down = True
            else:
                if var.rooms[down_xy['x']][down_xy['y']].created:
                    down = False
                else:
                    down = bool(random.getrandbits(1))

            if var.rooms[left_xy['x']][left_xy['y']].right:
                left = True
            else:
                if var.rooms[left_xy['x']][left_xy['y']].created:
                    left = False
                else:
                    left = bool(random.getrandbits(1))

            if var.rooms[right_xy['x']][right_xy['y']].left:
                right = True
            else:
                if var.rooms[right_xy['x']][right_xy['y']].created:
                    right = False
                else:
                    right = bool(random.getrandbits(1))

            if up:
                var.rooms[x][y].createup()
            if down:
                var.rooms[x][y].createdown()
            if left:
                var.rooms[x][y].createleft()
            if right:
                var.rooms[x][y].createright()

    Orb.generate_orbs("Easy")


# 6x6 grid, 3 orbs
def create_med_rooms():
    var.array_length = 6

    for y in range(6):  # create rows
        var.rooms.append([])
        for x in range(6):  # create columns
            room = Room.CreateRoom(False)
            var.rooms[y].append(room)

    # logic for creating entrances between rooms - pathing
    for y in range(6):
        for x in range(6):
            up_xy = var.game_window.get_up(x, y)
            down_xy = var.game_window.get_down(x, y)
            left_xy = var.game_window.get_left(x, y)
            right_xy = var.game_window.get_right(x, y)
            if var.rooms[up_xy['x']][up_xy['y']].down:
                up = True
            else:
                if var.rooms[up_xy['x']][up_xy['y']].created:
                    up = False
                else:
                    up = bool(random.getrandbits(1))

            if var.rooms[down_xy['x']][down_xy['y']].up:
                down = True
            else:
                if var.rooms[down_xy['x']][down_xy['y']].created:
                    down = False
                else:
                    down = bool(random.getrandbits(1))

            if var.rooms[left_xy['x']][left_xy['y']].right:
                left = True
            else:
                if var.rooms[left_xy['x']][left_xy['y']].created:
                    left = False
                else:
                    left = bool(random.getrandbits(1))

            if var.rooms[right_xy['x']][right_xy['y']].left:
                right = True
            else:
                if var.rooms[right_xy['x']][right_xy['y']].created:
                    right = False
                else:
                    right = bool(random.getrandbits(1))

            if up:
                var.rooms[x][y].createup()
            if down:
                var.rooms[x][y].createdown()
            if left:
                var.rooms[x][y].createleft()
            if right:
                var.rooms[x][y].createright()

    Orb.generate_orbs("Medium")


# 8x8 grid, 5 orbs
def create_hard_rooms():
    var.array_length = 8

    for y in range(8):  # create rows
        var.rooms.append([])
        for x in range(8):  # create columns
            room = Room.CreateRoom(False)
            var.rooms[y].append(room)

    # logic for creating entrances between rooms - pathing
    for y in range(8):
        for x in range(8):
            up_xy = var.game_window.get_up(x, y)
            down_xy = var.game_window.get_down(x, y)
            left_xy = var.game_window.get_left(x, y)
            right_xy = var.game_window.get_right(x, y)
            if var.rooms[up_xy['x']][up_xy['y']].down:
                up = True
            else:
                if var.rooms[up_xy['x']][up_xy['y']].created:
                    up = False
                else:
                    up = bool(random.getrandbits(1))

            if var.rooms[down_xy['x']][down_xy['y']].up:
                down = True
            else:
                if var.rooms[down_xy['x']][down_xy['y']].created:
                    down = False
                else:
                    down = bool(random.getrandbits(1))

            if var.rooms[left_xy['x']][left_xy['y']].right:
                left = True
            else:
                if var.rooms[left_xy['x']][left_xy['y']].created:
                    left = False
                else:
                    left = bool(random.getrandbits(1))

            if var.rooms[right_xy['x']][right_xy['y']].left:
                right = True
            else:
                if var.rooms[right_xy['x']][right_xy['y']].created:
                    right = False
                else:
                    right = bool(random.getrandbits(1))

            if up:
                var.rooms[x][y].createup()
            if down:
                var.rooms[x][y].createdown()
            if left:
                var.rooms[x][y].createleft()
            if right:
                var.rooms[x][y].createright()

    Orb.generate_orbs("Hard")
