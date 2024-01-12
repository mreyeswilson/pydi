from functools import wraps
from patterns import singleton

class Inject:

    def __init__(self, modules = []):
        self.modules = modules

    def __call__(self, cls):
        for module in self.modules:
            name = module.__name__.lower()
            setattr(cls, name, module())
        return cls
