from functools import wraps

def singleton(clase):
    new_cls = clase.__new__
    instance = None

    wraps(clase.__new__)
    def __new__(cls, *args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = new_cls(cls, *args, **kwargs)
        return instance
    clase.__new__ = __new__
    return clase

