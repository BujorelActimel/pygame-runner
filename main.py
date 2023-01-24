import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time

def game_over():
    screen.fill((94, 129, 162))
    game_over_surface = test_font.render("You lost", False, (111, 196, 169))
    game_over_rect = game_over_surface.get_rect(center = (400, 50))

    restart_surface = test_font.render("Press 'space' to restart", False, (111, 196, 169))
    restart_rect = restart_surface.get_rect(center = (400, 350))

    player_surface = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
    player_surface = pygame.transform.rotozoom(player_surface, 0, 2)
    player_rect = player_surface.get_rect(center = (400, 175))

    score_surface = test_font.render(f"Score: {score}", False, (111, 196, 169))
    score_rect = score_surface.get_rect(center = (400, 300))

    screen.blit(game_over_surface, game_over_rect)
    screen.blit(restart_surface, restart_rect)
    screen.blit(player_surface, player_rect)
    screen.blit(score_surface, score_rect)

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = True
start_time = 0
score = 0

sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()

# score_surface = test_font.render("My game", False, (64, 64, 64))
# score_rect = score_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800
                    start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, "#D0F4F7", score_rect)
        # screen.blit(score_surface, score_rect)
        score = display_score()

        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        # collison
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        game_over()

    pygame.display.update()
    clock.tick(60)