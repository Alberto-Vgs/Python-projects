import math
import random 

class Player:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        return super().get_move(game)

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.aviable_moves())
        return square

class RealHumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\'s turn, input move (0-9)" )
            try:
                val = int(square)
                if val not in game.aviable_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print("Invalid square. try again.")
    
        return val