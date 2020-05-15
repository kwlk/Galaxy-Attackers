import pygame

from Classes.Position import Position
from Classes.Player import Player
from Classes.Map import Map

pygame.init()
# display score on top?
size = (1200, 900)
starter_obstacle_speed = 1
starter_mobs_down_speed = 20
starter_mobs_speed = 1
starter_player_speed = 1
starter_mobs_acceleration = 0.1
screen = pygame.display.set_mode(size)
model = 0
game_map = Map(screen=screen, x=size[0], y=size[1], pu_spawn_rate=2, power_up_lifespan=5,
               obstacles_speed=starter_obstacle_speed,
               mobs_down_speed=starter_mobs_down_speed, obstacle_spawn_rate=10, mobs_speed=starter_mobs_speed,
               mobs_acceleration=starter_mobs_acceleration, difficulty=0,
               score_size=50)
pygame.display.set_caption("Galaxy Attackers", "Galaxy Attackers")
pygame.display.set_icon(pygame.image.load("school.png"))
player_position = Position(game_map.player_rect.centerx, game_map.player_rect.centery)
"""
player = Player(speed_vector=Position(0, 0), max_hp=10, position=player_position,
                rect=game_map.player_img.get_rect(center=(player_position.x, player_position.y)), speed=starter_player_speed)
"""
player = Player.spawn(player_position, model)
game_map.set_player(player)
clock = pygame.time.Clock()


def reset(current_map):
    new_map = Map(screen=current_map.screen, x=current_map.x, y=current_map.y,
                  pu_spawn_rate=current_map.power_up_likelihood, power_up_lifespan=current_map.power_up_lifespan,
                  obstacles_speed=starter_obstacle_speed,
                  mobs_down_speed=starter_mobs_speed,
                  obstacle_spawn_rate=current_map.obstacle_spawn_likelihood, mobs_speed=starter_mobs_speed,
                  mobs_acceleration=starter_mobs_acceleration, difficulty=current_map.difficulty,
                  score_size=current_map.score_size)
    new_map.set_player(Player.spawn(player_position, model))
    return new_map


def game_intro():
    intro = True
    play = True
    while intro:
        clock.tick(120)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                play = False
                intro = False
            if event.type == pygame.KEYDOWN:
                intro = False
        text_font_1 = pygame.font.Font("freesansbold.ttf", 64)
        text_1 = text_font_1.render("GALAXY ATTACKERS", True, (255, 255, 255))
        text_1_rect = text_1.get_rect()
        text_1_rect.center = (size[0] / 2, size[1] / 2 - 40)
        text_font_2 = pygame.font.Font("freesansbold.ttf", 32)
        text_2 = text_font_2.render("Click SPACE to start the game", True, (255, 255, 255))
        text_2_rect = text_2.get_rect()
        text_2_rect.center = (size[0] / 2, size[1] / 2 + 20)
        screen.blit(text_1, text_1_rect)
        screen.blit(text_2, text_2_rect)
        pygame.display.update()
    return play


def game_outro(game_not_over):
    while game_not_over:
        clock.tick(120)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_not_over = False
            if event.type == pygame.KEYDOWN:
                game_not_over = False
        text_font_1 = pygame.font.Font("freesansbold.ttf", 64)
        text_1 = text_font_1.render("GALAXY ATTACKERS", True, (255, 255, 255))
        text_1_rect = text_1.get_rect()
        text_1_rect.center = (size[0] / 2, size[1] / 2 - 40)
        text_font_2 = pygame.font.Font("freesansbold.ttf", 32)
        text_2 = text_font_2.render("Press any key to end it all.", True, (255, 255, 255))
        text_2_rect = text_2.get_rect()
        text_2_rect.center = (size[0] / 2, size[1] / 2 + 20)
        text_font_3 = pygame.font.Font("freesansbold.ttf", 16)
        text_3 = text_font_3.render("Autors: Michał Dronka, Emilia Kwolek", True, (255, 255, 255))
        text_3_rect = text_2.get_rect()
        text_3_rect.center = (size[0] / 2, size[1] / 2 + 60)
        screen.blit(text_1, text_1_rect)
        screen.blit(text_2, text_2_rect)
        screen.blit(text_3, text_3_rect)
        pygame.display.update()


def level_over(text):
    intro = True
    play = True
    while intro:
        clock.tick(120)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                intro = False
            if event.type == pygame.KEYDOWN:
                intro = False
        text_font_1 = pygame.font.Font("freesansbold.ttf", 64)
        text_1 = text_font_1.render(text + "level " + str(game_map.difficulty), True, (255, 255, 255))
        text_1_rect = text_1.get_rect()
        text_1_rect.center = (size[0] / 2, size[1] / 2 - 40)
        text_font_2 = pygame.font.Font("freesansbold.ttf", 32)
        text_2 = text_font_2.render("Click SPACE to continue", True, (255, 255, 255))
        text_2_rect = text_2.get_rect()
        text_2_rect.center = (size[0] / 2, size[1] / 2 + 20)
        screen.blit(text_1, text_1_rect)
        screen.blit(text_2, text_2_rect)
        pygame.display.update()
    return play


def game():
    global game_on
    win = False
    while game_on:
        clock.tick(120)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False, True
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
                if event.key == pygame.K_ESCAPE:
                    game_on = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    game_map.player.speed_vector.x = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    game_map.player.speed_vector.y = 0
        game_map.update()
        if game_map.game_over():
            win = False
            break
        if game_map.game_won():
            win = True
            break
        pygame.display.update()
    return win


game_on = game_intro()
pygame.display.set_mode(size, pygame.FULLSCREEN)
for i in range(4):
    if game_on:
        game_map.difficulty = i
        success = False
        while not success:
            game_map = reset(game_map)
            success = game()
            if success is None:
                break
            if game_on:
                if success:
                    game_on = level_over("You won")
                else:
                    game_on = level_over("You lost")
game_outro(game_on)
