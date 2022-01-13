import pygame, sys, os
from pygame.locals import *

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED']='1'

# Game Resolution
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

pista = pygame.image.load("images/pista_tenis_800x600.png")

# Color
black=(0, 0, 0)
white=(255, 255, 255)
blue=(0, 0, 255)

# Framerate
clock=pygame.time.Clock()
fps=200

# Initial Variables
lineWidth=10
paddleSize=50
paddleOffset=20


def BackgroundGameplay():
    screen.fill(black)
    pygame.draw.line(screen, white, ((screen_width / 2), 0), ((screen_width / 2), screen_height), 2)
    pygame.draw.rect(screen, blue, ((0, 0), (screen_width, screen_height)), lineWidth)
    screen.blit(pista, (0,0) )

def Paddle(paddle):
    if paddle.bottom > screen_height - lineWidth:
        paddle.bottom = screen_height - lineWidth
    elif paddle.top < lineWidth:
        paddle.top = lineWidth

    pygame.draw.rect(screen, white, paddle)

def Ball(ball):
    pygame.draw.rect(screen, white, ball)

def BallMovement(ball, ballDirX, ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY
    return ball


def main():

    ballPosX=screen_width/2 - lineWidth/2
    ballPosY=screen_height/2 - lineWidth/2

    playerPos=(screen_height-paddleSize)/2
    enemyPos=(screen_height-paddleSize)/2
    score=0

    ballDirX = -1
    ballDirY = -1

    paddle1=pygame.Rect(paddleOffset, playerPos, lineWidth, paddleSize)
    paddle2 = pygame.Rect(screen_width - paddleOffset - lineWidth, enemyPos, lineWidth, paddleSize)
    ball=pygame.Rect(ballPosX, ballPosY, lineWidth, lineWidth)

    BackgroundGameplay()
    Paddle(paddle1)
    Paddle(paddle2)
    Ball(ball)
    pygame.mouse.set_visible(0)
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEMOTION:
                mousex, mousey=event.pos
                print("Ratón: (x,y)=(", mousex, ", ", mousey)                
                paddle1.y=mousey

        BackgroundGameplay()
        Paddle(paddle1)
        Paddle(paddle2)
        Ball(ball)

        ball=BallMovement(ball, ballDirX, ballDirY)
        
        pygame.display.set_caption('Python - Pygame Simple Arcade Game')
        pygame.display.update()
        clock.tick(fps)




if __name__=='__main__':
    main()
