import pygame

from Classes.Position import Position
from Classes.Player import Player
from Classes.Map import Map

pygame.init()
size = (1200, 900)
screen = pygame.display.set_mode(size)
model = 0
game_map = Map(screen=screen, is_endless=False, model=model, difficulty=0)
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
    new_map = Map(screen=current_map.screen, difficulty=current_map.difficulty, model=model, is_endless=False)
    new_map.set_player(Player.spawn(player_position, model))
    return new_map


def game_intro():
    global game_on
    intro = True
    while intro and game_on:
        clock.tick(120)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
                intro = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_on = False
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


def game_outro():
    game_not_over = True
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
    global game_on
    intro = True
    while intro:
        clock.tick(120)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
                intro = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_on = False
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


def game():
    global game_on
    win = False
    play = True
    while play and game_on:
        clock.tick(120)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
                break
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
                    break
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    game_map.player.speed_vector.x = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    game_map.player.speed_vector.y = 0
        game_map.update()
        if game_map.game_over():
            win = False
            play = False
        if game_map.game_won():
            win = True
            play = False
        pygame.display.update()
    return win


# START OF THE GAME CODE
game_on = True
game_intro()
pygame.display.set_mode(size, pygame.FULLSCREEN)
for i in range(4):
    if game_on:
        game_map.difficulty = i
        success = False
        while not success and game_on:
            game_map = reset(game_map)
            success = game()
            if success is None:
                break
            if game_on:
                if success:
                    level_over("You won ")
                else:
                    level_over("You lost ")
game_outro()
