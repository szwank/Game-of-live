from typing import Optional


def singleton(cls):
    class_instance: Optional[cls] = None

    def class_wraper(*args, **kwargs):
        nonlocal class_instance
        if class_instance is None:
            class_instance = cls(*args, **kwargs)
            return class_instance
        elif not empty(args) or not empty(kwargs):
            message = 'Class {} is a singleton. Class {} was already initialized'.format(cls.__name__, cls.__name__)
            raise Exception(message)
        else:
            return class_instance
    return class_wraper


def empty(arg):
    if not arg:
        return True
    else:
        return False

def can_be_called_only_once(function):
    number_of_calls = 0

    def wraper(function):
        nonlocal number_of_calls
        number_of_calls += 1

        if number_of_calls == 0:
            return function
        else:
            raise Exception('Function/method {} can be called only once'.format(function.__name__))
    return wraper