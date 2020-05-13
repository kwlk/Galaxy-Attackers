from secrets import randbelow
import pygame

from .Mob import Mob
from .MobBullet import MobBullet
from .Obstacle import Obstacle
from .PlayerBullet import PlayerBullet
from .Position import Position
from .Player import Player
from .Barrier import Barrier


class Map:
    def __init__(self, obstacle_spawn_likelihood, screen, mobs_speed, mobs_acceleration, mobs_down_speed, mob_shoot_likelihood,
                 obstacles_speed=1, x=400, y=400,
                 obstacle_img="broom.png", player_img="tank.png", barrier_img="broom.png",
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
        self.player = None
        self.game_over = False
        self.player_img = pygame.transform.scale(pygame.image.load(player_img), (64, 64))
        self.barrier_img = pygame.transform.scale(pygame.image.load(barrier_img), (64, 16))
        self.mobs_speed = mobs_speed
        self.mobs_acceleration = mobs_acceleration
        self.mobs_go_right = True
        self.mobs_down_speed = mobs_down_speed
        self.player_bullets = []
        self.mob_bullets = []
        self.barriers = []
        self.mob_shoot_likelihood = mob_shoot_likelihood

        for i in range(1, 4):
            barrier_pos = Position(self.get_barrier_rect().centerx * i/2, self.get_barrier_rect().centery)
            barrier = Barrier(barrier_pos, 3,
                              self.player_img.get_rect(center=(barrier_pos.x, barrier_pos.y)))
            self.barriers.append(barrier)
        self.mobs = []
        for i in range(2, 8):
            for j in range(2, 6):
                mob_pos = Position(self.get_mob_rect().centerx * i/5, self.get_mob_rect().centery * j/4 - 100)
                mob_img = pygame.transform.scale(pygame.image.load(barrier_img), (32, 32))
                mob = Mob(1, None, mob_img, mob_img.get_rect(center=(mob_pos.x, mob_pos.y)))
                self.mobs.append(mob)

    def set_player(self, player: Player):
        self.player = player

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
        i = randbelow(1001)
        # print(f"i = {i}")
        if i < self.obstacle_spawn_likelihood:
            self.obstacles.append(self.generateObstacle())

    def get_player_rect(self):
        return self.player_rect

    def get_barrier_rect(self):
        return self.barrier_rect

    def get_mob_rect(self):
        return self.mob_rect

    def mob_left_out(self):
        left = self.getx() + 1
        for m in self.mobs:
            curr_left = m.get_rect().left
            if curr_left < left:
                left = curr_left
        return left <= 0

    def mob_right_out(self):
        right = - 1
        for m in self.mobs:
            curr_right = m.get_rect().left + m.get_rect().width
            if curr_right > right:
                right = curr_right
        return right >= self.getx()

    def mobs_won(self):
        bottom = 0
        for m in self.mobs:
            curr_bottom = m.get_rect().top + m.get_rect().height
            if curr_bottom > bottom:
                bottom = curr_bottom
        return bottom >= self.player_rect.top

    def player_shoot(self):
        bullet = PlayerBullet(self.player.get_rect(), 1, 2)
        self.player_bullets.append(bullet)

    def mob_shoot(self, mob: Mob):
        bullet = MobBullet(mob.get_rect(), mob.get_bullet_type())
        self.mob_bullets.append(bullet)

    def mob_random_shoot(self):
        i = randbelow(1001)
        if i < self.mob_shoot_likelihood:
            m = randbelow(len(self.mobs))
            self.mob_shoot(self.mobs[m])


    def update(self):

        for o in self.obstacles:
            if self.player_rect.left > o.get_rect().left or o.get_state == 1:
                self.obstacles.remove(o)
            elif self.player.get_rect().colliderect(o.get_rect()):
                self.player.take_damage(o.get_dmg())
                print("Hit by obstacle, remaining hp: " + str(self.player.hp))
                if self.player.is_dead():
                    self.game_over = True
                self.obstacles.remove(o)
            else:
                self.screen.blit(self.obstacle_img, (o.get_rect().x, o.get_rect().y))
                # print(f"obstacle x: {o.get_rect().x} y: {o.get_rect().y}")
                o.move(self.obstacles_speed)

        for pb in self.player_bullets:
            pygame.draw.circle(self.screen, (2, 255, 2), (pb.position.x, pb.position.y), 2)
            hit = False
            for b in self.barriers:
                if pb.inside(b.get_rect()):
                    b.receive_dmg(pb.dmg)
                    hit = True
                    break
            if not hit:
                for m in self.mobs:
                    if pb.inside(m.get_rect()):
                        m.receive_dmg(pb.dmg)
                        hit = True
                        break
            if hit:
                self.player_bullets.remove(pb)
            pb.move()
            if not pb.inside_map(self.get_mob_rect(), self.get_player_rect()):
                self.player_bullets.remove(pb)
        self.mob_random_shoot()
        for mb in self.mob_bullets:
            pygame.draw.circle(self.screen, (2, 255, 2), (mb.position.x, mb.position.y), 2)
            hit = False
            for b in self.barriers:
                if mb.inside(b.get_rect()):
                    b.receive_dmg(mb.dmg)
                    hit = True
                    break
            if not hit:
                if mb.inside(self.player.get_rect()):
                    self.player.take_damage(mb.dmg)
                    print("Hit by bullet, remaining hp: " + str(self.player.hp))
                    hit = True
            if hit:
                self.mob_bullets.remove(mb)
            mb.move()
            if not mb.inside_map(self.get_mob_rect(), self.get_player_rect()):
                self.mob_bullets.remove(mb)

        for b in self.barriers:
            if not b.is_dead():
                self.screen.blit(self.barrier_img, (b.get_rect().x, b.get_rect().y))
            else:
                self.barriers.remove(b)

        for m in self.mobs:
            if not m.is_dead():
                if self.mobs_go_right:
                    m.move(round(self.mobs_speed))
                else:
                    m.move(-round(self.mobs_speed))
                self.screen.blit(m.img, (m.get_rect().x, m.get_rect().y))
            else:
                self.mobs.remove(m)
                self.mobs_speed += self.mobs_acceleration

        if self.mobs_go_right:
            if self.mob_right_out():
                self.mobs_go_right = False
                for m in self.mobs:
                    m.down(self.mobs_down_speed)
        else:
            if self.mob_left_out():
                self.mobs_go_right = True
                for m in self.mobs:
                    m.down(self.mobs_down_speed)

        if self.mobs_won():
            self.game_over = True

        self.screen.blit(self.player_img, (self.player.get_rect().x, self.player.get_rect().y))

        self.spam_obstacle()

