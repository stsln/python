import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((400, 400))

screen.fill((255, 255, 255))
circle(screen, (255, 255, 0), [200, 200], 100, 0)
circle(screen, (0, 0, 0), [200, 200], 100, 1)
rect(screen, (0, 0, 0), (150, 240, 100, 25))
circle(screen, (0, 0, 0), [160, 170], 22, 0)
circle(screen, (255, 0, 0), [160, 170], 21, 10)
circle(screen, (0, 0, 0), [240, 170], 16, 0)
circle(screen, (255, 0, 0), [240, 170], 15, 6)
line(screen, (0, 0, 0), [110, 120], [188, 150], 14)
line(screen, (0, 0, 0), [220, 149], [290, 135], 14)
pygame.display.update()

clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
