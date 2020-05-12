from .Position import Position


class Barrier:
    def __init__(self, position: Position, max_hp, rect):
        self.position = position
        self.hp = max_hp
        self.rect = rect

    def receive_dmg(self, dmg):
        self.hp -= dmg

    def is_dead(self):
        return self.hp <= 0

    def get_rect(self):
        return self.rect
