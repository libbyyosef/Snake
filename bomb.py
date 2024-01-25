from game_parameters import *


class Bomb:
    """this class represent an object of a Bomb"""
    def __init__(self):
        """a constructor of the bomb objet """
        x, y, radius, time = get_random_bomb_data()
        self.__time = time
        self.__radius = radius
        self.__location = x, y
        self.__temp_radius = 0

    def get_location(self):
        """returns the location of the bomb"""
        return self.__location

    def reduce_time(self):
        """reduces one time unit of the bomb time to explode """
        self.__time -= 1

    def get_time(self):
        """returns the time of the bomb to explode"""
        return self.__time

    def get_temp_radius(self):
        """returns the temp radius of the blast"""
        return self.__temp_radius

    def add_temp_radius(self):
        """enlarge the temp radius of the blast """
        self.__temp_radius += 1

    def get_radius(self):
        """returns the temp radius"""
        return self.__radius

    def shock_wave(self):
        """This function creates a list of tuple locations that represents the
        shock wave of the bomb
        input: radius of the original bomb and its
        originally location( before it disappear and relocate)
        output: list of tuple locations of the bomb or None if there isn't
        blast yet"""
        if self.__time > 0:
            # there isn't blast yet
            return None
        list_blast: list[tuple] = []
        location = self.__location
        if self.__temp_radius == 0:
            # the blast begins
            return [location]
        x = location[0]
        y = location[1]
        r = 0
        for i in range(x - self.__temp_radius, x + 1):
            # creating the blast from left to right till the center of the
            # blast include
            list_blast.append((i, y - r))
            if (i, y + r) in list_blast:
                r += 1
                continue
            else:
                list_blast.append((i, y + r))
                r += 1
        r = self.__temp_radius - 1
        for j in range(x + 1, x + self.__temp_radius + 1):
            # creating the blast from left to right from the center of the
            # blast not included till the end of it
            list_blast.append((j, y - r))
            if (j, y + r) in list_blast:
                r -= 1
                continue
            else:
                list_blast.append((j, y + r))
                r -= 1
        return list_blast

    def is_collide(self, coordinates):
        """checks if the location of the bomb is collided with coordinate of
        other object's coordinate"""
        if self.__location in coordinates:
            return True
        else:
            return False

