"""全局状态污染的检测:可变全局扫描与快照对比。"""

CONFIG = {"debug": False}       # 潜在污染源
_counter = [0]


def inc():
    _counter[0] += 1
    return _counter[0]


def scan_module_globals(module):
    """列出模块里所有可变的全局对象。"""
    import types
    risky = {}
    simple = (str, int, float, bool, bytes, tuple, type(None),
              frozenset, types.ModuleType, types.FunctionType, type)
    for name, value in vars(module).items():
        if name.startswith("__"):
            continue
        if isinstance(value, (list, dict, set)):
            risky[name] = type(value).__name__
        elif not isinstance(value, simple):
            risky[name] = "自定义对象"
    return risky


def snapshot(module):
    return {k: repr(v) for k, v in vars(module).items() if not k.startswith("__")}


if __name__ == "__main__":
    import __main__
    print("可变全局清单:", scan_module_globals(__main__))

    before = snapshot(__main__)
    inc()
    inc()
    changed = [k for k in before if before[k] != snapshot(__main__)[k]]
    print("两次快照之间被改的全局:", changed)

    class Counter:
        def __init__(self):
            self.n = 0

        def inc(self):
            self.n += 1
            return self.n

        def reset(self):
            self.n = 0

    c = Counter()
    c.inc()
    c.reset()
    print("类封装后测试可复位:", c.n == 0)
