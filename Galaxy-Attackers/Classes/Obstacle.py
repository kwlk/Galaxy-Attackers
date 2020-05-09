from .Position import Position
from .Player import Player


class Obstacle:
    def __init__(self, position: Position, img):
        self.position = position
        self.state = 0
        self.damage = 1
        self.image = img
        self.rect = img.get_rect(center=(position.getx(), position.gety()))

    def get_state(self):
        return self.state

    def get_position(self):
        return self.position

    def move(self, x_vector):
        self.position.setx(self.position.gety()-x_vector)
        self.rect = self.rect.move(-x_vector, 0)

    def get_dmg(self):
        return self.damage

    def change_dmg(self, new_damage):
        self.damage = new_damage

    def get_img(self):
        return self.image

    def get_rect(self):
        return self.rect
