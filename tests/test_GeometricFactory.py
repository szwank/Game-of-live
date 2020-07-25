import pytest
from Geometry.GeometricFactory import GeometricFactory
from Geometry.Point import Point

class TestGeometricFactory:
    window_height = 600

    @classmethod
    def setup_class(cls):
        GeometricFactory(cls.window_height)
        print('Setup')

    def test_asert_correct_point_coordinates_after_transformation(self):
        geometric_factory = GeometricFactory()
        x = 40
        y = 100
        point = geometric_factory.point(40, 100)

        assert point.x == x
        assert point.y == self.window_height - y

    def test_assert_correct_rectangle_transformation_from_two_points(self):
        geometric_factory = GeometricFactory()
        x1 = 40
        y1 = 100
        x2 = 200
        y2 = 150
        point1 = Point(x1, y1)
        point2 = Point(x2, y2)

        translated_point1 = Point(x1, self.window_height - y1)
        translated_point2 = Point(x2, self.window_height - y2)

        rectangle = geometric_factory.rectangle(point1, point2)

        assert rectangle.point1.x == translated_point1.x or rectangle.point2.x == translated_point1.x
        assert rectangle.point1.x == translated_point2.x or rectangle.point2.x == translated_point2.x
        assert rectangle.point1.y == translated_point1.y or rectangle.point2.y == translated_point1.y
        assert rectangle.point1.y == translated_point2.y or rectangle.point2.y == translated_point2.y

    def test_singleton_property(self):

        assert GeometricFactory() == GeometricFactory()

    def test_point_transformation(self):
        geometric_factory = GeometricFactory()
        x = 100
        y = 200

        transformed_point = geometric_factory.point(x, y)

        assert transformed_point.x == x
        assert transformed_point.y == self.window_height - y


