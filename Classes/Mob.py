import pygame
from secrets import randbelow

from .Position import Position
from .MobBullet import MobBullet


def ez_pz(position: Position):
    img = pygame.transform.scale(pygame.image.load("broom.png"), (32, 32))
    return Mob(1, 0, img, img.get_rect(center=(position.x, position.y)), 0)


def sneaky_peaky(position: Position):
    img = pygame.transform.scale(pygame.image.load("broom.png"), (16, 16))
    return Mob(1, 0, img, img.get_rect(center=(position.x, position.y)), 0)


def the_wall(position: Position):
    img = pygame.transform.scale(pygame.image.load("broom.png"), (64, 64))
    return Mob(10, 0, img, img.get_rect(center=(position.x, position.y)), 0)


def rapid_fire(position: Position):
    img = pygame.transform.scale(pygame.image.load("broom.png"), (32, 32))
    return Mob(1, 1, img, img.get_rect(center=(position.x, position.y)), 10)


def normie(position: Position):
    img = pygame.transform.scale(pygame.image.load("broom.png"), (32, 32))
    return Mob(1, 1, img, img.get_rect(center=(position.x, position.y)), 4)


def big_chungus(position: Position):
    img = pygame.transform.scale(pygame.image.load("broom.png"), (64, 64))
    return Mob(5, 1, img, img.get_rect(center=(position.x, position.y)), 2)


class Mob:

    def __init__(self,  hp, bullet_dmg, img, rect: pygame.rect, shoot_chance):
        self.hp = hp
        self.bullet_dmg = bullet_dmg
        self.img = img
        self.rect = rect
        self.shoot_chance = shoot_chance

    def shoot(self):
        rand = randbelow(1001)
        if rand < self.shoot_chance:
            return MobBullet(self.rect, self.bullet_dmg)
        return None

    def receive_dmg(self, dmg):
        self.hp -= dmg

    def is_dead(self):
        return self.hp <= 0

    def move(self, x_vector):
        self.rect = self.rect.move(x_vector, 0)

    def down(self, y_vector):
        self.rect = self.rect.move(0, y_vector)

    @classmethod
    def spawn(cls, difficulty, position: Position):
        if difficulty == 0:
            return ez_pz(position)
        if difficulty == 1:
            i = randbelow(101)
            if i < 30:
                return normie(position)
            return ez_pz(position)
        if difficulty == 2:
            i = randbelow(101)
            if i < 10:
                return sneaky_peaky(position)
            if i < 15:
                return rapid_fire(position)
            if i < 25:
                return the_wall(position)
            if i < 50:
                return normie(position)
            return ez_pz(position)
        if difficulty == 3:
            i = randbelow(101)
            if i < 10:
                return big_chungus(position)
            if i < 20:
                return sneaky_peaky(position)
            if i < 30:
                return rapid_fire(position)
            if i < 35:
                return the_wall(position)
            if i < 70:
                return normie(position)
            return ez_pz(position)
