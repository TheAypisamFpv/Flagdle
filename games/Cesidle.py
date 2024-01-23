import os, sys, random, pygame, high_score_saver
from pygame.locals import *


pygame.init()
clock = pygame.time.Clock() 
# constants
# screen
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cesidle")
SKILL_ISSUE = "games\\skill issue.png"
# colors
GREY = (40, 40, 40)

# set background color to grey
screen.fill(GREY)

global QUESTIONS_PATH, QUESTIONS_PATH_LIST
# countrys
DEFAULT_PATH = "games\\cesidle"
QUESTIONS_PATH = "games\\cesidle"
QUESTIONS_PATH_LIST = os.listdir(QUESTIONS_PATH)
# lives
global LIVES, lives, SCORE, HIGH_SCORE, LIVES_POS, SCORE_POS, GUESS_POS, TEXT_WIDTH, border_radius, base_font, big_font, user_text, WIDTH, HEIGHT, input_rect, unactiv_color, activ_color, active, guess
LIVES = len(QUESTIONS_PATH_LIST)
lives = 0

# score
SCORE = 0
HIGH_SCORE = SCORE

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
def load_questions():
    questions = []
    
    if len(os.listdir(QUESTIONS_PATH)) == 0:
        screen.fill(GREY)
        screen.blit(big_font.render(f"No questions found in ", True, (255, 100, 100), (0, 0, 0)), (SCREEN_WIDTH/2-490, SCREEN_HEIGHT/2 - 100))
        screen.blit(big_font.render(f"'{QUESTIONS_PATH}'", True, (255, 100, 100), (0, 0, 0)), (SCREEN_WIDTH/2-500, SCREEN_HEIGHT/2))
        pygame.display.flip()
        pygame.time.wait(1000)
        return []
        # pygame.quit()
        # sys.exit()

    for question in os.listdir(QUESTIONS_PATH):
        if "_postanwser" not in question and question.endswith(".png"):
            questions.append(question.rsplit(".", 1)[0])
    return questions

def random_questions(questions, current_question):
    question = current_question
    if len(questions) == 1:
        return questions[0]
    else:
        while question == current_question:
            question = random.choice(questions)
        
    return question

def return_to_laucher():
    if pygame.display.get_caption()[0] != "Cesidle":
        high_score_saver.save_score(HIGH_SCORE, pygame.display.get_caption()[0])
        
    launcher_path = 'GameLauncher.py'
    pygame.quit()
    os.system(f'python {launcher_path}')
    sys.exit()


def show_current_mode(index):
    mode = QUESTIONS_PATH_LIST[index]
    screen.fill(GREY)
    #show the current mode
    screen.blit(big_font.render(f"{mode}", True, (255, 255, 255), (0, 0, 0)), (SCREEN_WIDTH/2-500, SCREEN_HEIGHT/2 - 100))
    pygame.display.flip()
    pygame.time.wait(3000)
    


def show_image(image_path):
    image = pygame.image.load(image_path).convert()
    image_width = image.get_width()
    image_height = image.get_height()
    # rezise the country to fit in the screen, without changing the aspect ratio
    if image_width > SCREEN_WIDTH:
        image = pygame.transform.scale(image, (SCREEN_WIDTH, int(image_height*SCREEN_WIDTH/image_width)))
    if image_height > SCREEN_HEIGHT:
        image = pygame.transform.scale(image, (int(image_width*SCREEN_HEIGHT/image_height), SCREEN_HEIGHT))

    screen.blit(image, (SCREEN_WIDTH/2 - image.get_width()/2, SCREEN_HEIGHT/2 - image.get_height()/2))


