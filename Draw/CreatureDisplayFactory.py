from Display import Display
from functools import partial
from Wolf import Wolf


class CreatureDisplayFactory:

    @staticmethod
    def get_creature_drawer(creature):
        creature_texture = {
            Wolf: partial(Display.rectangle, color=(255, 0, 0), line_thickness=0)
        }

        return creature_texture[creature.__class__]
