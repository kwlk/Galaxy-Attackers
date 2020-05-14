import pygame

from Classes.Position import Position
from Classes.Player import Player
from Classes.Map import Map

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
game_map = Map(screen=screen, x=size[0], y=size[1], power_up_likelihood=2, power_up_lifespan=5, obstacles_speed=1, mobs_down_speed=20,
               obstacle_spawn_likelihood=10, mobs_speed=1, mobs_acceleration=0.1, difficulty=3)
pygame.display.set_caption("Galaxy Attackers", "Galaxy Attackers")
pygame.display.set_icon(pygame.image.load("school.png"))
player_position = Position(game_map.player_rect.centerx, game_map.player_rect.centery)
player_speed = Position(0, 0)
player = Player(speed_vector=Position(0, 0), max_hp=1000, position=player_position,
                rect=game_map.player_img.get_rect(center=(player_position.x, player_position.y)))
game_map.set_player(player)

# barriers?

#print(f"player x:{player.get_rect().x}, player y{player.get_rect().y}\n player width: {player.get_rect().width}, player height: {player.get_rect().height}")
#print(f"player space\n x: {game_map.get_player_rect().x}, y: {game_map.get_player_rect().y}\n width: {game_map.get_player_rect().width}, height: {game_map.get_player_rect().height}")
clock = pygame.time.Clock()
game_on = True
while game_on:
    clock.tick(120)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game_map.player.speed_vector.x = -1
            if event.key == pygame.K_RIGHT:
                game_map.player.speed_vector.x = 1
            if event.key == pygame.K_DOWN:
                game_map.player.speed_vector.y = 1
            if event.key == pygame.K_UP:
                game_map.player.speed_vector.y = -1
            if event.key == pygame.K_SPACE:
                game_map.player_shoot()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                game_map.player.speed_vector.x = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                game_map.player.speed_vector.y = 0
    game_map.update()
    if game_map.game_over:
        game_on = False
    pygame.display.update()
