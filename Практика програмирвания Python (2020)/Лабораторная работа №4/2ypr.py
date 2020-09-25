import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((455, 300))
screen.fill((0, 179, 0))

# рисование неба
rect(screen, (117, 193, 255), (0, 0, 455, 150))

# рисование дома
rect(screen, (0, 0, 0), (100, 120, 110, 80))
rect(screen, (150, 75, 0), (101, 121, 108, 78))
rect(screen, (184, 110, 0), (127, 140, 56, 40))
rect(screen, (66, 170, 255), (128, 141, 54, 38))
polygon(screen, (0, 0, 0), [[100, 120], [155, 90], [210, 120]])
polygon(screen, (199, 0, 0), [[101, 119], [155, 91], [209, 119]])

# рисование дерева
circle(screen, (14, 59, 14), [350, 80], 20, 0)
circle(screen, (0, 0, 0), [350, 80], 20, 1)
rect(screen, (0, 0, 0), (343, 130, 15, 55))
circle(screen, (14, 59, 14), [325, 100], 20, 0)
circle(screen, (0, 0, 0), [325, 100], 20, 1)
circle(screen, (14, 59, 14), [375, 100], 20, 0)
circle(screen, (0, 0, 0), [375, 100], 20, 1)
circle(screen, (14, 59, 14), [350, 110], 20, 0)
circle(screen, (0, 0, 0), [350, 110], 20, 1)
circle(screen, (14, 59, 14), [335, 120], 20, 0)
circle(screen, (0, 0, 0), [335, 120], 20, 1)
circle(screen, (14, 59, 14), [365, 120], 20, 0)
circle(screen, (0, 0, 0), [365, 120], 20, 1)

# рисование облака
circle(screen, (255, 255, 255), [240, 50], 20, 0)
circle(screen, (0, 0, 0), [240, 50], 20, 1)
circle(screen, (255, 255, 255), [260, 50], 20, 0)
circle(screen, (0, 0, 0), [260, 50], 20, 1)
circle(screen, (255, 255, 255), [280, 50], 20, 0)
circle(screen, (0, 0, 0), [280, 50], 20, 1)
circle(screen, (255, 255, 255), [300, 50], 20, 0)
circle(screen, (0, 0, 0), [300, 50], 20, 1)
circle(screen, (255, 255, 255), [280, 30], 20, 0)
circle(screen, (0, 0, 0), [280, 30], 20, 1)
circle(screen, (255, 255, 255), [260, 30], 20, 0)
circle(screen, (0, 0, 0), [260, 30], 20, 1)

# рисование солнца
pygame.draw.ellipse(screen, (255, 244, 47), [380, 20, 40, 40])

pygame.display.update()

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
