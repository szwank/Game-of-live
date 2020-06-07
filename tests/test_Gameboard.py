from Gameboard import Gameboard

class TestGameboard:

    def test_fields_correct_creation(self):
        gameboard = Gameboard(5, 5)
        assert len(gameboard.fields.values()) == 25
        for coordinates, field in gameboard.fields.items():
            assert self.__field_have_correct_position(field, coordinates)

    def __field_have_correct_position(self, field, coordinates):
        return field.position == coordinates