import re

class Inject:
    """
    A decorator function for injecting dependencies into classes.

    :param modules: A list of modules providing the dependencies.
    :param singleton: Optional parameter specifying dependencies to be treated as singletons.
                      If None (default), all dependencies are created per instance.
                      If a list of module names is provided, the corresponding dependencies are treated as singletons.
    :return: A decorator function that, when applied to a class, injects the specified dependencies into the class and returns a class instance ready to use.

     **Examples**:

    Applying the `Inject` decorator to a class:

    ```python
    class ToInject:
        def __init__(self):
            pass
            
        def foo(self):
            return "bar"

    @Inject(modules=[ToInject])
    class MyClass:
        def __init__(self, to_inject: ToInject):
            self.to_inject = to_inject

            
    MyClass.foo() # should returns "bar"
    ```

    If you provide any dependency as string in the singleton list, that dependency will be instanciated only once.

    ```python
    class ToInject:
        def __init__(self):
            pass
            
        def foo(self):
            return "bar"

    @Inject(modules=[ToInject], singleton=["to_inject"])
    class MyClass:
        def __init__(self, to_inject: ToInject):
            self.to_inject = to_inject

            
    MyClass.foo() # should returns "bar"
    ```
    """

    instances = {}
    singleton = []

    def __init__(self, modules = [], singleton = []):
        self.modules = modules
        self.singleton = singleton

    def __call__(self, cls):
        modules = {}
        for module in self.modules:
            name = module.__name__

            words = re.findall(r'[A-Z][a-z]*', name)
            name = "_".join(words).lower()

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
