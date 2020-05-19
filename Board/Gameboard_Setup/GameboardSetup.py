from GameboardSetupInterface import GameboardSetupInterface
from abc import abstractmethod
import pygame
from Point import Point
from Rectangle import Rectangle


class GameboardSetup(GameboardSetupInterface):

    def __init__(self, board, position: Rectangle, height_in_fields: int, width_in_fields: int, line_thickness: int = 1):
        self.board = board
        self.position = position

        self.background_color = white = (255, 255, 255)

        self.line_thickness = line_thickness

        self.height_in_fields = height_in_fields
        self.width_in_fields = width_in_fields
        self.fields = []

    def setup_board(self):
        self._setup_fields()

    def _setup_fields(self):
        self._fill_background()
        self._init_fields()
        self._draw_fields()
        self._update_board()

    @abstractmethod
    def _init_fields(self):
        pass

    def _fill_background(self):
        self.board.fill(self.background_color)

    @abstractmethod
    def _draw_fields(self):
        pass

    def _draw_line(self, point1: Point, point2: Point):
        black = (0, 0, 0)
        pygame.draw.line(self.board, black, point1.position, point2.position, self.line_thickness)

    def _update_board(self):
        pygame.display.update()

