import pygame
import os

# Initialize Pygame
pygame.init()

class MainMenu():

    def __init__(self):

        # Menu On/Off Switch
        self.is_on = True

        # Main Menu Images
        self.image_array = [
                            pygame.image.load(os.path.join('Images', 'new_game.png')),
                            pygame.image.load(os.path.join('Images', 'load_game.png')),
                            pygame.image.load(os.path.join('Images', 'settings.png')),
                            pygame.image.load(os.path.join('Images', 'new_game_light.png')),
                            pygame.image.load(os.path.join('Images', 'load_game_light.png')),
                            pygame.image.load(os.path.join('Images', 'settings_light.png'))
                            ]
        
        # Main Menu Font
        self.font = pygame.font.SysFont('cambria', 20)

        # New Game Button
        self.new_game_rect = self.image_array[0].get_rect()
        self.new_game_rect.center = (220, 110)

        # Load Game Button
        self.load_game_rect = self.image_array[1].get_rect()
        self.load_game_rect.center = (220, 160)

        # Settings Button
        self.settings_rect = self.image_array[2].get_rect()
        self.settings_rect.center = (220, 210)

    # Display Menu If On
    def display_menu(self, window):

        if self.is_on:

            # Get Mouse Position
            pos = pygame.mouse.get_pos()
            
            # Detect Collision with each Button
            if self.new_game_rect.collidepoint(pos):
                self.new_game_rect = self.image_array[3].get_rect()
                self.new_game_rect.center = (220, 110)
                window.screen.blit(self.image_array[3], self.new_game_rect)
            else:
                self.new_game_rect = self.image_array[0].get_rect()
                self.new_game_rect.center = (220, 110)
                window.screen.blit(self.image_array[0], self.new_game_rect)
            if self.load_game_rect.collidepoint(pos):
                self.load_game_rect = self.image_array[4].get_rect()
                self.load_game_rect.center = (220, 160)
                window.screen.blit(self.image_array[4], self.load_game_rect)
            else:
                self.load_game_rect = self.image_array[1].get_rect()
                self.load_game_rect.center = (220, 160)
                window.screen.blit(self.image_array[1], self.load_game_rect)
            if self.settings_rect.collidepoint(pos):
                self.settings_rect = self.image_array[5].get_rect()
                self.settings_rect.center = (220, 210)
                window.screen.blit(self.image_array[5], self.settings_rect)
            else:
                self.settings_rect = self.image_array[2].get_rect()
                self.settings_rect.center = (220, 210)
                window.screen.blit(self.image_array[2], self.settings_rect)

    # Detect Clicking of each Button
    def detect_click(self):

        if self.is_on:
            
            # Get Mouse Position
            pos = pygame.mouse.get_pos()

            if self.new_game_rect.collidepoint(pos):
                print("Entering New Game\n Choose Class")
                self.is_on = False
            if self.load_game_rect.collidepoint(pos):
                print("Entering Load Game\n Choose File Save")
                self.is_on = False
            if self.settings_rect.collidepoint(pos):
                print("Entering Settings\n Choose Setting")
                self.is_on = False                    

# Main Menu Tool
main_menu = MainMenu()