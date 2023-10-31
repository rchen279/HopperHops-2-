import pygame
from sys import exit
from random import randint
pygame.init()
# create the display surface (window)
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Hopper Hops") # title
# control framerate
clock = pygame.time.Clock()

# create plain color surface
plain_color_surface = pygame.Surface((100,200))
plain_color_surface.fill('Red') # color

# create image surface
sky_surface = pygame.image.load("graphics/Sky.jpg").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# create text surface (center text using rect)
test_font = pygame.font.Font("font/open-sans/OpenSans-Regular.ttf",50)

# Display the score
# score_surf = test_font.render("My Game",False, "Black")
# score_rect = score_surf.get_rect(center = (400,50))

start_time = 0
# create score variable
score = 0

def display_score():
  current_time = int(pygame.time.get_ticks()/1000) - start_time
  score_surf = test_font.render(f'Score {current_time}',False,(64,64,64))
  score_rect = score_surf.get_rect(center=(400,50))
  screen.blit(score_surf,score_rect)
  # print(current_time)
  return current_time

# updating sammi surface to rect
sammi_surface = pygame.image.load("graphics/eboard_Faces/sammi_head_icon.png").convert_alpha()
# rescale sammi
sammi_surface = pygame.transform.scale(sammi_surface,(sammi_surface.get_width() * 0.7, sammi_surface.get_height() * 0.7))
sammi_rect = sammi_surface.get_rect(topleft = (600,260))

# create other eboard surfaces
lucy_surf = pygame.image.load("graphics/eboard_Faces/lucy_head_icon.png")
utsha_surf = pygame.image.load("graphics/eboard_Faces/utsha_icon.png")

obstacle_rect_list = []

def obstacle_movement(obstacle_list):
  if obstacle_list:
    for obstacle_rect in obstacle_list:
      obstacle_rect.x -= 5 # move obstacle left
      # screen.blit(sammi_surface,obstacle_rect)

      # draw obstacles based on rectangle bottom position
      if obstacle_rect.bottom ==316: # draw sammi
        screen.blit(sammi_surface,obstacle_rect)
      elif obstacle_rect.bottom == 170:
        screen.blit(lucy_surf,obstacle_rect)
      else:
        screen.blit(utsha_surf,obstacle_rect)

    obstacle_list = [obs for obs in obstacle_list if obs.x > -100] # remove rectanlges too far left
    return obstacle_list
  else:
    return []

def collisions(player,obstacles):
  if obstacles:
    for obstacle_rect in obstacles:
      if player.colliderect(obstacle_rect): return False
  return True

# create player surface
player_surf = pygame.image.load("graphics/player/hopper_player.png").convert_alpha()
# rectangle will take position via mid bottom spec
player_rect = player_surf.get_rect(midbottom = (100,screen.get_height() - ground_surface.get_height()))

# initialize player gravity
player_gravity = 0

# track game state
game_active = True

# intro/ game over screen
hopper_screen = pygame.image.load('graphics/hopper_intro.png').convert_alpha()
hopper_screen = pygame.transform.scale(hopper_screen,(hopper_screen.get_width() / 2.5, 
                                                             hopper_screen.get_height() / 2.5))
hopper_screen_rect = hopper_screen.get_rect(center = (400,200))

game_name = test_font.render("Hopper Hops",False, "#E85F5C")
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render("Press space to run",False, "Black")
game_message = pygame.transform.scale(game_message,(game_message.get_width() * 0.6, 
                                                    game_message.get_height() * 0.6))
game_message_rect = game_message.get_rect(center = (400,320))

# Create Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

# add jump sound effect and music
jump_sound = pygame.mixer.Sound("audio/jump.mp3")
jump_sound.set_volume(0.5)
bg_music = pygame.mixer.Sound("audio/music.wav")
bg_music.play(loops = -1) # play forever

while True:
  for event in pygame.event.get():
    # event loop based keyboard input
    if event.type == pygame.QUIT: # x button (close window)
      pygame.quit()
      exit()
    
    # condition event on game state
    if game_active:
      # handle hopper jump
      if event.type == pygame.KEYDOWN:
        # print("keydown")
        if event.key == pygame.K_SPACE and player_rect.bottom >= 300:  # detect jump (only when player on ground)
          player_gravity = -20
          # enable jump sound
          jump_sound.play()

      if event.type == pygame.KEYUP:
        print('key up')
    else:
      # update start time
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        game_active = True
        sammi_rect.left = 800
        start_time = int(pygame.time.get_ticks()/1000)
    # on obstacle timer event
    if event.type == obstacle_timer and game_active:
      # print("test")
      print(sammi_rect.bottomright)
      # lets make utsha and lucy fly and have sammi on the ground
      randNum = randint(0,2) # random number in [0,1,2] (inclusive both limits)
      if randNum == 0: # case sammi
        obstacle_rect_list.append(sammi_surface.get_rect(bottomright = (randint(900,1100),316))) # add rectangle
      elif randNum == 1: # case lucy
        obstacle_rect_list.append(lucy_surf.get_rect(bottomright = (randint(900,1100),170)))
      else: # case utsha
        obstacle_rect_list.append(utsha_surf.get_rect(bottomright = (randint(900,1100),140)))
      
  # condition display on game state
  if game_active:
    # display plain color surface
    # screen.blit(plain_color_surface,(200,100))

    # display image surface
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,screen.get_height() - ground_surface.get_height()))

    # Display the score
    # display score_surface and fill with color
    # pygame.draw.rect(screen,"#16b570",score_rect)
    # screen.blit(score_surf,score_rect)
    
    # display and assign score
    score = display_score()
   
    # comment out 
    # make sammi’s head move right to left
    # sammi_rect.x -= 3
    # if sammi_rect.x <= -100:
    #   sammi_rect.x = 800
    # screen.blit(sammi_surface,sammi_rect)


    # place and move hopper across ground (and give gravity)
    player_rect.left += 3
    # print(player_rect.right)
    if player_rect.right >= 800:
      player_rect.left = 0
    player_gravity += 1 # will first be 1, then 2 then, 3 and so on for each iteration
    player_rect.y += player_gravity # adding result to y
    if player_rect.bottom >= screen.get_height() - ground_surface.get_height():
      player_rect.bottom = screen.get_height() - ground_surface.get_height()
    screen.blit(player_surf,player_rect)

    # detect space key press (to be replaced)
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #   print("jump")

    # obstacle movement
    obstacle_rect_list = obstacle_movement(obstacle_rect_list)


    # # detect hopper and sammi collision
    # if(player_rect.colliderect(sammi_rect)):
    #   # game is now inactive
    #   game_active = False

    game_active = collisions(player_rect,obstacle_rect_list)

  else:
    # reset obstacles
    obstacle_rect_list.clear()
    player_rect.midbottom = (80,300)
    player_gravity = 0

    # display game over screen
    screen.fill("#086375")
    screen.blit(hopper_screen,hopper_screen_rect)
    screen.blit(game_name,game_name_rect)
    
    score_message = test_font.render(f'Your Score: {score}',False, "Black")
    score_message_rect = score_message.get_rect(center =(400,300))

    if score == 0:
      screen.blit(game_message,game_message_rect)
    else:
      screen.blit(score_message,score_message_rect)

  # draw elements + update everything
  pygame.display.update()
  clock.tick(60) # while loop run <= 60x/sec