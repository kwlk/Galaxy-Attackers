from secrets import randbelow
import time

from .Obstacle import Obstacle
from .Position import Position

class Map:
    def __init__(self, x, y, obstacles_speed, obstacle_spawn_likelihood, barrier_botom_y, barrier_top_y, player_range_bottom_y = 0):
        self.x = x
        self.y = y
        self.barrier_botom_y = barrier_botom_y
        self.barrier_top_y = barrier_top_y
        self.player_range_bottom_y = player_range_bottom_y
        self.player_range_top_y = barrier_botom_y - 1
        self.obstacles = self.generateObstacle()
        self.obstacles_speed = obstacles_speed
        self.obstacle_spawn_likelihood = obstacle_spawn_likelihood

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getBarrierBottomY(self):
        return self.barrier_botom_y

    def getBarrierTopY(self):
        return self.getBarrierTopY

    def getPlayerRangeBottomY(self):
        return self.player_range_bottom_y

    def getPlayerRangeTopY(self):
        return self.player_range_top_y

    def getObstaclesSpeed(self):
        return self.obstacles_speed

    def generateObstacle(self):
        return Obstacle(Position(randbelow(self.player_range_top_y - self.player_range_bottom_y) + self.player_range_bottom_y, self.x),self.obstacles_speed, self)

    def deleteObstacle(self, obstacle: Obstacle):
        self.obstacles = self.generateObstacle()

    def speedUpObstacles(self, newSpeed = -1, speedDifference = 0):
        if newSpeed != -1:
            self.obstacles_speed = newSpeed
        else:
            self.obstacles_speed += speedDifference
    
    def startObstacleCourse(self):
        while(1):
            if(randbelow(self.obstacle_spawn_likelihood) == 0):
                self.generateObstacle()

