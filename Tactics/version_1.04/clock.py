import pygame

from datetime import datetime

# Initialize Pygame
pygame.init()

class Clock():

    def __init__(self):
        
        # Clock On/Off Switch
        self.is_on = True

        # Retrieve Time
        self.current_time = datetime.now().strftime("%H:%M:%S")

        # Clock Rectangle
        self.font = pygame.font.SysFont('cambria', 16)
        self.text = self.font.render(f"Game Clock: {self.current_time}", True, (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (220, 417)

    def display_time(self, window):

        if self.is_on:

            # Reset Time
            self.current_time = datetime.now().strftime("%H:%M:%S")

            # Reset Text and Rect
            self.text = self.font.render(f"{self.current_time}", True, (255, 255, 255))
            self.rect = self.text.get_rect()
            self.rect.center = (220, 417)

            # Display Time
            window.screen.blit(self.text, self.rect)

# Clock Tool
clock = Clock()