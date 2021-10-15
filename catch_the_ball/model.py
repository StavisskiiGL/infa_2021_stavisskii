import math
from math import sqrt, sin, cos
from random import randint, random

from colors import *


FPS = 240
level = 1
counter = 0  # очки


def init():
    global P_LIST, T_LIST, time, clicked
    P_LIST = [_new_ball()]
    T_LIST = []
    time = 1
    clicked = False  # булевое значение, определяющее попали ли мы по какой-либо фигуре или нет"


def _move_ball(params):
    """ создается кортеж новых параметров для шаров
        params - кортеж параметров старого состояния шарика
        new_params - кортеж параметров нового состояния шарика
    """
    new_params = (
        params[0] + params[6] / FPS, params[1] + params[7] / FPS, params[2], params[3], params[4], params[5], params[6],
        params[7])
    return new_params


def _move_triangle(params):
    """ создается кортеж новых параметров для треугольника
        params - кортеж параметров старого состояния треугольника
        new_params - кортеж параметров нового состояния треугольника
    """
    x_m_new = params[14] + params[10] / FPS
    y_m_new = params[15] + params[11] / FPS
    phi_new = params[12] + params[13] / FPS
    x_1_new = x_m_new - sqrt(3) / 3 * params[9] * sin(math.pi / 3 + phi_new)
    y_1_new = y_m_new + sqrt(3) / 3 * params[9] * cos(math.pi / 3 + phi_new)
    x_2_new = x_m_new + sqrt(3) / 3 * params[9] * sin(math.pi / 3 - phi_new)
    y_2_new = y_m_new + sqrt(3) / 3 * params[9] * cos(math.pi / 3 - phi_new)
    x_3_new = x_m_new + sqrt(3) / 3 * params[9] * sin(phi_new)
    y_3_new = y_m_new - sqrt(3) / 3 * params[9] * cos(phi_new)
    new_params = (x_1_new, y_1_new, x_2_new, y_2_new, x_3_new, y_3_new, params[6], params[7], params[8], params[9],
                  params[10], params[11], phi_new, params[13], x_m_new, y_m_new)
    return new_params


def _new_ball():
    """ рисует новый шарик
        params - кортеж параметров нового шарика
    """
    r = randint(10, 100)
    x = randint(r, 1200 - r)
    y = randint(r, 700 - r)
    v_y = randint(-500, 500)
    v_x = randint(-500, 500)
    color = COLORS[randint(0, 5)]
    params = (x, y, color[0], color[1], color[2], r, v_x, v_y)
    return params


def _new_triangle():
    """ рисует новый треугольник
        params - кортеж параметров нового треугольника
    """
    a = randint(20, 200)
    x_1 = randint(100, 1200)
    y_1 = randint(100, 700)
    x_2 = x_1 + a
    y_2 = y_1
    x_3 = x_1 + a / 2
    y_3 = y_2 - sqrt(3) / 2 * a
    x_m = x_3
    y_m = y_1 - sqrt(3) / 6 * a
    phi = random() * (2 * math.pi / 3)
    x_1 = x_m - sqrt(3) / 3 * a * sin(math.pi / 3 + phi)
    y_1 = y_m + sqrt(3) / 3 * a * cos(math.pi / 3 + phi)
    x_2 = x_m + sqrt(3) / 3 * a * sin(math.pi / 3 - phi)
    y_2 = y_m + sqrt(3) / 3 * a * cos(math.pi / 3 - phi)
    x_3 = x_m + sqrt(3) / 3 * a * sin(phi)
    y_3 = y_m - sqrt(3) / 3 * a * cos(phi)
    v_y = randint(-500, 500)
    v_x = randint(-500, 500)
    w = random() * 2 * math.pi
    color = COLORS[randint(0, 5)]
    params = (x_1, y_1, x_2, y_2, x_3, y_3, color[0], color[1], color[2], a, v_x, v_y, phi, w, x_m, y_m)
    return params


