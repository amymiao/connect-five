from copy import copy
from time import clock

class SearchSpace:
    def __init__(self, board_size):
        self.search_space = [[0] * board_size for i in range(board_size)]

    def create_search_space_around(self, move, size):
        j = move[1] - 2
        while j<move[1]+3:
            if j<0 or j>=size:
                continue
            i = move[0] + 1
            while i>0:
                i = i - 1
                if i<move[0]-2:
                    break
                if self.search_space[i][j] == 0:
                    self.search_space[i][j] = 1

            i = move[0]
            while i<size-1:
                i = i + 1
                if i>move[0]+2:
                    break
                if self.search_space[i][j] == 0:
                    self.search_space[i][j] = 1
            j = j + 1

    def eliminate_search_space(self, previous_move):
        self.search_space[previous_move[0]][previous_move[1]] = -1

class AlphaBetaNode:
    max_value = 0
    min_value = 1
    empty_value = -1
   

    def __init__(self, board_state, alpha, beta, action, min_node = False, depth = float("inf"), value = None):
        self.alpha = alpha
        self.beta = beta
        self.min_node = min_node
        self.depth = depth
        self.action = action
        self.next_node = None

        self.board_state = board_state

        if value == None:
            self.terminal_node = False
        else:
            self.terminal_node = True

        self.value = value

    def board_value_representations(self, player, opponent, empty):
        AlphaBetaNode.max_value = player
        AlphaBetaNode.min_value = opponent
        AlphaBetaNode.empty_value = empty

    def generate_descendant_states(self, goal, heur, search_space):
        descendants = list()
        for i, row in enumerate(self.board_state):
            for j, col in enumerate(row):
                if search_space[i][j] == 1:
                    temp_bs = copy(self.board_state)
                    temp_bs[i] = copy(self.board_state[i])
                    if temp_bs[i][j] == AlphaBetaNode.empty_value:
                        if self.min_node:
                            temp_bs[i][j] = AlphaBetaNode.min_value
                            player_str = "user"
                        else:
                            temp_bs[i][j] = AlphaBetaNode.max_value
                            player_str = "computer"

                        if goal((i, j), temp_bs) or self.depth == 1:
                            term_value = heur(temp_bs)
                        else:
                            term_value = None

                        desc = AlphaBetaNode(temp_bs, self.alpha, self.beta, (i, j), not self.min_node, self.depth - 1, term_value)
                        descendants.append(desc)

        return descendants

class AlphaBetaTree(object):

    def __init__(self, board_size, heuristic_func, goal_state_func, min_node = False, max_depth=float("inf"), search_space = None):
        board_state = [[-1] * board_size for i in range(board_size)]
        self.root_node = AlphaBetaNode(board_state, -1 * float("inf"), float("inf"), "start", min_node, depth=max_depth)
        self.heuristic_func = heuristic_func
        self.goal_state_func = goal_state_func
        self.expanded_nodes = 0
        self.pruned_nodes = 0
        self.running_sum = 0
        self.generated_vals = 0
        self.search_space = search_space

    def alphaBetaPruning(self, node):
        self.expanded_nodes += 1

        if node.value != None:
            return node.value

        descendants = node.generate_descendant_states(self.goal_state_func, self.heuristic_func, self.search_space.search_space)

        if node.min_node:
            i = 0
            for descendant in descendants:
                i += 1
                descendant.alpha = node.alpha
                descendant.beta = node.beta
                temp_val = self.alphaBetaPruning(descendant)

                if node.beta > temp_val:
                    node.next_node = descendant

                node.beta = min(node.beta, temp_val)

                if node.beta <= node.alpha:
                    self.pruned_nodes += len(descendants) - i
                    break

            return node.beta
        else:
            i = 0
            for descendant in descendants:
                i += 1
                descendant.alpha = node.alpha
                descendant.beta = node.beta
                temp_val = self.alphaBetaPruning(descendant)

                if node.alpha < temp_val:
                    node.next_node = descendant

                node.alpha = max(node.alpha, temp_val)

                if node.beta <= node.alpha:
                    self.pruned_nodes += len(descendants) - i
                    break

            return node.alpha

    def first_move(self, node, board_size):
        i = (int) (board_size/2)
        temp_bs = copy(node.board_state)
        temp_bs[i] = copy(node.board_state[i])
        if temp_bs[i][i] == AlphaBetaNode.empty_value:
            if node.min_node:
                temp_bs[i][i] = AlphaBetaNode.min_value
                player_str = "user"
            else:
                temp_bs[i][i] = AlphaBetaNode.max_value
                player_str = "computer"

            desc = AlphaBetaNode(temp_bs, node.alpha, node.beta, (i,i), not node.min_node, 0, None)
            return desc
        else:
            return None
        
    def generate_next_move(self, previous_move = None):

        self.generated_vals += 1
        if self.root_node.min_node:
            piece_value = AlphaBetaNode.max_value
        else:
            piece_value = AlphaBetaNode.min_value

        if previous_move != None:
            self.search_space.eliminate_search_space(previous_move)
            self.search_space.create_search_space_around(previous_move, len(self.root_node.board_state))

            self.root_node.board_state[previous_move[0]][previous_move[1]] = piece_value
            elapsed_time = clock()
            self.alphaBetaPruning(self.root_node)
            elapsed_time = clock() - elapsed_time

            
        else:    
            elapsed_time = clock()
            desc = self.first_move(self.root_node, len(self.root_node.board_state))
            if desc == None:
                self.alphaBetaPruning(self.root_node)
            else:
                self.root_node.next_node = desc
            elapsed_time = clock() - elapsed_time

            
        self.running_sum += elapsed_time


        self.root_node = AlphaBetaNode(self.root_node.next_node.board_state, -1*float("inf"), float("inf"), \
                                       self.root_node.next_node.action, self.root_node.min_node, self.root_node.depth)

        return self.root_node.action

    def complete_game(self):
        print("Number of nodes pruned: " + str(self.pruned_nodes) + "\n")
        print("Number of nodes expanded: " + str(self.expanded_nodes) + "\n")

        if (self.generated_vals != 0):
            print("Average time to move: " + str(self.running_sum/self.generated_vals) + "s\n")
