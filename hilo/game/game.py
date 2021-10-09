# Tianna DeSpain 
# Nephi Malit
# Alan Crisanto
# Tatenda Felix Mukaro

from game.table import TableClass
from game.player import PlayerClass

class GameObject():
    """This class is responsible for starting the game and controlling the sequence of play.
     Attributes:
        keep_playing (STR): "y" or "n", breaks game loop if "n"
        Table (OBJECT):  An instance of the class TableClass.
        Player (OBJECT): An instance of the class PlayerClass
    Args:
        none
    """
    
    def __init__(self):
        """The class constructor.
        Args:
            self (GameObject): an instance of Game.
        """
        self.keep_playing = "y"

        # Create instances of TableClass and PlayerClass
        self.Table = TableClass()
        self.Player = PlayerClass()
        
    def game(self):
        """The main game loop.
        Keeps the game running until either:
            the player's score reaches zero or;
            the player decides to end the game (self.keep_playing == "n")
        Args:
            self (GameObject): an instance of Game.
        """
        user_input_player_name = input("Hi, what's your name? ")

        # create an object Player of the class PlayerClass
        self.Player.name = user_input_player_name

        # greet player
        print(f"Welcome to Hilo!, {self.Player.name}")

        while self.keep_playing == "y" and self.Player.score > 0:
            # begin game
            self.turn()
            # perform after-turn
            self.end_turn()
            print()
            continue

        # once self.keep_playing == "n"

        self.Player.dump_stats()
        print()
        print(f"Thanks for playing!")


        

        #while keep_playing == "y" and self.points > 0 and len(self.table.deck) > 0:
        #    keep_playing = self.turn()
        #    while keep_playing.lower() not in ["y","n"]:
        #        keep_playing = input("Not vaild imput. Do you want to keep playing? [y/n]")
        #if self.points <= 0:
        #    print("Try again next time!") 
        #else: 
        #    print(f"Game over! Good job! You got {self.points} total points!")



    def turn(self):
        """Starts the game loop to control sequence of play.
        Args:
            self (GameObject): an instance of GameObject.
        """
        # Draw a card pair to be used for this turn only
        self.Table.draw_pair()

        # Display the first card
        print(f"The card is: {self.Table.first_card}")

        # Take the player's guess
        while True:
            guess = input("Higher or Lower? [h/l] ")
            if guess.lower() not in ["h", "l"]:
                print("Invalid input.")
                continue
            else:
                break
        
        #  Display the second card
        print(f"The next card was: {self.Table.second_card}")

        if guess == "h":
            if self.Table.second_card > self.Table.first_card:
                self.Player.right_guess()
            else:
                self.Player.wrong_guess()

        elif guess == "l":
            if self.Table.second_card < self.Table.first_card:
                self.Player.right_guess()
            else:
                self.Player.wrong_guess()

    def end_turn(self):
        """Execute after a player takes a turn.
        Args:
            self (GameObject): an instance of GameObject.
        """
        # report new score
        # game over if score is less than or equal to zero 
        if self.Player.score > 0:
            print(f"Your new score is {self.Player.score}.")
        else:
            self.Player.score <= 0
            self.Player.score = 0
            print(f"Your new score is {self.Player.score}.")
            print(f"GAME OVER")

        # while player score is greater than 0    
        # keep asking player if they want to play again
        while self.Player.score > 0:
            self.keep_playing = input("Keep playing? [y/n] ")
            self.keep_playing = self.keep_playing.lower()

            if self.keep_playing in ["y", "n"]:
                break
            else:
                print("Invalid input.")
                continue
    
    #def end_game(self):
    #    self.dump_stats()
    #    print()
    #    print("Thanks for playing!")


        #result = self.compare_cards(self.current_card, self.next_card, guess)
        #self.scoringturn(result)
        #print(f"Next card was: {self.next_card}")
        #print(f"Your score is: {self.points}")
        #if len(self.table.deck) > 0 and self.points > 0 :
        #    return input("Keep playing? [y/n]")
        #else:
        #    return "n"

    #def scoringturn(self, result):
    #    """Calculates the points per the scoring method. 
    #    
    #    Args:
    #        self (Game): an instance of Game.
    #        result (Game): whether or not the player was correct.
    #    """
    #    if result == "correct":
    #        self.points += 100
    #    elif result == "incorrect":
    #        self.points -= 75

    #def compare_cards(self, current, next, guess):
    #    """Decideds whether or not the players guess is correct.
    #    
    #    Args:
    #        self (Game): an instance of Game.
    #        current (Game): the last card used.
    #        next (Game): the next card to be played.
    #        guess (Game): the players guess whether the next card 
    #            is higher or lower.
    #        
    #    """
    #    if guess == "l":
    #        if current > next: 
    #            print("Great Job!")
    #            return "correct"
    #        else: 
    #            print("Good try.")
    #            return "incorrect"
    #    elif guess == "h":
    #        if next > current:
    #            print("Great Job!")
    #            return "correct"
    #        else:
    #            print("Good try.")
    #            return "incorrect"
    #    else:
    #        print("incorrect input")
        


    