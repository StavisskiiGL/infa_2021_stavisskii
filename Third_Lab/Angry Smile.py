import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
circle(screen, (255, 255, 39), (400, 400), 300)
for i in range(0, 31):
    line(screen, (0, 0, 0), (150 - i, 110 + i), (350 - i, 270 + i), 5)

for i in range(0, 31):
    line(screen, (0, 0, 0), (500 - i, 295 - i), (700 - i, 135 - i), 5)
circle(screen, (255, 0, 0), (250, 320), 60)
circle(screen, (0, 0, 0), (250, 320), 25)
circle(screen, (255, 0, 0), (550, 320), 50)
circle(screen, (0, 0, 0), (550, 320), 25)
rect(screen, (0, 0, 0), (250, 550, 300, 50), 0)
pygame.display.update()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
