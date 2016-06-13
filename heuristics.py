


    '''
    Very simple admissible heuristic: each move is an action
    Therefore every blank space on board is a possible action
    Calculate heuristic for each action

    STORE HEURISTICS IN A TABLE: ONLY UPDATE WHEN A MOVE IS PLACED IN A 5 BY 5 BOX
    '''
    def attack_heuristic(self, move):
        row = move[0]
        col = move[1]
        value = 0
        not_value = 1
        
        hval1 = self.search_heuristic_horizontal(row, col, value, not_value)
        print(hval1)

        hval2 = self.search_heuristic_vertical(row, col, value, not_value)
        print(hval2)
        
        hval3 = self.search_heuristic_diagonal_right(row, col, value, not_value)
        print(hval3)

        hval4 = self.search_heuristic_diagonal_left(row, col, value, not_value)
        print(hval4)
        
        return min(hval1, hval2, hval3, hval4)
        
        
    def block_heuristic(self):
        print("here")


    def search_heuristic_horizontal(self, row, col, value, not_value):
        if not self.is_valid(row):
            return -1 #invalid
        #MAKE SURE board is not occupied         
        i = col + 1
        counter_right = 0
        blank_counter = 0
        capacity = 0
        
        while i < col+5:
            if not self.is_valid(i):
                break
            
            board_val = self.game_board[row][i]
            if board_val == not_value:
                break
            if board_val == value:
                counter_right = counter_right + 1
            if board_val == -1:
                blank_counter = blank_counter + 1
            i = i + 1
            
        if (5 - counter_right) <= 1:
            return 0
        
        i = col - 1
        counter_left = 0

        while i > col-5:
            if not self.is_valid(i):
                break
            
            board_val = self.game_board[row][i]
            if board_val == not_value:
                break
            if board_val == value:
                counter_left = counter_left + 1
            if board_val == -1:
                blank_counter = blank_counter + 1
            i = i - 1         


        if (5 - counter_left) <= 1:
            return 0

        if (5 - counter_left - counter_right) <= 1: #not sure
            return 0

        capacity = blank_counter + counter_right + counter_left

        if capacity < 4:
            return 10000 #really big number
        
        return (5 - counter_left - counter_right)
    


    def search_heuristic_vertical(self, row, col, value, not_value):
        if not self.is_valid(col):
            return -1 #invalid
        #MAKE SURE board is not occupied         
        i = row + 1
        counter_right = 0
        blank_counter = 0
        capacity = 0
        
        while i < row+5:
            if not self.is_valid(i):
                break
            
            board_val = self.game_board[i][col]
            if board_val == not_value:
                break
            if board_val == value:
                counter_right = counter_right + 1
            if board_val == -1:
                blank_counter = blank_counter + 1
            i = i + 1
            
        if (5 - counter_right) <= 1:
            return 0
        
        i = row - 1
        counter_left = 0

        while i > row-5:
            if not self.is_valid(i):
                break
            
            board_val = self.game_board[i][col]
            if board_val == not_value:
                break
            if board_val == value:
                counter_left = counter_left + 1
            if board_val == -1:
                blank_counter = blank_counter + 1
            i = i - 1         


        if (5 - counter_left) <= 1:
            return 0

        if (5 - counter_left - counter_right) <= 1: #not sure
            return 0

        capacity = blank_counter + counter_right + counter_left

        if capacity < 4:
            return 10000 #really big number
        
        return (5 - counter_left - counter_right)


    
    def search_heuristic_diagonal_right(self, row, col, value, not_value):
        #MAKE SURE board is not occupied         
        i = row + 1
        j = col + 1
        counter_right = 0
        blank_counter = 0
        capacity = 0
        
        while i < row+5 and j< col+5:
            if not self.is_valid(i) or not self.is_valid(j):
                break
            
            board_val = self.game_board[i][j]
            if board_val == not_value:
                break
            if board_val == value:
                counter_right = counter_right + 1
            if board_val == -1:
                blank_counter = blank_counter + 1
            i = i + 1
            j = j + 1
            
        if (5 - counter_right) <= 1:
            return 0
        
        i = row - 1
        j = col - 1
        counter_left = 0

        while i > row-5 and j> col-5:
            if not self.is_valid(i) or not self.is_valid(j):
                break
            
            board_val = self.game_board[i][j]
            if board_val == not_value:
                break
            if board_val == value:
                counter_left = counter_left + 1
            if board_val == -1:
                blank_counter = blank_counter + 1
            i = i - 1         
            j = j - 1

        if (5 - counter_left) <= 1:
            return 0

        if (5 - counter_left - counter_right) <= 1: #not sure
            return 0

        capacity = blank_counter + counter_right + counter_left

        if capacity < 4:
            return 10000 #really big number
        
        return (5 - counter_left - counter_right)
    




    def search_heuristic_diagonal_left(self, row, col, value, not_value):
        #MAKE SURE board is not occupied         
        i = row + 1
        j = col - 1
        counter_right = 0
        blank_counter = 0
        capacity = 0
        
        while i < row+5 and j> col-5:
            if not self.is_valid(i) or not self.is_valid(j):
                break
            
            board_val = self.game_board[i][j]
            if board_val == not_value:
                break
            if board_val == value:
                counter_right = counter_right + 1
            if board_val == -1:
                blank_counter = blank_counter + 1
            i = i + 1
            j = j - 1
            
        if (5 - counter_right) <= 1:
            return 0
        
        i = row - 1
        j = col + 1
        counter_left = 0

        while i > row-5 and j < col+5:
            if not self.is_valid(i) or not self.is_valid(j):
                break
            
            board_val = self.game_board[i][j]
            if board_val == not_value:
                break
            if board_val == value:
                counter_left = counter_left + 1
            if board_val == -1:
                blank_counter = blank_counter + 1
            i = i - 1         
            j = j + 1

        if (5 - counter_left) <= 1:
            return 0

        if (5 - counter_left - counter_right) <= 1: #not sure
            return 0

        capacity = blank_counter + counter_right + counter_left

        if capacity < 4:
            return 10000 #really big number
        
        return (5 - counter_left - counter_right)
