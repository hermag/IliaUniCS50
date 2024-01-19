import random

def check_table_cell(table,  x_coordinate, y_coordinate):
    if table[x_coordinate][y_coordinate]==" ":
        return "free"
    else:
        return "taken"
    
def update_table(table, x_coordinate, y_coordinate, symbol):
    table[x_coordinate][y_coordinate]=symbol
    return table

def print_table(table):
    print("| %s | %s | %s |"%(table[0][0],table[0][1],table[0][2]))
    print("| %s | %s | %s |"%(table[1][0],table[1][1],table[1][2]))
    print("| %s | %s | %s |"%(table[2][0],table[2][1],table[2][2]))

def check_winner(tictactoe_table, user_symbol, pc_symbol):
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


if __name__=="__main__":
    print("მოგესალმებით, დღეს ჩვენ ვითამაშებთ tic, tac, toe-ს")
    human_symbol=input("აირჩიეთ სიმბოლო, X ან O")
    if human_symbol=="X":
        player_1=input("გვითხარით თქვენი სახელი")
        player_2="PC"
    elif human_symbol=="O":
        player_1="PC"
        player_2=input("გვითხარით თქვენი სახელი")
    else:
        print(f"არ გდომებია შენ ძმაო თამაში, კარგად იყავი")
        exit(2)
    table = [[" "," "," "],[" "," "," "],[" "," "," "]]
    continue_game="yes"
    while(continue_game=="yes"):
        if player_1=="PC":
            pc_x = random.randint(0,2)
            pc_y = random.randint(0,2)
            while (check_table_cell(pc_x,pc_y)=="taken"):
                pc_x = random.randint(0,2)
                pc_y = random.randint(0,2)
            table=update_table(table,pc_x,pc_y,"X")
            print("%s-ს სვლა"%player_1)
            print_table(table)    
            print("--------------------------")
            user_x, user_y = input("შემოიტანეთ უჯრის ორი ხარვეზით გამოყოფილი კოორდინატი, 0,1 ან 2 ").split()
            user_x = int(user_x)
            user_y = int(user_y)
            while (check_table_cell(table,user_x,user_y)=="taken"):
                user_x, user_y = input("უჯრა დაკავებულია, შემოიტანეთ სხვა კოორდინატი").split()
                user_x = int(user_x)
                user_y = int(user_y)
            table=update_table(table, user_x, user_y,"O")
            print("%s-ს სვლა"%player_2)
            print_table(table)
            print("--------------------------")
            message, exit_code = check_winner(table, "O", "X")
            if exit_code!=0:
                print(message)
                continue_game=input("თუ გსურთ თამაშის გაგრძელება აკრიფეთ yes")
                table=[[" "," "," "],[" "," "," "],[" "," "," "]]
        else:
            user_x, user_y = input("შემოიტანეთ უჯრის ორი ხარვეზით გამოყოფილი კოორდინატი, 0,1 ან 2 ").split()
            user_x = int(user_x)
            user_y = int(user_y)
            while (check_table_cell(table, user_x, user_y)=="taken"):
                user_x, user_y = input("უჯრა დაკავებულია, შემოიტანეთ სხვა კოორდინატი").split()
                user_x = int(user_x)
                user_y = int(user_y)
            table=update_table(table, user_x, user_y,"X")
            print("%s-ს სვლა"%player_1)
            print_table(table)
            print("--------------------------")
            pc_x = random.randint(0,2)
            pc_y = random.randint(0,2)
            while (check_table_cell(table, pc_x, pc_y)=="taken"):
                pc_x = random.randint(0,2)
                pc_y = random.randint(0,2)
            table=update_table(table,pc_x,pc_y,"O")
            print("%s-ს სვლა"%player_2)
            print_table(table)
            print("--------------------------")
            message, exit_code = check_winner(table, "X", "O")
            if exit_code!=0:
                print(message)
                continue_game=input("თუ გსურთ თამაშის გაგრძელება აკრიფეთ yes")
                table=[[" "," "," "],[" "," "," "],[" "," "," "]]