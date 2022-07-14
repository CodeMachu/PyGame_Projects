import pygame
pygame.init()

import os


# ----------------------------------------------------------------------------------------------------

class MainMenu():

    def __init__(self):

        print("Global Main Menu Tool Instantiated - Datatype: MainMenu() Object")

        # Menu On/Off Switches
        self.is_on = True

        # Main Menu Images
        self.image_1 = pygame.image.load(os.path.join('Images', 'new_game.png'))
        self.image_2 = pygame.image.load(os.path.join('Images', 'new_game_light.png'))
        self.image_3 = pygame.image.load(os.path.join('Images', 'load_game.png'))
        self.image_4 = pygame.image.load(os.path.join('Images', 'load_game_light.png'))
        self.image_5 = pygame.image.load(os.path.join('Images', 'scores.png'))
        self.image_6 = pygame.image.load(os.path.join('Images', 'scores_light.png'))
                            
        # New Game Button
        self.new_game_rect = self.image_1.get_rect()
        self.new_game_rect.center = (427, 100)

        # Load Game Button
        self.load_game_rect = self.image_3.get_rect()
        self.load_game_rect.center = (427, 170)

        # Scores Button
        self.scores_rect = self.image_5.get_rect()
        self.scores_rect.center = (427, 240)

# ----------------------------------------------------------------------------------------------------

    # Update Menu Clicked Status
    def update_clicked(self, mouse, tilemap):

        if self.is_on:
            if mouse.left_clicked == True:

                pos = mouse.pos

                # New Game
                if self.new_game_rect.collidepoint(pos):
                    print("\nEntering New Game...\n")
                    # Menu Off
                    self.is_on = False
                    tilemap.is_on = True

                # Load Game
                if self.load_game_rect.collidepoint(pos):
                    print("\nLoad Game Selection...\n")
                    # Menu Off
                    self.is_on = False

                # Scores
                if self.scores_rect.collidepoint(pos):
                    print("\nDisplaying Hi-Scores...\n")
                    # Menu Off
                    self.is_on = False

# ----------------------------------------------------------------------------------------------------

    # Display Menu
    def display(self, window, mouse):

        if self.is_on:

            # Get Mouse Position
            pos = mouse.pos
            
            # Detect Collision with each Button
            if self.new_game_rect.collidepoint(pos):
                self.new_game_rect = self.image_2.get_rect()
                self.new_game_rect.center = (427, 100)
                window.screen.blit(self.image_2, self.new_game_rect)
            else:
                self.new_game_rect = self.image_1.get_rect()
                self.new_game_rect.center = (427, 100)
                window.screen.blit(self.image_1, self.new_game_rect)
            if self.load_game_rect.collidepoint(pos):
                self.load_game_rect = self.image_4.get_rect()
                self.load_game_rect.center = (427, 170)
                window.screen.blit(self.image_4, self.load_game_rect)
            else:
                self.load_game_rect = self.image_3.get_rect()
                self.load_game_rect.center = (427, 170)
                window.screen.blit(self.image_3, self.load_game_rect)
            if self.scores_rect.collidepoint(pos):
                self.scores_rect = self.image_6.get_rect()
                self.scores_rect.center = (427, 240)
                window.screen.blit(self.image_6, self.scores_rect)
            else:
                self.scores_rect = self.image_5.get_rect()
                self.scores_rect.center = (427, 240)
                window.screen.blit(self.image_5, self.scores_rect)

# ----------------------------------------------------------------------------------------------------