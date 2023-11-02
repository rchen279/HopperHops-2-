# Some boilerplate code to get you started 

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
plain_color_surface = None

# create image surface
sky_surface = None

# create text surface (center text using rect)
test_font = None

# Display the score
# score_surf = test_font.render("My Game",False, "Black")
# score_rect = score_surf.get_rect(center = (400,50))

start_time = 0
# create score variable
score = 0

def display_score():
  pass

# updating sammi surface to rect
sammi_surface = None
# rescale sammi
sammi_surface = None
sammi_rect = None

# create other eboard surfaces
lucy_surf = None
utsha_surf = None

obstacle_rect_list = []

def obstacle_movement(obstacle_list):
  pass

def collisions(player,obstacles):
  pass

# create player surface
player_surf = None
# rectangle will take position via mid bottom spec
player_rect = None

# initialize player gravity
player_gravity = 0

# track game state
game_active = True

# intro/ game over screen
hopper_screen = None
hopper_screen = None
hopper_screen_rect = None

game_name = None
game_name_rect = None

game_message = None
game_message = None
game_message_rect = None

# Create Timer
obstacle_timer = None

# add jump sound effect and music
jump_sound = None

bg_music = None

while True:
  for event in pygame.event.get():
    # event loop based keyboard input
    if event.type == pygame.QUIT: # x button (close window)
      pygame.quit()
      exit()

  # draw elements + update everything
  pygame.display.update()
  clock.tick(60) # while loop run <= 60x/sec
