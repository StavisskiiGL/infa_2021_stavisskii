import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def move_ball(params):
    new_params = (params[0] + params[6] / FPS, params[1] + params[7] / FPS, params[2], params[3], params[4], params[5], params[6], params[7])
    screen.fill(BLACK)
    circle(screen, (new_params[2], new_params[3], new_params[4]), (new_params[0], new_params[1]), new_params[5])
    pygame.display.update()
    return new_params


def new_ball():
    """ рисует новый шарик """
    r = randint(10, 100)
    x = randint(r, 1200 - r)
    y = randint(r, 700 - r)
    v_y = randint(-500, 500)
    v_x = randint(-500, 500)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    params = (x, y, color[0], color[1], color[2], r, v_x, v_y)
    return params


def click(counter, params):
    """Проводит операции, связанные с реагированием программы на нажатие кнопки
        counter - текущий счетчик попаданий по шарику
    """
    x = params[0]
    y = params[1]
    r = params[5]
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


clicked = False  # булевое значение, определяющее нажали ли мы конпку мыши"
params = new_ball()

clock = pygame.time.Clock()
finished = False
counter = 0  # счетчик
pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            counter = click(counter, params)
    if clicked:
        screen.fill(BLACK)
        params = new_ball()
        pygame.display.update()
        clicked = False
    else:
        if params[1] - params[5] <= 0:
            params = (params[0], params[1], params[2], params[3], params[4], params[5], randint(-500, 500), randint(100, 500))
        if params[1] + params[5] >= 700:
            params = (params[0], params[1], params[2], params[3], params[4], params[5], randint(-500, 500), randint(-500, -100))
        if params[0] - params[5] <= 0:
            params = (params[0], params[1], params[2], params[3], params[4], params[5], randint(100, 500), randint(-500, 500))
        if params[0] + params[5] >= 1200:
            params = (params[0], params[1], params[2], params[3], params[4], params[5], randint(-500, -100), randint(-500, 500))
        params = move_ball(params)

pygame.quit()
