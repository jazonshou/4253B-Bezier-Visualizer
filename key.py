import pygame

class Key:
    def __init__(self):
        self.pressed = False
        
    def isPressed(self, button, click=bool):
        key = pygame.key.get_pressed()[button]
        if click:
            if key and not self.pressed:
                self.pressed = True
                return True
            elif not key:
                self.pressed = False
                return False
        else:
            return key