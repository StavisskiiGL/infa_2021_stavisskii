import math
from random import choice, randint

import pygame
from pygame.draw import *
from pygame.draw import polygon

FPS = 60

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, xc, yc, len, an):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = xc + len * math.cos(an)
        self.y = yc - len * math.sin(an)
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.ay = 1
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.out_y = False
        self.out_x = False
        self.counter = 0
        self.time = 0

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        if (self.y >= HEIGHT - self.r or self.y < self.r) and not self.out_y:
            self.vy = -0.8 * self.vy
            self.ay = 0
            self.out_y = True
        if (self.x >= WIDTH - self.r or self.x < self.r) and not self.out_x:
            self.vx = -0.8 * self.vx
            self.out_x = True
        self.vy = self.vy + self.ay
        self.x += self.vx
        self.y += self.vy
        if HEIGHT - self.r > self.y > self.r:
            self.out_y = False
            self.ay = 1
        if WIDTH - self.r > self.x > self.r:
            self.out_x = False
        if abs(self.vy) <= 2 and abs(self.y - (HEIGHT - self.r)) <= 0.1:
            self.y = HEIGHT - self.r
            self.vy = 0
            self.ay = 0

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return math.sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2) <= self.r + obj.r


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.len = 10
        self.width = 5
        self.x1 = self.y1 = self.x2 = self.y2 = self.x3 = self.y3 = self.x4 = self.y4 = 0
        self.xc = 40
        self.yc = 450

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls
        self.xc = 40
        self.yc = 450
        new_ball = Ball(self.screen, self.xc, self.yc, self.len, self.an)
        self.an = math.atan2((-event.pos[1]+new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an) * 1/2
        new_ball.vy = - self.f2_power * math.sin(self.an) * 1/2
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targeting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((-event.pos[1]+self.yc) / (event.pos[0]-self.xc))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        self.x1 = self.xc + self.len * math.cos(self.an) + math.sin(self.an) * self.width
        self.y1 = self.yc - self.len * math.sin(self.an) + math.cos(self.an) * self.width
        self.x2 = self.xc + self.len * math.cos(self.an) - math.sin(self.an) * self.width
        self.y2 = self.yc - self.len * math.sin(self.an) - math.cos(self.an) * self.width
        self.x3 = self.xc + math.sin(self.an) * self.width
        self.y3 = self.yc + math.cos(self.an) * self.width
        self.x4 = self.xc - math.sin(self.an) * self.width
        self.y4 = self.yc - math.cos(self.an) * self.width
        polygon(screen, self.color, [(self.x4, self.y4), (self.x2, self.y2), (self.x1, self.y1), (self.x3, self.y3)])

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
                self.len += 1
                self.color = RED
        else:
            self.color = GREY
            self.len = 10


class Target:
    global screen

    def __init__(self):
        self.points = 0
        self.live = 1
        self.x = self.y = self.r = 0
        self.color = 0
        self.new_target()
        self.vy = 0
        self.h = 0

    def set_dest(self):
        self.h = randint(self.r, HEIGHT - self.r - 30)
        if self.y > self.h:
            self.vy = randint(-10, -5)
        if self.y < self.h:
            self.vy = randint(5, 10)

    def move_target(self):
        if self.vy < 0:
            if self.y < self.h:
                self.set_dest()
                return
        if self.vy > 0:
            if self.y > self.h:
                self.set_dest()
                return
        self.y += self.vy

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        r = self.r = randint(10, 50)
        color = self.color = choice(GAME_COLORS)
        self.live = 1

    def hit(self):
        """Попадание шарика в цель."""
        self.points += 1

    def draw(self):
        circle(screen, self.color, [self.x, self.y], self.r)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
points = 0
time = 1
balls = []
targets = []

clock = pygame.time.Clock()
gun = Gun(screen)
targets.append(Target())
targets.append(Target())
finished = False

for t in targets:
    t.set_dest()

while not finished:
    Nb = 0
    fontObj = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj = fontObj.render('Your score : ' + str(points), True, [0, 0, 0], [255, 255, 0])
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (200, 100)
    screen.fill(WHITE)
    screen.blit(textSurfaceObj, textRectObj)
    gun.draw()
    for t in targets:
        t.draw()
    for b in balls:
        if b.time % 300 == 0:
            balls.pop(Nb)
            pass
        b.draw()
        Nb += 1

    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targeting(event)

    for b in balls:
        b.move()
        b.time += 1
        for t in targets:
            if b.hittest(t) and t.live:
                t.live = 0
                points += 1
                t.new_target()
                t.set_dest()
    gun.power_up()

    for t in targets:
        t.move_target()

    time += 1

pygame.quit()
