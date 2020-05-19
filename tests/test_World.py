import pytest
from World import World

class TestWorld:

    @pytest.fixture
    def pygame_init_mock(self, mocker):
        return mocker.patch('pygame.init')


    def test_pygame_is_initialized_when_creating_World_instance(self, pygame_init_mock):
        world = World(20, 20)
        pygame_init_mock.assert_called_once()
