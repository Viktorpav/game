import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("C:/Python Project/Game/audio/crash_sound.ogg")
pygame.mixer.music.load("C:/Python Project/Game/audio/pause_sound.mp3")

display_width = 1280
display_height = 640

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
blue = (0, 0, 200)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

block_color = (53, 120, 230)

car_width = 151

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Vicar')

clock = pygame.time.Clock()

carImg = pygame.image.load("C:\Python Project\Game\pictures\Car(Python).png")
gameIcon = pygame.image.load("C:\Python Project\Game\pictures\Car(icon).png")

pygame.display.set_icon(gameIcon)

pause = False

#crash = True


def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImg,(x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, bright_red)
    return textSurface, textSurface.get_rect()

# def message_display(text):
#     largeText = pygame.font.SysFont("comicsansms", 115)
#     TextSurf, TextRect = text_objects(text, largeText)
#     TextRect.center = ((display_width/2), (display_height/2))
#     gameDisplay.blit(TextSurf, TextRect)
#
#     pygame.display.update()
#
#     time.sleep(2)
#
#     game_loop()

def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(white)


        button("Play Again", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 1050, 450, 100, 50, blue, bright_blue, quitgame)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():

    pygame.mixer.music.pause()

    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)


        button("Continue", 150, 450, 100, 50, green, bright_green, unpause)
        button("Quit", 1050, 450, 100, 50, blue, bright_blue, quitgame)

        pygame.display.update()
        clock.tick(15)



def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Vicar Game", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 1050, 450, 100, 50, blue, bright_blue, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.65)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -15
                if event.key == pygame.K_RIGHT:
                    x_change = 15
                if event.key == pygame.K_p:
                    pause = True
                    paused()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)

        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            print('step 1')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('step 2')
                crash()

        pygame.display.update()
        clock.tick(30)

game_intro()
game_loop()
pygame.quit()
quit()