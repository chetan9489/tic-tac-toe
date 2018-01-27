"""
Created on Fri Jan 26 20:31:23 2018

@author: Chetan Chauhan
"""

board=[" "," "," "," "," "," "," "," "," "]

def display_board(board):
    print("    |    |")
    print(" "+str(board[0])+ "  | "+str(board[1])+"  | "+str(board[2]))
    print("    |    |")
    print("-------------")
    
    print("    |    |")
    print(" "+str(board[3])+ "  | "+str(board[4])+"  | "+str(board[5]))
    print("    |    |")
    print("-------------")
    
    print("    |    |")
    print(" "+str(board[6])+ "  | "+str(board[7])+"  | "+str(board[8]))
    print("    |    |")
    
#print_grid()
    
def player_input():
    
    x = "" 
    while not (x=="X" or x=="O" or x=="x" or x=="o"):
        print("Player 1: Do you want to be X or O?")
        x=input()
    
    if(x=="X" or x=="x"):
        return "X","O"
    
    else:
        return "O","X"
    

def place_marker(board, marker, position):
    board[position] = marker
    
def win_check(board,mark):
    if(board[0] == mark and board[1] == mark and board[2] == mark):
        return 1
    elif(board[0] == mark and board[3] == mark and board[6] == mark):
        return 1
    elif(board[0] == mark and board[4] == mark and board[8] == mark):
        return 1
    elif(board[1] == mark and board[4] == mark and board[7] == mark):
        return 1
    elif(board[3] == mark and board[4] == mark and board[5] == mark):
        return 1
    elif(board[2] == mark and board[5] == mark and board[8] == mark):
        return 1
    elif(board[6] == mark and board[7] == mark and board[8] == mark):
        return 1
    elif(board[2] == mark and board[4] == mark and board[6] == mark):
        return 1
    else:
        return 0
    
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
def space_check(board, position):
    return board[position]==" "
    
def full_board_check(board):
    flag = True
    for x in board:
        if x==" ":
            flag = False
            break
    return flag
    

def player_choice(board):
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)-1):
        
        position = input('Choose your next position: (1-9) ')
    return int(position)

def replay():
    return input("Do you want to play again (yes/no) : ").lower().startswith('y') 


"""
display_board(board)   
print(win_check(board,"O"))
print(space_check(board,0))
print(player_choice(board))
print(replay())

while True:
    print("Welcome to TIC-TAC-TOE game!!!!")
    
    ## PLAYER INPUT
    players = player_input()
    
    print("Let's Play!!!!")
    display_board(board)
    print(choose_first()+" will make the first move!!!!")
    position = player_choice(board)
    place_marker(board,players[0],position)
    while not win_check(board,position):
        display_board(board)
    
    break
    
"""

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position-1)

            if win_check(board, player1_marker):
                display_board(board)
                print('Player 1 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position-1)

            if win_check(board, player2_marker):
                display_board(board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break