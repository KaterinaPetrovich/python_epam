from contextlib import contextmanager


@contextmanager
def suppress_exception(*ex):
    try:
        yield
    except ex:
        pass


class Suppressor:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return issubclass(exc_type, self.exceptions)
