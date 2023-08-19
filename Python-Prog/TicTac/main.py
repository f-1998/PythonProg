from player import Player
from board import Board

class TicTac:

    def start(self):
        print("The Game Begins...\n")

        board = Board()
        player = Player()
        comp = Player(False)

        board.print_board_with_positions()
        while True:
            while True:
                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_tie():
                    print("It's a Tie")
                    break
                elif board.check_game_over(player, player_move):
                    print("Awesome...You Won the game")
                    break

                comp_move = comp.get_move()
                board.submit_move(comp, comp_move)
                board.print_board()

                if board.check_game_over(comp, comp_move):
                    print("You Lost the game")
                    break

            play_more = input("Enter Y to play again or N to discontinue: ").upper()
            if play_more == "N":
                print("Bye Bye. See you later Alligator")
                break
            elif play_more == "Y":
                self.play_again(board)
            else:
                print("I assume you want to continue the game")
                self.play_again(board)

    def play_again(self, board):
        print("Welcome to the new round")
        board.reset_board()
        board.print_board()
        self.start()  # Restart the game

game = TicTac()
game.start()
