
import pygame
import pyglet as pyglet
from pygame.draw import *

import model
from colors import *

import pyglet
loop = True
while loop:
    print("Hello! Do you want to listen to music during your game session? Y/N")
    ans = input()
    if ans == 'Y' or ans == 'y':
        print("Then select volume, print a num 0 - 1")
        volume = float(input())
        loop = False
    elif ans == 'N' or ans == 'n':
        print("Ok, but you are missing a lot!")
        volume = 0
        loop = False
    else:
        print("Wrong input! Starting again")
        loop = True


sound = pyglet.media.load('undertale_031. Waterfall.mp3', streaming=False)
player = pyglet.media.Player()
player.volume = volume
player.queue(sound)
player.loop = True
player.play()



def draw_ball(params):
    """ отображает один шарик """
    circle(screen, (params[2], params[3], params[4]),
           (params[0], params[1]), params[5])


def draw_triangle(params):
    """ отображает один треугольник """
    polygon(screen, (params[6], params[7], params[8]),
            [(params[0], params[1]),
             (params[2], params[3]),
             (params[4], params[5])])


pygame.init()
screen = pygame.display.set_mode((1200, 700))

print("Enter players nickname:")
Name = input()
print("Select and type 'difficulty' (relaxation) level : 1; 2; 3; 4; 5; 6; 8; 10")
level = int(input())
model.init()

clock = pygame.time.Clock()
finished = False
pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            model.write_leaderboard(Name)
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            model.handler(pygame.mouse.get_pos())
    # вызов обсчёта модели
    model.tick(level)

    # отображение всех объектов
    screen.fill(BLACK)
    for ball in model.CIRCLE_LIST:
        draw_ball(ball)
    for triangle in model.TRIANGLE_LIST:
        draw_triangle(triangle)
    pygame.display.update()


pygame.quit()
