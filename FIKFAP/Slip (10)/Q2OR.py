import math

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_winner(board, player):
    
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
        return True
    return False

def is_tie(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    if is_winner(board, 'X'):
        return -1
    if is_tie(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        
        user_row = int(input("Enter row (0, 1, 2): "))
        user_col = int(input("Enter col (0, 1, 2): "))
        if board[user_row][user_col] == ' ':
            board[user_row][user_col] = 'X'
        else:
            print("Cell is already occupied. Try again.")
            continue

        if is_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_tie(board):
            print("It's a tie!")
            break

        
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'O'
            print_board(board)

        if is_winner(board, 'O'):
            print("You lose! Better luck next time.")
            break
        if is_tie(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()