import pygame
import random
from pygame.locals import *

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750

x1 = 250
x2 = 450

y = 350
paddle_width = 40
paddle_height = 100
ball_width = 15
ball_height = 15
paddle_vel = .05
ball_vel = 1

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong')


def pong_ball(ballxpos, ballypos):
    screen.fill((0, 0, 0))
    ball = pygame.draw.ellipse(screen, (255, 255, 255), (ballxpos, ballypos, ball_width, ball_height))
    horz = random.randint()
    vert = random.randint()



def paddles():
    ui_left_paddle = pygame.draw.rect(screen, (255, 255, 255), (10, WINDOW_HEIGHT/2, paddle_width, paddle_height))
    ui_top_paddle = pygame.draw.rect(screen, (255, 255, 255), (x1, 10, paddle_height, paddle_width))
    ui_bot_paddle3 = pygame.draw.rect(screen, (255, 255, 255), (x1, 700, paddle_height, paddle_width))
    right_paddle = pygame.draw.rect(screen, (255, 255, 255), (700, y, paddle_width, paddle_height))
    up_horizontal_paddle = pygame.draw.rect(screen, (255, 255, 255), (x2, 10, paddle_height, paddle_width))
    bot_horizontal_paddle = pygame.draw.rect(screen, (255, 255, 255), (x2, 700, paddle_height, paddle_width))


# Main Loop


quit_game = False
while not quit_game:
    for event in pygame.event.get():  # quit?
        if event.type == QUIT:
            quit_game = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x2 > WINDOW_WIDTH/2 - paddle_vel:
        x2 -= paddle_vel
    if keys[pygame.K_RIGHT] and x2 < WINDOW_WIDTH - paddle_height - paddle_vel:
        x2 += paddle_vel
    if keys[pygame.K_UP] and y > paddle_vel:
        y -= paddle_vel
    if keys[pygame.K_DOWN] and y < WINDOW_HEIGHT - paddle_height - paddle_vel:
        y += paddle_vel

    pong_ball(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    paddles()
    pygame.display.update()

pygame.quit()

