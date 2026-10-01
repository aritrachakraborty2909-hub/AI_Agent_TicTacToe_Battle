import copy

class TicTacToe:
    """Tic-Tac-Toe Game Engine."""
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        
    def display(self):
        """Displays board in human-readable terminal format."""
        print("\n  0   1   2")
        for i in range(3):
            row_str = f"{i} " + " | ".join(self.board[i])
            print(row_str)
            if i < 2:
                print("  " + "---+" * 2 + "---")
        print()

    def get_valid_moves(self):
        """Returns list of empty cells as (row, col) tuples."""
        moves = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == ' ':
                    moves.append((r, c))
        return moves

    def make_move(self, row, col, player):
        """Executes a move on the board."""
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def check_winner(self):
        """Checks for a winning player ('X' or 'O'). Returns None if no winner."""
        # Rows and Columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]

        # Diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def is_draw(self):
        """Checks if the game ended in a draw."""
        return len(self.get_valid_moves()) == 0 and self.check_winner() is None

    def is_terminal(self):
        """Checks if game is over (win or draw)."""
        return self.check_winner() is not None or self.is_draw()

    def clone(self):
        """Creates a deep copy of the game board."""
        new_game = TicTacToe()
        new_game.board = copy.deepcopy(self.board)
        return new_game