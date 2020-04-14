from .Map import Map
from .Position import Position


class Player:
    def __init__(self, map: Map, speed_vector: Position, max_hp, damage, position: Position, bullet_type=0):
        self.map = map
        self.speed_vector = speed_vector
        self.damage = damage
        self.hp = max_hp
        self.bullet_type = bullet_type
        self.position = position

    def shoot(self):
        return self.bullet_type

    def move(self):
        self.position = self.position.move(self.speed_vector)

    def take_damage(self, damage):
        self.hp -= damage

    def get_position(self):
        return self.getPosition
