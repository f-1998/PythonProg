class Board:

    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [[0, 0, 0], [0, 0, 0],  [0, 0, 0]]

    def print_board(self):
        print("Board")
        for row in self.game_board:
            print("|", end="")
            for col in row:
                if col == Board.EMPTY_CELL:
                    print(" |", end="")
                else:
                    print(f" {col} |", end="")
            print()
        print()

    def submit_move(self, player, move):
        row = move.get_row()
        col = move.get_column()
        val = self.game_board[row][col]

        if val == Board.EMPTY_CELL:
            self.game_board[row][col] = player.marker
        else:
            print("Please Try again.")

    def check_game_over(self, player, last_move):
        return (self.check_row(player, last_move) or
                self.check_column(player, last_move) or
                self.check_dia(player) or
                self.check_antidia(player))


    def check_row(self, player, last_move):
        row_ind = last_move.get_row()
        board_row = self.game_board[row_ind]

        return board_row.count(player.marker) == 3

    def check_column(self, player, last_move):
        markers_count = 0
        col_ind = last_move.get_column()

        for i in range(3):
            if self.game_board[i][col_ind] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_dia(self, player):
        markers_count = 0

        for i in range(3):
            if self.game_board[i][i] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_antidia(self, player):

        markers_count = 0
        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                markers_count += 1

        return markers_count == 3

    def check_tie(self):
        empty_counter = 0

        for row in self.game_board:
            empty_counter += row.count(Board.EMPTY_CELL)

        return empty_counter == 0

    def reset_board(self):
        self.game_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def print_board_with_positions(self):
        print("POSITIONS")
        print("| 1 | | 2 | | 3 |\n| 4 | | 5 | | 6 |\n| 7 | | 8 | | 9 |")