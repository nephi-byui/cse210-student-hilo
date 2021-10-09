# Tianna DeSpain 
# Nephi Malit
# Alan Crisanto
# Tatenda Felix Mukaro

class PlayerClass():
    """This class is used to create an Player object,
    where the player's score and statistics are stored.
    Attributes:
        score:                  (INT) The Player's running score
        name:                   (STR) The Player's name
        total_guesses:          (INT) The number of guesses made this session
        total_right:            (INT) The number of correct guesses
        total_wrong:            (INT) The number of incorrect guesses
        total_points_earned:    (INT) The gross total number of points earned from correct answers
        total_points_lost:      (INT) The gross total number of points lost from incorrect answers 
    """
    def __init__(self):
        """The class constructor.
        Args:
            self (PlayerClass): an instance of PlayerClass.
        """
        self.score = 300 # The player starts the game with 300 points
        self.name = "Player"
        self.total_guesses = 0
        self.total_right = 0
        self.total_wrong = 0

        self.total_points_earned = 0
        self.total_points_lost = 0

    def right_guess(self):
        """Run this function when a player makes a correct guess.
        Args:
            self (PlayerClass): an instance of PlayerClass.
        """
        self.total_guesses = self.total_guesses + 1
        self.total_right = self.total_right + 1

        self.score = self.score + 100
        self.total_points_earned = self.total_points_earned + 100
        print("You guessed correctly. Good job! (+100 points)")

    def wrong_guess(self):
        """Run this function when a player makes an incorrect guess.
        Args:
            self (PlayerClass): an instance of PlayerClass.
        """
        self.total_guesses = self.total_guesses + 1
        self.total_wrong = self.total_wrong + 1

        if self.score > 75:
            self.score = self.score - 75
            self.total_points_lost = self.total_points_lost + 75
            print("You guessed wrong. Nice try though. (-75 points)")

        elif self.score <= 75:
            score_left = self.score

            self.score = self.score - score_left
            self.total_points_lost = self.total_points_lost + score_left
            print(f"You guessed wrong. You lose the last of your points! (-{score_left} points!")

    def dump_stats(self):
        """Displays various player statistics.
        Args:
            self (PlayerClass): an instance of PlayerClass.
        """
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