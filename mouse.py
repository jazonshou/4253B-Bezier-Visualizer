import pygame
import enum

# Mouse button enum
class MouseButton(enum.Enum):
    LEFT = 0
    SCROLL_WHEEL = 1
    RIGHT = 2

# Position type enum
# Absoulte = gobal position; if ur rly kool, u call them cartesian coordinates 
# ^ no i did not just search up how to spell 'cartesian'
# Relative = how for since last checked (aka. polar coords)
class PoseType(enum.Enum):
    ABSOLUTE = 0
    RELATIVE = 1

# Mouse wrapper(ish) for pygame.mouse
class Mouse: 
    # Constructor - nothing special, just defining some variables
    def __init__(self):
        self.pressed = False
        self.lastPressedPose=[0, 0]

    # Checks if mouse is pressed
    # (with the added capability of allowing you to choose if you want to detect
    # individual clicks or just whenever the mouse gets pressed)
    def isPressed(self, button=MouseButton, click=bool):
        mouse = pygame.mouse.get_pressed()[button.value]
        if click:
            if mouse and not self.pressed:
                self.pressed = True
                return True
            elif not mouse:
                if self.pressed:
                    self.lastPressedPose = self.pose(PoseType.ABSOLUTE)
                self.pressed = False
                return False
        else:
            return mouse

    # Gets the position of the mouse 
    # You can choose to join the absolute coordinate gang or the loser gang (jk, both quite useful)
    def pose(self, type=PoseType):
        if type is PoseType.ABSOLUTE:
            return pygame.mouse.get_pos()
        else:
            return pygame.mouse.get_rel()