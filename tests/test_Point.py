from Geometry.Point import Point

class TestPoint:

    def test_position_values(self):
        point = Point(20, 40)
        assert point.position == (20, 40)