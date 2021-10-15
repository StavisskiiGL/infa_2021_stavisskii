import pygame
from pygame.draw import *

import model
from colors import *


def draw_ball(params):
    """ отображает один шарик """
    circle(screen, (params[2], params[3], params[4]),
           (params[0], params[1]), params[5])


def draw_triangle(params):
    """ отображает один треугольник """
    #polygon(screen, (params[6], params[7], params[8]), [(x_1_new, y_1_new), (x_2_new, y_2_new), (x_3_new, y_3_new)])
    polygon(screen, (params[6], params[7], params[8]),
            [(params[0], params[1]),
             (params[2], params[3]),
             (params[4], params[5])])


pygame.init()
screen = pygame.display.set_mode((1200, 700))

# print("Select and type difficulty level : 1; 2; 3; 4; 5; 6; 8; 10")
model.init()

clock = pygame.time.Clock()
finished = False
pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            model.handler(pygame.mouse.get_pos())
    # вызов обсчёта модели
    model.tick()

    # отображение всех объектов
    screen.fill(BLACK)
    for ball in model.P_LIST:
        draw_ball(ball)
    for triangle in model.T_LIST:
        draw_triangle(triangle)
    pygame.display.update()


pygame.quit()
