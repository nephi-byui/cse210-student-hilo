import random

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