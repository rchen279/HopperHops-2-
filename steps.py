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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, screen.get_height() - ground_surface.get_height()))
    screen.blit(text_surface, (300, 50))
    pygame.display.update()
    clock.tick(60)
