from Geometry.Point import Point
from Geometry.Rectangle import Rectangle
from Singleton import Singleton
from utils import overload


class GeometricFactory(metaclass=Singleton):
    """Factory translates cartesian coorginates into pygame coordinates creating Geometry objects."""

    def __init__(self, window_height):
        self.window_height = window_height

    def point(self, x, y):
        return Point(x, self.__translate_y(y))

    @overload
    def rectangle(self, point1, point2):
        translated_point1 = self.__translate_point(point1)
        translated_point2 = self.__translate_point(point2)
        return Rectangle(translated_point1, translated_point2)

    @overload
    def rectangle(self, upper_left_point: Point, height: int, width: int):
        transformed_upper_left_point = self.__translate_point(upper_left_point)
        return Rectangle(transformed_upper_left_point, height, width)

    def __translate_point(self, point):
        return Point(point.x, self.__translate_y(point.y))

    def __translate_y(self, y):
        return self.window_height - y