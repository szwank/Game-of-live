from Singleton import Singleton
import pygame
from GeometricFactory import GeometricFactory

BLACK = (0, 0, 0)

class Display(metaclass=Singleton):
    def __init__(self):
        super(Display, self).__init__()
        pygame.init()

        self.window_handle = None
        self.width = None
        self.hieght = None

    @classmethod
    def initiate_window(cls, height, width):
        cls.__initiate_fields(cls(), height, width)
        cls.__create_window(cls())

    def __initiate_fields(self, height, width):
        self.height = height
        self.width = width
        self.__initiate_geometric_factory()

    def __initiate_geometric_factory(self):
        GeometricFactory(self.height)

    def __create_window(self):
        pygame.display.set_mode(self.window_dimensions)

    @property
    def window_dimensions(self):
        return (self.width, self.height)

    @classmethod
    def line(cls, point1, point2, color=BLACK, line_thickness=1):
        point1_transformed = cls.__transform_point(point1)
        point2_transformed = cls.__transform_point(point2)
        cls.__draw_line(cls(), color, point1_transformed, point2_transformed, line_thickness)

    def __draw_line(self, color, point1, point2, line_thickness):
        pygame.draw.line(self.window_handle, color, point1, point2, line_thickness)

    @classmethod
    def __transform_point(cls, point):
        return GeometricFactory.point(point)

    @classmethod
    def rectangle(cls, rectangle, color=BLACK, line_thickness=1):
        transformed_rectangle = GeometricFactory.rectangle(rectangle)
        cls.__draw_rectangle(cls(), color, transformed_rectangle, line_thickness)

    def __draw_rectangle(self, color, rectangle, line_thickness):
        pygame.draw.rectangle(self.window_handle, color, rectangle.position, line_thickness)






