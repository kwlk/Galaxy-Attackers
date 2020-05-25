import pygame

from .Position import Position


class Barrier:
    def __init__(self, position: Position, max_hp):
        self.position = position
        self.hp = max_hp
        self.img = pygame.transform.scale(pygame.image.load("wall.png"), (64, 16))
        self.rect = self.img.get_rect(center=(position.x, position.y))

    def receive_dmg(self, dmg):
        self.hp -= dmg
        self.img = pygame.transform.scale(pygame.image.load("brick-wall.png"), (64, 16))

    def is_dead(self):
        return self.hp <= 0
