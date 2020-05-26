import pygame
from Board.Board import Board
from utils import singleton


@singleton
class World:
    def __init__(self, height, width):

        self.board = Board(height, width)

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()