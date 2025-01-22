board = [
    [-1,-1,-1],
    [-1,-1,-1],
    [-1,-1,-1]
]
players_symbols={}

def print_board(board):
    for row in board:
        for item in row:
            print(item,"   ",end="")
        print()

def symbol_validation(sym):
    if sym!='X' and sym!='O':
        print("თამაშის სიმბოლო უნდა იყოს X ან O, რადგან არც ერთი არ აგირჩევიათ თამაში დასრულდა")
        exit()
    else:
        pass

def board_update(board,pos1,pos2,sym):
    if 0<=pos1<=2 and 0<=pos2<=2 and board[pos1][pos2]==-1:
        board[pos1][pos2]=sym
        return board
    else:
        print("ან არასწორი კოორდინატები შეიტანეთ ან ადგილი უკვე დაკავებულია, თამაში დასრულებულია")
        exit()

def check_board(board):
    for row in board:
        if row.count('X')==3 or row.count('O')==3:
            return True,row[0]
        else:
            pass
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i] and (board[i][0]=='X' or board[i][0]=='O'):
            return True,board[i][0]
        else:
            pass
    if board[0][0]==board[1][1]==board[2][2] and (board[0][0]=='X' or board[0][0]=='O'):
        return True,board[0][0]
    elif board[0][2]==board[1][1]==board[2][0] and (board[0][2]=='X' or board[0][2]=='O'):
        return True,board[0][2]
    else:
        return False,''
    return False,''
player1_symbol=str(input("გთხოვთ აირჩიოთ პირველი მოთამაშის სიმბოლო X ან O"))
if player1_symbol=='X':
    #player2_symbol='O'
    players_symbols['X']='player 1'
    players_symbols['O']='player 2'
elif player1_symbol=='O':
    #player2_symbol='X'
    players_symbols['X']='player 2'
    players_symbols['O']='player 1'    
else:
    symbol_validation(player1_symbol)

while not check_board(board)[0]:
    print("პირველი სვლა უნდა გააკეთოს მოთამაშემ ვისაც აქვს არჩეული X")
    print("შემოიტანეთ X-ის კოორდინატები")
    pos1 = int(input("შემოიტანეთ X-ის ჰორიზონტალური პოზიცია"))
    pos2 = int(input("შემოიტანეთ X-ის ვერტიკალური პოზიცია"))
    board=board_update(board,pos1,pos2,'X')
    print_board(board)
    if check_board(board)[0]:
        break
    else:
        pass
    print("შემოიტანეთ O-ს კოორდინატები")
    pos1 = int(input("შემოიტანეთ O-ის ჰორიზონტალური პოზიცია"))
    pos2 = int(input("შემოიტანეთ O-ის ვერტიკალური პოზიცია"))
    board=board_update(board,pos1,pos2,'O')
    print_board(board)
    if check_board(board)[0]:
        break
    else:
        pass
