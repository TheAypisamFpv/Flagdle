import os, sys, random, pygame
import high_score_saver
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
BLACK = (25, 25, 25)

# set background color to black
screen.fill(BLACK)

global FLAGS_PATH
# flags
FLAGS_PATH = "games\\flags"

# lives
global LIVES, lives, SCORE, HIGH_SCORE, LIVES_POS, SCORE_POS, GUESS_POS, TEXT_WIDTH, border_radius, base_font, big_font, user_text, WIDTH, HEIGHT, input_rect, unactiv_color, activ_color, active, guess
LIVES = 5
lives = 0

# score
SCORE = 0
HIGH_SCORE = high_score_saver.get_score()
HIGH_SCORE = int(HIGH_SCORE.split(":")[2]) if ":" in HIGH_SCORE else 0

LIVES_POS = (5, 5)
SCORE_POS = (5, 55)
HIGH_SCORE_POS = (5, 105)
GUESS_POS = (5, 155)
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

def return_to_laucher():
    high_score_saver.save_score(HIGH_SCORE, pygame.display.get_caption()[0])
    launcher_path = 'GameLauncher.py'
    pygame.quit()
    os.system(f'python {launcher_path}')
    sys.exit()

def flagdle():
    global FLAGS_PATH, LIVES, SCORE, HIGH_SCORE, lives, guess, active, user_text, input_rect, WIDTH, HEIGHT, unactiv_color, activ_color, button_vertical_sepraration, border_radius, base_font, big_font, SCREEN_WIDTH, SCREEN_HEIGHT, screen, LIVES_POS, SCORE_POS, GUESS_POS, TEXT_WIDTH, clock, WHITE, BLACK, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, screen, FLAGS_PATH, LIVES, lives, SCORE, LIVES_POS, SCORE_POS, GUESS_POS, TEXT_WIDTH, border_radius, base_font, big_font, user_text, WIDTH, HEIGHT, input_rect, unactiv_color, activ_color, active, guess
    flags = []
    iso_color = unactiv_color
    french_color = unactiv_color
    iso_button = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - button_vertical_sepraration/2, 200, 50)
    french_button = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 + button_vertical_sepraration/2, 200, 50)
    # display menu
    while len(flags) == 0:
        french_button_text = base_font.render("French names", True, (255, 255, 255))
        iso_button_text = base_font.render("Iso names", True, (255, 255, 255))
        # align each text to the center of each buttons (use button position and size)
        screen.fill(BLACK)
        pygame.draw.rect(screen, french_color, french_button, border_radius=border_radius)
        pygame.draw.rect(screen, iso_color, iso_button, border_radius=border_radius)
        screen.blit(french_button_text, (french_button.x + french_button.width/2 - french_button_text.get_width()/2, french_button.y + french_button.height/2 - french_button_text.get_height()/2))
        screen.blit(iso_button_text, (iso_button.x + iso_button.width/2 - iso_button_text.get_width()/2, iso_button.y + iso_button.height/2 - iso_button_text.get_height()/2))
        pygame.display.flip()
        for event in pygame.event.get(): 
            if iso_button.collidepoint(pygame.mouse.get_pos()):
                iso_color = activ_color
            else:
                iso_color = unactiv_color
            
            if french_button.collidepoint(pygame.mouse.get_pos()):
                french_color = activ_color
            else:
                french_color = unactiv_color
            
            if event.type == pygame.QUIT: 
                return_to_laucher()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return_to_laucher()

                       
            if event.type == pygame.MOUSEBUTTONDOWN:
                # make the button smaller when clicked
                if iso_button.collidepoint(event.pos):
                    iso_button = pygame.Rect(SCREEN_WIDTH/2 - 175/2, SCREEN_HEIGHT/2 - button_vertical_sepraration/2+2.5, 175, 45)
                if french_button.collidepoint(event.pos):
                    french_button = pygame.Rect(SCREEN_WIDTH/2 - 175/2, SCREEN_HEIGHT/2 + button_vertical_sepraration/2+2.5, 175, 45)
                
            if event.type == pygame.MOUSEBUTTONUP:
                if iso_button.collidepoint(event.pos):                
                    pygame.display.set_caption("Flagdle iso mode")
                    FLAGS_PATH = "games\\flags\\iso"
                    iso_button = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - button_vertical_sepraration/2, 200, 50)
                    flags = load_flags()
                    
                if french_button.collidepoint(event.pos):
                    pygame.display.set_caption("Flagdle french mode")
                    FLAGS_PATH = "games\\flags\\french"
                    french_button = pygame.Rect(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 + button_vertical_sepraration/2, 200, 50)
                    flags = load_flags()

                
                    
            pygame.display.flip()


    flag = random_flag(flags)

    # main
    while True:
        if SCORE > HIGH_SCORE:
            HIGH_SCORE = SCORE
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
                    # print(flag)
                    final_text = ''.join(user_text)
                    
                    if final_text.lower() == flag.lower():
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
                    if len(flags) == 0:
                        screen.fill(BLACK)
                        screen.blit(big_font.render(f"You Win !", True, (100, 255, 100), (0, 0, 0)), (SCREEN_WIDTH/2-375, SCREEN_HEIGHT/2 - 100))
                        pygame.display.flip()
                        pygame.time.wait(1000)
                        # restart the game
                        LIVES = 5
                        SCORE = 0
                        flags = load_flags()
                        guess = None
                        
                    flag = random_flag(flags)
                    active = False

                # Unicode standard is used for string 
                # formation 
                elif event.key != pygame.K_BACKSPACE: 
                    user_text.append(event.unicode)

        screen.fill(BLACK)
        if LIVES <= 0:
            # display game over on the center of the screen
            screen.blit(big_font.render("Game over !", True, (255, 100, 100), (0, 0, 0)), (SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2 - 100))
            pygame.display.flip()
            pygame.time.wait(1000)
            # restart the game
            LIVES = 5
            SCORE = 0
            flags = load_flags()
            guess = None

        if SCORE % 10 == 0 and SCORE > 0 and guess:
            guess = None
            LIVES += 1
            # SCORE += 1
            screen.blit(big_font.render("You got an extra life !", True, (100, 255, 100), (0, 0, 0)), (SCREEN_WIDTH/2 - 400, SCREEN_HEIGHT/2 - 100))
            pygame.display.flip()
            pygame.time.wait(1000)
            screen.fill(BLACK)
            pygame.display.flip()
                
        final_text = ''.join(user_text)

        flag_img = pygame.image.load(os.path.join(FLAGS_PATH, flag+".png")).convert()
        
        flag_width = flag_img.get_width()
        flag_height = flag_img.get_height()
        # rezise the flag to fit in the screen, without changing the aspect ratio
        if flag_width > SCREEN_WIDTH:
            flag_img = pygame.transform.scale(flag_img, (SCREEN_WIDTH, int(flag_height*SCREEN_WIDTH/flag_width)))
        if flag_height > SCREEN_HEIGHT:
            flag_img = pygame.transform.scale(flag_img, (int(flag_width*SCREEN_HEIGHT/flag_height), SCREEN_HEIGHT))

        screen.blit(flag_img, (SCREEN_WIDTH/2 - flag_img.get_width()/2, SCREEN_HEIGHT/2 - flag_img.get_height()/2))



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

        high_score_text = base_font.render("High score: " + str(HIGH_SCORE), True, (255, 255, 255))
        high_score_rect = pygame.Rect(HIGH_SCORE_POS[0], HIGH_SCORE_POS[1], high_score_text.get_width()+border_radius, high_score_text.get_height()+border_radius)
        pygame.draw.rect(screen, (50,50,50), high_score_rect, border_radius=border_radius)
        screen.blit(high_score_text, (high_score_rect.x + high_score_rect.width/2 - high_score_text.get_width()/2, high_score_rect.y + high_score_rect.height/2 - high_score_text.get_height()/2))
        
        # rectangle width and height adjjust for text size
        score_rect = pygame.Rect(SCORE_POS[0], SCORE_POS[1], score_text.get_width()+border_radius, score_text.get_height()+border_radius)
        pygame.draw.rect(screen, (50,50,50), score_rect, border_radius=border_radius)

        # text centered in the rectangle
        screen.blit(score_text, (score_rect.x + score_rect.width/2 - score_text.get_width()/2, score_rect.y + score_rect.height/2 - score_text.get_height()/2))
        

        if type(guess) == bool:
            if guess:
                guezz_text = base_font.render("Good guezz !", True, (100, 255, 100))
            else:
                guezz_text = base_font.render(f"Wrong guezz, it was {prev_flag}", True, (255, 100, 100))
            # rectangle width and height adjjust for text size
            guezz_rect = pygame.Rect(GUESS_POS[0], GUESS_POS[1], guezz_text.get_width()+border_radius, guezz_text.get_height()+border_radius)
            pygame.draw.rect(screen, (50,50,50), guezz_rect, border_radius=border_radius)
            # text centered in the rectangle
            screen.blit(guezz_text, (guezz_rect.x + guezz_rect.width/2 - guezz_text.get_width()/2, guezz_rect.y + guezz_rect.height/2 - guezz_text.get_height()/2))
        


        # draw rectangle and argument passed which should 
        # be on screen 
        pygame.draw.rect(screen, (30, 30, 30), input_rect, border_radius=border_radius*2) 

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

flagdle()