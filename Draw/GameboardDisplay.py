from abc import ABC, abstractmethod
from math import floor
from Point import Point


class GameboardDisplay(ABC):
    def __init__(self, upper_left_corner_gameboard_position: Point, height_in_pixels: int,
                 width_in_pixels: int):
        self._upper_left_corner_gameboard_position = upper_left_corner_gameboard_position
        self.__height_in_pixels = height_in_pixels
        self.__width_in_pixels = width_in_pixels

    def _calculate_field_height(self, height_in_fields):
        return floor(self.__height_in_pixels/height_in_fields)

    def _calculate_field_width(self, width_in_fields):
        return floor(self.__width_in_pixels/width_in_fields)

    @abstractmethod
    def display(self, gameboard):
        pass

    @property
    def height_in_pixels(self) -> int:
        return self.__height_in_pixels