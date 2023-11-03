import pygame
from sys import exit
from random import randint

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

lucy_surf = pygame.image.load("graphics/eboard_Faces/lucy_head_icon.png")
utsha_surf = pygame.image.load("graphics/eboard_Faces/utsha_icon.png")

obstacle_rect_list = []

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 316:
                screen.blit(sammi_surface, obstacle_rect)
            elif obstacle_rect.bottom == 170:
                screen.blit(lucy_surf, obstacle_rect)
            else:
                screen.blit(utsha_surf, obstacle_rect)
        obstacle_list = [obs for obs in obstacle_list if obs.x > -100]
        return obstacle_list
    else:
        return obstacle_list

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

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

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

jump_sound = pygame.mixer.Sound("audio/jump.mp3")
jump_sound.set_volume(0.5)
bg_music = pygame.mixer.Sound("audio/music.wav")
bg_music.play(loops = -1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300: 
                    player_gravity = -20
                    jump_sound.play()
            if event.type == pygame.KEYUP:
                print("key up")
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                sammi_rect.left = 800
                start_time = int(pygame.time.get_ticks()/1000)
        if event.type == obstacle_timer and game_active:
            print(sammi_rect.bottomright)
            randNum = randint(0,2)
            if randNum == 0:
                obstacle_rect_list.append(sammi_surface.get_rect(bottomright = (randint(900, 1100), 316)))
            elif randNum == 1:
                obstacle_rect_list.append(lucy_surf.get_rect(bottomright = (randint(900, 1100), 170)))
            if randNum == 0:
                obstacle_rect_list.append(utsha_surf.get_rect(bottomright = (randint(900, 1100), 140)))

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, screen.get_height() - ground_surface.get_height()))
        score = display_score()

        player_rect.left += 3
        if player_rect.right >= 800:
            player_rect.left = 0
        player_gravity += 1

        player_rect.y += player_gravity
        if player_rect.bottom >= screen.get_height() - ground_surface.get_height():
            player_rect.bottom = screen.get_height() - ground_surface.get_height()
        screen.blit(player_surf, player_rect)

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        game_active = collisions(player_rect, obstacle_rect_list)
    else:
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

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
