from typing import List, Dict, Tuple
from Field import Field
from random import choice
from Creature import Creature
from Wolf import Wolf
from pprint import pprint

class Gameboard():
    def __init__(self, height_in_fields, width_in_fields):
        self.__height_in_fields = height_in_fields
        self.__width_in_fields = width_in_fields
        self.__fields: Dict[Tuple[int, int], Field] = self.__create_board()
        self.creatures: List[Creature] = self.__create_life()

    def __create_board(self):
        fields = {}

        for height_position in range(self.__height_in_fields):

            for width_position in range(self.__width_in_fields):
                position_in_fields = (width_position, height_position)
                fields[position_in_fields] = Field(*position_in_fields)

        return fields

    def print_fields(self):
        for i in range(self.__height_in_fields):
            list = []
            for j in range(self.__width_in_fields):
                field = self.__fields[(j, i)]
                list.append(field.is_occupied())
            print(list)
        print('\n')

    def __create_life(self) -> List[Creature]:
        creatures = []
        free_field = self.__get_random_free_field()
        wolf = Wolf(free_field, self)
        free_field.occupy(wolf)
        creatures.append(wolf)
        return creatures

    def __get_random_free_field(self):
        free_fields = self.__get_free_fields()
        return choice(free_fields)

    def __get_free_fields(self) -> [Field]:
        free_fields = []
        for field in self.__fields.values():
            if not field.is_occupied():
                free_fields.append(field)

        return free_fields

    @property
    def fields(self):
        return self.__fields

    @property
    def height_in_fields(self):
        return self.__height_in_fields

    @property
    def width_in_fields(self):
        return self.__width_in_fields

    def move_creature(self, creature):
        self.print_fields()
        old_field = creature.field
        new_field = self.__get_new_field(creature.field)

        if not self.__is_the_same_field(creature.field, new_field):
            if new_field.is_occupied():
                self.__resolve_collision(creature, new_field.get_occupant())
            else:
                old_field.set_free()
                new_field.occupy(creature)
                creature.set_field(new_field)
                self.print_fields()

    def __get_new_field(self, acctual_creature_field: Field) -> Field:
        direction_to_choice = ("up", "down", "left", "right")
        direction = choice(direction_to_choice)
        print(direction)
        if direction == "up":
            return self.__try_get_upper_field(acctual_creature_field)

        elif direction == "down":
            return self.__try_get_lower_field(acctual_creature_field)

        elif direction == "left":
            return self.__try_get_left_field(acctual_creature_field)

        elif direction == "right":
            return self.__try_get_right_field(acctual_creature_field)

    def __try_get_left_field(self, reference_field):
        x = reference_field.horizontal_position_in_fields - 1
        y = reference_field.vertical_position_in_fields

        return self.__fields.get((x, y), reference_field)

    def __try_get_right_field(self, reference_field):
        x = reference_field.horizontal_position_in_fields + 1
        y = reference_field.vertical_position_in_fields
        return self.__fields.get((x, y), reference_field)

    def __try_get_upper_field(self, reference_field):
        x = reference_field.horizontal_position_in_fields
        y = reference_field.vertical_position_in_fields + 1
        return self.__fields.get((x, y), reference_field)

    def __try_get_lower_field(self, reference_field):
        x = reference_field.horizontal_position_in_fields
        y = reference_field.vertical_position_in_fields - 1
        return self.__fields.get((x, y), reference_field)

    def __is_the_same_field(self, field1, field2):
        return field1 is field2

    def __resolve_collision(self, aggressor, defender):
        defender.collision(aggressor)

    def make_child(self, creature):
        child = creature(self.__get_free_adjacent_field_to_creature(creature), self)
        self.creatures.append(child)

    def __get_free_adjacent_field_to_creature(self, creature: Creature):
        free_adjacent_fields = []
        for field in self.__get_adjacent_fields(creature.field):
            if field.is_free():
                free_adjacent_fields.append(field)

        return choice(free_adjacent_fields)

    def __get_adjacent_fields(self, reference_field: Field) -> List[Field]:
        fields = []
        for x_translation, y_translation in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x = reference_field.horizontal_position_in_fields + x_translation
            y = reference_field.vertical_position_in_fields + y_translation
            adjacent_field = self.__fields.get((x, y))
            if adjacent_field is not None:
                fields.append(adjacent_field)
        return fields

    def kill(self, creature):
        self.creatures.remove(creature)

    def next_turn(self):
        for creature in self.creatures:
            creature.action()

