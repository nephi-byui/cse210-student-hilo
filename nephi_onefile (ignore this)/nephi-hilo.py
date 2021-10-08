"""
CSE 210
Team 02
Hilo (Nephi's Attempt)
"""

import random

class PlayerClass():
    """This class is used to create an object where the player's score and statistics are stored."""
    def __init__(self,user_input_name):
        self.score = 300 # The player starts the game with 300 points
        self.name = user_input_name
        self.total_guesses = 0
        self.total_right = 0
        self.total_wrong = 0

        self.total_points_earned = 0
        self.total_points_lost = 0

    def right(self):
        """Run this function when a player makes a correct guess."""
        self.score = self.score + 100
        self.total_points_earned = self.total_points_earned + 100

        self.total_guesses = self.total_guesses + 1
        self.total_right = self.total_right + 1

    def wrong(self):
        """Run this function when a player makes an incorrect guess."""
        self.score = self.score - 75
        self.total_points_lost = self.total_points_lost + 75

        self.total_guesses = self.total_guesses + 1
        self.total_wrong = self.total_wrong + 1

    def dump_stats(self):
        """Displays various player statistics"""
        print("="*64)
        print(f"Statistics for {self.name}")
        print("-"*64)
        if self.total_guesses == 1: #singular
            print(f"You made a total of {self.total_guesses} guess.")
        else: #plural
            print(f"You made a total of {self.total_guesses} guesses.")
        print(f"Correct guesses: {self.total_right} ({self.total_right/self.total_guesses*100:.2f}%)")
        print(f"Incorrect guesses: {self.total_wrong} ({self.total_wrong/self.total_guesses*100:.2f}%).")
        print(f"You earned a total of {self.total_points_earned} points and lost a total of {self.total_points_lost} points.")
        print(f"You achieved a final score of: {self.score}.")
        print("="*64)
        

class CardPairClass():
    """This class is used to create card pair objects"""
    def __init__(self):

        possible_values = [1,2,3,4,5,6,7,8,9,10,11,12,13]

        # get the first card
        first_number = random.choice(possible_values)
        possible_values.remove(first_number)

        # get the second card
        second_number = random.choice(possible_values)

        self.first = first_number
        self.second = second_number

def main():
    
    print("Welcome to Hilo!")
    user_input_player_name = input("Hi, what's your name? ")

    # INITIAL SETUP

    # create an object Player of the class PlayerClass
    Player = PlayerClass(user_input_player_name)

    print(f"Hi {Player.name}")
    print(f"Let's play!")
    print()
    

    # Game Loop
    while True:

        # create an object Cards of the class CardPairClass
        Cards = CardPairClass()
        print(f"The card is: {Cards.first}")

        # ask the user to guess
        # take only valid responses, else loop
        while True:
            guess = input("Higher or lower? [h/l]: ")
            
            if guess.lower() in ["h", "l"]:
                break 
            else:
                print("Invalid response")
                continue
        
        # reveal second card
        print(f"The next card was: {Cards.second}")

        if guess == "h":
            if Cards.second > Cards.first:
                Player.right()
            else:
                Player.wrong()
        

        elif guess == "l":
            if Cards.second < Cards.first:
                Player.right()
            else:
                Player.wrong()
        
        if Player.score > 0:
            print(f"Your new score is {Player.score}.")
        else:
            Player.score = 0
            print(f"Your new score is {Player.score}.")
            print(f"GAME OVER")

        # while player score is greater than 0    
        # keep asking player if they want to play again
        while Player.score > 0:
            keep_playing = input("Keep playing? [y/n] ")

            if keep_playing.lower() in ["y", "n"]:
                print() #blank line
                break 
            else:
                print("Invalid response")
                continue
        
        if keep_playing == "y":
            continue
        else:
            break
    
    # dump statistics
    Player.dump_stats()
    print()
    print(f"Thanks for playing!")

if __name__ == "__main__":
    main()