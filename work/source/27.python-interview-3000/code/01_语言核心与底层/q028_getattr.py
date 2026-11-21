class Lazy:
    def __init__(self):
        self.loaded = {}

    def __getattr__(self, name):     # 只在找不到时进入
        print(f"lazily computing {name}")
        self.loaded[name] = f"value-of-{name}"
        return self.loaded[name]

class Guarded:
    def __init__(self):
        self._x = 1

    def __getattribute__(self, name):
        print(f"access {name}")
        return super().__getattribute__(name)   # 必须 super 防递归

if __name__ == "__main__":
    o = Lazy()
    print(o.missing)     # 触发 __getattr__
    print(o.missing)     # 第二次走实例 dict,不再触发

    g = Guarded()
    _ = g._x
