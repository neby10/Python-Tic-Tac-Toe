# Author: Nick Eby
# 5.30.2023
# Tic Tac Toe: Reinforcement Learning

# Imports
import random

class Board:
    def __init__(self):
        self.grid = [0] * 9
        self.turn = True
        self.in_game = True
        self.cpu1_wins = 0
        self.cpu2_wins = 0
        self.total_cats = 0
        self.total_games = 0

    def print_board(self):
        print("{}|{}|{}".format(self.grid[0], self.grid[1], self.grid[2]))
        print("{}|{}|{}".format(self.grid[3], self.grid[4], self.grid[5]))
        print("{}|{}|{}".format(self.grid[6], self.grid[7], self.grid[8]))
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
            elif num_empty == 0 and player == 2: # no winners and no available spots after checking player 2 means 'CAT'
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
    
class SmartCPU(Player):
    def __init__(self, name, player):
        super().__init__(name, player)
    
    def get_move(self, board):
        if len(board.get_empty_squares()) == 9: # LATER: can we optimize here by choosing the middle square every time instead of a random square???
            return random.choice(board.get_empty_squares())
        else:
            val, index = self.minimax(board)
            # print("Val: {} | Index: {}".format(val, index))
            return index
    
    def minimax(self, board):
        player_MAX = self.player
        player_MIN = 1 if self.player == 2 else 2

        # base case terminal state
        if len(board.get_empty_squares()) == 0:
            winner = board.check_winner()
            if winner == player_MAX:
                return (1, None)
            elif winner == player_MIN:
                return (-1, None)
            else:
                return (0, None)
        
        # find MAX value, index where P1 and turn is True or P2 and turn is False
        if (player_MAX == 1 and board.turn) or (player_MAX == 2 and not board.turn):
            value_index = (float('-inf'), None)
            for index in board.get_empty_squares():
                # set grid to player number, turn to other person
                board.grid[index] = player_MAX
                board.turn = not board.turn

                value, _ = self.minimax(board) # recursively call minimax 

                # undo value changes
                board.turn = not board.turn
                board.grid[index] = 0

                value = value * len(board.get_empty_squares())

                if value > value_index[0]:
                    value_index = (value, index)
            return value_index
        # find MIN value
        else:
            value_index = (float('inf'), None)
            for index in board.get_empty_squares():
                # set grid to player number, turn to other person
                board.grid[index] = player_MIN
                board.turn = not board.turn

                value, _ = self.minimax(board) # recursively call minimax 

                # undo value changes
                board.turn = not board.turn
                board.grid[index] = 0

                value = value * len(board.get_empty_squares())

                if value < value_index[0]:
                    value_index = (value, index)
            return value_index

        # check terminal state
            # return the value(state)
            # undo
        # check if player == MAX
            # value = -inf
            # for a in actions
                # value = MAX(value, minimax(Result(state, a)))
            # return value
        # check if player == MIN
            # value = inf
            # for a in actions
                # value = MIN(value, minimax(Result(state, a)))
            # return value


def get_stats(board, player1, player2, num_games):
    """board is Board() object, player1 and player2 is Player object, num_games is integer number of games you want simulated"""
    while board.in_game:
        turn_message = "X Turn" if board.turn else "Y Turn"
        print(turn_message)
        if board.turn:
            board.grid[player1.get_move(board)] = 1
        else:
            board.grid[player2.get_move(board)] = 2
        board.print_board()

        board.turn = not board.turn

        winner = board.check_winner()
        if winner:
            if isinstance(player1, SmartCPU) or isinstance(player2, SmartCPU):
                print("Simulating game {}.".format(board.total_games))
            if winner == 1:
                board.cpu1_wins += 1
            elif winner == 2:
                board.cpu2_wins += 1
            elif winner == 3:
                board.total_cats += 1
            board.total_games += 1
            board.reset_board()

        if board.total_games > (num_games - 1):
            board.in_game = False
            print("{} Wins : {} : {}%".format(player1.name, board.cpu1_wins, round(board.cpu1_wins / board.total_games * 100, 2)))
            print("{} Wins : {} : {}%".format(player2.name, board.cpu2_wins, round(board.cpu2_wins / board.total_games * 100, 2)))
            print("      CATS      : {} : {}%".format(board.total_cats, round(board.total_cats / board.total_games * 100, 2)))

random_cpu_1 = RandomCPU("CPU Edward", 1)
random_cpu_2 = RandomCPU("CPU Trevor", 2)
smart_cpu_1 = SmartCPU("CPU Francesca", 1)
smart_cpu_2 = SmartCPU("CPU Anastasia", 2)

# Play Random vs Random
# game = Board()
# print("\nRandom CPU vs Random CPU")
# get_stats(game, random_cpu_1, random_cpu_2, 10000)

# Play Random vs CPU
game = Board()
print("\nRandom CPU vs Smart CPU")
get_stats(game, random_cpu_1, smart_cpu_2, 1)

# Play CPU vs CPU
# game = Board()
# print("\nSmart CPU vs Smart CPU")
# get_stats(game, smart_cpu_1, smart_cpu_2, 1)


# USE PANDAS to PLOT PERCENTAGES???