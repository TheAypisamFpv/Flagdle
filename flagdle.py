# flags are in the folder flags with their french name as filename
# display one flag at a time, the user must guess the name of the country
# the flag name is not displayed, only the flag
# the user can guess the flag in a box below the flag
# if the user guess right, the flag is removed from the list of flags, and the score is incremented
# if the user guess wrong, the score is decremented

import os, sys
import random
from typing import final
import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock() 
# constants
# screen
SCREEN_WIDTH = 1080


SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flagdle")

# colors
WHITE = (200, 200, 200)
BLACK = (50, 50, 50)

# set background color to black
screen.fill(BLACK)

# flags
FLAGS_PATH = "flags"

# lives
LIVES = 5
lives = 0

# score
SCORE = 0

# basic font for user typed 
base_font = pygame.font.Font(None, 32)
big_font = pygame.font.Font(None, 128)
user_text = []

# create rectangle 
WIDTH = 100
HEIGHT = 75
input_rect = pygame.Rect(SCREEN_WIDTH/2 - WIDTH/2, SCREEN_HEIGHT - HEIGHT, WIDTH, HEIGHT) 

  
active = False

guess = None
# functions
def load_flags():
    flags = []
    
    if len(os.listdir(FLAGS_PATH)) == 0:
        screen.fill(BLACK)
        screen.blit(big_font.render(f"No flags found in ", True, (255, 100, 100), (0, 0, 0)), (SCREEN_WIDTH/2-375, SCREEN_HEIGHT/2 - 100))
        screen.blit(big_font.render(f"'{FLAGS_PATH}'", True, (255, 100, 100), (0, 0, 0)), (SCREEN_WIDTH/2-275, SCREEN_HEIGHT/2))
        pygame.display.flip()
        pygame.time.wait(1000)
        return []
        # pygame.quit()
        # sys.exit()

    for flag in os.listdir(FLAGS_PATH):
        flags.append(flag.removesuffix(".png"))
    return flags

def random_flag(flags):
    flag = random.choice(flags)
    return flag

# menu to choose bvetween french names or iso names (iso name are in flags/iso forlder, french names are in flags/french)
# 1) french names
# 2) iso names
# menu has 2 button centered in height

iso_button = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 50, 200, 50)
french_button = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 + 50, 200, 50)
flags = []
# display menu
while len(flags) == 0:
    screen.fill(BLACK)
    pygame.draw.rect(screen, (100,100,100), iso_button)
    pygame.draw.rect(screen, (100,100,100), french_button)
    screen.blit(base_font.render("ISO names", True, (255, 255, 255), (0, 0, 0)), (SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 50))
    screen.blit(base_font.render("French names", True, (255, 255, 255), (0, 0, 0)), (SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 + 50))
    pygame.display.flip()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit() 
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if iso_button.collidepoint(event.pos):
                pygame.display.set_caption("Flagdle iso mode")
                FLAGS_PATH = "flags/iso"
                
            if french_button.collidepoint(event.pos):
                pygame.display.set_caption("Flagdle french mode")
                FLAGS_PATH = "flags/french"

            flags = load_flags()
                
    


flag = random_flag(flags)

# main
while True:
    
    pygame.display.flip()
    for event in pygame.event.get(): 
  
      # if user types QUIT then the screen will close 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
  
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if input_rect.collidepoint(event.pos): 
                active = True
            else: 
                active = False
  
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                pygame.quit() 
                sys.exit() 
            
            # Check for backspace 
            if event.key == pygame.K_BACKSPACE: 
  
                # get text input from 0 to -1 i.e. end. 
                user_text = user_text[:-1]
                
            
            # if the user press enter, check if the answer is right
            if event.key == pygame.K_RETURN:
                
                # print(flag)
                final_text = ''.join(user_text)
                
                if final_text.lower() in flag.lower():
                    SCORE += 1
                    lives = 0
                    flags.remove(flag)
                    guess = True
                else:
                    guess = False
                    lives = -1
                    SCORE -= 1
                    LIVES -= 1
                
                user_text = []
                prev_flag = flag
                flag = random_flag(flags)
                active = False

            # Unicode standard is used for string 
            # formation 
            elif event.key != pygame.K_BACKSPACE: 
                user_text.append(event.unicode)

    screen.fill(BLACK)
    if LIVES == 0:
        # display game over on the center of the screen
        screen.blit(big_font.render("Game over !", True, (255, 100, 100), (0, 0, 0)), (SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2 - 100))
        pygame.display.flip()
        pygame.time.wait(1000)
        pygame.quit()
        sys.exit()

    
    final_text = ''.join(user_text)

    flag_img = pygame.image.load(os.path.join(FLAGS_PATH, flag+".png")).convert()
    
    flag_width = flag_img.get_width()
    flag_height = flag_img.get_height()
    screen.blit(flag_img, (SCREEN_WIDTH/2 - flag_width/2, SCREEN_HEIGHT/2 - flag_height/2))
    if lives == -1:
        lives_text = base_font.render("Lives: " + str(LIVES), True, (255, 100, 100), (0, 0, 0))
    else:
        lives_text = base_font.render("Lives: " + str(LIVES), True, (255, 255, 255), (0, 0, 0))
    
    if SCORE <= 0:   
        score_text = base_font.render("Score: " + str(SCORE), True, (255, 100, 100), (0, 0, 0))
    else:
        score_text = base_font.render("Score: " + str(SCORE), True, (100, 255, 100), (0, 0, 0))
        
    screen.blit(lives_text, (0, 0))
    screen.blit(score_text, (0, 50))

    if type(guess) == bool:
        if guess:
            screen.blit(base_font.render("Good guezz !", True, (100, 255, 100), (0, 0, 0)), (0, 100))
        else:
            screen.blit(base_font.render(f"Wrong guezz ,it was {prev_flag}", True, (255, 100, 100), (0, 0, 0)), (0, 100))


    # draw rectangle and argument passed which should 
    # be on screen 
    pygame.draw.rect(screen, (100,100,100), input_rect) 
  
    text_surface = big_font.render(final_text, True, (255, 255, 255)) 
      
    # render at position stated in arguments 
    screen.blit(text_surface, (input_rect.x, input_rect.y)) 
      
    # set width of textfield so that text cannot get 
    # outside of user's text input 
    input_rect.w = max(100, text_surface.get_width()+10) 
      
    # display.flip() will update only a portion of the 
    # screen to updated, not full area 
    pygame.display.flip() 
      
    # clock.tick(60) means that for every second at most 
    # 60 frames should be passed. 
    clock.tick(60)
    