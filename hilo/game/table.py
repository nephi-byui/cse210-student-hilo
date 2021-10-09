# Tianna DeSpain 
# Nephi Malit
# Alan Crisanto
# Tatenda Felix Mukaro

import random 

class TableClass():
    """This class holds the deck of cards and shuffling deck for play
    Its responsibility is to store the list of cards for the game.
    Attributes:
        deck (LIST):        A list of the possible cards to be drawn
        first_card (INT):   A number between 1 and 13
        second_card (INT):  A number between 1 and 13
    """
    def __init__(self):
        """The class constructor.
        Args:
            self (TableClass): an instance of TableClass.
        """
        #self.deck = list()
        #self.deck = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ]
        #random.shuffle(self.deck)

    def shuffle(self):
        """This function restores the deck to its complete state
        Args:
            self (TableClass): an instance of TableClass.        
        """
        self.deck = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ]

    def draw_pair(self):
        """This function picks two numbers from the deck
        Args:
            self (TableClass): an instance of TableClass.        
        """
        
        # shuffle the deck before drawing
        self.shuffle()

        # get the first card
        self.first_card = random.choice(self.deck)
        self.deck.remove(self.first_card)

        # get the second card
        self.second_card = random.choice(self.deck)
        self.deck.remove(self.second_card)



# for testing
def main():

    # create a Table
    TestTableObject = TableClass()

    print("Drawing a card pair:")
    TestTableObject.draw_pair()
    print (f"The first card is: {TestTableObject.first_card}")
    print (f"The second card is: {TestTableObject.second_card}")

if __name__ == "__main__":
    main()