"""__init_subclass__ 的插件自动注册:声明即注册,重名即报错。"""


class PluginBase:
    registry = {}

    def __init_subclass__(cls, name=None, priority=100, **kwargs):
        super().__init_subclass__(**kwargs)
        key = name or cls.__name__.lower()
        if key in PluginBase.registry:
            occupied = PluginBase.registry[key].__name__
            raise ValueError(f"插件名重复:{key} 已被 {occupied} 占用")
        required = getattr(cls, "required", ())
        missing = [m for m in required if not callable(getattr(cls, m, None))]
        if missing:
            raise TypeError(f"插件 {cls.__name__} 缺少必需方法:{missing}")
        cls.priority = priority
        PluginBase.registry[key] = cls

    @classmethod
    def sorted_plugins(cls):
        return sorted(cls.registry.items(), key=lambda kv: kv[1].priority)


class Cleaner(PluginBase, name="clean", priority=10):
    required = ("run",)

    def run(self):
        return "cleaning"


class Report(PluginBase, name="report", priority=50):
    required = ("run",)

    def run(self):
        return "reporting"


if __name__ == "__main__":
    for key, cls in PluginBase.sorted_plugins():
        print(f"插件 {key:<7} priority={cls.priority:<4} run -> {cls().run()}")

    try:
        class Dup(PluginBase, name="clean"):
            def run(self):
                return "dup"
    except ValueError as e:
        print("重名拦截:", e)

    try:
        class HalfDone(PluginBase, name="half"):
            required = ("run",)
    except TypeError as e:
        print("缺方法拦截:", e)
