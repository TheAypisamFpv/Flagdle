import os, sys, random, pygame, high_score_saver
from pygame.locals import *

# pygame.init()
# clock = pygame.time.Clock()

# SCREEN_WIDTH = 1080
# SCREEN_HEIGHT = 720

# base_font = pygame.font.Font(None, 32)
# big_font = pygame.font.Font(None, 64)

# def return_to_laucher():
#     launcher_path = 'GameLauncher.py'
#     pygame.quit()
#     os.system(f'python {launcher_path}')
#     sys.exit()


# # display "game not implemented yet" for 1s then return to menu
# screen.fill((0, 0, 0))
# text = big_font.render("Game not implemented yet", True, (255, 255, 255))
# text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
# screen.blit(text, text_rect)
# pygame.display.flip()
# pygame.time.wait(1000)
# return_to_laucher()

pygame.init()
clock = pygame.time.Clock() 
# constants
# screen
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Countrydle")

# colors
GREY = (40, 40, 40)

# set background color to grey
screen.fill(GREY)

global COUNTRY_PATH
# countrys
COUNTRY_PATH = "games\\country"

# lives
global LIVES, lives, SCORE, LIVES_POS, SCORE_POS, GUESS_POS, TEXT_WIDTH, border_radius, base_font, big_font, user_text, WIDTH, HEIGHT, input_rect, unactiv_color, activ_color, active, guess
LIVES = 5
lives = 0

# score
SCORE = 0

LIVES_POS = (0, 0)
SCORE_POS = (0, 50)
GUESS_POS = (0, 100)
TEXT_WIDTH = 100
border_radius = 15
# basic font for user typed 
base_font = pygame.font.Font(None, 32)
big_font = pygame.font.Font(None, 128)
user_text = []

# create rectangle 
WIDTH = 200
HEIGHT = 100
input_rect = pygame.Rect(SCREEN_WIDTH/2 - WIDTH/2, SCREEN_HEIGHT - HEIGHT, WIDTH, HEIGHT) 

unactiv_color = (100, 100, 100)
activ_color = (200, 200, 200)
button_vertical_sepraration = 100
active = False

guess = None
# functions
def load_countrys():
    countrys = []
    
    if len(os.listdir(COUNTRY_PATH)) == 0:
        screen.fill(GREY)
        screen.blit(big_font.render(f"No country found in ", True, (255, 100, 100), (0, 0, 0)), (SCREEN_WIDTH/2-375, SCREEN_HEIGHT/2 - 100))
        screen.blit(big_font.render(f"'{COUNTRY_PATH}'", True, (255, 100, 100), (0, 0, 0)), (SCREEN_WIDTH/2-275, SCREEN_HEIGHT/2))
        pygame.display.flip()
        pygame.time.wait(1000)
        return []
        # pygame.quit()
        # sys.exit()

    for country in os.listdir(COUNTRY_PATH):
        countrys.append(country.removesuffix(".png"))
    return countrys

def random_country(countrys):
    country = random.choice(countrys)
    return country

def return_to_laucher():
    launcher_path = 'GameLauncher.py'
    pygame.quit()
    os.system(f'python {launcher_path}')
    sys.exit()

