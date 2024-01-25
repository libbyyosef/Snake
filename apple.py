from game_parameters import *


class Apple:
    """this class represents a object of a apple"""
    def __init__(self):
        """initial method of the apple, initial its location and score"""
        x, y, score = get_random_apple_data()
        self.__location: tuple = x, y
        self.__score: int = score

    def set_score(self, score):
        """sets the score of the apple"""
        self.__score = score

    def get_score(self):
        """sets the score of the apple"""
        return self.__score

    def get_location(self):
        """function returns location of function"""
        return self.__location
