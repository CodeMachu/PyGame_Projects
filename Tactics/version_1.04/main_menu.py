import pygame
import os

# Initialize Pygame
pygame.init()

class MainMenu():

    def __init__(self):

        # Menu On/Off Switches
        self.is_on = True

        self.class_select_is_on = False
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
                            pygame.image.load(os.path.join('Images', 'scores_light.png')),
                            pygame.image.load(os.path.join('Images', 'knight_button.png')),
                            pygame.image.load(os.path.join('Images', 'knight_button_light.png')),
                            pygame.image.load(os.path.join('Images', 'ranger_button.png')),
                            pygame.image.load(os.path.join('Images', 'ranger_button_light.png')),
                            pygame.image.load(os.path.join('Images', 'mage_button.png')),
                            pygame.image.load(os.path.join('Images', 'mage_button_light.png'))
                            ]
        
        # Main Menu Font
        self.font = pygame.font.SysFont('cambria', 20)

        # New Game Button
        self.new_game_rect = self.image_array[0].get_rect()
        self.new_game_rect.center = (220, 110)

        # Load Game Button
        self.load_game_rect = self.image_array[1].get_rect()
        self.load_game_rect.center = (220, 160)

        # Highscores Button
        self.scores_rect = self.image_array[2].get_rect()
        self.scores_rect.center = (220, 210)

        # Knight Button
        self.knight_rect = self.image_array[6].get_rect()
        self.knight_rect.center = (220, 110)

        # Ranger Button
        self.ranger_rect = self.image_array[8].get_rect()
        self.ranger_rect.center = (220, 160)

        # Mage Button
        self.mage_rect = self.image_array[10].get_rect()
        self.mage_rect.center = (220, 210)

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
            if self.scores_rect.collidepoint(pos):
                self.scores_rect = self.image_array[5].get_rect()
                self.scores_rect.center = (220, 210)
                window.screen.blit(self.image_array[5], self.scores_rect)
            else:
                self.scores_rect = self.image_array[2].get_rect()
                self.scores_rect.center = (220, 210)
                window.screen.blit(self.image_array[2], self.scores_rect)

        # Display Class Selection If On
        self.display_class_select(window)

    # Display Class Selection If On
    def display_class_select(self, window):

        if self.class_select_is_on:

            # Get Mouse Position
            pos = pygame.mouse.get_pos()

            # Detect Collision with each Button
            if self.knight_rect.collidepoint(pos):
                self.knight_rect = self.image_array[7].get_rect()
                self.knight_rect.center = (220, 110)
                window.screen.blit(self.image_array[7], self.knight_rect)
            else:
                self.knight_rect = self.image_array[6].get_rect()
                self.knight_rect.center = (220, 110)
                window.screen.blit(self.image_array[6], self.knight_rect)
            if self.ranger_rect.collidepoint(pos):
                self.ranger_rect = self.image_array[9].get_rect()
                self.ranger_rect.center = (220, 160)
                window.screen.blit(self.image_array[9], self.ranger_rect)
            else:
                self.ranger_rect = self.image_array[8].get_rect()
                self.ranger_rect.center = (220, 160)
                window.screen.blit(self.image_array[8], self.ranger_rect)
            if self.mage_rect.collidepoint(pos):
                self.mage_rect = self.image_array[11].get_rect()
                self.mage_rect.center = (220, 210)
                window.screen.blit(self.image_array[11], self.mage_rect)
            else:
                self.mage_rect = self.image_array[10].get_rect()
                self.mage_rect.center = (220, 210)
                window.screen.blit(self.image_array[10], self.mage_rect)

    # Detect Click
    def detect_click(self):

        # Get Mouse Position
        pos = pygame.mouse.get_pos()

        ## IMPORTANT - Iterate thru menues in backwards order to avoid
        ##             colliding with multiple rects in one game loop

        # If Class Selection Is On
        if self.class_select_is_on:

            # Knight
            if self.knight_rect.collidepoint(pos):
                print("Knight Selected")
                # Turn class selection off, stat selection on
                self.class_select_is_on = False
                self.stat_select_is_on = True

            # Ranger
            if self.ranger_rect.collidepoint(pos):
                print("Ranger Selected")
                # Turn class selection off, stat selection on
                self.class_select_is_on = False
                self.stat_select_is_on = True

            # Mage
            if self.mage_rect.collidepoint(pos):
                print("Mage Selected")
                # Turn class selection off, stat selection on
                self.class_select_is_on = False
                self.stat_select_is_on = True

        # If Main Menu Is On
        if self.is_on:

            # New Game
            if self.new_game_rect.collidepoint(pos):
                print("Entering Class Selection\n - Choose Class")
                # Turn main menu off, class selection on
                self.is_on = False
                self.class_select_is_on = True

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