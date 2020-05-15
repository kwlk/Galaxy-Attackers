from secrets import randbelow
import pygame
import timeit

from .Mob import Mob
from .Obstacle import Obstacle
from .PlayerBullet import PlayerBullet
from .Position import Position
from .Player import Player
from .Barrier import Barrier
from .PowerUp import PowerUp
from .PowerUp import Type



class Map:
    def __init__(self, obstacle_spawn_likelihood, screen, mobs_speed, mobs_acceleration, mobs_down_speed, difficulty,
                 power_up_likelihood, power_up_lifespan, score_size,
                 obstacles_speed=1, x=400, y=400,
                 obstacle_img="broom.png", player_img="tank.png", barrier_img="broom.png",
                 barrier_width=10,
                 player_width=130):
        self.x = x
        self.y = y
        self.difficulty = difficulty
        self.obstacles = []
        self.obstacles_speed = obstacles_speed
        self.obstacle_spawn_likelihood = obstacle_spawn_likelihood
        self.power_up_likelihood = power_up_likelihood
        self.power_up_lifespan = power_up_lifespan
        self.player_rect = pygame.Rect(0, y - player_width, x, player_width)
        self.barrier_rect = pygame.Rect(0, y - player_width - barrier_width, x, barrier_width)
        self.mob_rect = pygame.Rect(0, score_size, x, y - barrier_width - player_width-score_size)
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
        self.power_ups = []
        self.score_size = score_size
        self.game_won = False

        for i in range(1, 4):
            barrier_pos = Position(self.barrier_rect.centerx * i / 2, self.barrier_rect.centery)
            barrier = Barrier(barrier_pos, 3,
                              self.player_img.get_rect(center=(barrier_pos.x, barrier_pos.y)))
            self.barriers.append(barrier)
        self.mobs = []
        for i in range(2, 8):
            for j in range(2, 6):
                mob_pos = Position(self.mob_rect.centerx * i / 5, self.mob_rect.centery * j / 4 - 100)
                self.mobs.append(Mob.spawn(self.difficulty, mob_pos))

    def set_player(self, player: Player):
        self.player = player

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
        if i < self.obstacle_spawn_likelihood:
            self.obstacles.append(self.generateObstacle())

    def spam_power_up(self):
        i = randbelow(1001)
        if i < self.power_up_likelihood:
            self.power_ups.append(self.generate_power_up())

    def delete_old_power_ups(self):
        t = timeit.timeit()
        for pu in self.power_ups:
            if t - pu.timestamp > self.power_up_lifespan:
                self.power_ups.remove(pu)

    def generate_power_up(self):
        print("I'm generating a Power-up!")
        return PowerUp.spawn(Position(randbelow(self.x), randbelow(self.player_rect.height) + self.player_rect.top),
                             timeit.timeit())

    def mob_left_out(self):
        left = self.x + 1
        for m in self.mobs:
            curr_left = m.rect.left
            if curr_left < left:
                left = curr_left
        return left <= 0

    def mob_right_out(self):
        right = - 1
        for m in self.mobs:
            curr_right = m.rect.left + m.rect.width
            if curr_right > right:
                right = curr_right
        return right >= self.x

    def mobs_won(self):
        bottom = 0
        for m in self.mobs:
            curr_bottom = m.rect.top + m.rect.height
            if curr_bottom > bottom:
                bottom = curr_bottom
        return bottom >= self.player_rect.top

    def player_shoot(self):
        bullet = PlayerBullet(self.player.rect, 1, 2)
        self.player_bullets.append(bullet)

    def mobs_shoot(self):
        for m in self.mobs:
            bullet = m.shoot()
            if bullet:
                self.mob_bullets.append(bullet)

    def apply_power_up(self, power_up: PowerUp):
        if power_up.type == Type.fast_up_player:
            self.player.speed += 1
        elif power_up.type == Type.fast_up_mob:
            self.mobs_speed += 1
        elif power_up.type == Type.fast_up_obstacle:
            self.obstacles_speed += 1
        elif power_up.type == Type.slow_down_obstacle and self.obstacles_speed > 0:
            self.obstacles_speed -= 1

    def show_score(self):
        font = pygame.font.Font('freesansbold.ttf', 20)
        score = font.render(" level: "+ str(self.difficulty), True, (255, 255, 255))
        score_rect = score.get_rect()
        score_rect.center = (self.x/2, self.score_size/2)
        self.screen.blit(score, score_rect)

    def power_up_update(self):
        self.delete_old_power_ups()
        for pu in self.power_ups:
            if pu.inside(self.player.rect):
                self.apply_power_up(pu)
                self.power_ups.remove(pu)
            else:
                self.screen.blit(pu.image, (pu.rect.x, pu.rect.y))

    def obstacle_update(self):
        for o in self.obstacles:
            if self.player_rect.left > o.rect.left or o.state == 1:
                self.obstacles.remove(o)
            elif self.player.rect.colliderect(o.rect):
                self.player.take_damage(o.dmg)
                print("Hit by obstacle, remaining hp: " + str(self.player.hp))
                if self.player.is_dead():
                    self.game_over = True
                self.obstacles.remove(o)
            else:
                self.screen.blit(self.obstacle_img, (o.rect.x, o.rect.y))
                o.move(self.obstacles_speed)

    def player_bullets_update(self):
        removed = False
        for pb in self.player_bullets:
            pygame.draw.circle(self.screen, (2, 255, 2), (pb.position.x, pb.position.y), 2)
            hit = False
            for b in self.barriers:
                if pb.inside(b.rect):
                    b.receive_dmg(pb.dmg)
                    hit = True
                    break
            if not hit:
                for m in self.mobs:
                    if pb.inside(m.rect):
                        m.receive_dmg(pb.dmg)
                        hit = True
                        break
            if hit:
                self.player_bullets.remove(pb)
                removed = True
            pb.move()
            if not pb.inside_map(self.mob_rect, self.player_rect) and not removed:
                self.player_bullets.remove(pb)

    def mob_bullets_update(self):
        removed = False
        for mb in self.mob_bullets:
            pygame.draw.circle(self.screen, (255, 2, 2), (mb.position.x, mb.position.y), 2)
            hit = False
            for b in self.barriers:
                if mb.inside(b.rect):
                    b.receive_dmg(mb.dmg)
                    hit = True
                    break
            if not hit:
                if mb.inside(self.player.rect):
                    self.player.take_damage(mb.dmg)
                    print("Hit by bullet, remaining hp: " + str(self.player.hp))
                    hit = True
            if hit:
                self.mob_bullets.remove(mb)
                removed = True
            mb.move()
            if not mb.inside_map(self.mob_rect, self.player_rect) and not removed:
                self.mob_bullets.remove(mb)

    def barriers_update(self):
        for b in self.barriers:
            if not b.is_dead():
                self.screen.blit(self.barrier_img, (b.rect.x, b.rect.y))
            else:
                self.barriers.remove(b)

    def mobs_update(self):
        for m in self.mobs:
            if not m.is_dead():
                if self.mobs_go_right:
                    m.move(round(self.mobs_speed))
                else:
                    m.move(-round(self.mobs_speed))
                self.screen.blit(m.img, (m.rect.x, m.rect.y))
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

        self.mobs_shoot()

    def show_hp(self):
        heart_img = pygame.transform.scale(pygame.image.load("heart.png"), (16, 16))
        heart_rect = heart_img.get_rect(center=(20, 20))
        for i in range(self.player.hp):
            self.screen.blit(heart_img, (heart_rect.x + i * 20, heart_rect.y))

    def update(self):
        if self.player_rect.contains(self.player.rect.move(self.player.speed_vector.x, self.player.speed_vector.y)):
            self.player.move()

        self.obstacle_update()
        self.player_bullets_update()
        self.mob_bullets_update()
        self.mobs_update()
        self.barriers_update()
        self.power_up_update()
        self.show_score()
        self.show_hp()

        if self.mobs_won():
            self.game_over = True
        if len(self.mobs) == 0:
            self.game_won = True

        self.screen.blit(self.player_img, (self.player.rect.x, self.player.rect.y))

        self.spam_obstacle()
        self.spam_power_up()
