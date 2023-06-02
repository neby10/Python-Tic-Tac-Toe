# Author: Nicholas Eby
# Date Created: 5.26.2023
# Project: TicTacToe - TicTacToe Class
# Website: https://nicholaseby.com
# GitHub: https://github.com/neby10
# LinkedIn: https://www.linkedin.com/in/nicholas-eby-software-engineer/
# Twitter: @neby10_sisyphus

import pygame, random
from constants import GameColors, GameMeasurements as GM
from helper_functions import render_text

class Board:
    def __init__(self):
        self.grid = [0] * 9
        self.turn = True
        self.in_game = True
        self.p1_wins = 0
        self.p2_wins = 0
        self.total_cats = 0
        self.total_games = 0

    def print_board(self):
        rows = ["{}|{}|{}".format(self.grid[i], self.grid[i+1], self.grid[i+2]) for i in range(0, 9, 3)]
        print("\n".join(rows))
        print()

    def reset_board(self):
        self.grid = [0] * 9

    def get_empty_squares(self):
        return [i for i, square in enumerate(self.grid) if square == 0]

    def check_winner(self):
        """Return winner: 0, 1, 2, 3
        0 = no winner yet, 1 = P1, 2 = P2, 3 = CAT"""
        num_empty = sum(1 for i in range(9) if self.grid[i] == 0)

        # check each of the eight ways to win
        for player in range(1, 3, 1):
            if (self.grid[0] == player and self.grid[1] == player and self.grid[2] == player) or \
               (self.grid[3] == player and self.grid[4] == player and self.grid[5] == player) or \
               (self.grid[6] == player and self.grid[7] == player and self.grid[8] == player) or \
               (self.grid[0] == player and self.grid[3] == player and self.grid[6] == player) or \
               (self.grid[1] == player and self.grid[4] == player and self.grid[7] == player) or \
               (self.grid[2] == player and self.grid[5] == player and self.grid[8] == player) or \
               (self.grid[0] == player and self.grid[4] == player and self.grid[8] == player) or \
                (self.grid[2] == player and self.grid[4] == player and self.grid[6] == player):
                return player

        if num_empty == 0: # no winners and no available spots means 'CAT'
            return 3
        return 0
    
class Player():
    def __init__(self, name, player):
        self.name = name
        self.player = player
    def get_move(self):
        pass

class RandomCPU(Player):
    def __init__(self, name, player):
        super().__init__(name, player)
    
    def get_move(self, board):
        return random.choice(board.get_empty_squares())