def tick():
    global P_LIST, T_LIST, time, clicked
    # породить новые игровые объекты (по времени)
    if time % (FPS / level) == 0:
        P_LIST.append(_new_ball())
    if time % (3 * FPS / level) == 0:
        T_LIST.append(_new_triangle())

    for i in range(0, len(P_LIST)):
        params = P_LIST[i]
        if params[1] - params[5] <= 0:
            params = (
                params[0], params[1], params[2], params[3], params[4], params[5], randint(-500, 500), randint(100, 500))
        if params[1] + params[5] >= 700:
            params = (
                params[0], params[1], params[2], params[3], params[4], params[5], randint(-500, 500),
                randint(-500, -100))
        if params[0] - params[5] <= 0:
            params = (
                params[0], params[1], params[2], params[3], params[4], params[5], randint(100, 500), randint(-500, 500))
        if params[0] + params[5] >= 1200:
            params = (
                params[0], params[1], params[2], params[3], params[4], params[5], randint(-500, -100),
                randint(-500, 500))
        params = _move_ball(params)
        P_LIST[i] = params

    for i in range(0, len(T_LIST)):
        params = T_LIST[i]
        params = _move_triangle(params)
        T_LIST[i] = params

    clicked = False
    time += 1



def _area_triangle_a(x_1, y_1, x_2, y_2, x_3, y_3, a):
    """ считает площадь треугольника с стороной длины a, координаты вершин которой (2) и (3) и вершиной (1)
        x_1, y_1 - соответственные координаты вершины (1)
        x_2, y_2 - соответственные координаты вершины (2)
        x_3, y_3 - соответственные координаты вершины (3)
        a - длина стороны, привязанной к вершинам (2) и (3)
    """
    p = (a + sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) + sqrt((x_1 - x_3) ** 2 + (y_1 - y_3) ** 2)) / 2
    return sqrt(
        p * (p - a) * (p - sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)) * (p - sqrt((x_1 - x_3) ** 2 + (y_1 - y_3) ** 2)))


def _click_circle(counter, params, mouse_pos):
    """ Проводит операции, связанные с реагированием программы на нажатие кнопки
        counter - текущий счетчик попаданий по фигурам
        params - кортеж с параметрами проверяемого шарика
    """
    x = params[0]
    y = params[1]
    r = params[5]
    global clicked
    if (mouse_pos[0] - x) ** 2 + (mouse_pos[1] - y) ** 2 <= r ** 2:
        counter += 1
        clicked = True
        print("You got a hit! Total number of strikes:", counter)
    return counter


def _click_triangle(counter, params, mouse_pos):
    """ Проводит операции, связанные с реагированием программы на нажатие кнопки
        counter - текущий счетчик попаданий по фигурам
        params - кортеж с параметрами проверяемого треугольника
        :return: количество очков
    """
    global clicked
    if abs((area_triangle_a(mouse_pos[0], mouse_pos[1], params[0], params[1], params[2],
                            params[3], params[9]) + _area_triangle_a(mouse_pos[0],
                                                                     mouse_pos[1], params[2], params[3],
                                                                     params[4], params[5], params[9]) + area_triangle_a(
            mouse_pos[0], mouse_pos[1], params[0], params[1], params[4], params[5],
            params[9]) - sqrt(3) / 4 * (params[9]) ** 2)) <= 0.1:
        print("Nice hit! Total number of strikes:", counter)
        clicked = True
        return 3  # количество очков за успешное попадание
    return 0


def handler(mouse_pos):
    start = counter
    for i in range(0, len(P_LIST)):
        counter = _click_circle(counter, P_LIST[i])
        if counter > start:
            circle(screen, (0, 0, 0), (P_LIST[i][0], P_LIST[i][1]), P_LIST[i][5])
            P_LIST.pop(i)
            break
    start = counter
    for i in range(0, len(T_LIST)):
        counter = _click_triangle(counter, T_LIST[i])
        if counter > start:
            polygon(screen, (0, 0, 0), [(T_LIST[i][0], T_LIST[i][1]), (T_LIST[i][2], T_LIST[i][3]), (T_LIST[i][4], T_LIST[i][5])])
            T_LIST.pop(i)
            break
    if not clicked:
        print("You missed! Try again.")
