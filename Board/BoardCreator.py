from typing import Tuple
import pygame
from CartesianGameboardSetup import CartesianGameboardSetup

def can_be_called_only_once(function):
    number_of_calls = 0

    def wraper(function):
        nonlocal number_of_calls
        number_of_calls += 1

        if number_of_calls == 0:
            return function
        else:
            raise Exception('Function/method {} can be called only once'.format(function.__name__))
    return wraper

class BoardCreator:
    def __init__(self, height_in_fields: int, width_in_fields: int, field_height: int, field_width: int,
                 console_height: int = 300):
        self.height_in_fields = height_in_fields
        self.width_in_fields = width_in_fields
        self.field_width = field_width
        self.field_height = field_height
        self.console_height = console_height

        self.board = self.__create_board()
        gameboard_setup = CartesianGameboardSetup()

    def __create_board(self):
        return pygame.display.set_mode(self.__get_board_size())

    def __get_board_size(self) -> Tuple[int, int]:
        return (self.__get_board_height(), self.__get_board_width())

    def __get_board_width(self) -> int:
        return self.width_in_fields * self.field_width

    def __get_board_height(self) -> int:
        return self.height_in_fields * self.field_height + self.console_height

