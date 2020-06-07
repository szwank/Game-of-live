from World import World
from Display import Display
from Point import Point
from Gameboard import Gameboard
from RectangleFieldGameboardDisplay import RectangleFieldGameboardDisplay
from WorldDisplay import WorldDisplay
WIDTH = 300
HEIGTH = 300
g = Gameboard(10, 10)
p = RectangleFieldGameboardDisplay(Point(100, 500), HEIGTH, WIDTH)
wd = WorldDisplay(p)
w = World(b)
Display.create_window(600, 600)
Display.set_background()
# p.display(g)
w.display(g)
# world = World(30, 30)
# world1 = World()
# pygame.init()
# x = 500
# y = 100
# handle = pygame.display.set_mode((x, y))
# handle.fill((255, 255, 255))

# pygame.draw.line(handle, (0, 0, 0), (100, 100), (200, 200))
# pygame.draw.line(handle, (0, 255, 0), (100, 100), (100, 200))
# pygame.draw.line(handle, (0, 0, 255), (100, 100), (200, 100))
# pygame.draw.rect(handle, (0, 0, 0), (100, 100, 100, -50), 1)
