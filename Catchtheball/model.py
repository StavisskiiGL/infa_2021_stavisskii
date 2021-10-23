import math
from math import sqrt, sin, cos
from random import randint, random
from colors import *


FPS = 240
level = 1
clicked = False  # булевое значение, определяющее попали ли мы по какой-либо фигуре или нет"
counter = 0


def init():
    """ Создание основных массивов и счетчиков"""
    global CIRCLE_LIST, TRIANGLE_LIST, time, clicked
    CIRCLE_LIST = [_new_ball()]
    TRIANGLE_LIST = []
    time = 1


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


def tick(level):
    """ Функция, применяющая к модели ее изменения во времени
        level - уровень релаксации от 1 до 10
    """
    global CIRCLE_LIST, TRIANGLE_LIST, time, clicked
    # породить новые игровые объекты (по времени)
    if time % (FPS / level) == 0:
        CIRCLE_LIST.append(_new_ball())
    if time % (3 * FPS / level) == 0:
        TRIANGLE_LIST.append(_new_triangle())

    for i in range(0, len(CIRCLE_LIST)):
        params = CIRCLE_LIST[i]
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
        CIRCLE_LIST[i] = params

    for i in range(0, len(TRIANGLE_LIST)):
        params = TRIANGLE_LIST[i]
        params = _move_triangle(params)
        TRIANGLE_LIST[i] = params

    clicked = False
    time += 1



def _area_triangle_a(x_1, y_1, x_2, y_2, x_3, y_3, a):
    """ считает площадь треугольника с стороной длины a, координаты вершин которой (2) и (3) и вершиной (1)
        x_1, y_1 - соответственные координаты вершины (1)
        x_2, y_2 - соответственные координаты вершины (2)
        x_3, y_3 - соответственные координаты вершины (3)
        a - длина стороны, привязанной к вершинам (2) и (3)
        :return: плошадь соответственного координатам и стороне треугольника
    """
    p = (a + sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) + sqrt((x_1 - x_3) ** 2 + (y_1 - y_3) ** 2)) / 2
    return sqrt(
        p * (p - a) * (p - sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)) * (p - sqrt((x_1 - x_3) ** 2 + (y_1 - y_3) ** 2)))


def _click_circle(counter, params, mouse_pos):
    """ Проводит операции, связанные с реагированием программы на нажатие кнопки
        counter - текущий счетчик попаданий по фигурам
        params - кортеж с параметрами проверяемого шарика
        mouse_pos - координаты курсора мыши на экране
        :return: количество очков
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
        mouse_pos - координаты курсора мыши на экране
        :return: количество очков
    """
    global clicked
    if abs((_area_triangle_a(mouse_pos[0], mouse_pos[1], params[0], params[1], params[2],
                            params[3], params[9]) + _area_triangle_a(mouse_pos[0],
                                                                     mouse_pos[1], params[2], params[3],
                                                                     params[4], params[5], params[9]) + _area_triangle_a(
            mouse_pos[0], mouse_pos[1], params[0], params[1], params[4], params[5],
            params[9]) - sqrt(3) / 4 * (params[9]) ** 2)) <= 0.1:
        counter +=3
        print("Nice hit! Total number of strikes:", counter)
        clicked = True
    return counter


def handler(mouse_pos):
    """ Передает действия игрока модели
        mouse_pos - координаты курсора мыши на экране
    """
    global counter, clicked
    start = counter
    for i in range(0, len(CIRCLE_LIST)):
        counter = _click_circle(counter, CIRCLE_LIST[i], mouse_pos)
        if counter > start:
            CIRCLE_LIST.pop(i)
            break
    start = counter
    for i in range(0, len(TRIANGLE_LIST)):
        counter = _click_triangle(counter, TRIANGLE_LIST[i], mouse_pos)
        if counter > start:
            TRIANGLE_LIST.pop(i)
            break
    if not clicked:
        print("You missed! Try again.")
    clicked = False


def _leaderboard_update(Name):
    """ Считывает и обновляет таблицу лидеров
        Name - имя игрока
    """
    global counter
    len = 0
    LEADER = []
    file = open('Leaderboards.txt', 'r')
    for line in file:
        LEADER.append([line.split(' - ')[0], int(line.split(' - ')[1])])
        len += 1

    for i in range(0, len):
            if LEADER[i][0] == Name and LEADER[i][1] >= counter:
                return LEADER
            if LEADER[i][0] == Name and LEADER[i][1] < counter:
                LEADER.pop(i)
                len -= 1
                for j in range(0, len):
                    if LEADER[j][1] < counter:
                        LEADER = LEADER[0:j] + [[Name, counter]] + LEADER[j:]
                        return LEADER

    for i in range(0, len):
        if LEADER[i][1] < counter:
            LEADER = LEADER[0:i] + [[Name, counter]] + LEADER[i:]
            return LEADER
        if LEADER[i][1] == counter:
            LEADER = LEADER[0:i+1] + [[Name, counter]] + LEADER[i+1:]
            return LEADER

    LEADER.append([Name, counter])
    return LEADER


def write_leaderboard(Name):
    """ Записывает обновленную таблицу лидеров в текстовый файл Leaderboards.txt
        Name - имя игрока
    """
    TABLE = _leaderboard_update(Name)
    file = open('Leaderboards.txt', 'w')
    for line in TABLE:
        file.write(line[0] + " - " + str(line[1]) + '\n')
    return


