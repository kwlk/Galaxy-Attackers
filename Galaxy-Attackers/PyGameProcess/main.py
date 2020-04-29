import pygame

from Classes.Position import Position
from Classes.Player import Player
from Classes.Map import Map

pygame.init()

screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("Galaxy Attackers", "Galaxy Attackers")
pygame.display.set_icon(pygame.image.load("school.png"))
player_icon = pygame.image.load("tank.png")
player_position = Position(168, 168)
player_speed = Position(0, 0)
player = Player(speed_vector=Position(0, 0), max_hp=3, damage=0, position=player_position)

game_on = True
while game_on:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_vector.setx(-0.1)
            if event.key == pygame.K_RIGHT:
                player.speed_vector.setx(0.1)
            if event.key == pygame.K_DOWN:
                player.speed_vector.sety(0.1)
            if event.key == pygame.K_UP:
                player.speed_vector.sety(-0.1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_vector.setx(0)
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player.speed_vector.sety(0)
    player.move(Position(0, 0), Position(400, 400))
    screen.blit(player_icon, (player.position.x, player.position.y))
    pygame.display.update()
