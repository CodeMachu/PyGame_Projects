import pygame
import os

# Initialize Pygame
pygame.init()

class MainMenu():

    def __init__(self):

        print("Global Main_Menu Tool Instantiated - Datatype: MainMenu() Object")

        # Menu On/Off Switches
        self.is_on = True

        # Main Menu Images
        self.image_array = [
                            pygame.image.load(os.path.join('Images', 'new_game.png')),
                            pygame.image.load(os.path.join('Images', 'new_game_light.png')),
                            pygame.image.load(os.path.join('Images', 'load_game.png')),
                            pygame.image.load(os.path.join('Images', 'load_game_light.png')),
                            pygame.image.load(os.path.join('Images', 'scores.png')),
                            pygame.image.load(os.path.join('Images', 'scores_light.png'))
                            ]

        # New Game Button
        self.new_game_rect = self.image_array[0].get_rect()
        self.new_game_rect.center = (427, 100)

        # Load Game Button
        self.load_game_rect = self.image_array[2].get_rect()
        self.load_game_rect.center = (427, 170)

        # Scores Button
        self.scores_rect = self.image_array[4].get_rect()
        self.scores_rect.center = (427, 240)

    # Display Menu If On
    def display_menu(self, window):

        if self.is_on:

            # Get Mouse Position
            pos = pygame.mouse.get_pos()
            
            # Detect Collision with each Button
            if self.new_game_rect.collidepoint(pos):
                self.new_game_rect = self.image_array[1].get_rect()
                self.new_game_rect.center = (427, 100)
                window.screen.blit(self.image_array[1], self.new_game_rect)
            else:
                self.new_game_rect = self.image_array[0].get_rect()
                self.new_game_rect.center = (427, 100)
                window.screen.blit(self.image_array[0], self.new_game_rect)
            if self.load_game_rect.collidepoint(pos):
                self.load_game_rect = self.image_array[3].get_rect()
                self.load_game_rect.center = (427, 170)
                window.screen.blit(self.image_array[3], self.load_game_rect)
            else:
                self.load_game_rect = self.image_array[2].get_rect()
                self.load_game_rect.center = (427, 170)
                window.screen.blit(self.image_array[2], self.load_game_rect)
            if self.scores_rect.collidepoint(pos):
                self.scores_rect = self.image_array[5].get_rect()
                self.scores_rect.center = (427, 240)
                window.screen.blit(self.image_array[5], self.scores_rect)
            else:
                self.scores_rect = self.image_array[4].get_rect()
                self.scores_rect.center = (427, 240)
                window.screen.blit(self.image_array[4], self.scores_rect)

    # Detect Click
    def detect_click(self, mouse, tilemap, clock, player):

        if self.is_on:
            if mouse.left_clicked == True:

                # Get Mouse Position
                pos = pygame.mouse.get_pos()

                # New Game
                if self.new_game_rect.collidepoint(pos):
                    print("Entering New Game")
                    # Turn main menu off, tilemap on, player on
                    self.is_on = False
                    tilemap.is_on = True
                    player.is_on = True
                    clock.is_on = True
                # Load Game
                if self.load_game_rect.collidepoint(pos):
                    print("Load Game Selection")
                    self.is_on = False
                # Scores
                if self.scores_rect.collidepoint(pos):
                    print("Displaying Hi-Scores")
                    self.is_on = False