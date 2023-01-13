"""
# ----- Fist way to import the package -----
# import utils submodule
import text_analyzer.utils

# print a description of the package
print(help(text_analyzer))

# Decide to start seeing other people
text_analyzer.utils.we_need_to_talk(break_up=True)

# ----- Second way of import a package -----
from text_analyzer import utils

utils.we_need_to_talk(break_up=True)

# ----- third way of import a package -----
from text_analyzer.utils import we_need_to_talk

we_need_to_talk(break_up=True)

# Import local package
import text_analyzer

# Sum word_counts using sum_counters from text_analyzer
word_count_totals = ____.____(word_counts)

# Plot word_count_totals using plot_counter from text_analyzer
____.____(word_count_totals)
"""
# Write the class Point as outlined in the instructions
from datetime import datetime
from math import sqrt


class Point:
    def __init__(self, x=0., y=0.):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x
        return self.__x

    def set_y(self, y):
        self.__y = y
        return self.__y

    def distance_to_origin(self):
        return sqrt(self.__x * self.__x + self.__y * self.__y)

    def reflect(self, axis):
        if axis == "x":
            self.__y = -self.__y
            return self.__y
        if axis == "y":
            self.__x = -self.__x
            return self.__x


# Create a Player class
class Player:
    MAX_POSITION = 10

    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
            self.position = self.position + steps
            return self.position
        else:
            self.position = Player.MAX_POSITION
            return self.position

    # This method provides a rudimentary visualization in the console
    def draw(self):
        drawing = "-" * self.position + "|" + "-" * (Player.MAX_POSITION - self.position)
        print(drawing)


class BetterDate:
    # Constructor
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)

    @classmethod
    def from_datetime(cls, date):
        year, month, day = date.year, date.month, date.day
        return cls(year, month, day)


if __name__ == '__main__':
    pt = Point(x=3.0)
    pt.reflect("y")
    print('Point:', (pt.x, pt.y))
    print(pt.distance_to_origin())

    pt.set_y(4.0)
    print('New y:', pt.y)
    print(pt.distance_to_origin())

    # -------
    p1 = Player()
    p1.draw()
    p1.move(4)
    p1.draw()
    p1.move(5)
    p1.draw()
    p1.move(3)
    p1.draw()

    bd = BetterDate.from_str('2020-04-30')
    print(bd.year)
    print(bd.month)
    print(bd.day)

    bd2 = BetterDate.from_datetime(datetime.now())
    print(bd2.year)
    print(bd2.month)
    print(bd2.day)



