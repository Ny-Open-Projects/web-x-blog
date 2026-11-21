"""依赖注入缓存: 同一请求内按可调用对象缓存, 不同参数各自缓存(纯标准库模拟)。"""


class RequestScope:
    """一次请求一个作用域: 缓存键 = 依赖可调用对象 + 其参数。"""

    def __init__(self):
        self.cache = {}
        self.log = []

    def resolve(self, dep_id, params=(), use_cache=True):
        key = (dep_id, params) if use_cache else None
        if key is not None and key in self.cache:
            self.log.append(f"hit {dep_id}{params}")
            return self.cache[key]
        self.log.append(f"call {dep_id}{params}")
        value = f"<{dep_id} 实例>"
        if key is not None:
            self.cache[key] = value
        return value


req = RequestScope()
# 场景1: get_db 被认证依赖与路由处理器同时依赖 -> 一次解析, 全请求同一个连接
db1 = req.resolve("get_db")
db2 = req.resolve("get_db")
print("同一请求内 get_db 复用:", db1 == db2)

# 场景2: 分页依赖带不同参数 -> 缓存键不同, 各解析一次, 互不污染
req.resolve("paginator", params=("page=1",))
req.resolve("paginator", params=("page=2",))
print("不同参数各解析一次:", req.log)

# 场景3: use_cache=False 的会话依赖被引用两次 -> 两个会话, 事务互不可见
req.resolve("session", use_cache=False)
req.resolve("session", use_cache=False)
print("use_cache=False 每次新建, 写了不回滚的假象就是这么来的")
print("调用序列:", req.log)
