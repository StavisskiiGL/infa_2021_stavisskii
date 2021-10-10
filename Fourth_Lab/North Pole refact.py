import pygame
from pygame.draw import *

black = (0, 0, 0)
white = (255, 255, 255)
gray = (220, 220, 220)
brown = (138, 102, 66)
brown1 = (101, 67, 33)
skin = (244, 222, 204)
red = (255, 0, 0)
fishc = (163, 198, 192)
dark_blue = (8, 37, 103)
transparent = (0, 0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()

screen.fill(white)
rect(screen, gray, (0, 0, 800, 400), 0)


def make_transp(scr):
    """делает surface прозрачным"""
    scr1 = scr.convert_alpha()
    scr1.fill(transparent)
    return scr1


def drawiglu(xcor, ycor, size):
    """рисует иглу с центром основания в xcor, ycor, скейлом size"""
    iglu = make_transp(pygame.Surface((350, 175)))

    circle(iglu, gray, (175, 210), 175)
    circle(iglu, black, (175, 210), 175, 2)
    arc(iglu, black, (120, 35, 110, 20), 3.14, 6.28, 2)
    arc(iglu, black, (65, 60, 220, 30), 3.14, 6.28, 2)
    arc(iglu, black, (25, 110, 300, 25), 3.14, 6.28, 2)

    for x1, y1, x2, y2 in [
        [5, 175, 345, 175], [60, 130, 50, 175], [135, 133, 130, 175], [200, 133, 202, 175], [255, 131, 262, 175],
        [305, 128, 315, 174], [103, 85, 90, 130], [170, 90, 170, 133], [223, 88, 228, 131], [274, 82, 290, 130],
        [140, 52, 130, 88], [188, 55, 192, 88], [225, 49, 242, 86], [5, 173, 345, 173]]:
        line(iglu, black, (x1, y1), (x2, y2), 2)

    pygame.Surface.blit(screen, pygame.transform.smoothscale(iglu, (int(350*size), int(175*size))), (xcor-175*size, ycor-175*size))


def draweskimos(xcor, ycor, size, ort):
    """рисует эскимоса с центром лица в xcor, ycor, скейлом size
    
    ориентация ort принимает значения 1 и -1 для эскимосов левшей и правшей соответственно

    """
    eskimos = make_transp(pygame.Surface((500, 500)))

    ellipse(eskimos, gray, (50, 50, 200, 140))

    body = make_transp(pygame.Surface((400, 210)))
    ellipse(body, brown, (25,  40, 150, 300))
    pygame.Surface.blit(eskimos, body, (50, 100))
    arm = pygame.transform.smoothscale(body, (85, 85))
    pygame.Surface.blit(eskimos, pygame.transform.rotate(
        arm, (-35-90)*ort), (78 + 83*ort, 185+15*ort))

    for x, y, r1, r2 in [[100 - 60 * ort, 200, 100, 30], [70, 70, 160, 120], [90, 200, 45, 150], [160,  200, 45, 150], [77, 330, 50, 25], [165, 330, 50, 25]]:
        ellipse(eskimos, brown, (x, y, r1, r2))

    ellipse(eskimos, skin, (100, 100, 100, 60))
    rect(eskimos, brown1, (120, 180, 35, 120))
    rect(eskimos, brown1, (75, 300, 150, 15))

    for x1, y1, x2, y2 in [[150-100*ort, 100, 100 - 97*ort + 50, 340], [115, 115, 135, 125], [180, 115, 160, 125], [130, 140, 170, 140]]:
        line(eskimos, black, (x1, y1), (x2, y2), 3)

    pygame.Surface.blit(screen, pygame.transform.smoothscale(eskimos, (int(500*size), int(500*size))), (int(xcor-100*size), int(ycor-100*size)))


def draw_cat(xcor, ycor, size):
    """рисует кота с центром основания в xcor, ycor, скейлом size"""
    cat = make_transp(pygame.Surface((500, 500)))

    tail = make_transp(pygame.Surface((120, 20)))
    ellipse(tail, gray, (0, 0, 120, 20))
    pygame.Surface.blit(cat, pygame.transform.rotate(tail, 30), (205, 45))

    leg = make_transp(pygame.Surface((70, 20)))
    ellipse(leg, gray, (0, 0, 70, 20))
    for angle, x, y in [[-135, 5, 105], [-135, 60, 110], [-45, 180, 105], [-45, 130, 105]]:
        pygame.Surface.blit(cat, pygame.transform.rotate(leg, angle), (x, y))

    for color, x, y, r1, r2 in [[gray, 50, 100, 170, 30], [red, 82, 110, 10, 5], [fishc, 55, 105, 30, 15], [dark_blue, 57, 109, 6, 6],[white,64, 103, 4, 10],[white,74, 103, 4, 10],
        [gray, 50, 80, 45, 30], [white, 54, 84, 12, 8], [white, 72, 88, 12, 8], [black, 80, 91, 4, 4], [black, 62, 87, 4, 4], [black, 63, 96, 4, 4]
        ]:
        ellipse(cat, color, (x, y, r1, r2))

    ear = make_transp(pygame.Surface((16, 9)))
    ellipse(ear, (220, 220, 220), (0, 0, 16, 9))
    pygame.Surface.blit(cat, pygame.transform.rotate(ear, 115), (60, 71))
    pygame.Surface.blit(cat, pygame.transform.rotate(ear, 60), (77, 71))
    circle(cat, red, (150, 150), 4)
    pygame.Surface.blit(screen, pygame.transform.smoothscale(cat, (int(500*size), int(500*size))), (int(xcor-150*size), int(ycor-150*size)))


for x, y, size in [[110, 425, 0.3], [320, 450, 0.3], [205, 480, 0.75], [130, 530, 0.5], [250, 570, 0.5]]:
    drawiglu(x, y, size)

for x, y, size, ort in [[540, 400, 0.25, 1], [450, 390, 0.25, 1], [480, 445, 0.25, 1], [390, 500, 0.25, -1], [460, 520, 0.25, -1], [550, 530, 0.25, 1], [480, 600, 0.75, 1]]:
    draweskimos(x, y, size, ort)

for x, y, size in [[200, 780, 0.5], [150, 700, 1], [70, 600, 0.5], [340, 715, 0.55], ]:
    draw_cat(x, y, size)

pygame.display.update()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
