"""super 在多继承混入中的协作:MRO 接力与 object 默认落地。"""


class Fetcher:
    """核心实现:混入链最终接力到这里,object 是隐式终点。"""

    def fetch(self, key):
        return f"data:{key}"


class LoggingMixin:
    def fetch(self, key):
        print(f"  [log] 进入 {type(self).__name__}.fetch key={key}")
        return super().fetch(key)


class CacheMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)      # 参数沿 MRO 继续传递
        self.cache = {}

    def fetch(self, key):
        if key in self.cache:
            print(f"  [cache] 命中 {key}")
            return self.cache[key]
        value = super().fetch(key)
        self.cache[key] = value
        return value


class Client(CacheMixin, LoggingMixin, Fetcher):
    pass


class BrokenClient(LoggingMixin, Fetcher):
    """少一层混入也能工作:MRO 跳过缺失能力,只要终点存在。"""
    pass


if __name__ == "__main__":
    print("MRO:", [cls.__name__ for cls in Client.__mro__])
    c = Client()
    print("第一次:", c.fetch("user:1"))
    print("第二次:", c.fetch("user:1"))

    b = BrokenClient()
    print("缺 CacheMixin 的客户端:", b.fetch("user:1"))

    # 反例:混入链上没有可接力的终点,super 停在 object
    class LoneMixin:
        def fetch(self, key):
            return super().fetch(key)

    class Lone(LoneMixin):
        pass

    try:
        Lone().fetch("x")
    except AttributeError as e:
        print("接力断在 object:", e)
