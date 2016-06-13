'''
AI Project: Connect 5

Rules:
The game board will be a square board of length n where n is greater than or equal to 5
User will always start

'''
from alphaBeta import *

class Connect5():
    game_board = []
    game_board_size = 0
    
    def __init__(self, game_board_size):
        self.game_board_size = game_board_size
        self.game_board = [[-1] * game_board_size for i in range(game_board_size)]
        

    '''
    is_goal_state
    Parameter: last_move, game_board
    Returns True or False depending on whether last_move has connected five
    '''
    def is_goal_state(self, last_move, game_board):
        row = 1
        col = 1
        right_dia = 1
        left_dia = 1
        value = game_board[last_move[0]][last_move[1]]
        i = last_move[0] + 1

        #Check column win
        while i < (last_move[0]+5):
            if i>=self.game_board_size:
                break
            if game_board[i][last_move[1]]!= value:
                break
            col = col + 1
            i = i + 1
            
        i = last_move[0] - 1
        while i > (last_move[0]-5):
            if i<=0:
                break
            if game_board[i][last_move[1]]!= value:
                break
            col = col + 1
            i = i - 1
            
        if col>=5:
            return True

        #Check row win
        i = last_move[1] + 1
        while i < (last_move[1]+5):
            if i>=self.game_board_size:
                break
            if game_board[last_move[0]][i]!= value:
                break
            row = row + 1
            i = i + 1
            
        i = last_move[1] - 1
        while i > (last_move[1]-5):
            if i<=0:
                break
            if game_board[last_move[0]][i]!= value:
                break
            row = row + 1
            i = i - 1
            
        if row>=5:
            return True

        #Check right diagonal win
        i = last_move[1] + 1
        j = last_move[0] + 1
        while i < (last_move[1]+5) and j < (last_move[0]+5):
            if i>=self.game_board_size or j>=self.game_board_size:
                break

            if game_board[j][i]!= value:
                break
            right_dia = right_dia + 1
            i = i + 1
            j = j + 1
            
        i = last_move[1] - 1
        j = last_move[0] - 1
        while i > (last_move[1]-5) and j > (last_move[0]-5):
            if i<=0 or j<=0:
                break
            if game_board[j][i]!= value:
                break
            right_dia = right_dia + 1
            i = i - 1
            j = j - 1
            
        if right_dia>=5:
            return True

        #Check left diagonal win
        i = last_move[1] + 1
        j = last_move[0] - 1
        while i < (last_move[1]+5) and j > (last_move[0]-5):
            if i>=self.game_board_size or j<=0:
                break
            if game_board[j][i]!= value:
                break
            left_dia = left_dia + 1
            i = i + 1
            j = j - 1
            
        i = last_move[1] - 1
        j = last_move[0] + 1
        while i > (last_move[1]-5) and j < (last_move[0]+5):
            if i<=0 or j>=self.game_board_size:
                break
            if game_board[j][i]!= value:
                break
            left_dia = left_dia + 1
            i = i - 1
            j = j + 1
            
        if left_dia>=5:
            return True
        
        return False
    

    def update_board(self, move_row, move_col, player):
        value = -1
        if player == "user" or player == "player1":
            value = 1
        else:
            value = 0

        self.game_board[move_row][move_col] = value


    def is_valid(self, coor):
        if coor>=0 and coor<self.game_board_size:
            return True
        return False


    def is_valid_move(self, row, col):
        if self.is_valid(row) and self.is_valid(col):
            if self.game_board[row][col] == -1:
                return True
        return False    

        
    def print_board(self):
        for row in self.game_board:
            print_row = "| "
            for r in row:
                
                if r == -1:
                    print_row = print_row + "_"
                elif r == 0:
                    print_row = print_row + "O"
                elif r == 1:
                    print_row = print_row + "X"
                print_row = print_row + " | "
            print(print_row)
            print("")


    def print_user_board(self):
        n_row = 0
        for row in self.game_board:
            print_row = "| "
            n_col = 0
            for r in row:
                
                if r == -1:
                    print_row = print_row + str(n_row) + "," + str(n_col)
                elif r == 0:
                    print_row = print_row + " O "
                elif r == 1:
                    print_row = print_row + " X "
                print_row = print_row + " | "
                n_col = n_col + 1
            print(print_row)
            print("")
            n_row = n_row + 1

            
