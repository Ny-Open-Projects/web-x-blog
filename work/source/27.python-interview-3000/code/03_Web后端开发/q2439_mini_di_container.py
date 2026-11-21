"""极简依赖注入容器: 注册、解析、单例与环检测(纯标准库)。"""


class CycleError(Exception):
    """依赖图存在环。"""


class MissingError(Exception):
    """解析了未注册的名字。"""


class Container:
    def __init__(self):
        self._factories = {}                     # name -> (factory, singleton)
        self._cache = {}
        self._stack = []                         # 解析中的名字栈, 用于环检测

    def register(self, name, factory, singleton=False):
        self._factories[name] = (factory, singleton)
        return self

    def resolve(self, name):
        if name in self._cache:
            return self._cache[name]
        if name in self._stack:
            raise CycleError("依赖环: " + " -> ".join(self._stack + [name]))
        if name not in self._factories:
            raise MissingError("未注册的依赖: " + name)
        factory, singleton = self._factories[name]
        self._stack.append(name)
        try:
            instance = factory(self)             # 工厂拿容器自己解析下层依赖
        finally:
            self._stack.pop()
        if singleton:
            self._cache[name] = instance
        return instance


def make_config(c):
    return {"db_url": "sqlite://:memory:", "retries": 3}


def make_db(c):
    return {"url": c.resolve("config")["db_url"], "conns": 2}


def make_service(c):
    return {"db": c.resolve("db"), "retries": c.resolve("config")["retries"]}


box = (Container()
       .register("config", make_config, singleton=True)
       .register("db", make_db, singleton=True)
       .register("service", make_service))

svc = box.resolve("service")
print("service:", svc)
assert svc["db"]["url"] == "sqlite://:memory:" and svc["retries"] == 3
assert box.resolve("db") is svc["db"]            # 单例: 同一实例
assert box.resolve("config") is box.resolve("config")

# 缺失依赖
try:
    box.resolve("cache")
except MissingError as exc:
    print("缺失依赖 ->", exc)
    assert "cache" in str(exc)

# 循环依赖
bad = Container()
bad.register("a", lambda c: c.resolve("b"))
bad.register("b", lambda c: c.resolve("a"))
try:
    bad.resolve("a")
except CycleError as exc:
    print("循环依赖 ->", exc)
    assert "a -> b -> a" in str(exc)
print("要点: 容器三件套 注册 解析 缓存, 解析栈负责抓环; "
      "工厂接收容器自身从而把依赖图串起来, 单例靠缓存字典实现")
