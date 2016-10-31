import pygame
from random import randint
import sys
from pygame.locals import*

black = (0,0,0)
white = (255,255,255)
grey = (48,48,48)
green = (0,255,0)
red = (255,0,0)
pygame.init()

size = 700,500
screen = pygame.display.set_mode(size)
background = pygame.image.load("pics/background2.png")
screen.blit(background, [0,0])
pygame.display.set_caption("Fiber HOPtics Demo")


done = False
clock = pygame.time.Clock()

ballsprite = pygame.image.load("pics/Ujjsprite.png")
ballsprite = pygame.transform.scale(ballsprite, [37,56])
wiretop = pygame.image.load("pics/GoogleFiberWire_top.png")
wiretop = pygame.transform.scale(wiretop, [70, 250])
wirebottom = pygame.image.load("pics/GoogleFiberWire.png")
wirebottom = pygame.transform.scale(wirebottom, [70, 500])

def ball(x,y,screen):
    #pygame.draw.circle(screen,black,[x,y], 20)
    #ballsprite = pygame.image.load("pics/Ujjsprite.png")
    #ballsprite = pygame.transform.scale(ballsprite, [37,56])
    screen.blit(ballsprite, [x,y])

def gameover():
    font = pygame.font.SysFont(None, 75)
    text = font.render("Game Over", True, red)
    screen.blit(text, [200, 250])

def obstacle(xloc, yloc, xsize, ysize):
    #screen.blit(wiretop, [xloc, yloc-100])
    pygame.draw.rect(screen, grey, [xloc, yloc, xsize, ysize])
    #screen.blit(wiretop, [xloc, int(yloc+ysize+space)])
    #pygame.draw.rect(screen, green, [xloc, int(yloc+ysize+space), xsize, ysize+500])
    #wirebottom = pygame.transform.scale(wirebottom, [xsize, ysize+500])
    screen.blit(wirebottom, [xloc, int(yloc+ysize+space)])

def Score(score):
    font = pygame.font.SysFont(None, 100)
    text = font.render(str(score), True, white)
    screen.blit(text, [0,0])
    # obspeed should increase when the score increases

x = 350
y = 250
x_speed = 0
y_speed = 0
ground = 437
xloc = 700
yloc = 0
xsize = 70
ysize = randint(0,200)
space = 150
obspeed = 2.5
score = 0

def flappy():
    black = (0,0,0)
    white = (255,255,255)
    green = (0,255,0)
    red = (255,0,0)
    pygame.init()

    size = 700,500
    screen = pygame.display.set_mode(size)
    background = pygame.image.load("pics/background2.png")
    screen.blit(background, [0,0])
    pygame.display.set_caption("Fiber HOPtics Demo")


    done = False
    clock = pygame.time.Clock()

    ballsprite = pygame.image.load("pics/Ujjsprite.png")
    ballsprite = pygame.transform.scale(ballsprite, [37,56])
    wiretop = pygame.image.load("pics/GoogleFiberWire_top.png")
    wiretop = pygame.transform.scale(wiretop, [70, 250])
    wirebottom = pygame.image.load("pics/GoogleFiberWire.png")
    wirebottom = pygame.transform.scale(wirebottom, [70, 500])
    x = 350
    y = 250
    x_speed = 0
    y_speed = 0
    ground = 437
    xloc = 700
    yloc = 0
    xsize = 70
    ysize = randint(0,200)
    space = 150
    obspeed = 2.5
    score = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_speed = -8

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    y_speed = 5

        background = pygame.image.load("pics/background2.png")
        screen.blit(background, [0,0])

        obstacle(xloc, yloc, xsize, ysize)
        ball(x,y,screen)
        Score(score)

        y += y_speed
        xloc -= obspeed

        if y > ground:
            gameover()
            y_speed = 0
            obspeed = 0
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        flappy()

        if x+39 > xloc and y-4 < ysize and x-1 < xsize+xloc:
            gameover()
            obspeed = 0
            y_speed = 0
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        flappy()
                        
        if x+39 > xloc and y+58 > ysize+space and x-1 < xsize+xloc:
            gameover()
            obspeed = 0
            y_speed = 0
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        flappy()
                        
        if xloc < -80:
            xloc = 700
            ysize = randint(0,300)

        if x > xloc and x < xloc+3:
            score = (score + 1)


        pygame.display.flip()
        clock.tick(60)
    
flappy()
pygame.quit()
