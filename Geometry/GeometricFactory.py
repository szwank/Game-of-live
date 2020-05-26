from Geometry.Point import Point
from Geometry.Rectangle import Rectangle
from utils import singleton
from typing import Tuple
from GeometricTransformer import GeometricTransformer
from Singleton import Singleton
from utils import overload

class GeometricFactory(metaclass=Singleton):
    """Factory translates cartesian coorginates into pygame coordinates creating Geometry objects."""

    def __init__(self, window_height):
        self.window_height = window_height

    def point(self, x, y):
        return Point(x, self.__translate_y(y))

    def rectangle(self, point1, point2):
        translated_point1 = self.__translate_point(point1)
        translated_point2 = self.__translate_point(point2)
        return Rectangle(translated_point1, translated_point2)

    def pygame_rectangle(self, rectangle):
        upper_left_corner = GeometricTransformer.get_upper_left_corner()

    def __translate_point(self, point):
        return Point(point.x, self.__translate_y(point.y))

    def __translate_y(self, y):
        return self.window_height - y