class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  
        self.current_player = 'X'  

    def print_board(self):
        print("\n")
        print("Current board:")
        for i in range(3):
            print(f"{self.board[i*3]} | {self.board[i*3 + 1]} | {self.board[i*3 + 2]}")
            if i < 2:
                print("--|---|--")
        print("\n")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)               
        ]
        
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        return None

    def is_draw(self):
        return ' ' not in self.board

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()
            try:
                move = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid move. Please enter a number between 1 and 9.")
                    continue
                if not self.make_move(move):
                    print("This position is already taken. Try again.")
                    continue
                
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    print(f"Player {winner} wins!")
                    break
                
                if self.is_draw():
                    self.print_board()
                    print("It's a draw!")
                    break
                
                self.switch_player()
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()