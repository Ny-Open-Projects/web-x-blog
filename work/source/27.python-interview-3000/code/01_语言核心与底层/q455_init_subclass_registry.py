class Plugin:
    """基类:自动注册子类并强制实现 run"""
    registry = {}

    def __init_subclass__(cls, name=None, strict=True, **kwargs):
        super().__init_subclass__(**kwargs)
        if strict and "run" not in cls.__dict__:
            raise TypeError(f"{cls.__name__} must implement run")
        key = name or cls.__name__.lower()
        if key in Plugin.registry:
            raise ValueError(f"plugin {key} already registered")
        Plugin.registry[key] = cls

class CsvPlugin(Plugin, name="csv"):
    def run(self, src):
        return f"csv from {src}"

class JsonPlugin(Plugin):
    def run(self, src):
        return f"json from {src}"

if __name__ == "__main__":
    try:
        class Broken(Plugin):             # strict 且没实现 run:定义即报错
            pass
    except TypeError as e:
        print("rejected at class creation:", e)

    print(sorted(Plugin.registry))
    print(Plugin.registry["csv"]().run("data.csv"))
