import pygame
from sys import exit

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
score_surf = test_font.render("My Game",False, "Black")
score_rect = score_surf.get_rect(center = (400,50))
# updating sammi surface to rect
sammi_surface = pygame.image.load("graphics/eboard_Faces/sammi_head_icon.png").convert_alpha()
sammi_rect = sammi_surface.get_rect(topleft = (600,240))

# create player surface
player_surf = pygame.image.load("graphics/player/hopper_player.png").convert_alpha()
# rectangle will take position via mid bottom spec
player_rect = player_surf.get_rect(midbottom = (100,screen.get_height() - ground_surface.get_height()))

# initialize player gravity
player_gravity = 0

while True:
  for event in pygame.event.get():
    # event loop based keyboard input
    if event.type == pygame.QUIT: # x button (close window)
      pygame.quit()
      exit()
    
    # handle hopper jump
    if event.type == pygame.KEYDOWN:
      # print("keydown")
      if event.key == pygame.K_SPACE and player_rect.bottom >= 300:  # detect jump (only when player on ground)
        player_gravity = -20
    if event.type == pygame.KEYUP:
      print('key up')
    
  # display plain color surface
  # screen.blit(plain_color_surface,(200,100))

  # display image surface
  screen.blit(sky_surface,(0,0))
  screen.blit(ground_surface,(0,screen.get_height() - ground_surface.get_height()))

  # display score_surface and fill with color
  pygame.draw.rect(screen,"#16b570",score_rect)
  screen.blit(score_surf,score_rect)
 
  # make sammi’s head move right to left
  sammi_rect.x -= 3
  if sammi_rect.x <= -100:
    sammi_rect.x = 800
  screen.blit(sammi_surface,sammi_rect)

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


  # detect hopper and sammi collision
  if(player_rect.colliderect(sammi_rect)):
    print('hiii')

  # draw elements + update everything
  pygame.display.update()
  clock.tick(60) # while loop run <= 60x/sec