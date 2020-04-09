from math import sqrt


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def move_x(self, x):
        self.x += x

    def move_y(self, y):
        self.y += y

    def distance(self, other_position):
        return sqrt((self.x-other_position.x)**2+(self.y-other_position.y)**2)

