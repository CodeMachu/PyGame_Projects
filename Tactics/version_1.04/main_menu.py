import pygame
import os

# Initialize Pygame
pygame.init()

class MainMenu():

    def __init__(self):

        # Menu On/Off Switches
        self.is_on = True

        self.stat_select_is_on = False

        self.load_select_is_on = False
        self.scores_is_on = False

        # Main Menu Images
        self.image_array = [
                            pygame.image.load(os.path.join('Images', 'new_game.png')),
                            pygame.image.load(os.path.join('Images', 'load_game.png')),
                            pygame.image.load(os.path.join('Images', 'scores.png')),
                            pygame.image.load(os.path.join('Images', 'new_game_light.png')),
                            pygame.image.load(os.path.join('Images', 'load_game_light.png')),
                            pygame.image.load(os.path.join('Images', 'scores_light.png'))
                            ]
        
        # Main Menu Font
        self.font = pygame.font.SysFont('cambria', 20)

        # New Game Button
        self.new_game_rect = self.image_array[0].get_rect()
        self.new_game_rect.center = (220, 100)

        # Load Game Button
        self.load_game_rect = self.image_array[1].get_rect()
        self.load_game_rect.center = (220, 140)

        # Scores Button
        self.scores_rect = self.image_array[2].get_rect()
        self.scores_rect.center = (220, 180)

    # Display Menu If On
    def display_menu(self, window):

        if self.is_on:

            # Get Mouse Position
            pos = pygame.mouse.get_pos()
            
            # Detect Collision with each Button
            if self.new_game_rect.collidepoint(pos):
                self.new_game_rect = self.image_array[3].get_rect()
                self.new_game_rect.center = (220, 100)
                window.screen.blit(self.image_array[3], self.new_game_rect)
            else:
                self.new_game_rect = self.image_array[0].get_rect()
                self.new_game_rect.center = (220, 100)
                window.screen.blit(self.image_array[0], self.new_game_rect)
            if self.load_game_rect.collidepoint(pos):
                self.load_game_rect = self.image_array[4].get_rect()
                self.load_game_rect.center = (220, 140)
                window.screen.blit(self.image_array[4], self.load_game_rect)
            else:
                self.load_game_rect = self.image_array[1].get_rect()
                self.load_game_rect.center = (220, 140)
                window.screen.blit(self.image_array[1], self.load_game_rect)
            if self.scores_rect.collidepoint(pos):
                self.scores_rect = self.image_array[5].get_rect()
                self.scores_rect.center = (220, 180)
                window.screen.blit(self.image_array[5], self.scores_rect)
            else:
                self.scores_rect = self.image_array[2].get_rect()
                self.scores_rect.center = (220, 180)
                window.screen.blit(self.image_array[2], self.scores_rect)

    # Detect Click
    def detect_click(self, tilemap):

        # Get Mouse Position
        pos = pygame.mouse.get_pos()

        # If Main Menu Is On
        if self.is_on:
            # New Game
            if self.new_game_rect.collidepoint(pos):
                print("Entering Game")
                # Turn main menu off, class selection on
                self.is_on = False
                tilemap.is_on = True
            # Load Game
            if self.load_game_rect.collidepoint(pos):
                print("Entering Load Game\n - Choose File Save")
                self.is_on = False
            # Scores
            if self.scores_rect.collidepoint(pos):
                print("Entering Scores\n - Have a Look")
                self.is_on = False

# Main Menu Tool
main_menu = MainMenu()