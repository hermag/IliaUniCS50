# Initialize the board
board = [[-1, -1, -1],
         [-1, -1, -1],
         [-1, -1, -1]]

# Print the board function
def print_the_board(board):
    for row in board:
        print("  ".join(str(cell) if cell != -1 else '.' for cell in row))
    print()

# Check if there's a winner
def analyse_the_board(board):
    # Check rows and columns
    for i in range(3):
        if board[i].count('X') == 3 or [board[j][i] for j in range(3)].count('X') == 3:
            print("X won")
            return True
        if board[i].count('O') == 3 or [board[j][i] for j in range(3)].count('O') == 3:
            print("O won")
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
        print("X won")
        return True
    if board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        print("O won")
        return True
    
    return False

# Validate move
def validate_the_move(board, pos1, pos2):
    return 0 <= pos1 <= 2 and 0 <= pos2 <= 2 and board[pos1][pos2] == -1

# Exit the game if the rules are violated
def exit_the_game():
    print("Due to the violation of the game rules, the game stops\n")
    exit()

# Get player's figure and set the opponent's figure
player1_figure = input("Player 1, identify your figure (X or O): ").upper()
if player1_figure == 'X':
    player2_figure = 'O'
elif player1_figure == 'O':
    player2_figure = 'X'
else:
    exit_the_game()

# Main game loop
def player_turn(player_figure, opponent_figure):
    while True:
        try:
            pos1 = int(input(f"Player {player_figure}, enter the preferred position for {player_figure} in rows (0-2): "))
            pos2 = int(input(f"Player {player_figure}, enter the preferred position for {player_figure} in columns (0-2): "))
        except ValueError:
            print("Invalid input, please enter numbers between 0 and 2.")
            continue
        
        if validate_the_move(board, pos1, pos2):
            board[pos1][pos2] = player_figure
            print_the_board(board)
            if analyse_the_board(board):
                return True
            return False
        else:
            print("Invalid move. The cell is either occupied or out of bounds.")
            continue

# Game loop: alternate turns between players
while True:
    if player_turn(player1_figure, player2_figure):
        break
    if player_turn(player2_figure, player1_figure):
        break
