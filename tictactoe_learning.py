# Author: Nick Eby
# 5.30.2023
# Tic Tac Toe: Reinforcement Learning

# Imports
import random

# Initialize necessary variables
grid = [0] * 9
turn = True
user_choice = 0
in_game = True
cpu_1_wins = 0
cpu_2_wins = 0
cats = 0
num_games = 0

def print_board():
    """Display grid"""
    my_grid = [0] * 9
    for i in range(9):
        if grid[i] == 0:
            my_grid[i] = "_"
        elif grid[i] == 1:
            my_grid[i] = "X"
        elif grid[i] == 2:
            my_grid[i] = "O"
    print("{}|{}|{}".format(my_grid[0], my_grid[1], my_grid[2]))
    print("{}|{}|{}".format(my_grid[3], my_grid[4], my_grid[5]))
    print("{}|{}|{}".format(my_grid[6], my_grid[7], my_grid[8]))
    print()

def get_winner():
    """Return winner: 0, 1, 2, 3"""
    num_empty = sum(1 for i in range(9) if grid[i] == 0)

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

def get_available_moves():
    return [i for i, square in enumerate(grid) if square == 0]

class Player():
    def __init__(self, name, player):
        self.name = name
        self.player = player
    def get_move(self):
        pass

class RandomCPU(Player):
    def __init__(self, name, player):
        super().__init__(name, player)
    
    def get_move(self, grid):
        return random.choice(get_available_moves())
    
class SmartCPU(Player):
    def __init__(self, name, player):
        super().__init__(name, player)
    
    def get_move(self):
        if len(get_available_moves()) == 9: # LATER: can we optimize here by choosing the middle square every time instead of a random square???
            return random.choice(get_available_moves())
        else:
            return self.minimax(grid)
    
    def minimax(self, grid):
        grid_copy = grid.copy()

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


        # check for MIN recursion
        print()


    
random_cpu_1 = RandomCPU("CPU Edward", 1)

random_cpu_2 = RandomCPU("CPU Trevor", 2)

smart_cpu_1 = SmartCPU("CPU Francesca", 1)

smart_cpu_2 = SmartCPU("CPU Anastasia", 2)

while in_game:
    
    if turn:
        grid[random_cpu_1.get_move(grid)] = 1
    else:
        grid[random_cpu_2.get_move(grid)] = 2

    # flip turn
    turn = not turn

    winner = get_winner()
    if winner:
        if winner == 1:
            cpu_1_wins += 1
        elif winner == 2:
            cpu_2_wins += 1
        elif winner == 3:
            cats += 1
            pass
        num_games += 1
        grid = [0] * 9

    if num_games > 2:
        in_game = False
        print("{} Wins : {} : {}%".format(random_cpu_1.name, cpu_1_wins, round(cpu_1_wins / num_games * 100, 2)))
        print("{} Wins : {} : {}%".format(random_cpu_2.name, cpu_2_wins, round(cpu_2_wins / num_games * 100, 2)))
        print("      CATS      : {} : {}%".format(cats, round(cats / num_games * 100, 2)))
