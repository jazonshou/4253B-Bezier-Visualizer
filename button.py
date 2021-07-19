import pygame
import enum
import mouse
import math

# button shape enum
class ButtonShape(enum.Enum):
    RECTANGLE = 0
    CIRCLE = 1

# Button class for ease of use
class Button:
    # Button constructor 
    def __init__(self, display, type, color=(), pose=(), dimensions=(), width=float):
        self.pose = pose
        self.w = dimensions[0]
        self.h = dimensions[1]
        self.r = dimensions[0]
        self.color = color
        self.type = type
        self.display = display
        self.width = width
        self.buttonPressed = False
        self.prevPose=pose

    # Displays the button
    def draw(self):
        if self.type is ButtonShape.RECTANGLE:
            pygame.draw.rect(self.display, self.color, (self.pose, (self.w, self.h)), self.width)
        else:
            pygame.draw.circle(self.display, self.color, self.pose, self.r, self.width)

    # Detects if the button is being pressed
    # Click = False --> continuously return True when being pressed
    # Click = True --> only returns True after 1 full click 
    def isPressed(self, m=mouse.Mouse, button=mouse.MouseButton, click=bool):
        if self.type is ButtonShape.RECTANGLE:
            if (m.pose(mouse.PoseType.ABSOLUTE)[0] >= self.pose[0] and
                m.pose(mouse.PoseType.ABSOLUTE)[0] <= self.pose[0] + self.w and
                m.pose(mouse.PoseType.ABSOLUTE)[1] >= self.pose[1] and
                m.pose(mouse.PoseType.ABSOLUTE)[1] <= self.pose[1] + self.h and 
                m.isPressed(button, click)):
                return True
        if self.type is ButtonShape.CIRCLE:
            if math.dist([m.pose(mouse.PoseType.ABSOLUTE)[0], m.pose(mouse.PoseType.ABSOLUTE)[1]], [self.pose[0], self.pose[1]]) < self.r and m.isPressed(button, click):
                return True
        return False

    # Moves button to desired position
    def move(self, newPose=()):
        self.pose = newPose

    # Sets button color
    def setColor(self, color=()):
        self.color = color

    # Moves the button when clicked
    # The reason why I didn't just do: 
    # if button is pressed: 
    #     button position = mouse position
    # Was because if the mouse moved too fast, it would move past the *button perimeter
    # This is due to the refresh rate being ~10ms, the computer simply cannot keep up 
    # with fast mouse movements
    # *And trust me, it's really annoying when it happens
    def drag(self, _mouse=mouse.Mouse, button=mouse.MouseButton, newPose=()):
        if self.isPressed(_mouse, button, False):
            self.buttonPressed = True
            # print('i was pressed')

        if not _mouse.isPressed(button, False):
            self.buttonPressed = False
            self.move(self.prevPose)
            return False

        if self.buttonPressed:
            self.move(newPose)
            self.prevPose = newPose
            return True