class TicTacToe:
    def __init__(self, screen, board, mode):
        """Constructor for TicTacToe class; initializes necessary variables"""
        print("Tic Tac Toe game starting...")
        self.screen = screen
        self.board = board
        self.mode = mode

    def __del__(self):
        """Destructor for TicTacToe class"""
        print("Tic Tac Toe game ending... P1={} | P2={}".format(self.board.p1_wins, self.board.p2_wins))

    def check_valid_click(self, index):
        """Check validity of box click"""
        # check for valid click in grid
        if self.board.grid[index] == 0:
            self.board.grid[index] = 1 if self.board.turn else 2
            self.board.turn = not self.board.turn

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
        render_text(self.screen, "Turn: Player 1 (X)" if self.board.turn else "Turn: Player 2 (O)", GM.SCREEN_WIDTH // 2, GM.BOX_SIZE // 6, font_size=44, font_color=GameColors.BLUEISH)

        # Display player 1 wins count
        render_text(self.screen, "P1: {}".format(self.board.p1_wins), GM.BOX_SIZE, GM.BOX_SIZE / 6, font_color=GameColors.LIGHTERGREY)

        # Display player 2 wins count
        render_text(self.screen, "P2: {}".format(self.board.p2_wins), GM.SCREEN_WIDTH - GM.BOX_SIZE, GM.BOX_SIZE / 6, font_color=GameColors.LIGHTERGREY)

        # Display grid values
        for index, item in enumerate(self.board.grid):
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
    
    def minimax_primitive(self, board, is_maximizing):
        """Minimax algorithm, can manipulate grid_copy because it is a copy"""

        # Check if the game has reached a terminal state
        if len(self.board.get_empty_squares()) == 0:
            # Evaluate the state and return the value of state
            winner = self.board.check_winner()
            if winner == 1:
                return (-1, None)
            elif winner == 2:
                return (1, None)
            else:
                return (0, None)
        
        # If player is P2 i.e. CPU i.e. MAX
        if is_maximizing:
            value_index = (float('-inf'), None)

            # iterate over possible actions
            for index in self.board.get_empty_squares():

                # change square
                self.board.grid[index] = 2
                self.board.turn = not self.board.turn

                # recursively call minimax
                value, _ = self.minimax_primitive(self.board, False)

                # undo change
                self.board.turn = not self.board.turn
                self.board.grid[index] = 0


                value = value * len(self.board.get_empty_squares())

                if value > value_index[0]:
                    value_index = (value, index)

            return value_index

        # If player is P1 i.e. Player i.e. MIN
        else:
            value_index = (float('inf'), None)

            # iterate over possible actions
            for index in self.board.get_empty_squares():
                # change square
                self.board.grid[index] = 1
                self.board.turn = not self.board.turn

                # recursively call minimax
                value, _ = self.minimax_primitive(self.board, True)

                # undo square
                self.board.turn = not self.board.turn
                self.board.grid[index] = 0


                value = value * len(self.board.get_empty_squares())

                if value < value_index[0]:
                    value_index = (value, index)

            return value_index


    def minimax_advanced(self, board, is_maximizing, alpha=float('-inf'), beta=float('inf')):
        """Minimax algorithm, can manipulate grid_copy because it is a copy"""
        
        # Check if the game has reached a terminal state
        if (len(self.board.get_empty_squares()) == 0) or self.board.check_winner():
            # Evaluate the state and return the value of state
            winner = self.board.check_winner()
            if winner == 1:
                return (-1, None)
            elif winner == 2:
                return (1, None)
            else:
                return (0, None)
        
        # If player is P2 i.e. CPU i.e. MAX
        if is_maximizing:
            value_index = (float('-inf'), None)

            # iterate over possible actions
            for index in self.board.get_empty_squares():

                # change board values
                self.board.grid[index] = 2
                self.board.turn = not self.board.turn

                # recursively call minimax
                value, _ = self.minimax_advanced(self.board, False)

                # reset board values
                self.board.turn = not board.turn
                self.board.grid[index] = 0

                value = value * len(self.board.get_empty_squares())

                if value > value_index[0]:
                    value_index = (value, index)

                alpha = max(alpha, value_index[0])
                if alpha >= beta:
                    break
            return value_index

        # If player is P1 i.e. Player i.e. MIN
        else:
            value_index = (float('inf'), None)

            # iterate over possible actions
            for index in self.board.get_empty_squares():
                # change board values
                self.board.grid[index] = 1
                self.board.turn = not self.board.turn

                # recursively call minimax
                value, _ = self.minimax_advanced(self.board, True)

                # undo value changes
                board.turn = not board.turn
                board.grid[index] = 0

                value = value * len(self.board.get_empty_squares())

                if value < value_index[0]:
                    value_index = (value, index)

                beta = max(beta, value_index[0])
                if alpha >= beta:
                    break
            return value_index
    
    def local_2_player(self):
        """Handles events for Local: 2 Player"""
        for event in pygame.event.get():
            # handle quit game
            if event.type == pygame.QUIT:
                self.board.in_game = False
            # handle player 1 or player 2 click
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.handle_click(event)

    def cpu_random(self, randomCPU):
        """Handles events for CPU: Random; CPU follows random selection against P1"""
        if not self.board.turn:
            # switch turn variable
            while not self.board.turn:
                # randomize CPU choice
                move = randomCPU.get_move(self.board)
                # random_int = random.randint(0, 8)
                if self.board.grid[move] == 0:
                    self.board.grid[move] = 2
                    self.board.turn = not self.board.turn
        elif self.board.turn:
            for event in pygame.event.get():
                # handle quit
                if event.type == pygame.QUIT:
                    self.board.in_game = False
                # handle player 1 click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_click(event)

    def cpu_difficult(self):
        """Handles events for CPU: Difficult; calls minimax_primitive because this was my first iteration of minimax"""
        if not self.board.turn:
            # switch turn variable
            self.board.turn = not self.board.turn
            # all squares open so randomize first choice for CPU
            if len(self.board.get_empty_squares()) == 9:
                self.board.grid[random.choice([0, 2, 4, 6, 8])] = 2 # optimize later maybe??
            else:
                # uses minimax algorithm to choose optimal choice for CPU
                val, index = self.minimax_primitive(self.board, True)
                self.board.grid[index] = 2
        elif self.board.turn:
            for event in pygame.event.get():
                # handle quit
                if event.type == pygame.QUIT:
                    self.board.in_game = False
                # handle player 1 click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_click(event)

    def cpu_mega_difficult(self):
        """Handles events for CPU: Mega Difficult; CPU follows mega difficult selection against P1"""
        if not self.board.turn:
            # switch turn variable
            self.board.turn = not self.board.turn
            # all squares open so randomize first choice for CPU
            if len(self.board.get_empty_squares()) == 9:
                self.board.grid[random.choice([0, 2, 4, 6, 8])] = 2 # optimize later maybe??
            else:
                # uses minimax algorithm to choose optimal choice for CPU
                val, index = self.minimax_advanced(self.board, True)
                # print("Val: {} | Index: {}".format(val, index))
                self.board.grid[index] = 2
        elif self.board.turn:
            for event in pygame.event.get():
                # handle quit
                if event.type == pygame.QUIT:
                    self.board.in_game = False
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
            randomCPU = RandomCPU("RCPU", 2)
        elif self.mode == 3:
            print("Playing Mode 3: CPU: Difficult")
        elif self.mode == 4:
            print("Playing Mode 4: CPU: Mega Difficult")

        while self.board.in_game:

            # Draw Board
            self.draw_screen()

            # Event handling based on mode, each function is an event handler for that mode
            if self.mode == 0:
                self.board.in_game = False
            elif self.mode == 1:
                self.local_2_player()
            elif self.mode == 2:
                self.cpu_random(randomCPU)
            elif self.mode == 3:
                self.cpu_difficult()
            elif self.mode == 4:
                self.cpu_mega_difficult()        

            # Check for a winner
            winner = self.board.check_winner()
            if winner:
                # update wins count
                if winner == 1:
                    self.board.p1_wins += 1
                elif winner == 2:
                    self.board.p2_wins += 1
                elif winner == 3:
                    # do nothing except reset board for now
                    pass
                # reset grid
                self.board.reset_board()

            # Update game screen
            pygame.display.flip()