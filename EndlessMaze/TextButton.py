import arcade
import var

# clickable buttons
class TextButton:
    def __init__(self,
                 center_x, center_y,
                 width, height,
                 text, difficulty,
                 font_size=14,
                 font_face="Times New Roman",
                 face_color=arcade.color.LIGHT_GRAY,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.GRAY,
                 button_height=2):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.difficulty = difficulty
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height

    # draws the button
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        # gives difficulty buttons appearance of staying "pressed"
        if var.difficulty == self.difficulty or self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y - self.height / 2,
                         color, self.button_height)

        # right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # gives difficulty buttons appearance of staying "pressed"
        if var.difficulty == self.difficulty or self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # left vertical
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x - self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # gives difficulty buttons appearance of staying "pressed"
        x = self.center_x
        y = self.center_y
        if var.difficulty == self.difficulty or self.pressed:
            x += self.button_height
            y -= self.button_height

        arcade.draw_text(self.text, x, y,
                         arcade.color.BLACK, font_size=self.font_size, font_name="Copperplate Gothic Bold",
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False


# checks if mouse press is on button
def check_mouse_press_for_buttons(x, y, button_list):
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


# checks when mouse is released
def check_mouse_release_for_buttons(x, y, button_list):
    for button in button_list:
        if button.pressed:
            button.on_release()


# class to create button for easy difficulty
class EasyTextButton(TextButton):
    # center_x / center_y: coordinates to center the button at
    # action_function: function to be called when button is pressed
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Easy", "Easy",  14, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


# class to create button for medium difficulty
class MedTextButton(TextButton):
    # center_x / center_y: coordinates to center the button at
    # action_function: function to be called when button is pressed
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Medium", "Medium",  14, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


# class to create button for hard difficulty
class HardTextButton(TextButton):
    # center_x / center_y: coordinates to center the button at
    # action_function: function to be called when button is pressed
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Hard", "Hard",  14, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


# class to create a start button
class StartButton(TextButton):
    # center_x / center_y: coordinates to center the button at
    # action_function: function to be called when button is pressed
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Start", None, 14, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


# class to create a general button
class CreateButton(TextButton):
    # center_x / center_y: coordinates to center the button at
    # action_function: function to be called when button is pressed
    # width / height: width and height of the button
    # text: string of text to put on the button
    def __init__(self, center_x, center_y, action_function, width, height, text):
        super().__init__(center_x, center_y, width, height, text, None, 14, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()
