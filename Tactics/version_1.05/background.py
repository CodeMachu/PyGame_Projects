import pygame
import os

# Initialize Pygame
pygame.init()

class Background():

    def __init__(self):

        self.counter = 0
        self.image = pygame.image.load(os.path.join('Images', 'checkered_bg.png'))

        self.rect_1 = self.image.get_rect()
        self.rect_2 = self.image.get_rect()

        self.rect_1.x = -400
        self.rect_1.y = 0

        self.rect_2.x = 0
        self.rect_2.y = 0

    def move(self, window):
        
        self.counter += 1

        if self.counter > 4: # Increase counter to decrease velocity
            self.counter = 0
        if self.counter == 4:
            self.rect_1.x += 1
            self.rect_2.x += 1
        if self.rect_1.x > -1:
            self.rect_1.x = -400
            self.rect_2.x = 0

        window.screen.blit(self.image, self.rect_1)
        window.screen.blit(self.image, self.rect_2)

# Background Tool
background = Background()