import random




    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        """
    Function that randomly select a player to begin the game
        """

        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def has_player_won(self, player):
        """
    Function that shows wich player has won the game
    """

        n = len(self.board)
        board_values = set()

        # Checking Rows

        for i in range(n):
            for j in range(n):
                board_values.add(self.board[i][j])

            if board_values == {player}:
                return True
            else:
                board_values.clear()

        # Checking Cols

            for i in range(n):
            for j in range(n):
                board_values.add(self.board[j][i])

            if board_values == {player}:
                return True
            else:
                board_values.clear()

        # Checking Diagonals

        for i in range(n):
            board_values.add(self.board[i][i])
        if board_values == {player}:
            return True
        else:
            board_values.clear()

        board_values.add(self.board[0][2])
        board_values.add(self.board[1][1])
        board_values.add(self.board[2][0])
        if board_values == {player}:
            return True
        else:
            return False

    # Functions

      def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()

    def start(self):
        self.create_board()
        player = 'X' if self.get_random_first_player() == 1 else 'O'
        game_over = False

        while not game_over:
            try:
                self.show_board()
                print(f'\nPlayer {player} turn')

                row, col = list(
                    map(int, input(
                        'Enter row & column numbers to fix spot: ').split()))
                print()

                if col is None:
                    raise ValueError(
                        'not enough values to unpack (expected 2, got 1)')

                self.fix_spot(row - 1, col - 1, player)

               
               
               
               #Game Over
               
                game_over = self.has_player_won(player)
                if game_over:
                    print(f'Player {player} is the winner!')
                    continue

                game_over = self.is_board_filled()
                if game_over:
                    print('Game Over!')
                    continue

                player = self.swap_player_turn(player)

            except ValueError as err:
                print(err)

        print()
        self.show_board()


if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()
