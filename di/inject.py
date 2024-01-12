class Inject:

    def __init__(self, modules = []):
        self.modules = modules

    def __call__(self, cls):
        modules = {}
        for module in self.modules:
            name = module.__name__.lower()
            modules[name] = module()
        return cls(**modules)