def countrydle():
    global COUNTRY_PATH, LIVES, SCORE, lives, guess, active, user_text, input_rect, WIDTH, HEIGHT, unactiv_color, activ_color, button_vertical_sepraration, border_radius, base_font, big_font, SCREEN_WIDTH, SCREEN_HEIGHT, screen, LIVES_POS, SCORE_POS, GUESS_POS, TEXT_WIDTH, clock, GREY, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, screen, COUNTRY_PATH, LIVES, lives, SCORE, LIVES_POS, SCORE_POS, GUESS_POS, TEXT_WIDTH, border_radius, base_font, big_font, user_text, WIDTH, HEIGHT, input_rect, unactiv_color, activ_color, active, guess
    countrys = []
    
    europe_color = unactiv_color
    europe_button_pos = (SCREEN_WIDTH/4 - 100, SCREEN_HEIGHT/2 - button_vertical_sepraration/2, 200, 50)
    europe_button = pygame.Rect(europe_button_pos)
    
    amerique_color = unactiv_color
    amerique_button_pos = (SCREEN_WIDTH/4 - 100, SCREEN_HEIGHT/2 + button_vertical_sepraration/2, 200, 50)
    amerique_button = pygame.Rect(amerique_button_pos)
    
    asie_color = unactiv_color
    asie_button_pos = (SCREEN_WIDTH/1.33 - 100, SCREEN_HEIGHT/2 - button_vertical_sepraration/2, 200, 50)
    asie_button = pygame.Rect(asie_button_pos)
    
    afrique_color = unactiv_color
    afrique_button_pos = (SCREEN_WIDTH/1.33 - 100, SCREEN_HEIGHT/2 + button_vertical_sepraration/2, 200, 50)
    afrique_button = pygame.Rect(afrique_button_pos)
    
    oceanie_color = unactiv_color
    oceanie_button = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - button_vertical_sepraration/2, 200, 50)
    # display menu
    while len(countrys) == 0:
        europe_button_text = base_font.render("Europe names", True, (255, 255, 255))
        amerique_button_text = base_font.render("Amerique names", True, (255, 255, 255))
        asie_button_text = base_font.render("Asie names", True, (255, 255, 255))
        afrique_button_text = base_font.render("Afrique names", True, (255, 255, 255))
        oceanie_button_text = base_font.render("Oceanie names", True, (255, 255, 255))
        # align each text to the center of each buttons (use button position and size)
        screen.fill(GREY)
        pygame.draw.rect(screen, europe_color, europe_button, border_radius=border_radius)
        pygame.draw.rect(screen, amerique_color, amerique_button, border_radius=border_radius)
        pygame.draw.rect(screen, asie_color, asie_button, border_radius=border_radius)
        pygame.draw.rect(screen, afrique_color, afrique_button, border_radius=border_radius)
        pygame.draw.rect(screen, oceanie_color, oceanie_button, border_radius=border_radius)
        screen.blit(europe_button_text, (europe_button.x + europe_button.width/2 - europe_button_text.get_width()/2, europe_button.y + europe_button.height/2 - europe_button_text.get_height()/2))
        screen.blit(amerique_button_text, (amerique_button.x + amerique_button.width/2 - amerique_button_text.get_width()/2, amerique_button.y + amerique_button.height/2 - amerique_button_text.get_height()/2))
        screen.blit(asie_button_text, (asie_button.x + asie_button.width/2 - asie_button_text.get_width()/2, asie_button.y + asie_button.height/2 - asie_button_text.get_height()/2))
        screen.blit(afrique_button_text, (afrique_button.x + afrique_button.width/2 - afrique_button_text.get_width()/2, afrique_button.y + afrique_button.height/2 - afrique_button_text.get_height()/2))
        screen.blit(oceanie_button_text, (oceanie_button.x + oceanie_button.width/2 - oceanie_button_text.get_width()/2, oceanie_button.y + oceanie_button.height/2 - oceanie_button_text.get_height()/2))
        pygame.display.flip()
        for event in pygame.event.get(): 
            if europe_button.collidepoint(pygame.mouse.get_pos()):
                europe_color = activ_color
            else:
                europe_color = unactiv_color
            
            if amerique_button.collidepoint(pygame.mouse.get_pos()):
                amerique_color = activ_color
            else:
                amerique_color = unactiv_color
            
            if asie_button.collidepoint(pygame.mouse.get_pos()):
                asie_color = activ_color
            else:
                asie_color = unactiv_color
            
            if afrique_button.collidepoint(pygame.mouse.get_pos()):
                afrique_color = activ_color
            else:
                afrique_color = unactiv_color
            
            if oceanie_button.collidepoint(pygame.mouse.get_pos()):
                oceanie_color = activ_color
            else:
                oceanie_color = unactiv_color
            
            if event.type == pygame.QUIT: 
                return_to_laucher()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return_to_laucher()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                # make the button smaller when clicked
                if europe_button.collidepoint(event.pos):
                    europe_button = pygame.Rect(SCREEN_WIDTH/4 - 175/2, SCREEN_HEIGHT/2 - button_vertical_sepraration/2+2.5, 175, 45)
                if amerique_button.collidepoint(event.pos):
                    amerique_button = pygame.Rect(SCREEN_WIDTH/4 - 175/2, SCREEN_HEIGHT/2 + button_vertical_sepraration/2+2.5, 175, 45)
                if asie_button.collidepoint(event.pos):
                    asie_button = pygame.Rect(SCREEN_WIDTH/1.33 - 175/2, SCREEN_HEIGHT/2 - button_vertical_sepraration/2+2.5, 175, 45)
                if afrique_button.collidepoint(event.pos):
                    afrique_button = pygame.Rect(SCREEN_WIDTH/1.33 - 175/2, SCREEN_HEIGHT/2 + button_vertical_sepraration/2+2.5, 175, 45)
                if oceanie_button.collidepoint(event.pos):
                    oceanie_button = pygame.Rect(SCREEN_WIDTH/2 - 175/2, SCREEN_HEIGHT/2 - button_vertical_sepraration/2+2.5, 175, 45)
                
            if event.type == pygame.MOUSEBUTTONUP:
                if europe_button.collidepoint(event.pos):                
                    pygame.display.set_caption("countrydle name mode Europe")
                    COUNTRY_PATH = "games\\country\\Europe"
                    europe_button = pygame.Rect(europe_button_pos)
                    countrys = load_countrys()
                if amerique_button.collidepoint(event.pos):                
                    pygame.display.set_caption("countrydle name mode Amerique")
                    COUNTRY_PATH = "games\\country\\Amerique"
                    amerique_button = pygame.Rect(amerique_button_pos)
                    countrys = load_countrys()
                if asie_button.collidepoint(event.pos):                
                    pygame.display.set_caption("countrydle name mode Asie")
                    COUNTRY_PATH = "games\\country\\Asie"
                    asie_button = pygame.Rect(asie_button_pos)
                    countrys = load_countrys()
                if afrique_button.collidepoint(event.pos):                
                    pygame.display.set_caption("countrydle name mode Afrique")
                    COUNTRY_PATH = "games\\country\\Afrique"
                    afrique_button = pygame.Rect(afrique_button_pos)
                    countrys = load_countrys()
                if oceanie_button.collidepoint(event.pos):                
                    pygame.display.set_caption("countrydle name mode Oceanie")
                    COUNTRY_PATH = "games\\country\\Oceanie"
                    oceanie_button = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - button_vertical_sepraration/2, 200, 50)
                    countrys = load_countrys() 
                    
            pygame.display.flip()


    country = random_country(countrys)

    # main
    while True:
        
        pygame.display.flip()
        for event in pygame.event.get(): 

        # if user types QUIT then the screen will close 
            if event.type == pygame.QUIT: 
                return_to_laucher() 

            if event.type == pygame.MOUSEBUTTONDOWN: 
                if input_rect.collidepoint(event.pos): 
                    active = True
                else: 
                    active = False

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    return_to_laucher() 
                
                # Check for backspace 
                if event.key == pygame.K_BACKSPACE: 

                    # get text input from 0 to -1 i.e. end. 
                    user_text = user_text[:-1]
                    
                
                # if the user press enter, check if the answer is right
                if event.key == pygame.K_RETURN:
                    if len(user_text) == 0:
                        continue
                    # print(country)
                    final_text = ''.join(user_text)
                    
                    if final_text.lower() == country.lower():
                        SCORE += 1
                        lives = 0
                        countrys.remove(country)
                        guess = True
                    else:
                        guess = False
                        lives = -1
                        SCORE -= 1
                        LIVES -= 1
                    
                    user_text = []
                    prev_country = country
                    if len(countrys) == 0:
                        screen.fill(GREY)
                        screen.blit(big_font.render(f"You Win !", True, (100, 255, 100), (0, 0, 0)), (SCREEN_WIDTH/2-375, SCREEN_HEIGHT/2 - 100))
                        pygame.display.flip()
                        pygame.time.wait(1000)
                        # restart the game
                        LIVES = 5
                        SCORE = 0
                        countrys = load_countrys()
                        guess = None
                        
                    country = random_country(countrys)
                    active = False

                # Unicode standard is used for string 
                # formation 
                elif event.key != pygame.K_BACKSPACE: 
                    user_text.append(event.unicode)

        screen.fill(GREY)
        if LIVES <= 0:
            # display game over on the center of the screen
            screen.blit(big_font.render("Game over !", True, (255, 100, 100), (0, 0, 0)), (SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2 - 100))
            pygame.display.flip()
            pygame.time.wait(1000)
            # restart the game
            LIVES = 5
            SCORE = 0
            countrys = load_countrys()
            guess = None

        if SCORE % 10 == 0 and SCORE > 0 and guess:
            guess = None
            LIVES += 1
            # SCORE += 1
            screen.blit(big_font.render("You got an extra life !", True, (100, 255, 100), (0, 0, 0)), (SCREEN_WIDTH/2 - 400, SCREEN_HEIGHT/2 - 100))
            pygame.display.flip()
            pygame.time.wait(1000)
            screen.fill(GREY)
            pygame.display.flip()
                
        final_text = ''.join(user_text)

        country_img = pygame.image.load(os.path.join(COUNTRY_PATH, country+".png")).convert()
        
        country_width = country_img.get_width()
        country_height = country_img.get_height()
        # rezise the country to fit in the screen, without changing the aspect ratio
        if country_width > SCREEN_WIDTH:
            country_img = pygame.transform.scale(country_img, (SCREEN_WIDTH, int(country_height*SCREEN_WIDTH/country_width)))
        if country_height > SCREEN_HEIGHT:
            country_img = pygame.transform.scale(country_img, (int(country_width*SCREEN_HEIGHT/country_height), SCREEN_HEIGHT))

        screen.blit(country_img, (SCREEN_WIDTH/2 - country_img.get_width()/2, SCREEN_HEIGHT/2 - country_img.get_height()/2))



        if lives == -1:
            lives_text = base_font.render("Lives: " + str(LIVES), True, (255, 100, 100))
        else:
            lives_text = base_font.render("Lives: " + str(LIVES), True, (255, 255, 255))
        # rectangle width and height adjjust for text size
        lives_rect = pygame.Rect(LIVES_POS[0], LIVES_POS[1], lives_text.get_width()+border_radius, lives_text.get_height()+border_radius)
        pygame.draw.rect(screen, (50,50,50), lives_rect, border_radius=border_radius)
        # text centered in the rectangle
        screen.blit(lives_text, (lives_rect.x + lives_rect.width/2 - lives_text.get_width()/2, lives_rect.y + lives_rect.height/2 - lives_text.get_height()/2))
        

        
        

        
        if SCORE <= 0:   
            score_text = base_font.render("Score: " + str(SCORE), True, (255, 100, 100))
        else:
            score_text = base_font.render("Score: " + str(SCORE), True, (100, 255, 100))
        # rectangle width and height adjjust for text size
        score_rect = pygame.Rect(SCORE_POS[0], SCORE_POS[1], score_text.get_width()+border_radius, score_text.get_height()+border_radius)
        pygame.draw.rect(screen, (50,50,50), score_rect, border_radius=border_radius)
        # text centered in the rectangle
        screen.blit(score_text, (score_rect.x + score_rect.width/2 - score_text.get_width()/2, score_rect.y + score_rect.height/2 - score_text.get_height()/2))
        

        if type(guess) == bool:
            if guess:
                guezz_text = base_font.render("Good guezz !", True, (100, 255, 100))
            else:
                guezz_text = base_font.render(f"Wrong guezz, it was {prev_country}", True, (255, 100, 100))
            # rectangle width and height adjjust for text size
            guezz_rect = pygame.Rect(GUESS_POS[0], GUESS_POS[1], guezz_text.get_width()+border_radius, guezz_text.get_height()+border_radius)
            pygame.draw.rect(screen, (50,50,50), guezz_rect, border_radius=border_radius)
            # text centered in the rectangle
            screen.blit(guezz_text, (guezz_rect.x + guezz_rect.width/2 - guezz_text.get_width()/2, guezz_rect.y + guezz_rect.height/2 - guezz_text.get_height()/2))
        


        # draw rectangle and argument passed which should 
        # be on screen 
        pygame.draw.rect(screen, (100,100,100), input_rect, border_radius=border_radius*2) 

        text_surface = big_font.render(final_text, True, (255, 255, 255)) 

        # move rectangle to the center if the width is increased
        input_rect.x = SCREEN_WIDTH/2 - input_rect.width/2
        
        # render in the center of input_rect
        screen.blit(text_surface, (input_rect.x + input_rect.width/2 - text_surface.get_width()/2, input_rect.y + input_rect.height/2 - text_surface.get_height()/2))
        
        # set width of textfield so that text cannot get 
        # outside of user's text input 
        input_rect.w = max(WIDTH, text_surface.get_width()+border_radius) 
        
        # display.flip() will update only a portion of the 
        # screen to updated, not full area 
        pygame.display.flip() 
        
        # clock.tick(60) means that for every second at most 
        # 60 frames should be passed. 
        clock.tick(60)

countrydle()
