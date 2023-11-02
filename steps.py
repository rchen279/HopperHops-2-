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
text_surface = test_font.render("My Game", False, "Black")

sammi_surface = pygame.image.load("graphics/eboard_Faces/sammi_head_icon.png").convert_alpha()
sammi_x_pos = 600

player_surf = pygame.image.load("graphics/player/hopper_player.png")
player_rect = player_surf.get_rect(midbottom = (100, screen.get_height() - ground_surface.get_height()))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, screen.get_height() - ground_surface.get_height()))
    screen.blit(text_surface, (300, 50))

    sammi_x_pos -= 3
    if sammi_x_pos <= -100:
        sammi_x_pos = 800
    screen.blit(sammi_surface, (sammi_x_pos, 240))

    player_rect.left += 3
    print(player_rect.right)
    if player_rect.right >= 800:
        player_rect.left = 0
    screen.blit(player_surf, player_rect)
    pygame.display.update()
    clock.tick(60)
