import pygame

# Initialize Pygame
pygame.init()

class Mouse():

    def __init__(self):
        
        print("Global Mouse Tool Instantiated - Datatype: Mouse() Object")

        # Left and Right Click Switches
        self.left_clicked = False
        self.right_clicked = False

    def left_click(self):

        self.left_clicked = True
        print(f"Mouse Left Clicked - at position: {pygame.mouse.get_pos()}")

    def right_click(self):

        self.right_clicked = True
        print(f"Mouse Right Clicked - at position: {pygame.mouse.get_pos()}")