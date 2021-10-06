"""
The game package contains the classes for playing Hilo.
"""

import random

class PlayerClass():
    def __init__(self):
        self.score = 300 # The player starts the game with 300 points
        self.name = ""
        self.total_guesses = 0
        self.total_right = 0
        self.total_wrong = 0

        self.total_points_earned = 0
        self.total_points_lost = 0

    def right(self):
        self.score = self.score + 100
        self.total_points_earned = self.total_points_earned + 100

        self.total_guesses = self.total_guesses + 1
        self.total_right = self.total_right + 1

    def wrong(self):
        self.score = self.score - 75
        self.total_points_lost = self.total_points_lost + 75

        self.total_guesses = self.total_guesses + 1
        self.total_wrong = self.total_wrong + 1

    def print_score(self):
        print(self.score)

class CardPairClass():
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

    user_input_player_name = input("Hi, what's your name? ")

    # INITIAL SETUP

    # create an object Player of the class PlayerClass
    Player = PlayerClass()
    Player.name = user_input_player_name

    print(f"Hi {Player.name}")

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
        
        if Player.score >= 0:
            print(f"Your new score is {Player.score}")
        else:
            print(f"You are out of points: GAME OVER")
            Player.score = 0

        # ask player if they want to play again
        while True:
            keep_playing = input("Keep playing? [y/n] ")

            if keep_playing.lower() in ["y", "n"]:
                    break 
            else:
                print("Invalid response")
                continue
        
        if keep_playing == "y":
            continue
        else:
            break

    #dump statistics
    print(f"Thanks for playing, {Player.name}!")
    print()
    print("STATISTICS")
    print(f"You made a total of {Player.total_guesses} guesses.")
    print(f"You got {Player.total_right} guesses right ({Player.total_right/Player.total_guesses*100:.2f}%) and {Player.total_wrong} guesses wrong ({Player.total_wrong/Player.total_guesses*100:.2f}%).")
    print(f"You earned a total of {Player.total_points_earned} points and lost a total of {Player.total_points_lost}.")
    print(f"Your final score was: {Player.score}")

main()
