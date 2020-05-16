from BoardSetup.CartesianGameboardSetup import CartesianGameboardSetup
import pygame
from typing import Optional
from __future__ import annotations

world = None

class WorldMeta:
    _instance: Optional[World] = None
    def __call__(self):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class World(MetaClass=WorldMeta):
    def __init__(self, height, width):
        self.__init_pytest()

        board_creator = CartesianGameboardSetup(height, width)
        board_creator.create_board()
        board = board_creator.get_board()

    def __init_pytest(self):
        pygame.init()

    def __get_board_handle(self):
        pygame.display.set_mode(())