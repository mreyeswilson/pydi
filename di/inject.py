class Inject:

    instances = {}
    singleton = []

    def __init__(self, modules = [], singleton = []):
        self.modules = modules
        self.singleton = singleton

    def __call__(self, cls):
        modules = {}
        for module in self.modules:
            name = module.__name__.lower()
            instance = None
            if name in self.singleton:
                if name in self.instances:
                    instance = self.instances[name]
                else:
                    instance = module()
                    self.instances[name] = instance
            else:
                instance = module()
                
            modules[name] = instance
        return cls(**modules)
