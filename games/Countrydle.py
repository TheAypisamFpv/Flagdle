import os, sys
import random
import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Countrydle")

base_font = pygame.font.Font(None, 32)
big_font = pygame.font.Font(None, 64)


def return_to_laucher():
    launcher_path = 'GameLauncher.py'
    pygame.quit()
    os.system(f'python {launcher_path}')
    sys.exit()


# display "game not implemented yet" for 1s then return to menu
screen.fill((0, 0, 0))
text = big_font.render("Game not implemented yet", True, (255, 255, 255))
text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
screen.blit(text, text_rect)
pygame.display.flip()
pygame.time.wait(1000)
return_to_laucher()


