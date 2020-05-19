from Field import Field
import pygame
from Rectangle import Rectangle


class RectangleField(Field):
    def __init__(self, board, center, height, width, line_thickness):
        super(RectangleField, self).__init__()
        self.center = center
        self.height = height
        self.width = width
        self.board = board
        self.line_thickness = line_thickness
        self.position = self.__get_position()

        self.border_color = black = (0, 0, 0)

    def __get_position(self):
        return Rectangle.from_point(self.center, self.width, self.height)

    def draw(self):
        pygame.draw.rect(self.board, self.border_color, self.__pygame_rectangle(), self.line_thickness)

    def __pygame_rectangle(self):
        return (*self.position.point1.position, *self.position.point2.position)

