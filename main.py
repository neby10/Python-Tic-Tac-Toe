# Author: Nick Eby
# 5.26.2023
# Tic Tac Toe: Main 

import pygame
from tic_tac_toe import TicTacToe
from constants import GameColors, GameMeasurements as GM
from helper_functions import render_text

if __name__ == '__main__':
    # Initialize pygame
    pygame.init()

    # Game Screen
    screen = pygame.display.set_mode((GM.SCREEN_WIDTH, GM.SCREEN_HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    
    # Main Menu Variables
    mode = 0 # for game type selection
    at_main_menu = True # for main menu display
    while at_main_menu:
        screen.fill(GameColors.BACKGROUND)

        # Display Main Menu
        choices = ["Local: 2 Player", "CPU: Random", "CPU: Difficult", "CPU: Mega Difficult"]
        render_text(screen, "Welcome to Tic Tac Toe!", GM.SCREEN_WIDTH // 2, GM.SCREEN_HEIGHT // 6)
        for i in range(len(choices)):
            render_text(screen, choices[i], GM.SCREEN_WIDTH // 2, GM.SCREEN_HEIGHT // 4 + (i * GM.FONT_SIZE))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                at_main_menu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    # Selecting Mode: Local: 2 Player => 1
                    if x > GM.SCREEN_WIDTH // 2 - (1.5 * GM.BOX_SIZE) and x < GM.SCREEN_WIDTH // 2 + (1.5 * GM.BOX_SIZE) and y > GM.SCREEN_HEIGHT // 4 + (0 * GM.FONT_SIZE) - (GM.FONT_SIZE // 2) and y < GM.SCREEN_HEIGHT // 4 + (0 * GM.FONT_SIZE) + (GM.FONT_SIZE // 2):
                        mode = 1
                        print("x is {} | y is {} | mode = {}".format(x, y, mode))
                        at_main_menu = False
                    # Selecting Mode: CPU: Random => 2
                    elif x > GM.SCREEN_WIDTH // 2 - (1.5 * GM.BOX_SIZE) and x < GM.SCREEN_WIDTH // 2 + (1.5 * GM.BOX_SIZE) and y > GM.SCREEN_HEIGHT // 4 + (GM.FONT_SIZE) - (GM.FONT_SIZE // 2) and y < GM.SCREEN_HEIGHT // 4 + (GM.FONT_SIZE) + (GM.FONT_SIZE // 2):
                        mode = 2
                        print("x is {} | y is {} | mode = {}".format(x, y, mode))
                        at_main_menu = False
                    # Selecting Mode: CPU: Difficult => 3
                    elif x > GM.SCREEN_WIDTH // 2 - (1.5 * GM.BOX_SIZE) and x < GM.SCREEN_WIDTH // 2 + (1.5 * GM.BOX_SIZE) and y > GM.SCREEN_HEIGHT // 4 + (2 * GM.FONT_SIZE) - (GM.FONT_SIZE // 2) and y < GM.SCREEN_HEIGHT // 4 + (2 * GM.FONT_SIZE) + (GM.FONT_SIZE // 2):
                        mode = 3
                        print("x is {} | y is {} | mode = {}".format(x, y, mode))
                        at_main_menu = False
                    # Selecting Mode: CPU: Mega Difficult => 4
                    elif x > GM.SCREEN_WIDTH // 2 - (1.5 * GM.BOX_SIZE) and x < GM.SCREEN_WIDTH // 2 + (1.5 * GM.BOX_SIZE) and y > GM.SCREEN_HEIGHT // 4 + (3 * GM.FONT_SIZE) - (GM.FONT_SIZE // 2) and y < GM.SCREEN_HEIGHT // 4 + (3 * GM.FONT_SIZE) + (GM.FONT_SIZE // 2):
                        mode = 4
                        print("x is {} | y is {} | mode = {}".format(x, y, mode))
                        at_main_menu = False


        pygame.display.flip()

    
    # Create Game Instance and Run Game
    game = TicTacToe(screen, mode)
    game.game_loop()

    # Exit pygame
    pygame.quit()
