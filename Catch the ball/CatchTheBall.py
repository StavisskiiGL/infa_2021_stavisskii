import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    """ рисует новый шарик """
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 700)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(counter):
    """Проводит операции, связанные с реагированием программы на нажатие кнопки
        counter - текущий счетчик попаданий по шарику
    """
    global clicked
    print('Click!')
    if (pygame.mouse.get_pos()[0] - x) ** 2 + (pygame.mouse.get_pos()[1] - y) ** 2 <= r ** 2:
        counter += 1
        clicked = True
        print("You got a hit! Total number of strikes:", counter)
    else:
        print("You missed! Try again. Total number of strikes:", counter)
        clicked = True
    return counter


clock = pygame.time.Clock()
finished = False
counter = 0  # счетчик
clicked = False  # булевое значение, определяющее нажали ли мы конпку мыши
new_ball()
pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            counter = click(counter)
    if clicked:
        screen.fill(BLACK)
        new_ball()
        pygame.display.update()
        clicked = False

pygame.quit()
