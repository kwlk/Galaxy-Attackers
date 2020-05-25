from .Position import Position
import pygame


def quick(position: Position):
    player_img = pygame.transform.scale(pygame.image.load("tank1.png"), (64, 37))
    return Player(Position(0, 0), 3, position, player_img.get_rect(center=(position.x, position.y)), 2, player_img)


class Player:

    def __init__(self, speed_vector: Position, max_hp, position: Position, rect, speed, img):
        self.speed_vector = speed_vector
        self.hp = max_hp
        self.position = position
        self.rect = rect
        self.speed = speed
        self.img = img

    def move(self, where: tuple):
        if where[0]:
            self.position = Position(self.position.x + self.speed_vector.x * self.speed, self.position.y)
            self.rect = self.rect.move(self.speed_vector.x * self.speed, 0)
        if where[1]:
            self.position = Position(self.position.x, self.position.y + self.speed_vector.y * self.speed)
            self.rect = self.rect.move(0, self.speed_vector.y * self.speed)

    def take_damage(self, damage):
        self.hp -= damage

    def is_dead(self):
        return self.hp <= 0

    @classmethod
    def spawn(cls, position: Position, model):
        if model == 0:
            return quick(position)

