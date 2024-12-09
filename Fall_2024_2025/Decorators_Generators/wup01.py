board = [[-1,-1,-1],
         [-1,-1,-1],
         [-1,-1,-1]]

def print_the_board(board):
    for row_item in board[:]:
        for column_item in row_item:
            print(str(column_item)+"  ",end="")
        print()

def analyse_the_board(board):
    if board[0].count('X')==3 or board[1].count('X')==3 or board[2].count('X')==3:
        print("X won")
        return True
    if board[:][0].count('X')==3 or board[:][1].count('X')==3 or board[:][2].count('X')==3:
        print("X won")
        return True
    if board[0][0]==board[1][1]==board[2][2]=='X':
        print("X won")
        return True
    if board[0][2]==board[1][1]==board[2][0]=='X':
        print("X won")
        return True
    #------------------------------------------------------------------------------------------       
    if board[0].count('O')==3 or board[1].count('O')==3 or board[2].count('O')==3:
        print("O won")
        return True
    if board[:][0].count('O')==3 or board[:][1].count('O')==3 or board[:][2].count('O')==3:
        print("O won")
        return True
    if board[0][0]==board[1][1]==board[2][2]=='O':
        print("O won")
        return True
    if board[0][2]==board[1][1]==board[2][0]=='O':
        print("O won")
        return True    

def validate_the_move(board,pos1, pos2):
    if pos1>=0 and pos1<=2 and pos2>=0 and pos2<=2:
        if board[pos1][pos2]==-1:
            return True
    else:
        return False


def exit_the_game():
    print("Due to the violation of the game rules, game stops\n")
    exit()

player1_figure=input("Player 1, identify your figure, it should X or O\n")
if player1_figure=='X':
    player2_figure='O'
elif player1_figure=='O':
    player2_figure='X'
else:
    exit_the_game()

while not analyse_the_board(board):
    if player1_figure=='X':
        pos1 = int(input("Player 1 please enter the prefered position of X in rows"))
        pos2 = int(input("Player 1 please enter the prefered position of X in columns"))
        if validate_the_move(board,pos1, pos2):
            board[pos1][pos2]='X'
            print_the_board(board)
            if analyse_the_board(board):
                break
        else:
            exit_the_game()
        pos1 = int(input("Player 2 please enter the prefered position of O in rows"))
        pos2 = int(input("Player 2 please enter the prefered position of O in columns"))
        if validate_the_move(board, pos1, pos2):
            board[pos1][pos2]='O'
            print_the_board(board)
            if analyse_the_board(board):
                break
        else:
            exit_the_game()
    else:
        pos1 = int(input("Player 2 please enter the prefered position of X in rows"))
        pos2 = int(input("Player 2 please enter the prefered position of X in columns"))
        if validate_the_move(board,pos1, pos2):
            board[pos1][pos2]='X'
            print_the_board(board)
            if analyse_the_board(board):
                break
        else:
            exit_the_game()
        pos1 = int(input("Player 1 please enter the prefered position of O in rows"))
        pos2 = int(input("Player 1 please enter the prefered position of O in columns"))
        if validate_the_move(board,pos1, pos2):
            board[pos1][pos2]='O'
            print_the_board(board)
            if analyse_the_board(board):
                break
        else:
            exit_the_game()
