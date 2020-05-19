import pygame
from BoardCreator import BoardCreator
from utils import singleton


@singleton
class World:
    def __init__(self, height, width):
        self.__init_pytest()

        self.board_creator = BoardCreator(height, width)

    def __init_pytest(self):
        pygame.init()

    def init(self):
        self.board_creator.init()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()