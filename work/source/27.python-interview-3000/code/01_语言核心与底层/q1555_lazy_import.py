import importlib
import time


class LazyModule:
    """延迟代理:首次属性访问才真正导入。"""

    def __init__(self, name):
        self._name = name
        self._module = None

    def _load(self):
        if self._module is None:
            self._module = importlib.import_module(self._name)
            print("  [lazy] %s imported on first use" % self._name)
        return self._module

    def __getattr__(self, attr):
        return getattr(self._load(), attr)


def parse_with_json(data):
    """模式一:import 进函数,冷路径按需付费。"""
    import json
    return json.loads(data)


def make_plotter():
    """模式三:工厂——只有真要产出时才构建工具。"""
    def plot(points):
        import json
        return json.dumps({"points": points})
    return plot


if __name__ == "__main__":
    print("parse:", parse_with_json('{"ok": true}'))

    json_mod = LazyModule("json")
    print("proxy dumps:", json_mod.dumps([1, 2, 3]))
    print("proxy again:", json_mod.dumps({"a": 1}))

    plot = make_plotter()
    print("factory plot:", plot([(0, 1), (2, 3)]))

    # 首次 vs 二次导入的耗时差:第二次只是 sys.modules 字典命中
    t0 = time.perf_counter()
    importlib.import_module("json")
    t1 = time.perf_counter()
    importlib.import_module("json")
    t2 = time.perf_counter()
    print("first import :", round((t1 - t0) * 1e6, 1), "us")
    print("second import:", round((t2 - t1) * 1e6, 1), "us")
