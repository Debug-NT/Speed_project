import sys

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
mask_bot1 = pygame.mask.from_surface(bot_car1)
bot_car2 = pygame.image.load('bot car2.png')
bot_car2 = pygame.transform.scale(bot_car2, (250, 500))
bot_car3 = pygame.image.load('bot car3.png')
bot_car3 = pygame.transform.scale(bot_car3, (250, 500))
map = pygame.image.load("race.jpg")
background_image = pygame.image.load('background.png')

car_width = 56
pause = False

bots = pygame.sprite.Group()


class Player_Mask(pygame.sprite.Sprite):
    image = player_car

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Player_Mask.image
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(600, 600)
        self.mask = pygame.mask.from_surface(self.image)


class Bot(pygame.sprite.Sprite):
    image = bot_car1

    def __init__(self, name_png):
        global image
        super().__init__(bots)
        if name_png == 0:
            image = bot_car1
        elif name_png == 1:
            image = bot_car2
        elif name_png == 2:
            image = bot_car3
        elif name_png == 3:
            image = player_car
        self.bot_image = Bot.image
        self.rect = self.bot_image.get_rect()
        self.bot_mask = pygame.mask.from_surface(self.bot_image)

    def check_crash(self):
        if pygame.sprite.collide_mask(self, maskplay):
            return True


class gameplay():

    def __init__(self):
        super().__init__()
        self.bot_mask1 = pygame.mask.from_surface(bot_car1)
        self.rect = bot_car1.get_rect()
        self.image = pygame.image.load('bot car1.png')

    def lobbi(self):
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
            TextSurf, TextRect = self.text_object("CAR RACING", largetext)
            TextRect.center = (900, 100)
            gamedisplays.blit(TextSurf, TextRect)

            self.button("Start", 800, 600, 300, 100, green,
                        bright_green, "play")

            self.button("Quit", 800, 900, 300, 100, red,
                        bright_red, "quit")

            self.button("Options", 800, 750, 300,
                        100, blue, bright_blue, "lobbi")

            pygame.display.update()
            clock.tick(50)

    def car(self, x, y):
        gamedisplays.blit(player_car, (x, y))

    def game_process(self):
        global pause
        x = (width * 0.3)
        y = (height * 0.5)
        x_change = 0
        obstacle_speed = 9
        obs = 0
        obs_startx = random.randrange(200, (width - 200))
        obs_starty = 300
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
                            x_change = -20
                        else:
                            x_change = 0
                    if event.key == pygame.K_RIGHT:
                        if x + x_change < 1820:
                            x_change = 20
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
            maskplay.rect.x = x
            pause = True

            gamedisplays.fill(gray)
            self.countdown_background()
            MYEVENTTYPE = pygame.USEREVENT + 1
            pygame.time.set_timer(MYEVENTTYPE, 10)
            Bot(obs)
            self.obstacle(obs_startx, obs_starty, obs)
            for bot in bots:
                if bot.check_crash():
                    self.crash()
                    bumped = True

            obs_starty += obstacle_speed
            self.car(x, y)
            if obs_starty > height:
                obs_starty = 0 - obs_height
                obs_startx = random.randrange(320,
                                              1350)
                obs = random.randrange(0, 3)

            # if Bot.check_crash():
            #     self.crash()
            pygame.display.update()
            clock.tick(60)
            pygame.time.set_timer(MYEVENTTYPE, 0)
            for bot in bots:
                bot.kill()

    def crash(self):
        self.message_display("YOU CRASHED")



    def obstacle(self, obs_startx, obs_starty, obs):
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
        for bot in bots:
            bot.rect.x = obs_startx
            bot.rect.y = obs_starty

    def text_object(self, text, font):
        textsurface = font.render(text, True, black)
        return textsurface, textsurface.get_rect()

    def button(self, msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gamedisplays, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                if action == "play":
                    self.countdown()
                elif action == "quit":
                    pygame.quit()
                    quit()
                    sys.exit()

                elif action == "menu":
                    self.lobbi()

        else:
            pygame.draw.rect(gamedisplays, ic, (x, y, w, h))
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textsurf, textrect = self.text_object(msg, smalltext)
        textrect.center = ((x + (w / 2)), (y + (h / 2)))
        gamedisplays.blit(textsurf, textrect)

    def countdown(self):
        countdown = True
        while countdown:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()

            gamedisplays.fill(gray)
            self.countdown_background()

            largetext = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = self.text_object("3", largetext)
            TextRect.center = ((width / 2), (height / 2))
            gamedisplays.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)

            gamedisplays.fill(gray)
            self.countdown_background()

            largetext = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = self.text_object("2", largetext)
            TextRect.center = ((width / 2), (height / 2))
            gamedisplays.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)

            gamedisplays.fill(gray)
            self.countdown_background()

            largetext = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = self.text_object("1", largetext)
            TextRect.center = ((width / 2), (height / 2))
            gamedisplays.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)

            gamedisplays.fill(gray)
            self.countdown_background()

            largetext = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = self.text_object("GO!!!", largetext)
            TextRect.center = ((width / 2), (height / 2))
            gamedisplays.blit(TextSurf, TextRect)
            pygame.display.update()
            clock.tick(1)

            gamedisplays.fill(gray)
            self.countdown_background()

            self.game_process()

    def countdown_background(self):
        font = pygame.font.SysFont(None, 25)
        x = (width * 0.45)
        y = (height * 0.8)
        # gamedisplays.blit(player_car, (x, y))
        gamedisplays.blit(map, (0, 0))
        text = font.render("DODGED: 0", True, black)
        score = font.render("SCORE: 0", True, red)
        gamedisplays.blit(text, (0, 50))
        gamedisplays.blit(score, (0, 30))

    def text_object(self, text, font):
        textsurface = font.render(text, True, black)
        return textsurface, textsurface.get_rect()

    def message_display(self, text):
        largetext = pygame.font.Font("freesansbold.ttf", 80)
        textsurf, textrect = self.text_object(text, largetext)
        textrect.center = ((width / 2), (height / 2))
        gamedisplays.blit(textsurf, textrect)
        pygame.display.update()
        time.sleep(3)
        self.game_process()


all_sprites = pygame.sprite.Group()
maskplay = Player_Mask()
gameplay().lobbi()
pygame.quit()
quit()
