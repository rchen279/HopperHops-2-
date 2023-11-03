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
start_time = 0
score = 0
def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f"Score {current_time}", False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)

    return current_time

sammi_surface = pygame.image.load("graphics/eboard_Faces/sammi_head_icon.png").convert_alpha()
sammi_rect = sammi_surface.get_rect(topleft = (600, 240))
sammi_surface = pygame.transform.scale(sammi_surface, (sammi_surface.get_width() * 0.7, sammi_surface.get_height() * 0.7))
sammi_rect = sammi_surface.get_rect(topleft = (600,260))

player_surf = pygame.image.load("graphics/player/hopper_player.png")
player_rect = player_surf.get_rect(midbottom = (100, screen.get_height() - ground_surface.get_height()))

player_gravity = 0

game_active = True

hopper_screen = pygame.image.load('graphics/hopper_intro.png').convert_alpha()
hopper_screen = pygame.transform.scale(hopper_screen, (hopper_screen.get_width()/2.5, hopper_screen.get_height() / 2.5))
hopper_screen_rect = hopper_screen.get_rect(center = (400, 200))

game_name = test_font.render("Hopper Hops", False, '#E85F5C')
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render("Press space to run", False, "Black")
game_message = pygame.transform.scale(game_message, (game_message.get_width() * 0.6, game_message.get_height()*0.6))
game_message_rect = game_message.get_rect(center = (400, 320))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300: 
                    player_gravity = -20
            if event.type == pygame.KEYUP:
                print("key up")
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                sammi_rect.left = 800
                start_time = int(pygame.time.get_ticks()/1000)
    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, screen.get_height() - ground_surface.get_height()))
        score = display_score()

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
            game_active = False
    else:
        screen.fill("#086375")
        screen.blit(hopper_screen, hopper_screen_rect)
        screen.blit(game_name, game_name_rect)

        score_message = test_font.render(f'Your Score: {score}', False, "Black")
        score_message_rect = score_message.get_rect(center = (400, 300))

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
