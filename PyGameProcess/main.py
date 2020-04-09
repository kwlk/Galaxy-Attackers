import pygame

from Classes.Position import Position

pygame.init()

screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("Galaxy Attackers", "Galaxy Attackers")
pygame.display.set_icon(pygame.image.load("school.png"))
player_icon = pygame.image.load("tank.png")
player_position = Position(168, 168)
player_position_change_x = 0
player_position_change_y = 0

game_on = True
while game_on:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_position_change_x = -0.1
            if event.key == pygame.K_RIGHT:
                player_position_change_x = 0.1
            if event.key == pygame.K_DOWN:
                player_position_change_y = 0.1
            if event.key == pygame.K_UP:
                player_position_change_y = -0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_position_change_x = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_position_change_y = 0
    player_position.move_x(player_position_change_x)
    player_position.move_y(player_position_change_y)
    screen.blit(player_icon, (player_position.getx(), player_position.gety()))
    pygame.display.update()
