#Tianna DeSpain 
#Attempt at HiLo Game for W04 Team Project
#10/07/2021

import random 

class Table():
    """This class holds the deck of cards and shuffling deck for play
    It's responsibility is to store the list of cards for the game.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Table): an instance of Table.
        """
        self.deck = list()
        self.deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        random.shuffle(self.deck)