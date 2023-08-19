from move import Move
import random

class Player:

    HUMAN_MARK = "X"
    COMP_MARK = "O"

    def __init__ (self,is_human = True):
        self._is_human = is_human

        if is_human:
            self._marker = Player.HUMAN_MARK

        else:
            self._marker = Player.COMP_MARK

    @property
    def marker(self):
        return self._marker

    @property
    def is_human(self):
        return self._is_human

    def get_move(self):
        if self.is_human:
            return self.get_human_move()
        else:
            return self.get_comp_move()

    def get_human_move(self):
        while True:
            user_inp = int(input("Enter a value between 1-9: "))
            move= Move(user_inp)
            if move.is_valid():
                break
            else:
                print("Please enter a valid number")
        return move

    def get_comp_move(self):
        comp_move_value = random.randint(1, 9)
        comp_move = Move(comp_move_value)
        print("Computer move is:", comp_move.value)
        return comp_move