def Cesidle():
    global QUESTIONS_PATH, LIVES, SCORE, HIGH_SCORE, lives, guess, active, user_text, input_rect, WIDTH, HEIGHT, unactiv_color, activ_color, button_vertical_sepraration, border_radius, base_font, big_font, SCREEN_WIDTH, SCREEN_HEIGHT, screen, LIVES_POS, SCORE_POS, GUESS_POS, TEXT_WIDTH, clock, GREY, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, screen, QUESTIONS_PATH, LIVES, lives, SCORE, LIVES_POS, SCORE_POS, GUESS_POS, TEXT_WIDTH, border_radius, base_font, big_font, user_text, WIDTH, HEIGHT, input_rect, unactiv_color, activ_color, active, guess
    questions = []
    
    index = 0
    show_current_mode(index)
    
    QUESTIONS_PATH = DEFAULT_PATH+"\\"+QUESTIONS_PATH_LIST[index]
    questions = load_questions()


    question = random_questions(questions, "")

    HIGH_SCORE = high_score_saver.get_score(pygame.display.get_caption()[0])

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
                    final_text = ''.join(user_text)
                    
                    if final_text.lower() == question.lower():
                        SCORE += 1
                        lives = 0
                        questions.remove(question)
                        guess = True
                        # check if there is a postanwser image
                        if os.path.isfile(os.path.join(QUESTIONS_PATH, question+"_postanwser.png")):
                            show_image(os.path.join(QUESTIONS_PATH, question+"_postanwser.png"))
                            pygame.display.flip()
                            pygame.time.wait(5000)
                    else:
                        guess = False
                        lives = -1
                        SCORE -= 1
                        LIVES -= 1
                    
                    user_text = []
                    prev_country = question
                    if len(questions) == 0:
                        if index < len(QUESTIONS_PATH_LIST)-1:
                            LIVES += 1
                            index += 1
                            QUESTIONS_PATH = DEFAULT_PATH+"\\"+QUESTIONS_PATH_LIST[index]
                            show_current_mode(index)
                        else:
                            screen.fill(GREY)
                            screen.blit(big_font.render(f"You Win !", True, (100, 255, 100), (0, 0, 0)), (SCREEN_WIDTH/2-375, SCREEN_HEIGHT/2 - 100))
                            high_score_saver.save_score(HIGH_SCORE, pygame.display.get_caption()[0])
                            pygame.display.flip()
                            pygame.time.wait(1000)
                            # restart the game
                            return_to_laucher()
                        questions = load_questions()
                        guess = None
                        
                    question = random_questions(questions, question)
                    active = False

                # Unicode standard is used for string 
                # formation 
                elif event.key != pygame.K_BACKSPACE: 
                    user_text.append(event.unicode)

        screen.fill(GREY)
        if LIVES <= 0:
            # display game over on the center of the screen
            screen.blit(big_font.render("Game over !", True, (255, 100, 100), (0, 0, 0)), (SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2 - 100))
            show_image(SKILL_ISSUE)
            pygame.display.flip()
            pygame.time.wait(1000)
            # restart the game
            LIVES = 5
            SCORE = 0
            questions = load_questions()
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


        #show image
        show_image(os.path.join(QUESTIONS_PATH, question+".png"))


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

        high_score_text = base_font.render("High score: " + str(HIGH_SCORE), True, (255, 255, 255))
        high_score_rect = pygame.Rect(HIGH_SCORE_POS[0], HIGH_SCORE_POS[1], high_score_text.get_width()+border_radius, high_score_text.get_height()+border_radius)
        pygame.draw.rect(screen, (50,50,50), high_score_rect, border_radius=border_radius)
        screen.blit(high_score_text, (high_score_rect.x + high_score_rect.width/2 - high_score_text.get_width()/2, high_score_rect.y + high_score_rect.height/2 - high_score_text.get_height()/2))
        

        if type(guess) == bool:
            if guess:
                guezz_text = base_font.render("Good guezz !", True, (100, 255, 100))
            else:
                guezz_text = base_font.render(f"Wrong guezz", True, (255, 100, 100))
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

try:
    Cesidle()
except Exception as e:
    print(e)
    return_to_laucher()