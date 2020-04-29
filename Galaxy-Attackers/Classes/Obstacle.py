from .Position import Position

class Obstacle:
    def __init__(self, position: Position, speed, end_of_map):
        self.speed = speed
        self.position = position
        self.end_of_map = end_of_map

    def collision(self, player, damage):
        player.take_damage(damage)
        self.position = Position(-1, -1)

    def getPosition(self):
        return self.position
    
    def move(self, y_vector):
        self.position.gety += y_vector