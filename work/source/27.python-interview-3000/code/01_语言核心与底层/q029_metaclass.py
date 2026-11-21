class Registry(type):
    registry = {}

    def __new__(mcls, name, bases, ns):
        cls = super().__new__(mcls, name, bases, ns)
        if bases:                       # 跳过抽象基类自身
            Registry.registry[name.lower()] = cls
        return cls

class Handler(metaclass=Registry):
    pass

class JsonHandler(Handler):
    def handle(self, data):
        return f"json:{data}"

class XmlHandler(Handler):
    def handle(self, data):
        return f"xml:{data}"

if __name__ == "__main__":
    print(Registry.registry)   # 子类定义时自动注册
    h = Registry.registry["jsonhandler"]()
    print(h.handle("payload"))
