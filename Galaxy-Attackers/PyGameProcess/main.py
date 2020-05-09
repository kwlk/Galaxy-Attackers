import pygame

from Classes.Position import Position
from Classes.Player import Player
from Classes.Map import Map

pygame.init()

screen = pygame.display.set_mode((400, 400))
game_map = Map(screen=screen, x=400, y=400, obstacles_speed=1, obstacle_spawn_likelihood=150)
pygame.display.set_caption("Galaxy Attackers", "Galaxy Attackers")
pygame.display.set_icon(pygame.image.load("school.png"))
player_icon = pygame.image.load("tank.png")
player_position = Position(game_map.get_player_rect().centerx, game_map.get_player_rect().centery)
player_speed = Position(0, 0)
player = Player(speed_vector=Position(0, 0), max_hp=3, damage=0, position=player_position, image=player_icon)
# barriers?
print(f"player x:{player.get_rect().x}, player y{player.get_rect().y}\n player width: {player.get_rect().width}, player height: {player.get_rect().height}")
print(f"player space\n x: {game_map.get_player_rect().x}, y: {game_map.get_player_rect().y}\n width: {game_map.get_player_rect().width}, height: {game_map.get_player_rect().height}")
game_on = True
while game_on:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_vector.setx(-1)
            if event.key == pygame.K_RIGHT:
                player.speed_vector.setx(1)
            if event.key == pygame.K_DOWN:
                player.speed_vector.sety(1)
            if event.key == pygame.K_UP:
                player.speed_vector.sety(-1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_vector.setx(0)
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player.speed_vector.sety(0)
    # check and move
    if game_map.get_player_rect().contains(player.get_rect().move(player.speed_vector.getx(), player.speed_vector.gety())):
        player.move()
        # print("Can'y move!!")
    game_map.turn(player)

    screen.blit(player_icon, (player.get_rect().x, player.get_rect().y))
    pygame.display.update()
