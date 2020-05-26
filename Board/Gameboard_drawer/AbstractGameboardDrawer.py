from Singleton import Singleton
from Gameboard import Gameboard
from abc import ABC, abstractmethod
from Rectangle import Rectangle
from Display import Display

class AbstractGameboardDrawer(ABC):
    def __init__(self, gameboard: Gameboard, gameboard_position: Rectangle):
        self._gameboard = gameboard
        self._gameboard_position = gameboard_position
        self._display = Display(self._get_gameboard_height_in_pixels(), self._get_gameboard_width_in_pixels())
        self._display.create_window()

    def draw(self):
        fields = self._gameboard.fields

        for row in fields:
            for field in row:
                self._draw_field(field)

    @abstractmethod
    def _draw_field(self, field):
        pass

    @abstractmethod
    def _get_display(self):
        pass

    @abstractmethod
    def _get_gameboard_height_in_pixels(self):
        pass

    @abstractmethod
    def _get_gameboard_width_in_pixels(self):
        pass