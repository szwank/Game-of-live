import pygame
from BoardException import BoardException
from typing import Tuple
from Point import Point
from BoardSetup.GameboardSetup import GameboardSetup


class CartesianGameboardSetup(GameboardSetup):
    def __init__(self, height_in_fields: int, width_in_fields: int, field_height: int, field_width: int,
                 line_thickness: int = 1):
        self.field_height = field_height
        self.field_width = field_width

        white = (255, 255, 255)
        self.background_color = white

        self.line_thickness = line_thickness

        self.height_in_fields = height_in_fields
        self.width_in_fields = width_in_fields
        self.board = None

    @property
    def size(self) -> Tuple[int, int]:
        return (self.height_in_fields * self.field_height, self.width_in_fields * self.field_width)


    def create_board(self):
        self.__try_create_board()

    def __try_create_board(self):
        if not self.__board_already_created():
            self.__create_board()
        else:
            self.__throw_error("Board already created")

    def __create_board(self):
        self.__create_gameboard()
        self.__setup_board()
        self.__update_board()

    def __create_gameboard(self):
        self.board = pygame.display.set_mode(self.size)

    def __setup_board(self):
        self.__fill_background()
        self.__draw_fields()

    def __fill_background(self):
        white = (255, 255, 255)
        self.board.fill(white)

    def __draw_fields(self):
        self.__draw_vertical_lines()
        self.__draw_horizontal_lines()

    def __draw_vertical_lines(self):
        y1 = 0
        y2 = self.height_in_fields * self.field_height
        for vertical_line_number in range(1, self.width_in_fields):
            x = vertical_line_number * self.field_width

            point1 = Point(x, y1)
            point2 = Point(x, y2)

            self.__draw_line(point1, point2)

    def __draw_horizontal_lines(self):
        x1 = 0
        x2 = self.width_in_fields * self.field_width
        for horizontal_line_number in range(1, self.height_in_fields):
            y = horizontal_line_number * self.field_height

            point1 = Point(x1, y)
            point2 = Point(x2, y)

            self.__draw_line(point1, point2)

    def __draw_line(self, point1: Point, point2: Point):
        black = (0, 0, 0)
        pygame.draw.line(self.board, black, point1.position, point2.position, self.line_thickness)

    def __board_already_created(self):
        return self.board is not None

    def __update_board(self):
        pygame.display.update()

    def get_board(self):
        return self.board

    def __throw_error(self, message):
        raise BoardException(message)
