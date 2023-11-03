import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

plain_color_surface = pygame.Surface((100, 200))
plain_color_surface.fill('Red')

sky_surface = pygame.image.load("graphics/Sky.jpg").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

test_font = pygame.font.Font("font/open-sans/OpenSans-Regular.ttf", 50)
score_surf = test_font.render("My Game", False, "Black")
score_rect = score_surf.get_rect(center = (400, 50))

sammi_surface = pygame.image.load("graphics/eboard_Faces/sammi_head_icon.png").convert_alpha()
sammi_rect = sammi_surface.get_rect(topleft = (600, 240))

player_surf = pygame.image.load("graphics/player/hopper_player.png")
player_rect = player_surf.get_rect(midbottom = (100, screen.get_height() - ground_surface.get_height()))

player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300: 
                player_gravity = -20
        if event.type == pygame.KEYUP:
            print("key up")
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, screen.get_height() - ground_surface.get_height()))
    pygame.draw.rect(screen, '#16b570', score_rect)
    screen.blit(score_surf, score_rect)

    sammi_rect.x -= 3
    if sammi_rect.x <= -100:
        sammi_rect.x = 800
    screen.blit(sammi_surface, sammi_rect)

    player_rect.left += 3
    if player_rect.right >= 800:
        player_rect.left = 0
    player_gravity += 1

    player_rect.y += player_gravity
    if player_rect.bottom >= screen.get_height() - ground_surface.get_height():
        player_rect.bottom = screen.get_height() - ground_surface.get_height()
    screen.blit(player_surf, player_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("jump")

    if player_rect.colliderect(sammi_rect):
        print("hii")

    pygame.display.update()
    clock.tick(60)
