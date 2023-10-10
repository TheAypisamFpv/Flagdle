import os, sys, pygame
from pygame.locals import *


pygame.init()
clock = pygame.time.Clock() 

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flagdle")

base_font = pygame.font.Font(None, 32)
big_font = pygame.font.Font(None, 64)

# colors
WHITE = (200, 200, 200)
DARK_GREY = (25, 25, 25)
BLACK = (0, 0, 0)

# set background color to black
screen.fill(DARK_GREY)

GAME_PATH = "games"


inactiv_color = (100, 100, 100)
activ_color = (200, 200, 200)
button_sepraration = 100
border_radius = 15

GAMES = {}

def load_games(path):

    if len(path) == 0:
        return GAMES

    for game in os.listdir(path):
        # check if the file is a python file
        if game.endswith(".py"):
            game = game.split(".")[0]  
            GAMES[game] = game

    return GAMES


def menu():
    # menu to chose between different games
    # buttons are stacked vertically
    # buttons are centered horizontally

    game_number = len(GAMES)
    button_width = 200
    button_height = 50
    button_separation = 100
    button_start_x = (SCREEN_WIDTH - button_width) / 2
    button_start_y = (SCREEN_HEIGHT/2 - (game_number/2 * button_separation))
    game_buttons = {}
    
    
    # draw buttons
    for game in GAMES:
        game_buttons[game] = pygame.Rect(button_start_x, button_start_y, button_width, button_height)
        button_start_y += button_separation

    # wait for user input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # draw buttons with appropriate color and text
        for game in game_buttons:
            if game_buttons[game].collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, activ_color, game_buttons[game], border_radius=border_radius)
            else:
                pygame.draw.rect(screen, inactiv_color, game_buttons[game], border_radius=border_radius)
            text_surface = base_font.render(game, True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.center = game_buttons[game].center
            screen.blit(text_surface, text_rect)

        # check for mouse click
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            for game in game_buttons:
                if game_buttons[game].collidepoint(mouse_pos):
                    pygame.quit()
                    os.system("python " + GAME_PATH + "/" + game + ".py")
                    sys.exit()

        pygame.display.update()
        clock.tick(60)
        

if __name__ == "__main__":
    GAMES = load_games(GAME_PATH)
    menu()