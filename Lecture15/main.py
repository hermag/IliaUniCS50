import random

def update_table(tictactoe_list, file_content, message):
    file_content = file_content%(player1,
                                 player2,
                                 tictactoe_list[0][0],
                                 tictactoe_list[0][1],
                                 tictactoe_list[0][2],
                                 tictactoe_list[1][0],
                                 tictactoe_list[1][1],
                                 tictactoe_list[1][2],
                                 tictactoe_list[2][0],
                                 tictactoe_list[2][1],
                                 tictactoe_list[2][2],
                                 message)
    f=open("index.html",'w')
    f.write(file_content)
    f.close()
    return 0

def cell_is_not_taken(tictactoe_table, x_coordinate, y_coordinate):
    if tictactoe_table[x_coordinate][y_coordinate]=='X' or tictactoe_table[x_coordinate][y_coordinate]=='O':
        return False
    elif tictactoe_table[x_coordinate][y_coordinate]==' * ':
        return True
    else:
        print("Whooops, not *, not X not O, what game you play?")
        exit()

def check_the_status(tictactoe_table, user_symbol, pc_symbol):
    for item_list in tictactoe_table:
        if (item_list[0]==item_list[1]==item_list[2]) and item_list[2]==user_symbol:
            return "User won",1
        elif (item_list[0]==item_list[1]==item_list[2]) and item_list[2]==pc_symbol:
            return "PC won",2
        else:
            pass
    for i in range(3):
        if (tictactoe_table[0][i]==tictactoe_table[1][i]==tictactoe_table[2][i]) and tictactoe_table[2][i]==user_symbol:
            return "User won",1
        elif (tictactoe_table[0][i]==tictactoe_table[1][i]==tictactoe_table[2][i]) and tictactoe_table[2][i]==pc_symbol:
            return "PC won",2
        else:
            pass
    if (tictactoe_table[0][0]==tictactoe_table[1][1]==tictactoe_table[2][2]) and tictactoe_table[2][2]==user_symbol:
        return "User won",1
    elif (tictactoe_table[0][0]==tictactoe_table[1][1]==tictactoe_table[2][2]) and tictactoe_table[2][2]==pc_symbol:
        return "PC won",2
    else:
        pass
    if (tictactoe_table[0][2]==tictactoe_table[1][1]==tictactoe_table[2][0]) and tictactoe_table[0][2]==user_symbol:
        return "User won",1
    elif (tictactoe_table[0][2]==tictactoe_table[1][1]==tictactoe_table[2][0]) and tictactoe_table[0][2]==pc_symbol:
        return "PC won",2
    else:
        pass
    return "Game Goes On",0

if __name__ == "__main__":
    file_content = """
                    <!DOCTYPE html>
                    <html>
                        <head>
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        </head>
                        <body>
                            Player 1: %s
                            <br>
                            Player 2: %s
                            <br>
                            <table border="1" align="center">
                            <tr>
                                <td width="100" align="center"> %s </td>
                                <td width="100" align="center"> %s </td>
                                <td width="100" align="center"> %s </td>
                            </tr>
                            <tr>
                                <td width="100" align="center"> %s </td>
                                <td width="100" align="center"> %s </td>
                                <td width="100" align="center"> %s </td>
                            </tr>
                            <tr>
                                <td width="100" align="center"> %s </td>
                                <td width="100" align="center"> %s </td>
                                <td width="100" align="center"> %s </td>
                            </tr>
                            </table>
                            <br>
                            The Winner is : %s
                        </body>
                    </html>
                """
    message = ""
    global player1 
    player1 = input("Welcome, you and I are going to play a tic tac toe Game :) Tell me your name")
    tictactoe_table=[[" * "," * "," * "],[" * "," * " ," * "],[" * "," * "," * "]]
    global player2 
    player2 = "PC"
    print("Check your table here: http://127.0.0.1:5500/iframes.html")
    file_content_to_dump = update_table(tictactoe_table, file_content, message)
    
    stop_game=0

    user_symbol=input("Which symbol you prefer, enter X or O")
    if user_symbol=='X':
        pc_symbol='O'
    elif user_symbol=='O':
        pc_symbol='X'
    else:
        print("You should have typed X or O, since you didn't I don't want to play with you, bye!")
        exit(2)

    while (stop_game==0):
        user_x, user_y = input("Please provide indices of the cell in the mesh, values should be between 0 and 2 inclusive").split()
        user_x = int(user_x)
        user_y = int(user_y)
        if (cell_is_not_taken(tictactoe_table, user_x,user_y)):
            tictactoe_table[user_x][user_y]=user_symbol
            update_table(tictactoe_table, file_content, message)
        else:
            exit()
        message, stop_game = check_the_status(tictactoe_table,user_symbol,pc_symbol)
        #Generating random numbers to simulate the computer player
        pc_x = random.randint(0,2)
        pc_y = random.randint(0,2)
        if (cell_is_not_taken(tictactoe_table,pc_x,pc_y)):
            tictactoe_table[pc_x][pc_y]=pc_symbol
            update_table(tictactoe_table, file_content, message)
        else:
            exit()
        message, stop_game = check_the_status(tictactoe_table, user_symbol, pc_symbol)

    #print(message)
    #print(tictactoe_table)
    update_table(tictactoe_table, file_content, message)
