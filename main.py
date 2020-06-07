from World import World
import pygame
from Gameboard import Gameboard
from Board import Board
from RectangleFieldGameboardDisplay import RectangleFieldGameboardDisplay
from WorldDisplay import WorldDisplay
from Point import Point
from Display import Display
from time import time

def main():
    clock = pygame.time.Clock()
    width = 600
    height = 600
    margin = 10

    gameboard = Gameboard(5, 5)
    board = Board(gameboard)
    world = World(board)

    Display.create_window(height, width)
    Display.set_background()

    gameboard_display = RectangleFieldGameboardDisplay(Point(margin, height-margin), int(height/2), int(width/2))
    world_display = WorldDisplay(gameboard_display)

    world_display.display(world)


    i = 0

    while True:
        clock.tick(0.)

        Display.set_background()
        gameboard.next_turn()
        world_display.display(world)

        pygame.display.update()

        for event in pygame.event.get():
            start_time = time()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


if __name__ == '__main__':
    main()