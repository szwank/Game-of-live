import pygame
from Board import Board
from utils import singleton

@singleton
class World:
    def __init__(self, board: Board):

        self.__board = board

    @property
    def board(self):
        return self.__board

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()