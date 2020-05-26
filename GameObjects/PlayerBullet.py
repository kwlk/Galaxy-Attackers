import pygame

from GameObjects.Position import Position


class PlayerBullet:

    def __init__(self, player_rect: pygame.rect, dmg, speed):
        self.position = Position(player_rect.centerx, player_rect.centery)
        self.dmg = dmg
        self.speed = speed

    def inside(self, rect: pygame.rect):
        if (self.position.x <= rect.left) or (self.position.x >= rect.left + rect.width) or (self.position.y <= rect.top) or (self.position.y >= rect.top + rect.height):
            return False
        return True

    def inside_map(self, mobs_rect: pygame.rect, player_rect):
        if (self.position.y <= mobs_rect.top) or (self.position.y >= player_rect.top + player_rect.height):
            return False
        return True

    def move(self):
        self.position.y -= round(self.speed)
