from BoardSetup.CartesianGameboardSetup import CartesianGameboardSetup
import pytest
from BoardException import BoardException
from unittest.mock import ANY

class TestCartesianBoard:
    @classmethod
    def setup_class(self):
        self.height = 300
        self.width = 400
        self.field_height = 20
        self.field_width = 20


    @pytest.fixture(scope='function')
    def display_mock(self, mocker):
        return mocker.patch('pygame.display')

    @pytest.fixture(scope='function')
    def draw_mock(self, mocker):
        return mocker.patch('pygame.draw')


    def test_size_property(self):
        board = CartesianGameboardSetup(self.height, self.width, self.field_height, self.field_width)
        assert board.size == (self.height * self.field_height, self.width * self.field_width)

    def test_create_board_is_called_with_proper_arguments(self, display_mock, draw_mock):
        board = CartesianGameboardSetup(self.height, self.width, self.field_height, self.field_width)

        board.create_board()

        display_mock.set_mode.assert_called_once()
        display_mock.set_mode.assert_called_with((self.height * self.field_height, self.width * self.field_width))

    def test_create_board_set_bard_field(self, display_mock, draw_mock):
        board = CartesianGameboardSetup(self.height, self.width)

        board.create_board()

        assert board.board == display_mock.set_mode()

    def test_rise_error_when_creating_second_board(self, display_mock, draw_mock):
        board = CartesianGameboardSetup(self.height, self.width)

        board.create_board()
        with pytest.raises(BoardException):
            board.create_board()

    def test_setup_board_calling_setup_methods(self, display_mock, draw_mock):
        board = CartesianGameboardSetup(self.height, self.width)
        board.create_board()

        display_mock.set_mode().fill.assert_called_once()
        draw_mock.line.assert_called_with(display_mock.set_mode(), ANY, ANY, ANY, ANY)
        assert draw_mock.line.call_count > 1
