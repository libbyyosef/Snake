from apple import *
from snake import *
from bomb import *
from game_parameters import *
from game_display import *


class Board:
    """this class represent an object of a board"""

    def __init__(self, gd):
        """a constructor of a Board object"""
        self.__game_display = gd
        new_board = [[[(i, j)] for j in range(HEIGHT)] for i in range(WIDTH)]
        self.__board = new_board
        self.__snake = Snake()
        self.__bomb = Bomb()
        while self.__bomb.is_collide(self.__snake.get_snake_coordinates()):
            # checks that the new bomb location doesn't collide with the snakes
            # coordinates anf if it does, relocate it
            self.__bomb = Bomb()
        self.__apples: list[Apple] = []

    def draw_board(self):
        """this function colors the draw cells of all the objects"""
        for coor in (self.__snake.get_snake_coordinates()):
            # colors snake in black
            x, y = coor
            self.__game_display.draw_cell(x, y, "black")
        for apple in self.__apples:
            # colors the apples in green
            x, y = apple.get_location()
            self.__game_display.draw_cell(x, y, "green")
        blasts = self.__bomb.shock_wave()
        if not blasts:
            # colors the bomb in red, while there is no blast
            x, y = self.__bomb.get_location()
            self.__game_display.draw_cell(x, y, "red")
        if blasts:
            # colors the blast in orange
            for blast in blasts:
                x, y = blast
                self.__game_display.draw_cell(x, y, "orange")

    def get_snake(self):
        """returns the snake"""
        return self.__snake

    def snake_eats_apple(self):
        """check if the snake eats the apple, if not return false, and if it
        does, remove the eaten apple from the apples' list and return the score
        of the apple"""
        for apple in self.__apples:
            if self.__snake.get_head() == apple.get_location():
                # snake eats apple
                self.__apples.remove(apple)
                return apple.get_score()
        return False

    def can_place_apple(self, apple):
        """check if a new apple is located in an empty cell(returns true),
        if not, creates a new one that does(returns false)"""
        if apple.get_location() in self.__snake.get_snake_coordinates():
            # check if the new apple located in one of the snake's coordinates
            return False
        elif self.__bomb.is_collide([apple.get_location]):
            # check if the new apple located in the bomb location
            return False
        for apl in self.__apples:
            # check if the new apple located in one of the other apples'
            # coordinates
            if apple.get_location() == apl.get_location():
                return False
        return True

    def add_apple(self, apple):
        """adds a new apple to the apples list"""
        self.__apples.append(apple)

    def get_bomb(self):
        """returns the bomb"""
        return self.__bomb

    def snake_out_of_board(self):
        """check if the snake is out of board, returns true if it does,
        otherwise returns false"""
        w, h = self.__snake.get_head()
        if (w >= WIDTH) or w < 0 or (h >= HEIGHT) or h < 0:
            return True
        return False

    def can_add_bomb(self, bomb):
        """check if a new bomb is located in an empty cell(returns true),
             if not, creates a new one that does(returns false)"""
        if bomb.get_location() in self.__snake.get_snake_coordinates():
            # check if the new bomb located in one of the snake's coordinates
            return False
        else:
            for apple in self.__apples:
                if bomb.is_collide([apple.get_location]):
                    # check if the new bomb is located in one of the other
                    # apples' coordinates
                    return False
        x, y = bomb.get_location()
        if (x < 0) or (x >= WIDTH) or (y < 0) or (y >= HEIGHT):
            # checks if new bomb is in the board
            return False
        return True

    def number_of_apples(self):
        """returns the number of apples"""
        return len(self.__apples)

    def snake_hits_bomb(self):
        """returns true if the snake hits the bomb, false otherwise"""
        return self.__bomb.is_collide([self.__snake.get_head()])

    def snake_hits_blast(self):
        """returns true if the snake hits the blast,it there is one,
        false otherwise"""
        if self.__bomb.shock_wave():
            # if the blast exist check if the snake hits it
            for blast in self.__bomb.shock_wave():
                if blast in self.__snake.get_snake_coordinates():
                    return True
            return False

    def blast_crashed_apple(self):
        """check if the blast crashed apple, if it does return the crashed
        apple, false otherwise"""
        if self.__bomb.shock_wave():
            # if there is a blast check if it crashed an apple
            for apple in self.__apples:
                for blast in self.__bomb.shock_wave():
                    if apple.get_location() == blast:
                        return apple
        return False

    def is_full_board(self):
        """checks if the board is full-for locating a new apple"""
        new_list = [self.__bomb.get_location()]
        # appends all the objects coordinates to a list, if it is the size of
        # the board, there is no empty cells for location an apple
        # append bomb coordinates to the list
        for cor in self.__snake.get_snake_coordinates():
            # append snakes coordinates to the list
            new_list.append(cor)
        for apple in self.__apples:
            # append apples coordinates to the list
            new_list.append(apple.get_location())
        if self.__bomb.shock_wave():
            # append blast coordinates to the list
            for b in self.__bomb.shock_wave():
                new_list.append(b)
        if len(new_list) == HEIGHT * WIDTH:
            return True
        else:
            return False

    def set_bomb(self):
        """sets a new bomb"""
        bomb = Bomb()
        while not self.can_add_bomb(bomb):
            # if the new bomb cannot be added to the board, creates a new bomb
            # that can
            bomb = Bomb()
        self.__bomb = bomb

    def blast_out_board(self):
        """if there is a blast check if it is out of the board, if it is
        returns true, false otherwise"""
        if self.__bomb.shock_wave():
            for blast in self.__bomb.shock_wave():
                x, y = blast
                if (x < 0) or (x >= WIDTH) or (y < 0) or (y >= HEIGHT):
                    return True
        return False

    def remove_apple(self, apple):
        """remove an apple from the apples list"""
        self.__apples.remove(apple)
