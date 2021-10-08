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