import pygame
pygame.init()

from datetime import datetime


# ----------------------------------------------------------------------------------------------------

class Clock():

    def __init__(self):

        print("Global Clock Tool Instantiated - Datatype: Clock() Object")
        
        # Clock On/Off Switch
        self.is_on = True

        # Retrieve Time
        self.current_time = datetime.now().strftime("%H:%M:%S")

        # Clock Rectangle
        self.font = pygame.font.SysFont('cambria', 16)
        self.text = self.font.render(f"{self.current_time}", True, (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (427, 650)

# ----------------------------------------------------------------------------------------------------

    # Update Time
    def update(self):

        if self.is_on:

            # Retrieve Current Time
            self.current_time = datetime.now().strftime("%H:%M:%S")

            # Reset Text and Rect
            self.text = self.font.render(f"{self.current_time}", True, (255, 255, 255))
            self.rect = self.text.get_rect()
            self.rect.center = (427, 650)

# ----------------------------------------------------------------------------------------------------

    # Display Time
    def display(self, window):

        if self.is_on:

            # Display Time
            window.screen.blit(self.text, self.rect)

# ----------------------------------------------------------------------------------------------------