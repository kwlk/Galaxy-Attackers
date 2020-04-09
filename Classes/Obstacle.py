from .Map import Map
from .Position import Position

class Obstacle:
    def __init__(self, position: Position, speed, map: Map):
        self.speed = speed
        self.position = position
        self.map = map

    def collision(self, player, damage):
        player.take_damage(damage)
        self.map.deleteObstacle(self)

