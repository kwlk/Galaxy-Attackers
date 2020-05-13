import pygame

from Classes.Position import Position


# from here
class MobBullet:
    def __init__(self, mob_rect: pygame.rect, mob_bullet_type=1):
        self.position = Position(mob_rect.centerx, mob_rect.centery)
        self.speed = 1
        self.dmg = 1
        if mob_bullet_type == 1:
            self.speed = 1
            self.dmg = 10

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
        self.position.y += self.speed
# to here
# could be joined for both bullets? just change the move vector / bullet type
