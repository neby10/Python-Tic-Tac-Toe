# Author: Nick Eby
# 5.26.2023
# Tic Tac Toe: TicTacToe Class

import pygame, random
from constants import GameColors, GameMeasurements as GM
from helper_functions import render_text


class TicTacToe:
    def __init__(self, screen, mode):
        """Constructor for TicTacToe class; initializes necessary variables"""
        print("Tic Tac Toe game starting...")
        self.screen = screen
        self.mode = mode
        self.is_running = True
        self.turn = True # True => P1 turn, False => P2 turn or CPU turn (depending on mode)
        self.grid = [0, 0, 0, 0, 0, 0, 0, 0, 0] # 0 => nothing, 1 => P1 / X, 2 => P2 or CPU / O
        # self.grid = [0, 0, 2, 0, 1, 0, 0, 0, 0]

        self.p1_wins = 0
        self.p2_wins = 0 # for local two player, also represents CPU wins!!!

    def __del__(self):
        """Destructor for TicTacToe class"""
        print("Tic Tac Toe game ending... P1={} | P2={}".format(self.p1_wins, self.p2_wins))

    def check_valid_click(self, index):
        """Check validity of box click"""
        # check for valid click in grid
        if self.grid[index] == 0:
            self.grid[index] = 1 if self.turn else 2
            self.turn = not self.turn

    def handle_click(self, event):
        """Handle box click location"""
        x, y = event.pos
        # top boxes 1, 2, 3
        if y < GM.VERTICAL_GAP + GM.BOX_SIZE:
            if x < GM.HORIZONTAL_GAP + GM.BOX_SIZE and y > GM.VERTICAL_GAP and x > GM.HORIZONTAL_GAP:
                # Box 1
                print("Box 1: Mouse clicked at x={}, y={}".format(x, y))
                self.check_valid_click(0)
            elif x < GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE) and y > GM.VERTICAL_GAP and x > GM.HORIZONTAL_GAP + GM.BOX_SIZE:
                # BOX 2
                print("Box 2: Mouse clicked at x={}, y={}".format(x, y))
                self.check_valid_click(1)
            elif x < GM.HORIZONTAL_GAP + (3 * GM.BOX_SIZE) and y > GM.VERTICAL_GAP and x > GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE):
                # BOX 3
                print("Box 3: Mouse clicked at x={}, y={}".format(x, y))
                self.check_valid_click(2)
        # middle boxes 4, 5, 6
        elif y < GM.VERTICAL_GAP + (2 * GM.BOX_SIZE):
            if x < GM.HORIZONTAL_GAP + GM.BOX_SIZE and y > GM.VERTICAL_GAP + GM.BOX_SIZE and x > GM.HORIZONTAL_GAP:
                # Box 4
                print("Box 4: Mouse clicked at x={}, y={}".format(x, y))
                self.check_valid_click(3)
            elif x < GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE) and y > GM.VERTICAL_GAP + GM.BOX_SIZE and x > GM.HORIZONTAL_GAP + GM.BOX_SIZE:
                # BOX 5
                print("Box 5: Mouse clicked at x={}, y={}".format(x, y))
                self.check_valid_click(4)
            elif x < GM.HORIZONTAL_GAP + (3 * GM.BOX_SIZE) and y > GM.VERTICAL_GAP + GM.BOX_SIZE and x > GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE):
                # BOX 6
                print("Box 6: Mouse clicked at x={}, y={}".format(x, y))
                self.check_valid_click(5)
        # middle boxes 7, 8, 9
        elif y < GM.VERTICAL_GAP + (3 * GM.BOX_SIZE):
            if x < GM.HORIZONTAL_GAP + GM.BOX_SIZE and y > GM.VERTICAL_GAP + (2 * GM.BOX_SIZE) and x > GM.HORIZONTAL_GAP:
                # Box 7
                print("Box 7: Mouse clicked at x={}, y={}".format(x, y))
                self.check_valid_click(6)
            elif x < GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE) and y > GM.VERTICAL_GAP + (2 * GM.BOX_SIZE) and x > GM.HORIZONTAL_GAP + GM.BOX_SIZE:
                # BOX 8
                print("Box 8: Mouse clicked at x={}, y={}".format(x, y))
                self.check_valid_click(7)
            elif x < GM.HORIZONTAL_GAP + (3 * GM.BOX_SIZE) and y > GM.VERTICAL_GAP + (2 * GM.BOX_SIZE) and x > GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE):
                # BOX 9
                print("Box 9: Mouse clicked at x={}, y={}".format(x, y))
                self.check_valid_click(8)

    def check_winner(self, grid):
        """Check for winner; returns 0 for no winner yet, 1 for p1, 2 for p2, 3 for 'CAT'"""
        # Check for number of empty squares i.e. the number of squares that are 0
        num_empty = sum(1 for i in range(9) if self.grid[i] == 0)

        # check each of the eight ways to win
        for player in range(1, 3, 1):
            if grid[0] == player and grid[1] == player and grid[2] == player: # top row
                return player
            elif grid[3] == player and grid[4] == player and grid[5] == player: # middle row
                return player
            elif grid[6] == player and grid[7] == player and grid[8] == player: # bottom row
                return player
            elif grid[0] == player and grid[3] == player and grid[6] == player: # left column
                return player
            elif grid[1] == player and grid[4] == player and grid[7] == player: # middle column
                return player
            elif grid[2] == player and grid[5] == player and grid[8] == player: # right column
                return player
            elif grid[0] == player and grid[4] == player and grid[8] == player: # left to right diagonal
                return player
            elif grid[2] == player and grid[4] == player and grid[6] == player: # right to left diagonal
                return player
            elif num_empty == 0 and player == 2: # no winners and no available spots after checking player 2 means 'CAT'
                return 3
        return 0
    
    def draw_screen(self):
        """Updates pygame screen details"""
        # Draw Screen
        self.screen.fill(GameColors.BACKGROUND)

        # Draw tictactoe board: vertical lines
        pygame.draw.line(self.screen, GameColors.REDDISH, (GM.HORIZONTAL_GAP + GM.BOX_SIZE, GM.VERTICAL_GAP), (GM.HORIZONTAL_GAP + GM.BOX_SIZE, GM.SCREEN_HEIGHT - GM.VERTICAL_GAP), (GM.LINE_WIDTH))
        pygame.draw.line(self.screen, GameColors.REDDISH, (GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE), GM.VERTICAL_GAP), (GM.HORIZONTAL_GAP + (2 * GM.BOX_SIZE), GM.SCREEN_HEIGHT - GM.VERTICAL_GAP), (GM.LINE_WIDTH))
        # Draw tictactoe board: horizontal lines
        pygame.draw.line(self.screen, GameColors.REDDISH, (GM.HORIZONTAL_GAP, GM.VERTICAL_GAP + GM.BOX_SIZE), (GM.SCREEN_WIDTH - GM.HORIZONTAL_GAP, GM.VERTICAL_GAP + GM.BOX_SIZE), (GM.LINE_WIDTH))
        pygame.draw.line(self.screen, GameColors.REDDISH, (GM.HORIZONTAL_GAP, GM.VERTICAL_GAP + (2 * GM.BOX_SIZE)), (GM.SCREEN_WIDTH - GM.HORIZONTAL_GAP, GM.VERTICAL_GAP + (2 * GM.BOX_SIZE)), (GM.LINE_WIDTH))

        # Display player turn
        render_text(self.screen, "Turn: Player 1 (X)" if self.turn else "Turn: Player 2 (O)", GM.SCREEN_WIDTH // 2, GM.BOX_SIZE // 6, font_size=44, font_color=GameColors.BLUEISH)

        # Display player 1 wins count
        render_text(self.screen, "P1: {}".format(self.p1_wins), GM.BOX_SIZE, GM.BOX_SIZE / 6, font_color=GameColors.LIGHTERGREY)

        # Display player 2 wins count
        render_text(self.screen, "P2: {}".format(self.p2_wins), GM.SCREEN_WIDTH - GM.BOX_SIZE, GM.BOX_SIZE / 6, font_color=GameColors.LIGHTERGREY)

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

    def get_available_squares(self, grid):
        """Returns list of indexes of available squares"""
        return [i for i, square in enumerate(grid) if square == 0]

    def minimax(self, grid_copy, is_maximizing):
        """Minimax algorithm, can manipulate grid_copy because it is a copy"""

        # Check if the game has reached a terminal state
        if len(self.get_available_squares(grid_copy)) == 0:
            # Evaluate the state and return the value of state
            winner = self.check_winner(grid_copy)
            if winner == 1:
                return (-1, None)
            elif winner == 2:
                return (1, None)
            else:
                return (0, None)
        
        # If player is P2 i.e. CPU i.e. MAX
        if is_maximizing:
            value_index = (-1000, None)

            # iterate over possible actions
            for index in self.get_available_squares(grid_copy):
                # copy grid and apply index
                new_grid = grid_copy.copy()
                new_grid[index] = 2

                # recursively call minimax
                value, _ = self.minimax(new_grid, False)

                if value > value_index[0]:
                    value_index = (value, index)

            return value_index

        # If player is P1 i.e. Player i.e. MIN
        else:
            value_index = (1000, None)

            # iterate over possible actions
            for index in self.get_available_squares(grid_copy):
                # copy grid and apply index
                new_grid = grid_copy.copy()
                new_grid[index] = 1

                # recursively call minimax
                value, _ = self.minimax(new_grid, True)

                if value < value_index[0]:
                    value_index = (value, index)

            return value_index
    
    def local_2_player(self):
        """Handles events for Local: 2 Player"""
        for event in pygame.event.get():
            # handle quit
            if event.type == pygame.QUIT:
                self.is_running = False
            # handle player 1 or player 2 click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.handle_click(event)

    def cpu_random(self):
        """Handles events for CPU: Random; CPU follows random selection against P1"""
        if not self.turn:
            while not self.turn:
                random_int = random.randint(0, 8)
                if self.grid[random_int] == 0:
                    self.grid[random_int] = 2
                    self.turn = not self.turn
        elif self.turn:
            for event in pygame.event.get():
                # handle quit
                if event.type == pygame.QUIT:
                    self.is_running = False
                # handle player 1 click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_click(event)

    def cpu_difficult(self):
        """Handles events for CPU: Difficult; CPU follows difficult selection against P1"""
        if not self.turn:
            self.turn = not self.turn
            # HANDLE CPU DIFFICULT CHOICE!!!
            #######
        elif self.turn:
            for event in pygame.event.get():
                # handle quit
                if event.type == pygame.QUIT:
                    self.is_running = False
                # handle player 1 click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_click(event)

    def cpu_mega_difficult(self):
        """Handles events for CPU: Mega Difficult; CPU follows mega difficult selection against P1"""
        if not self.turn:
            self.turn = not self.turn
            # all squares open so randomize first choice for CPU
            if len(self.get_available_squares(self.grid)) == 9:
                self.grid[random.choice([0, 2, 4, 6, 8])] = 2 # optimize later maybe??
            else:
                # uses minimax algorithm to choose optimal choice for CPU
                grid_copy = self.grid.copy()
                val, index = self.minimax(grid_copy, True)
                print("Val: {} | Index: {}".format(val, index))
                self.grid[index] = 2
        elif self.turn:
            for event in pygame.event.get():
                # handle quit
                if event.type == pygame.QUIT:
                    self.is_running = False
                # handle player 1 click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_click(event)

    def game_loop(self):
        """Essential game loop function for tictactoe game play"""
        if self.mode == 0:
            print("Mode is 0. Exiting...")
        elif self.mode == 1:
            print("Playing Mode 1: Local 2 Player")
        elif self.mode == 2:
            print("Playing Mode 2: CPU: Random")
        elif self.mode == 3:
            print("Playing Mode 3: CPU: Difficult")
        elif self.mode == 4:
            print("Playing Mode 4: CPU: Mega Difficult")

        while self.is_running:

            # Draw Board
            self.draw_screen()

            # Event handling based on mode, each function is an event handler for that mode
            if self.mode == 0:
                self.is_running = False
            elif self.mode == 1:
                self.local_2_player()
            elif self.mode == 2:
                self.cpu_random()
            elif self.mode == 3:
                self.cpu_difficult()
            elif self.mode == 4:
                self.cpu_mega_difficult()        

            # Check for a winner
            winner = self.check_winner(self.grid)
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

            # Update game screen
            pygame.display.flip()