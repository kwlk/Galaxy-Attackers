import pygame


class Mob:
    def __init__(self,  hp, bullet_type, img, rect: pygame.rect):
        self.hp = hp
        self.bullet_type = bullet_type
        self.img = img
        self.rect = rect

    def get_position(self):
        return self.position

    def is_dead(self):
        return self.hp <= 0

    def get_rect(self):
        return self.rect

    def move(self, x_vector):
        self.rect = self.rect.move(x_vector, 0)

    def down(self, y_vector):
        self.rect = self.rect.move(0, y_vector)
