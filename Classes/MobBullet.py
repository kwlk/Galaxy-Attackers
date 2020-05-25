import pygame

from Classes.Position import Position


class MobBullet:
    def __init__(self, mob_rect: pygame.rect):
        self.position = Position(mob_rect.centerx, mob_rect.centery)
        self.speed = 1
        self.dmg = 1

    def inside(self, rect: pygame.rect):
        if (self.position.x <= rect.left) or (self.position.x >= rect.left + rect.width) or (
                self.position.y <= rect.top) or (self.position.y >= rect.top + rect.height):
            return False
        return True

    def inside_map(self, mobs_rect: pygame.rect, player_rect):
        if (self.position.y <= mobs_rect.top) or (self.position.y >= player_rect.top + player_rect.height):
            return False
        return True

    def move(self):
        self.position.y += round(self.speed)
