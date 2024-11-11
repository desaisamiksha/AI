def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)
        
def check_winner(board, player):
    
    for row in board:
        if all([spot == player for spot in row]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    
    return False

def is_draw(board):
    return all([spot in ["X", "O"] for row in board for spot in row])

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        
        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
