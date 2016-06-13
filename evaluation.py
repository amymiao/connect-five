'''
Evaluation Function for alpha beta pruning

'''
import random
from connect_5 import *

class Evaluate():

    def __init__(self):
        self.separator = 4
        self.defense_separator = 12
        self.evaluations = {}
        self.evaluations_defense = {}

    def create_key(self, game_board):
        key = ()
        for x in game_board:
            key = key + (tuple(x))
        
    def evaluation_function(self, game_board):
        evaluation = [[],[]]

        for r_num in range(len(game_board)):
            i = 0
            while i < len(game_board):
                val = game_board[r_num][i]
                
                if val != -1:
                    new_val = val
                    j = i
                    while new_val == val:
                        j = j + 1
                        if j >= len(game_board):
                            break
                        new_val = game_board[r_num][j]
                    evaluation[val].append(j-i)
                    i = j - 1
                i = i + 1

        for c_num in range(len(game_board)):
            i = 0
            while i < len(game_board):
                val = game_board[i][c_num]
                
                if val != -1:
                    new_val = val
                    j = i
                    while new_val == val:
                        j = j + 1
                        if j >= len(game_board):
                            break
                        new_val = game_board[j][c_num]
                    evaluation[val].append(j-i)
                    i = j - 1
                i = i + 1            

        i = 4
        while i<len(game_board):
            m = i
            n = 0
            while m>=0 and n<len(game_board):
                val = game_board[m][n]
                if val != -1:
                    new_val = val
                    k = m
                    l = n
                    x = 0
                    while new_val == val:
                        k = k - 1
                        l = l + 1
                        x = x + 1
                        if k<0 or l>=len(game_board):
                            break
                        new_val = game_board[k][l]
                        
                    m = k + 1
                    n = l - 1
                    evaluation[val].append(x)
                    
                m = m - 1
                n = n + 1
                
            i = i + 1

        j = 1
        while j<len(game_board)-4:
            m = len(game_board)-1
            n = j
            while m>=0 and n<len(game_board):
                val = game_board[m][n]
                if val != -1:
                    new_val = val
                    k = m
                    l = n
                    x = 0
                    while new_val == val:
                        k = k - 1
                        l = l + 1
                        x = x + 1
                        if k<0 or l>=len(game_board):
                            break
                        new_val = game_board[k][l]
                        
                    m = k + 1
                    n = l - 1
                    evaluation[val].append(x)
                    
                m = m - 1
                n = n + 1
                
            j = j + 1

        i = 0
        j = 0
        while i<len(game_board)-4:
            m = i
            n = j
            while m<len(game_board) and j<len(game_board):
                val = game_board[m][n]
                if val != -1:
                    new_val = val
                    k = m
                    l = n
                    x = 0
                    while new_val == val:
                        k = k + 1
                        l = l + 1
                        x = x + 1
                        if k>=len(game_board) or l>=len(game_board):
                            break
                        new_val = game_board[k][l]
                        
                    m = k - 1
                    n = l - 1
                    evaluation[val].append(x)
                    
                m = m + 1
                n = n + 1
                
            i = i + 1
            
        i = 0
        j = 1
        while j<len(game_board)-4:
            m = i
            n = j
            while m<len(game_board) and n<len(game_board):
                val = game_board[m][n]
                if val != -1:
                    new_val = val
                    k = m
                    l = n
                    x = 0
                    while new_val == val:
                        k = k + 1
                        l = l + 1
                        x = x + 1
                        if k>=len(game_board) or l>=len(game_board):
                            break
                        new_val = game_board[k][l]
                        
                    m = k - 1
                    n = l - 1
                    evaluation[val].append(x)
                    
                m = m + 1
                n = n + 1
                
            j = j + 1
        return evaluation

    def get_random_heuristic_value(self, game_board):
        return random.randint(-1000, 1000)


    def get_heuristic_value_max(self, game_board):
        key = self.create_key(game_board)
        if key in self.evaluations:
            return self.evaluations[key][0] - self.evaluations[key][1]
        
        max_value = 0
        min_value = 0
        
        evaluation_list = self.evaluation_function(game_board)
        for e in evaluation_list[0]:
            max_value = max_value + self.separator**e
        for e in evaluation_list[1]:
            min_value = min_value + self.separator**e

        self.evaluations[key] = (max_value, min_value)

        return max_value - min_value

    
    def get_heuristic_value_min(self, game_board):
        key = self.create_key(game_board)
        if key in self.evaluations:
            return self.evaluations[key][1] - self.evaluations[key][0]
        
        max_value = 0
        min_value = 0

        evaluation_list = self.evaluation_function(game_board)
        
        for e in evaluation_list[0]:
            max_value = max_value + self.separator**e
        for e in evaluation_list[1]:
            min_value = min_value + self.separator**e
    
        self.evaluations[key] = (max_value, min_value)

        return min_value - max_value


    def get_heuristic_value_defense_max(self, game_board):
        key = self.create_key(game_board)
        if key in self.evaluations:
            return self.evaluations[key][0] - self.evaluations[key][1]
        
        max_value = 0
        min_value = 0
        
        evaluation_list = self.evaluation_function(game_board)
        for e in evaluation_list[0]:
            max_value = max_value + self.separator**e
        for e in evaluation_list[1]:
            min_value = min_value + self.defense_separator**e

        self.evaluations_defense[key] = (max_value, min_value)

        return max_value - min_value

    
    def get_heuristic_value_defense_min(self, game_board):
        key = self.create_key(game_board)
        if key in self.evaluations:
            return self.evaluations[key][1] - self.evaluations[key][0]
        
        max_value = 0
        min_value = 0

        evaluation_list = self.evaluation_function(game_board)
        
        for e in evaluation_list[0]:
            max_value = max_value + self.defense_separator**e
        for e in evaluation_list[1]:
            min_value = min_value + self.separator**e
    
        self.evaluations_defense[key] = (max_value, min_value)

        return min_value - max_value
    

    def set_separator(self, value):
        self.separator = value

    def set_defense_separator(self, value):
        self.defense_separator = value




        
