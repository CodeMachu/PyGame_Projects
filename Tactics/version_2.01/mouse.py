import pygame
pygame.init()


# ----------------------------------------------------------------------------------------------------

# CLASS
class Mouse():

    def __init__(self):
        
        print("Global Mouse Tool Instantiated - Datatype: Mouse() Object")

        # Left and Right Click Switches
        self.left_clicked = False
        self.right_clicked = False

# ----------------------------------------------------------------------------------------------------

    def update(self, event_button):

        if event_button == 1:
            self.left_clicked = True
            print(f"Pygame Event: Left Click")
        if event_button == 3:
            self.right_clicked = True
            print(f"Pygame Event: Right Click")

# ----------------------------------------------------------------------------------------------------