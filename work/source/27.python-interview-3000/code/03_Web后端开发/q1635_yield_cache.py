"""缓存命中的 yield 依赖: 资源只进出各一次, 清理在响应后倒序执行(纯标准库模拟)。"""


class Scope:
    """模拟一次请求的依赖作用域。"""

    def __init__(self):
        self.cache = {}
        self.events = []
        self.stack = []

    def yield_dep(self, name, factory):
        if name in self.cache:
            self.events.append(f"{name}: 缓存命中, 不再 setup")
            return self.cache[name]
        self.events.append(f"{name}: setup 进入")
        value = factory()
        self.cache[name] = value
        self.stack.append(name)              # 登记, 供响应完成后清理
        return value

    def teardown(self):
        while self.stack:
            self.events.append(f"{self.stack.pop()}: teardown 清理")   # 后进先出


scope = Scope()
db = scope.yield_dep("db", lambda: "conn-1")
scope.yield_dep("db", lambda: "conn-2")      # 同请求第二次引用 -> 命中
scope.yield_dep("auth", lambda: "ctx")       # auth 内部也依赖 db -> 命中
scope.yield_dep("auth", lambda: "ctx2")
scope.teardown()
for e in scope.events:
    print(e)
print("要点: 命中的 yield 依赖不会重复 setup, teardown 倒序且发生在响应之后")
