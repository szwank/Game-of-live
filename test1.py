import pygame
from World import World
from Display import Display


Display.create_window(200, 300)

world = World(30, 30)
world1 = World()
pygame.init()
x = 500
y = 100
handle = pygame.display.set_mode((x, y))
handle.fill((255, 255, 255))

pygame.draw.line(handle, (0, 0, 0), (100, 100), (200, 200))
pygame.draw.line(handle, (0, 255, 0), (100, 100), (100, 200))
pygame.draw.line(handle, (0, 0, 255), (100, 100), (200, 100))
pygame.draw.rect(handle, (0, 0, 0), (100, 100, 100, -50), 1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()