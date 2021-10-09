#Tianna DeSpain 
#Attempt at HiLo Game for W04 Team Project
#10/07/2021
from game.table import Table
import random 

class Game():
    """This class holds the table and the running score. 
    The resposi ility of this class of objects is to keep track of 
    the score and control the sequence of play
    
     Attributes: 
        points (number): The total number of points earned.
        next_card (number): An instance of the object known as Table.
        next_card (string): A placeholder for use in the turn function.
        table (Table): An instance of the class of objects known as Table.
    """
    
    
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Game): an instance of Game.
        """
        #creating and shuffling deck for play
        self.table = Table()
        self.points = 300
        self.next_card = self.table.deck.pop()
        self.current_card = ""

    def turn(self): 
        """Starts the game loop to control sequence of play.
        
        Args:
            self (Game): an instance of Game.
        """
        self.current_card = self.next_card
        self.next_card = self.table.deck.pop()
        print(f"The card is: {self.current_card}")
        guess = input("Higher or Lower? [h/l]")
        result = self.compare_cards(self.current_card, self.next_card, guess)
        self.scoringturn(result)
        print(f"Next card was: {self.next_card}")
        print(f"Your score is: {self.points}")
        if len(self.table.deck) > 0 and self.points > 0 :
            return input("Keep playing? [y/n]")
        else:
            return "n"

    def scoringturn(self, result):
        """Calculates the points per the scoring method. 
        
        Args:
            self (Game): an instance of Game.
            result (Game): whether or not the player was correct.
        """
        if result == "correct":
            self.points += 100
        elif result == "incorrect":
            self.points -= 75

    def compare_cards(self, current, next, guess):
        """Decideds whether or not the players guess is correct.
        
        Args:
            self (Game): an instance of Game.
            current (Game): the last card used.
            next (Game): the next card to be played.
            guess (Game): the players guess whether the next card 
                is higher or lower.
            
        """
        if guess == "l":
            if current > next: 
                print("Great Job!")
                return "correct"
            else: 
                print("Good try.")
                return "incorrect"
        elif guess == "h":
            if next > current:
                print("Great Job!")
                return "correct"
            else:
                print("Good try.")
                return "incorrect"
        else:
            print("incorrect input")
        
    def game(self):
        """keeps the game playing until the points run out, they 
        decide to quit or they finish all 13 cards.
        
        Args:
            self (Game): an instance of Game.
        """
        keep_playing = "y"
        while keep_playing == "y" and self.points > 0 and len(self.table.deck) > 0:
            keep_playing = self.turn()
            while keep_playing not in ["y","n"]:
                keep_playing = input("Not vaild imput. Do you want to keep playing? [y/n]")
        if self.points <= 0:
            print("Try again next time!") 
        else: 
            print(f"Game over! Good job! You got {self.points} total points!")

    