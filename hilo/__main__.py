from game.player_class import PlayerClass
from game.card_pair_class import CardPairClass

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