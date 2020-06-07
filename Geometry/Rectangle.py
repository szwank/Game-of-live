from Geometry.Point import Point
from typing import Optional, Tuple
from utils import overload

class Rectangle:
    def __init__(self, upper_left_corner: Point, height: int, width: int):
        self.__height = height
        self.__width = width
        self.__upper_left_corner = upper_left_corner

    @classmethod
    def from_diagonally_opposite_points(cls, point: Point, diagonally_opposite_point: Point):
        upper_left_corner = cls.__get_upper_left_corner(point, diagonally_opposite_point)
        height = cls.__calculate_height(point, diagonally_opposite_point)
        width = cls.__calculate_width(point, diagonally_opposite_point)
        return cls(upper_left_corner, height, width)

    @classmethod
    @overload
    def __get_upper_left_corner(cls, point: Point, diagonally_opposite_point: Point):
        x = cls.__get_smaller_x_position(point, diagonally_opposite_point)
        y = cls.__get_bigger_y_position(point, diagonally_opposite_point)
        return Point(x, y)

    @staticmethod
    def __get_smaller_x_position(point1: Point, point2: Point) -> int:
        if point1.x < point2.x:
            return point1.x
        else:
            return point2.x

    @staticmethod
    def __get_bigger_y_position(point1: Point, point2: Point) -> int:
        if point1.y > point2.y:
            return point1.y
        else:
            return point2.y

    @staticmethod
    def __calculate_height(point1: Point, point2: Point):
        return abs(point1.y - point2.y)

    @staticmethod
    def __calculate_width(point1: Point, point2: Point):
        return abs(point1.x - point2.x)

    @classmethod
    def from_central_point(cls, central_point, height, width):
        x = central_point.x - round(width / 2)
        y = central_point.y + round(height/2)
        upper_left_corner = Point(x, y)
        return cls(upper_left_corner, height, width)
    #
    # @staticmethod
    # @overload
    # def __get_upper_left_corner(central_point, height, width):
    #     x = central_point.x - round(width/2)
    #     y = central_point.y - round(height/2)
    #     return Point(x, y)

    @classmethod
    def from_lower_left_point(cls, lower_left_point, height, width):
        x = lower_left_point.x
        y = lower_left_point.y + height
        upper_left_corner = Point(x, y)
        return cls(upper_left_corner, height, width)

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def upper_left_corner(self):
        return self.__upper_left_corner

    @property
    def get_pygame_position(self) -> Tuple[int, int, int, int]:
        return self.upper_left_corner.x, self.upper_left_corner.y, self.width, self.height

    def lower_left_corner(self):
        x = self.upper_left_corner.x
        y = self.upper_left_corner.y - self.height
        return Point(x, y)


    # def get_upper_right_corner(self) -> Point:
    #     x = self.__get_bigger_x_position()
    #     y = self.__get_bigger_y_position()
    #     return Point(x, y)
    #
    # def get_upper_left_corner(self, point1, point2):
    #     pass
    #
    # def __get_upper_left_corner(self) -> Point:
    #     x = self.__get_bigger_x_position()
    #     y = self.__get_smaller_y_position()
    #     return Point(x, y)
    #
    # def get_lower_right_corner(self) -> Point:
    #     x = self.__get_smaller_x_position()
    #     y = self.__get_bigger_y_position()
    #     return Point(x, y)
    #
    # def get_lower_left_corner(self) -> Point:
    #     x = self.__get_bigger_x_position()
    #     y = self.__get_smaller_y_position()
    #     return Point(x, y)