from .Position import Position

class Obstacle:
    def __init__(self, position: Position, img):
        self.state = 0
        self.dmg = 1
        self.image = img
        self.rect = img.get_rect(center=(position.x, position.y))

    def get_state(self):
        return self.state

    def move(self, x_vector):
        self.rect = self.rect.move(-x_vector, 0)

    def change_dmg(self, new_damage):
        self.dmg = new_damage
