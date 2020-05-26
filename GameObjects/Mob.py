import pygame
from secrets import randbelow

from .Position import Position
from .MobBullet import MobBullet


def ez_pz(position: Position):
    img = pygame.transform.scale(pygame.image.load("ufo (1).png"), (46, 32))
    return Mob(1, img, img.get_rect(center=(position.x, position.y)), 0)


def sneaky_peaky(position: Position):
    img = pygame.transform.scale(pygame.image.load("ovni (1).png"), (23, 11))
    return Mob(1, img, img.get_rect(center=(position.x, position.y)), 0)


def the_wall(position: Position):
    img = pygame.transform.scale(pygame.image.load("strongUfo.png"), (64, 64))
    return Mob(10, img, img.get_rect(center=(position.x, position.y)), 0)


def rapid_fire(position: Position):
    img = pygame.transform.scale(pygame.image.load("space-ship (1).png"), (30, 32))
    return Mob(1, img, img.get_rect(center=(position.x, position.y)), 10)


def normie(position: Position):
    img = pygame.transform.scale(pygame.image.load("green-space-ship.png"), (32, 32))
    return Mob(1, img, img.get_rect(center=(position.x, position.y)), 4)


def big_chungus(position: Position):
    img = pygame.transform.scale(pygame.image.load("spaceship (1).png"), (64, 59))
    return Mob(5, img, img.get_rect(center=(position.x, position.y)), 7)


class Mob:

    def __init__(self,  hp, img, rect: pygame.rect, shoot_chance):
        self.hp = hp
        self.img = img
        self.rect = rect
        self.shoot_chance = shoot_chance

    def shoot(self):
        rand = randbelow(1001)
        if rand < self.shoot_chance:
            return MobBullet(self.rect)
        return None

    def receive_dmg(self, dmg):
        self.hp -= dmg

    def is_dead(self):
        return self.hp <= 0

    def move(self, x_vector):
        self.rect = self.rect.move(round(x_vector), 0)

    def down(self, y_vector):
        self.rect = self.rect.move(0, round(y_vector))

    @classmethod
    def endless_spawn(cls, difficulty, position: Position):
        i = randbelow(101)
        if i < difficulty:
            return big_chungus(position)
        if i < 2 * difficulty:
            return sneaky_peaky(position)
        if i < 3 * difficulty:
            return rapid_fire(position)
        if i < 4 * difficulty:
            return the_wall(position)
        if i < 5 * difficulty:
            return normie(position)
        return ez_pz(position)

    @classmethod
    def spawn(cls, difficulty, position: Position):
        if difficulty == 0:
            return ez_pz(position)
        if difficulty == 1:
            i = randbelow(101)
            if i < 10:
                return normie(position)
            return ez_pz(position)
        if difficulty == 2:
            i = randbelow(101)
            if i < 30:
                return normie(position)
            return ez_pz(position)
        if difficulty == 3:
            i = randbelow(101)
            if i < 20:
                return the_wall(position)
            if i < 40:
                return normie(position)
            return ez_pz(position)
        if difficulty == 4:
            i = randbelow(101)
            if i < 40:
                return sneaky_peaky(position)
            if i < 50:
                return normie(position)
            return ez_pz(position)
        if difficulty == 5:
            i = randbelow(101)
            if i < 20:
                return rapid_fire(position)
            return ez_pz(position)
        if difficulty == 6:
            i = randbelow(101)
            if i < 10:
                return rapid_fire(position)
            if i < 20:
                return sneaky_peaky(position)
            if i < 30:
                return the_wall(position)
            if i < 40:
                return normie(position)
            return ez_pz(position)
        if difficulty == 7:
            i = randbelow(101)
            if i < 20:
                return big_chungus(position)
            if i < 40:
                return normie(position)
            return ez_pz(position)
        if difficulty == 8:
            i = randbelow(101)
            if i < 50:
                return big_chungus(position)
            if i < 60:
                return normie(position)
            return ez_pz(position)
