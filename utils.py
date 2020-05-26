from typing import Optional, Callable, List, Tuple
from Singleton import Singleton
from inspect import getfullargspec


def singleton(cls: Callable) -> Callable:
    class_instance: Optional[cls] = None

    def class_wrapper(*args, **kwargs):
        nonlocal class_instance
        if class_instance is None:
            class_instance = cls(*args, **kwargs)
            return class_instance
        elif not empty(args) or not empty(kwargs):
            message = 'Class {} is a singleton. Class {} was already initialized'.format(cls.__name__, cls.__name__)
            raise Exception(message)
        else:
            return class_instance
    return class_wrapper


def empty(arg: List or Tuple):
    if not arg:
        return True
    else:
        return False


def can_be_called_only_once(function: Callable) -> Callable:
    number_of_calls = 0

    def wrapper(*args, **kwargs):
        nonlocal number_of_calls
        number_of_calls += 1

        if number_of_calls == 0:
            return function(*args, **kwargs)
        else:
            raise Exception('Function/method {} can be called only once'.format(function.__name__))
    return wrapper


def overload(func: Callable) -> Callable:
    namespace = NameSpace()
    namespace.register(func)
    wrapped_func = Function(func)

    def wrapper(*args, **kwargs):

        return wrapped_func(*args, **kwargs)

    return wrapper

class Function:
    def __init__(self, func: Callable):
        self.__func = func
        self.__function_origin = self.__get_function_origin(func)

    def __call__(self, *args, **kwargs):
        namespace = NameSpace()
        function = namespace.get_function(self.key(args))
        return function(*args, **kwargs)

    def __get_function_origin(self, func: Callable) -> Tuple:
        return (func.__module__, func.__class__, func.__name__)

    def key(self, args: Optional[Tuple] = None) -> Tuple:
        if args is None:
            args = getfullargspec(self.__func).args
        return tuple([*self.__function_origin, len(args or [])])

class NameSpace(metaclass=Singleton):
    def __init__(self):
        self.__namespace = {}

    def register(self, func: Callable):
        wrapped_func = Function(func)
        key = wrapped_func.key()
        self.__namespace[key] = func

    def get_function(self, function_key: Tuple):
        return self.__namespace[function_key]

