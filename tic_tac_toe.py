# Author: Nick Eby
# 5.26.2023
# Tic Tac Toe

import pygame
from constants import GameColors, GameMeasurements as GM


class TicTacToe:
    def __init__(self):
        print("Tic Tac Toe game starting...")
        pygame.init()
        self.is_running = True
        self.turn = True # True => P1 turn, False => P2 turn
        self.grid = [0, 0, 0, 0, 0, 0, 0, 0, 0] # 0 => nothing, 1 => P1 / X, 2 => P2 / O
        self.p1_wins = 0
        self.p2_wins = 0
        self.screen = pygame.display.set_mode((GM.SCREEN_WIDTH, GM.SCREEN_HEIGHT))

        # Game Screen Details
        pygame.display.set_caption("Tic Tac Toe")

    def __del__(self):
        print("Deleting game state...")
        pygame.quit()

    def handle_click(self, index):
        # check for valid click in grid
        if self.grid[index] == 0:
            self.grid[index] = 1 if self.turn else 2
            self.turn = not self.turn

    def check_winner(self):
        # returns the game winner: 0 for no-one yet, 1 for p1, 2 for p2, 3 for CAT
        num_empty = sum(1 for i in range(9) if self.grid[i] == 0)

        # check each of the eight ways to win
        for player in range(1, 3, 1):
            if self.grid[0] == player and self.grid[1] == player and self.grid[2] == player: # top row
                return player
            elif self.grid[3] == player and self.grid[4] == player and self.grid[5] == player: # middle row
                return player
            elif self.grid[6] == player and self.grid[7] == player and self.grid[8] == player: # bottom row
                return player
            elif self.grid[0] == player and self.grid[3] == player and self.grid[6] == player: # left column
                return player
            elif self.grid[1] == player and self.grid[4] == player and self.grid[7] == player: # middle column
                return player
            elif self.grid[2] == player and self.grid[5] == player and self.grid[8] == player: # right column
                return player
            elif self.grid[0] == player and self.grid[4] == player and self.grid[8] == player: # left to right diagonal
                return player
            elif self.grid[2] == player and self.grid[4] == player and self.grid[6] == player: # right to left diagonal
                return player
            elif num_empty == 0: # no winners and no available spots means 'CAT'
                return 3
        return 0
    
    def draw_board(self):
        # Draw Screen
        self.screen.fill(GameColors.BACKGROUND)

        # Draw tictactoe board: vertical lines
        pygame.draw.line(self.screen, GameColors.REDDISH, (GM.HORIZONTAL_GAP + GM.BOX_SIZE, GM.VERTICAL_GAP), (GM.HORIZONTAL_GAP + GM.BOX_SIZE, GM.SCREEN_HEIGHT - GM.VERTICAL_GAP), (GM.LINE_WIDTH))
        pygame.draw.line(self.screen, GameColors.REDDISH, (GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE), GM.VERTICAL_GAP), (GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE), GM.SCREEN_HEIGHT - GM.VERTICAL_GAP), (GM.LINE_WIDTH))
        # Draw tictactoe board: horizontal lines
        pygame.draw.line(self.screen, GameColors.REDDISH, (GM.HORIZONTAL_GAP, GM.VERTICAL_GAP + GM.BOX_SIZE), (GM.SCREEN_WIDTH - GM.HORIZONTAL_GAP, GM.VERTICAL_GAP + GM.BOX_SIZE), (GM.LINE_WIDTH))
        pygame.draw.line(self.screen, GameColors.REDDISH, (GM.HORIZONTAL_GAP, GM.VERTICAL_GAP + (2 * GM.BOX_SIZE)), (GM.SCREEN_WIDTH - GM.HORIZONTAL_GAP, GM.VERTICAL_GAP + (2 * GM.BOX_SIZE)), (GM.LINE_WIDTH))

        # Display player turn
        font = pygame.font.Font(None, 32)
        turn_text_content = "Turn: Player 1 (X)" if self.turn else "Turn: Player 2 (O)" 
        turn_text_surface = font.render(turn_text_content, True, GameColors.LIGHTERGREY)
        turn_text_rect = turn_text_surface.get_rect()
        turn_text_rect.center = (GM.SCREEN_WIDTH // 2, GM.BOX_SIZE // 6)
        self.screen.blit(turn_text_surface, turn_text_rect)

        # Display player 1 wins count
        font = pygame.font.Font(None, 32)
        p1_text_content = "P1: {}".format(self.p1_wins)
        p1_text_surface = font.render(p1_text_content, True, GameColors.LIGHTERGREY)
        p1_text_rect = p1_text_surface.get_rect()
        p1_text_rect.center = (GM.BOX_SIZE, GM.BOX_SIZE / 6)
        self.screen.blit(p1_text_surface, p1_text_rect)

        # Display player 2 wins count
        font = pygame.font.Font(None, 32)
        p2_text_content = "P2: {}".format(self.p2_wins)
        p2_text_surface = font.render(p2_text_content, True, GameColors.LIGHTERGREY)
        p2_text_rect = p2_text_surface.get_rect()
        p2_text_rect.center = (GM.SCREEN_WIDTH - GM.BOX_SIZE, GM.BOX_SIZE / 6)
        self.screen.blit(p2_text_surface, p2_text_rect)

        # Display grid values
        for index, item in enumerate(self.grid):
            x = GM.HORIZONTAL_GAP + (GM.BOX_SIZE * (index % 3)) + (GM.BOX_SIZE / 2)
            y = GM.VERTICAL_GAP + (GM.BOX_SIZE * (index // 3)) + (GM.BOX_SIZE / 2)
            font = pygame.font.Font(None, 60)
            if item == 1:
                # draw X's
                content = "X"
                surface = font.render(content, True, GameColors.ORANGISH)
                rect = surface.get_rect()
                rect.center = (x, y)
                self.screen.blit(surface, rect)
            elif item == 2:
                # draw O's
                content = "O"
                surface = font.render(content, True, GameColors.ORANGISH)
                rect = surface.get_rect()
                rect.center = (x, y)
                self.screen.blit(surface, rect)
            elif item == 0:
                # do nothing
                pass
            else:
                print("TICTACTOE GRID_VALUE_ERROR: Issue with grid. This should not be printed.")

    def game_loop(self):
        while self.is_running:

            self.draw_board()

            # Event handling
            for event in pygame.event.get():
                # handle quit
                if event.type == pygame.QUIT:
                    self.is_running = False
                # handle player click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        # top boxes 1, 2, 3
                        if y < GM.VERTICAL_GAP + GM.BOX_SIZE:
                            if x < GM.HORIZONTAL_GAP + GM.BOX_SIZE and y > GM.VERTICAL_GAP and x > GM.HORIZONTAL_GAP:
                                # Box 1
                                print("Box 1: Mouse clicked at x={}, y={}".format(x, y))
                                self.handle_click(0)
                            elif x < GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE) and y > GM.VERTICAL_GAP and x > GM.HORIZONTAL_GAP + GM.BOX_SIZE:
                                # BOX 2
                                print("Box 2: Mouse clicked at x={}, y={}".format(x, y))
                                self.handle_click(1)
                            elif x < GM.HORIZONTAL_GAP + (3 * GM.BOX_SIZE) and y > GM.VERTICAL_GAP and x > GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE):
                                # BOX 3
                                print("Box 3: Mouse clicked at x={}, y={}".format(x, y))
                                self.handle_click(2)
                        # middle boxes 4, 5, 6
                        elif y < GM.VERTICAL_GAP + (2 * GM.BOX_SIZE):
                            if x < GM.HORIZONTAL_GAP + GM.BOX_SIZE and y > GM.VERTICAL_GAP + GM.BOX_SIZE and x > GM.HORIZONTAL_GAP:
                                # Box 4
                                print("Box 4: Mouse clicked at x={}, y={}".format(x, y))
                                self.handle_click(3)
                            elif x < GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE) and y > GM.VERTICAL_GAP + GM.BOX_SIZE and x > GM.HORIZONTAL_GAP + GM.BOX_SIZE:
                                # BOX 5
                                print("Box 5: Mouse clicked at x={}, y={}".format(x, y))
                                self.handle_click(4)
                            elif x < GM.HORIZONTAL_GAP + (3 * GM.BOX_SIZE) and y > GM.VERTICAL_GAP + GM.BOX_SIZE and x > GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE):
                                # BOX 6
                                print("Box 6: Mouse clicked at x={}, y={}".format(x, y))
                                self.handle_click(5)
                        # middle boxes 7, 8, 9
                        elif y < GM.VERTICAL_GAP + (3 * GM.BOX_SIZE):
                            if x < GM.HORIZONTAL_GAP + GM.BOX_SIZE and y > GM.VERTICAL_GAP + (2 * GM.BOX_SIZE) and x > GM.HORIZONTAL_GAP:
                                # Box 7
                                print("Box 7: Mouse clicked at x={}, y={}".format(x, y))
                                self.handle_click(6)
                            elif x < GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE) and y > GM.VERTICAL_GAP + (2 * GM.BOX_SIZE) and x > GM.HORIZONTAL_GAP + GM.BOX_SIZE:
                                # BOX 8
                                print("Box 8: Mouse clicked at x={}, y={}".format(x, y))
                                self.handle_click(7)
                            elif x < GM.HORIZONTAL_GAP + (3 * GM.BOX_SIZE) and y > GM.VERTICAL_GAP + (2 * GM.BOX_SIZE) and x > GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE):
                                # BOX 9
                                print("Box 9: Mouse clicked at x={}, y={}".format(x, y))
                                self.handle_click(8)
                    print(self.grid)            

            # check for a winner
            winner = self.check_winner()
            if winner:
                # update wins count
                if winner == 1:
                    self.p1_wins += 1
                elif winner == 2:
                    self.p2_wins += 1
                elif winner == 3:
                    # do nothing except reset board for now
                    pass
                # reset grid
                self.grid = [0] * 9

                print(winner)

            # update game screen
            pygame.display.flip()