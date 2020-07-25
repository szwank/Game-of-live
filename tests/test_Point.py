from Geometry.Point import Point

class TestPoint:

    def test_position_values(self):
        point = Point(20, 40)
        assert point.position == (20, 40)


    def test_x_y_property(self):
        x = 20
        y = 40
        point = Point(x, y)

        assert point.x == x
        assert point.y == y