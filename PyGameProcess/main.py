import pygame

from Classes.Position import Position

pygame.init()

screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("Galaxy Attackers", "Galaxy Attackers")
pygame.display.set_icon(pygame.image.load("school.png"))
player_icon = pygame.image.load("tank.png")
player_position = Position(168, 168)


def player():
    screen.blit(player_icon, (player_position.getx(), player_position.gety()))


game_on = True
while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    screen.fill((0, 0, 0))
    player()
    pygame.display.update()
