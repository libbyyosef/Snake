class Node:
    def __init__(self, data=None, next1=None):
        self.__data = data
        self.__next = next1

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_next(self, next1):
        self.__next = next1


class Snake:
    """this class represents a object of snake"""
    def __init__(self):
        """a constructor for a snake object"""
        self.__direction = 'Up'
        self.__tail = Node((10, 8), Node((10, 9), Node((10, 10))))
        self.__head = self.__tail.get_next().get_next()
        self.__size = 3
        self.__last_apple = 0

    def __str__(self):
        curr = self.__tail
        to_print = ''
        while curr is not None:
            to_print += (str(curr.get_data()) + ' ')
            curr = curr.get_next()
        return to_print

    def set_direction(self, direction):
        """function sets snake direction to direction"""
        if self.__direction == 'Up' or self.__direction == 'Down':
            if direction == 'Right' or direction == 'Left':
                self.__direction = direction
        if self.__direction == 'Right' or self.__direction == 'Left':
            if direction == 'Up' or direction == 'Down':
                self.__direction = direction

    def add_space(self, new_head):
        """function adds to head of snake new_head node, and adds 1 to size
        of snake"""
        self.__head.set_next(Node(new_head))
        self.__head = self.__head.get_next()
        self.__head.set_next(None)
        self.__size += 1

    def add_space_in_direction(self):
        """function adds a link to the head of the snake according to snake
        direction"""
        col, row = self.__head.get_data()
        if self.__direction == 'Up':
            self.add_space((col, row + 1))
        elif self.__direction == 'Down':
            self.add_space((col, row - 1))
        elif self.__direction == 'Right':
            self.add_space((col + 1, row))
        elif self.__direction == 'Left':
            self.add_space((col - 1, row))

    def remove_space(self):
        """function removes the tail of the snake, and removes 1 from
        snake size"""
        self.__tail = self.__tail.get_next()
        self.__size -= 1

    def remove_head(self):
        curr = self.__tail
        while curr.get_next() is not self.__head:
            curr = curr.get_next()
        self.__head = curr

    def move_snake(self):
        """function moves snake one step in snake direction"""
        self.add_space_in_direction()
        self.remove_space()

    def get_head(self):
        """function returns coordinate head of snake is in"""
        return self.__head.get_data()

    def get_coordinates_beside_for_head(self):
        """function returns a list of coordinates of snake besides for head """
        coordinates = []
        curr = self.__tail
        while curr is not self.__head:
            coordinates.append(curr.get_data())
            curr = curr.get_next()
        return coordinates[:]

    def get_snake_coordinates(self):
        """function returns list of coordinates of snake"""
        coordinates = self.get_coordinates_beside_for_head()
        coordinates.append(self.get_head())
        return coordinates

    def snake_eats_himself(self):
        """function returns true if snake hits himself, false otherwise"""
        if self.get_head() in self.get_coordinates_beside_for_head():
            return True
        else:
            return False

    def eat_apple(self):
        """function checks if snake ate apple and needs to grow in one space,
        and if true adds a space and removes one from spaces needed to be
        added"""
        if self.__last_apple > 0:
            self.add_space_in_direction()
            self.__last_apple -= 1
            return True

    def add_last_apple(self):
        """function adds 3 to last apple, so snake grows in one space in the
        next 3 rounds"""
        self.__last_apple += 3
