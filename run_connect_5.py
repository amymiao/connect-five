'''
AI Project: Connect 5

Rules:
The game board will be a square board of length n where n is greater than or equal to 5
User will always start

'''
from connect_5 import *
from alphaBeta import *
from evaluation import *
            
'''
play_game:
Parameters: game_board_size to construct the board and two functions that determine the player's move
Simulates playing the game between user vs. computer or computer vs. computer
If there's a user player, it must be player1
'''

def play_game(game_board_size, player1, player2):
    if game_board_size<5:
        print("Invalid board size.")
        return
    evaluate = Evaluate()        
    connect = Connect5(game_board_size)
    ss = SearchSpace(game_board_size)
    abtree1 = AlphaBetaTree(game_board_size, evaluate.get_heuristic_value_defense_max, connect.is_goal_state, True, 4, "NONE", ss)
    abtree2 = AlphaBetaTree(game_board_size, evaluate.get_heuristic_value_defense_max, connect.is_goal_state, False, 5, "CONCISE", ss)

    player2_move = None


    while True:
        connect.print_user_board()

        player1_move = player1(abtree1, player2_move)
        while not connect.is_valid_move(player1_move[0], player1_move[1]):
            print("Invalid move")
            player1_move = player1(abtree1, player2_move)
        last_move = connect.update_board(player1_move[0], player1_move[1], "player1")
        connect.print_board()

        if connect.is_goal_state((player1_move[0], player1_move[1]), connect.game_board):
            #if player1 != user_move:
            abtree1.complete_game()
            abtree2.complete_game()
            print("Player 1 won")
            return

        player2_move = player2(abtree2, player1_move)
        while not connect.is_valid_move(player2_move[0], player2_move[1]):
            print("Invalid move")
            player2_move = player2()
        last_move = connect.update_board(player2_move[0], player2_move[1], "player2")        
        connect.print_board()
        
        if connect.is_goal_state((player2_move[0], player2_move[1]), connect.game_board):
            abtree1.complete_game()
            abtree2.complete_game()
            print("Player 2 won")
            return


    
'''
user_move:
Provides the interface for the user to input a move with the console
If input is not in expected form, there will be an error.
If the input move is out of bounds or attempts to overwrite an existing move,
the user will be asked again to make a valid move
'''
def user_move(abtree, player_move):
    input_move = input("Enter the coordinates for your next move in the form (row, col): ")

    input_move = input_move.strip()
    move = input_move.split(",")      
            
    return ((int) (move[0]), (int) (move[1]))


def computer_move1(abtree, player_move):
    move_row, move_col = abtree.generate_next_move(player_move)
    print("computer move: " + str((move_row, move_col)))

    return (move_row, move_col)

def computer_move2(abtree, player_move):
    move_row, move_col = abtree.generate_next_move(player_move)
    print("computer move: " + str((move_row, move_col)))

    return (move_row, move_col)


play_game(10, user_move, computer_move1)
#play_game(10, computer_move1, computer_move2)

