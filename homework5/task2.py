import functools


def print_result(func):
    @save_func_info(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


def save_func_info(func):
    def inner(wrapper):
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__original_func = func
        return wrapper

    return inner


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)
