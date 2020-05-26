from typing import Tuple
from Point import Point
from Rectangle import Rectangle


class GeometricTransformer:

    @staticmethod
    def translate_point(point: Point, translation_vector: Tuple[int, int]) -> Point:
        return Point(point.x + translation_vector[0], point.y - translation_vector[1])

    @classmethod
    def translate_rectangle(cls, rectangle: Rectangle, translation_vector: Tuple[int, int]) -> Rectangle:
        upper_left_corner_transformed = cls.translate_point(rectangle.upper_left_corner, translation_vector)
        return Rectangle(upper_left_corner_transformed, rectangle.height, rectangle.width)

    # def __translate_point(self, point):
    #     return Point(point.x, self.__translate_y(point.y))
    #
    # def __translate_y(self, y):
    #     return self.window_height - y
    #
    # @staticmethod
    # def get_lower_left_corner(rectangle):
    #     if rectangle.point1.x < rectangle.point2.x:
    #         x = rectangle.point1.x
    #     else:
    #         x = rectangle.point2.x
    #
    #     if rectangle.point1.y < rectangle.point2.y:
    #         y = rectangle.point2.y
    #     else:
    #         y = rectangle.point1.y
    #
    #     return Point(x, y)
    #
    # @staticmethod
    # def get_upper_left_corner(rectangle):
    #     if rectangle.point1.x < rectangle.point2.x:
    #         x = rectangle.point1.x
    #     else:
    #         x = rectangle.point2.x
    #
    #     if rectangle.point1.y > rectangle.point2.y:
    #         y = rectangle.point2.y
    #     else:
    #         y = rectangle.point1.y
    #
    #     return Point(x, y)