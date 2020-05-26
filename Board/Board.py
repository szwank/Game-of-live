from typing import Tuple
import pygame
from GeometricFactory import GeometricFactory
from Point import Point
from GeometricTransformer import GeometricTransformer
from Rectangle import Rectangle
from Gameboard import Gameboard
from RectangleGameboardDrawer import RectangleGameboardDrawer

class Board:
    def __init__(self, height_in_fields: int, width_in_fields: int, field_height: int = 20, field_width: int = 20,
                 console_height: int = 300):
        self.height_in_fields = height_in_fields
        self.width_in_fields = width_in_fields
        self.field_width = field_width
        self.field_height = field_height
        self.console_height = console_height

        self.gameboard_margin_height = 30
        self.gameboard_margin_width = 30

        self.gameboard_position = self.__get_gameboard_position()

        self.gameboard_setup = Gameboard(height_in_fields, width_in_fields)

        self.gameboard_drawer = RectangleGameboardDrawer(self.gameboard_setup, self.gameboard_position)

    def __get_gameboard_position(self):
        lower_right_point = Point(self.__gameboard_width(), self.console_height)
        higher_left_point = Point(0, self.console_height + self.__gameboard_height())
        translation_vector = (self.gameboard_margin_width, -self.gameboard_margin_height)
        gameboard_position = Rectangle.from_diagonally_opposite_points(lower_right_point, higher_left_point)
        return GeometricTransformer.translate_rectangle(gameboard_position, translation_vector)

    def __gameboard_height(self):
        return self.height_in_fields * self.field_height

    def __gameboard_width(self):
        return self.width_in_fields * self.field_width

    def __get_board_size(self) -> Tuple[int, int]:
        return (self.__get_board_width(), self.__get_board_height())

    def __get_board_width(self) -> int:
        return self.width_in_fields * self.field_width + 2 * self.gameboard_margin_width

    def __get_board_height(self) -> int:
        return self.height_in_fields * self.field_height + self.console_height + 2 * self.gameboard_margin_height

