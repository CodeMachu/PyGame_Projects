import pygame

# Initialize Pygame
pygame.init()

class FPS():

    def __init__(self):

        print("Global FPS Tool Instantiated - Datatype: FPS() Object")
        
        # FPS On/Off Switch
        self.is_on = True

        # Create Game Clock
        self.clock = pygame.time.Clock()
        self.FPS = 60

        # Retrieve FPS
        self.current_fps = str(self.clock.get_fps())

        # FPS Rectangle 
        self.font = pygame.font.SysFont('cambria', 14)
        self.text = self.font.render(f"FPS: {self.current_fps[0:5]}", True, (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.topleft = (3, 3)

    # Tick Game Clock
    def tick(self):

        # Constant Sync of Game Clock - calculates how many frames 
        # have passed since last check and adjusts accordingly
        self.clock.tick(self.FPS)

    # Display FPS
    def display_fps(self, window):

        if self.is_on:

            # Reset FPS
            self.current_fps = str(self.clock.get_fps())

            # Reset Text and Rect
            self.text = self.font.render(f"FPS: {self.current_fps[0:5]}", True, (255, 255, 255))
            self.rect = self.text.get_rect()
            self.rect.topleft = 3, 3

            # Display Time
            window.screen.blit(self.text, self.rect)