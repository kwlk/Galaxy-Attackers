from .Position import Position
import pygame


class Player:
    def __init__(self, speed_vector: Position, max_hp, damage, position: Position, image, bullet_type=0):
        self.speed_vector = speed_vector
        self.damage = damage
        self.hp = max_hp
        self.bullet_type = bullet_type
        self.position = position
        self.rect = image.get_rect(center=(position.getx(), position.gety()))

    def shoot(self):
        return self.bullet_type

    def get_rect(self):
        return self.rect

    def check_new_position(self):
        return Position(self.position.x + self.speed_vector.x, self.position.y + self.speed_vector.y)

    def move(self):
        self.position = Position(self.position.x + self.speed_vector.x, self.position.y + self.speed_vector.y)
        self.rect.move(self.speed_vector.getx(), self.speed_vector.gety())

    def take_damage(self, damage):
        self.hp -= damage

    def get_position(self):
        return self.getPosition

