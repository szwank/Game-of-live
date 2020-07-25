from Rectangle import Rectangle
from Point import Point
from unittest.mock import MagicMock
import pytest


class TestRectangle:
    @pytest.fixture()
    def point_mock(self, mocker):
        return mocker.patch('Geometry.Point.Point')

    def test_properties(self, point_mock):
        width = 30
        height = 40
        upper_left_corner = point_mock
        upper_left_corner.x = 50
        upper_left_corner.y = 60

        rectangle = Rectangle(upper_left_corner, height, width)

        assert rectangle.get_pygame_position == (50, 60, 30, 40)
        assert rectangle.upper_left_corner == point_mock
        assert rectangle.height == height
        assert rectangle.width == width

    def test_creation_from_diagonally_opposite_points(self):
        point = Point(30, 40)
        diagonally_opposite_point = Point(100, 110)

        rectangle = Rectangle.from_diagonally_opposite_points(point, diagonally_opposite_point)

        assert rectangle.upper_left_corner.x == 30
        assert rectangle.upper_left_corner.y == 110
        assert rectangle.width == 100 - 30
        assert rectangle.height == 110 - 40

    def test_creation_from_central_point(self):
        central_point = Point(70, 80)
        width = 50
        height = 60

        rectangle = Rectangle.from_central_point(central_point, height, width)

        assert rectangle.upper_left_corner.x == 45
        assert rectangle.upper_left_corner.y == 110
        assert rectangle.width == width
        assert rectangle.height == height
