import pygame
from Classes.Position import Position
from secrets import randbelow
from enum import Enum

GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
NEARBLACK = (19, 15, 48)
COMBLUE = (233, 232, 255)


class Type(Enum):
    fast_up_player = 1
    slow_down_player = 2
    fast_up_mob = 3
    slow_down_mob = 4
    fast_up_obstacle = 5
    slow_down_obstacle = 6


class PowerUp:
    def __init__(self, position: Position, timestamp, color, type: Type):
        self.position = position
        self.timestamp = timestamp
        self.image = pygame.Surface((16, 16))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(position.x, position.y))
        self.type = type

    def inside(self, rect: pygame.rect):
        return self.rect.colliderect(rect)


    @classmethod
    def spawn(cls, position: Position, timestamp):
        p = randbelow(100)
        if p < 25:
            return PowerUp(position, timestamp, GRAY, Type.fast_up_player)
        if p < 50:
            return PowerUp(position, timestamp, NAVYBLUE, Type.fast_up_mob)
        if p < 75:
            return PowerUp(position, timestamp, WHITE, Type.fast_up_obstacle)
        return PowerUp(position, timestamp, RED, Type.slow_down_obstacle)
