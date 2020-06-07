from Singleton import Singleton
import pygame
from GeometricFactory import GeometricFactory
from utils import overload
from Rectangle import Rectangle
from Point import Point
from utils import print_time
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()


class Display(metaclass=Singleton):
    window_handle = None
    geometric_factory = None

    @classmethod
    def create_window(cls, height, width):
        cls.geometric_factory = GeometricFactory(height)
        cls.window_handle = pygame.display.set_mode((width, height))

    @classmethod
    def set_background(cls, color: tuple = WHITE):
        cls.window_handle.fill(color)

    @staticmethod
    def set_window_title(title: str):
        pygame.display.set_caption(title)

    @classmethod
    def line(cls, point1, point2, color=BLACK, line_thickness=1):
        point1_transformed = cls.__transform_point(point1)
        point2_transformed = cls.__transform_point(point2)
        cls.__draw_line(color, point1_transformed, point2_transformed, line_thickness)

    @classmethod
    def __draw_line(cls, color, point1, point2, line_thickness):
        pygame.draw.line(cls.window_handle, color, point1, point2, line_thickness)

    @classmethod
    def __transform_point(cls, point):
        return cls.geometric_factory.point(point)

    @classmethod
    def rectangle(cls, upper_left_corner: Point, height: int, width: int, color: tuple = BLACK, line_thickness: int = 1):
        rectangle = cls.__get_rectangle(upper_left_corner, height, width)
        cls.__draw_rectangle(rectangle, color, line_thickness)

    @classmethod
    def __get_rectangle(cls, upper_left_corner: Point, height: int, width: int):
        return cls.geometric_factory.rectangle(upper_left_corner, height, width)

    @classmethod
    def __draw_rectangle(cls, rectangle: Rectangle, color: tuple, line_thickness: int):
        pygame.draw.rect(cls.window_handle, color, rectangle.get_pygame_position, line_thickness)






