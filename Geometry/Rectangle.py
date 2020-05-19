from Geometry.Point import Point

class Rectangle:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2


    @classmethod
    def from_point(cls, point, height, width):
        half_width = round(width / 2)
        half_height = round(height / 2)
        point1 = Point(point.x + half_width, point.y + half_height)
        point2 = Point(point.x - half_width, point.y - half_height)
        return cls(point1, point2)

    @property
    def height(self):
        return abs(self.point1.y - self.point2.y)

    @property
    def width(self):
        return abs(self.point1.x - self.point2.x)

    def get_upper_right_corner(self) -> Point:
        x = self.__get_bigger_x_position()
        y = self.__get_bigger_y_position()
        return Point(x, y)

    def get_upper_left_corner(self) -> Point:
        x = self.__get_bigger_x_position()
        y = self.__get_smaller_y_position()
        return Point(x, y)

    def get_lower_right_corner(self) -> Point:
        x = self.__get_smaller_x_position()
        y = self.__get_bigger_y_position()
        return Point(x, y)

    def get_lower_left_corner(self) -> Point:
        x = self.__get_bigger_x_position()
        y = self.__get_smaller_y_position()
        return Point(x, y)

    def __get_smaller_x_position(self) -> int:
        if self.point1.x < self.point2.x:
            return self.point1.x
        else:
            return self.point2.x

    def __get_bigger_x_position(self) -> int:
        if self.point1.x > self.point2.x:
            return self.point1.x
        else:
            return self.point2.x

    def __get_smaller_y_position(self) -> int:
        if self.point1.y < self.point2.y:
            return self.point1.y
        else:
            return self.point2.y

    def __get_bigger_y_position(self) -> int:
        if self.point1.y > self.point2.y:
            return self.point1.y
        else:
            return self.point2.y