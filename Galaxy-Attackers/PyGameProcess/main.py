import pygame

from Classes.Position import Position
from Classes.Player import Player
from Classes.Map import Map

pygame.init()

screen = pygame.display.set_mode((400, 400))
game_map = Map(400, 400, obstacles_speed=0.05, obstacle_spawn_likelihood=15)
pygame.display.set_caption("Galaxy Attackers", "Galaxy Attackers")
pygame.display.set_icon(pygame.image.load("school.png"))
player_icon = pygame.image.load("tank.png")
player_position = Position(168, 340)
player_speed = Position(0, 0)
player = Player(speed_vector=Position(0, 0), max_hp=3, damage=0, position=player_position, image=player_icon)
# barriers?

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
    # check and move
    if game_map.get_player_rect().contains(pygame.Rect.copy(player.get_rect()).move(player.speed_vector.getx(),
                                                                                        player.speed_vector.gety())):
        player.move()
    game_map.turn(player)

    screen.blit(player_icon, player.get_rect())
    pygame.display.update()
