from typing import Tuple
from Point import Point
from Rectangle import Rectangle
from utils import singleton


@singleton
class GeometricAbstractTransformator:
    def __init__(self, window_height):
        self.window_height = window_height

    @staticmethod
    def translate_point(point: Point, translation_vector: Tuple[int, int]) -> Point:
        return Point(point.x + translation_vector[0], point.y - translation_vector[1])

    @classmethod
    def translate_rectangle(cls, rectangle: Rectangle, translation_vector: Tuple[int, int]) -> Rectangle:
        point1 = cls.translate_point(rectangle.point1, translation_vector)
        point2 = cls.translate_point(rectangle.point2, translation_vector)
        return Rectangle(point1, point2)

    def __translate_point(self, point):
        return Point(point.x, self.__translate_y(point.y))

    def __translate_y(self, y):
        return self.window_height - y

    @staticmethod
    def get_lower_left_corner(rectangle):
        if rectangle.point1.x < rectangle.point2.x:
            x = rectangle.point1.x
        else:
            x = rectangle.point2.x

        if rectangle.point1.y < rectangle.point2.y:
            y = rectangle.point2.y
        else:
            y = rectangle.point1.y

        return Point(x, y)

    @staticmethod
    def get_upper_left_corner(rectangle):
        if rectangle.point1.x < rectangle.point2.x:
            x = rectangle.point1.x
        else:
            x = rectangle.point2.x

        if rectangle.point1.y > rectangle.point2.y:
            y = rectangle.point2.y
        else:
            y = rectangle.point1.y

        return Point(x, y)