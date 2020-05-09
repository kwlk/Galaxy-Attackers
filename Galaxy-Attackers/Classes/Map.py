from secrets import randbelow
import pygame
import time

from .Obstacle import Obstacle
from .Position import Position
from .Player import Player


class Map:
    def __init__(self, obstacle_spawn_likelihood, obstacles_speed=1, x=400, y=400, screen="test no obstacles", obstacle_img="broom.png",
                 barrier_width=10,
                 player_width=130):
        self.x = x
        self.y = y
        self.obstacles = []
        self.obstacles_speed = obstacles_speed
        self.obstacle_spawn_likelihood = obstacle_spawn_likelihood
        self.player_rect = pygame.Rect(0, y - player_width, x, player_width)
        # print(f"player rect arguments: 0, {y-player_width}, {x}, {player_width}")
        self.barrier_rect = pygame.Rect(0, y-player_width-barrier_width, x, barrier_width)
        self.mob_rect = pygame.Rect(0, 0, x, y - barrier_width - player_width)
        self.obstacle_img = pygame.transform.scale(pygame.image.load(obstacle_img), (32, 32))
        self.screen = screen

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getBarrierTopY(self):
        return self.getBarrierTopY

    def getObstaclesSpeed(self):
        return self.obstacles_speed

    def generateObstacle(self):
        return Obstacle(Position(self.x, randbelow(self.player_rect.height) + self.player_rect.top),
                        self.obstacle_img)

    def deleteObstacle(self, obstacle: Obstacle):
        self.obstacles.remove(obstacle)

    def speedUpObstacles(self, newSpeed=-1, speedDifference=0):
        if newSpeed != -1:
            self.obstacles_speed = newSpeed
        else:
            self.obstacles_speed += speedDifference

    def spam_obstacle(self):
        i = randbelow(self.obstacle_spawn_likelihood)
        # print(f"i = {i}")
        if i == 0:
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
        # print(len(self.obstacles))
        for o in self.obstacles:
            if self.player_rect.left > o.get_rect().left:
                print("OUT!")
                obstacles_to_remove.append(o)
            if o.get_state == 1:
                obstacles_to_remove.append(o)
            elif player.get_rect().colliderect(o.get_rect()):
                print("In the player!")
                player.take_damage(o.get_dmg())
                obstacles_to_remove.append(o)
            else:
                self.screen.blit(o.get_img(), (o.get_rect().x, o.get_rect().y))
                # print(f"obstacle x: {o.get_rect().x} y: {o.get_rect().y}")
                o.move(self.obstacles_speed)

        for o in obstacles_to_remove:
            self.obstacles.remove(o)

        self.spam_obstacle()

