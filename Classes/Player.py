from .Position import Position
import pygame


class Player:
    def __init__(self, speed_vector: Position, max_hp, position: Position, rect, speed):
        self.speed_vector = speed_vector
        self.hp = max_hp
        self.position = position
        self.rect = rect
        self.speed = speed

    def shoot(self):
        return self.bullet_type

    def get_rect(self):
        return self.rect

    def check_new_position(self):
        return Position(self.position.x + self.speed_vector.x + self.faster, self.position.y + self.speed_vector.y + self.faster)

    def move(self):
        self.position = Position(self.position.x + self.speed_vector.x * self.speed,
                                 self.position.y + self.speed_vector.y * self.speed)
        self.rect = self.rect.move(self.speed_vector.x * self.speed, self.speed_vector.y * self.speed)

    def take_damage(self, damage):
        self.hp -= damage

    def is_dead(self):
        return self.hp <= 0

