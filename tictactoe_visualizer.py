# Author: Nicholas Eby
# Date Created: 5.30.2023
# Project: TicTacToe - TicTacToe Game Simulator
# Website: https://nicholaseby.com
# GitHub: https://github.com/neby10
# LinkedIn: https://www.linkedin.com/in/nicholas-eby-software-engineer/
# Twitter: @neby10_sisyphus

# Imports
import random, matplotlib.pyplot as plt

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
    
class SmartCPU(Player):
    def __init__(self, name, player):
        super().__init__(name, player)
    
    def get_move(self, board):
        if len(board.get_empty_squares()) == 9:
            return random.choice([0, 2, 4, 6, 8])
        else:
            val, index = self.minimax(board, 0)
            # print("Val: {} | Index: {}".format(val, index))
            return index
    
    def minimax(self, board, alpha=float('-inf'), beta=float('inf')):
        player_MAX = self.player
        player_MIN = 1 if self.player == 2 else 2

        # base case terminal state
        if len(board.get_empty_squares()) == 0 or board.check_winner():
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

                value, _ = self.minimax(board, alpha, beta) # recursively call minimax 

                # undo value changes
                board.turn = not board.turn
                board.grid[index] = 0

                value = value * len(board.get_empty_squares())

                if value > value_index[0]:
                    value_index = (value, index)
                alpha = max(alpha, value_index[0])
                if alpha >= beta:
                    break
            return value_index
        # find MIN value
        else:
            value_index = (float('inf'), None)
            for index in board.get_empty_squares():
                # set grid to player number, turn to other person
                board.grid[index] = player_MIN
                board.turn = not board.turn

                value, _ = self.minimax(board, alpha, beta) # recursively call minimax 

                # undo value changes
                board.turn = not board.turn
                board.grid[index] = 0

                value = value * len(board.get_empty_squares())

                if value < value_index[0]:
                    value_index = (value, index)

                beta = min(beta, value_index[0])
                if alpha >= beta:
                    break
            return value_index
        
def get_stats(board, player1, player2, num_games):
    """board is Board() object, player1 and player2 is Player object, num_games is integer number of games you want simulated"""
    while board.in_game:
        if board.turn:
            board.grid[player1.get_move(board)] = 1
        else:
            board.grid[player2.get_move(board)] = 2

        board.turn = not board.turn

        winner = board.check_winner()
        if winner:
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
            return ([board.cpu1_wins, board.cpu2_wins, board.total_cats], [player1.name, player2.name, "CATS"])

def display_bar_chart_of_stats(display_tuple, title, xlabel, ylabel, limit):
    plt.bar(display_tuple[1], display_tuple[0])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(0, limit)
    plt.show()

# Initialize Players
random_cpu_1 = RandomCPU("CPU Edward", 1)
random_cpu_2 = RandomCPU("CPU Trevor", 2)
smart_cpu_1 = SmartCPU("CPU Francesca", 1)
smart_cpu_2 = SmartCPU("CPU Anastasia", 2)

num_games = 200

# Play Random vs Random
game = Board()
print("\nRandom CPU vs Random CPU")
rand_v_rand = get_stats(game, random_cpu_1, random_cpu_2, num_games)

# Play Random vs Smart
game = Board()
print("\nRandom CPU vs Smart CPU")
rand_v_smart = get_stats(game, random_cpu_1, smart_cpu_1, num_games)
game = Board()
print("\nSmart CPU vs Random CPU")
rand_v_smart = get_stats(game, smart_cpu_1, random_cpu_1, num_games)

# Play Smart vs Smart
game = Board()
print("\nSmart CPU vs Smart CPU")
smart_v_smart_1 = get_stats(game, smart_cpu_1, smart_cpu_2, num_games)

# # Play Smart vs Smart (reversed order)
game = Board()
print("\nSmart CPU vs Smart CPU")
smart_v_smart_2 = get_stats(game, smart_cpu_2, smart_cpu_1, num_games)


# Use Matplotlib to Visualize
display_bar_chart_of_stats(rand_v_rand, "TicTacToe: Random vs Random", "Player", "Number of Wins", num_games)
display_bar_chart_of_stats(rand_v_smart, "TicTacToe: Random vs Smart", "Player", "Number of Wins", num_games)
display_bar_chart_of_stats(smart_v_smart_1, "TicTacToe: Smart vs Smart", "Player", "Number of Wins", num_games)
display_bar_chart_of_stats(smart_v_smart_2, "TicTacToe: Smart vs Smart (Reversed Parameters)", "Player", "Number of Wins", num_games)