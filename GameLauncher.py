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
WHITE = (255, 255, 255)
LIGHT_GREY = (200, 200, 200)
GREY = (100, 100, 100)
DARK_GREY = (40, 40, 40)
BLACK = (0, 0, 0)

# set background color to black
screen.fill(DARK_GREY)

GAME_PATH = "games"


inactiv_color = GREY
activ_color = LIGHT_GREY
button_sepraration = 100
border_radius = 20

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
    game_buttons_pos = []
    game_buttons_color = {}
    
    
    # draw buttons
    for game in GAMES:
        game_buttons[game] = pygame.Rect(button_start_x, button_start_y, button_width, button_height)
        game_buttons_pos.append((button_start_x, button_start_y))
        game_buttons_color[game] = inactiv_color
        button_start_y += button_separation

    # wait for user input
    while True:
        screen.fill(DARK_GREY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            # draw the buttons active color if the mouse if not over them, inactive color if the mouse is over them
            # draw the buttonssmaller if the mouse clicks on them, normal size if the mouse is not clicking on them (mouse button down)
            # lauch the appropriate game if the mouse clicks on them (mouse button up)
            for game in GAMES:
                index = list(GAMES.keys()).index(game)
                if game_buttons[game].collidepoint(pygame.mouse.get_pos()):
                    game_buttons_color[game] = activ_color
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        game_buttons[game] = pygame.Rect(game_buttons_pos[index][0]+5, game_buttons_pos[index][1]+5, button_width-10, button_height-10)
                    else:
                        game_buttons[game] = pygame.Rect(game_buttons_pos[index][0], game_buttons_pos[index][1], button_width, button_height)

                    if event.type == pygame.MOUSEBUTTONUP: 
                        game_buttons[game] = pygame.Rect(game_buttons_pos[index][0], game_buttons_pos[index][1], button_width, button_height)
                        pygame.quit()
                        os.system("python " + GAME_PATH + "/" + GAMES[game] + ".py")
                        sys.exit()
                else:
                    game_buttons[game] = pygame.Rect(game_buttons_pos[index][0], game_buttons_pos[index][1], button_width, button_height)
                    game_buttons_color[game] = inactiv_color
                    
        for game in GAMES:
            pygame.draw.rect(screen, game_buttons_color[game], game_buttons[game], border_radius=border_radius)                 
            text_surface = base_font.render(game, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = game_buttons[game].center
            screen.blit(text_surface, text_rect)
            
        pygame.display.flip()
                
        pygame.display.update()
        clock.tick(60)
        

if __name__ == "__main__":
    GAMES = load_games(GAME_PATH)
    menu()