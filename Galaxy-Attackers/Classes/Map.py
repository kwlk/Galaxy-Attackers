from secrets import randbelow
import pygame
import time

from .Obstacle import Obstacle
from .Position import Position
from .Player import Player


class Map:
    def __init__(self, x, y, obstacles_speed, obstacle_spawn_likelihood, obstacle_img = "broom.png", barrier_top_y=350, barrier_width=10,
                 player_width=50):
        self.x = x
        self.y = y
        self.barrier_top_y = barrier_top_y
        self.obstacles = []
        self.obstacles_speed = obstacles_speed
        self.obstacle_spawn_likelihood = obstacle_spawn_likelihood
        self.player_rect = pygame.Rect(0, 350, x, player_width)
        self.barrier_rect = pygame.Rect(0, barrier_top_y, x, barrier_width)
        self.mob_rect = pygame.Rect(0, 0, x, y - barrier_width - player_width)
        self.obstacle_img = obstacle_img

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getBarrierTopY(self):
        return self.getBarrierTopY

    def getObstaclesSpeed(self):
        return self.obstacles_speed

    def generateObstacle(self):
        return Obstacle(Position(randbelow(self.player_rect.height) + self.player_rect.top, self.x),
                        self.obstacle_img)

    def deleteObstacle(self, obstacle: Obstacle):
        self.obstacles.remove(obstacle)

    def speedUpObstacles(self, newSpeed=-1, speedDifference=0):
        if newSpeed != -1:
            self.obstacles_speed = newSpeed
        else:
            self.obstacles_speed += speedDifference

    def spam_obstacle(self):
        if randbelow(self.obstacle_spawn_likelihood) == 0:
            self.obstacles.append(self.generateObstacle())

    def get_player_rect(self):
        return self.player_rect

    def get_barrier_rect(self):
        return self.barrier_rect

    def get_mob_rect(self):
        return self.mob_rect

    def turn(self, player: Player):
        self.spam_obstacle()
        obstacles_to_remove = []
        for o in self.obstacles:
            if not self.player_rect.colliderect(o.get_rect):
                obstacles_to_remove.append(o)
            ##if o.get_state == 1:
            ##    self.obstacles.remove(o)
            elif player.get_rect().colliderect(o.get_rect):
                player.take_damage(o.get_dmg())
                obstacles_to_remove.append(o)
            else:
                o.move(self.obstacles_speed)
                pygame.display.set_mode((400, 400)).blit(o.get_image, (o.get_position.getx, o.get_position.gety))

        for o in obstacles_to_remove:
            self.obstacles.remove(o)
