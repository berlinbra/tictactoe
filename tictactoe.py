class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def make_move(self, position):
        if self.is_valid_move(position):
            self.board[position - 1] = self.current_player
            if not self.check_winner():
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def is_valid_move(self, position):
        return 1 <= position <= 9 and self.board[position - 1] == ' '

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return True

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return True

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return True
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return True

        return False

    def is_board_full(self):
        return ' ' not in self.board

    def display_board(self):
        for i in range(0, 9, 3):
            print(f' {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ')
            if i < 6:
                print('-----------')

def main():
    game = TicTacToe()
    print('Welcome to Tic-tac-toe!')
    print('Positions are numbered 1-9, left to right, top to bottom.')

    while True:
        game.display_board()
        try:
            position = int(input(f'Player {game.current_player}, enter your move (1-9): '))
            if game.make_move(position):
                if game.check_winner():
                    game.display_board()
                    print(f'Player {game.current_player} wins!')
                    break
                elif game.is_board_full():
                    game.display_board()
                    print('Game is a draw!')
                    break
            else:
                print('Invalid move. Try again.')
        except ValueError:
            print('Please enter a number between 1 and 9.')

if __name__ == '__main__':
    main()