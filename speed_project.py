import pygame
import random
import time

size = width, height = 1920, 1080

pygame.init()

# цветовые коды
gray = (119, 118, 110)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

gamedisplays = pygame.display.set_mode((width, height))
pygame.display.set_caption("car racing")
clock = pygame.time.Clock()

# Загрузить изображение
player_car = pygame.image.load('car1.png')
player_car = pygame.transform.scale(player_car, (250, 500))
bot_car1 = pygame.image.load('bot car1.png')
bot_car1 = pygame.transform.scale(bot_car1, (250, 500))
bot_car2 = pygame.image.load('bot car2.png')
bot_car2 = pygame.transform.scale(bot_car2, (250, 500))
bot_car3 = pygame.image.load('bot car3.png')
bot_car3 = pygame.transform.scale(bot_car3, (250, 500))
map = pygame.image.load("race.jpg")
background_image = pygame.image.load('background.png')

car_width = 56
pause = False


def lobbi():
    lob = True
    while lob:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        gamedisplays.blit(background_image,
                          (0, 0))

        largetext = pygame.font.Font('freesansbold.ttf', 110)
        TextSurf, TextRect = text_object("CAR RACING", largetext)
        TextRect.center = (900, 100)
        gamedisplays.blit(TextSurf, TextRect)

        button("Start", 800, 600, 300, 100, green,
               bright_green, "play")

        button("Quit", 800, 900, 300, 100, red,
               bright_red, "quit")

        button("Options", 800, 750, 300,
               100, blue, bright_blue, "lobbi")

        pygame.display.update()
        clock.tick(50)


def car(x, y):
    gamedisplays.blit(player_car, (x, y))


def game_process():
    global pause
    x = (width * 0.3)
    y = (height * 0.5)
    x_change = 0
    obstacle_speed = 9
    obs = 0
    obs_startx = random.randrange(200, (width - 200))
    obs_starty = 150
    obs_height = 300
    y2 = 7

    bumped = False

    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if x + x_change > 100:
                        x_change = -5
                    else:
                        x_change = 0
                if event.key == pygame.K_RIGHT:
                    if x + x_change < 1820:
                        x_change = 5
                    else:
                        x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = 0

        if x + x_change > 1350 or x + x_change < 320:
            x += 0
        else:
            x += x_change
        pause = True

        gamedisplays.fill(gray)
        countdown_background()

        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed
        car(x, y)
        if obs_starty > height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(320,
                                          1350)
            obs = random.randrange(0, 3)

        pygame.display.update()
        clock.tick(60)


def crash():
    message_display("YOU CRASHED")


def obstacle(obs_startx, obs_starty, obs):
    global obs_pic
    if obs == 0:
        obs_pic = bot_car1
    elif obs == 1:
        obs_pic = bot_car2
    elif obs == 2:
        obs_pic = bot_car3
    elif obs == 3:
        obs_pic = player_car
    gamedisplays.blit(obs_pic, (obs_startx, obs_starty))


def text_object(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                countdown()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()

            elif action == "menu":
                lobbi()

    else:
        pygame.draw.rect(gamedisplays, ic, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_object(msg, smalltext)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    gamedisplays.blit(textsurf, textrect)


def countdown():
    countdown = True
    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        gamedisplays.fill(gray)
        countdown_background()

        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_object("3", largetext)
        TextRect.center = ((width / 2), (height / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)

        gamedisplays.fill(gray)
        countdown_background()

        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_object("2", largetext)
        TextRect.center = ((width / 2), (height / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)

        gamedisplays.fill(gray)
        countdown_background()

        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_object("1", largetext)
        TextRect.center = ((width / 2), (height / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)

        gamedisplays.fill(gray)
        countdown_background()

        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_object("GO!!!", largetext)
        TextRect.center = ((width / 2), (height / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)

        gamedisplays.fill(gray)
        countdown_background()

        game_process()


def countdown_background():
    font = pygame.font.SysFont(None, 25)
    x = (width * 0.45)
    y = (height * 0.8)
    # gamedisplays.blit(player_car, (x, y))
    gamedisplays.blit(map, (0, 0))
    text = font.render("DODGED: 0", True, black)
    score = font.render("SCORE: 0", True, red)
    gamedisplays.blit(text, (0, 50))
    gamedisplays.blit(score, (0, 30))


def text_object(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_object(text, largetext)
    textrect.center = ((width / 2), (height / 2))
    gamedisplays.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(3)
    game_process()


lobbi()
game_process()
pygame.quit()
quit()
