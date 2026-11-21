---
title: [Q1634] 依赖缓存的键与 use_cache 陷阱
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1634 · 依赖缓存的键与 use_cache 陷阱

> 难度:★★★★ | 标签:FastAPI, 依赖注入

**问**:同一个依赖在一条依赖链上被引用三次,会执行几次?什么情况下会执行多次?

**答**:默认 use_cache=True 时,缓存键由依赖可调用对象加其参数构成,同一请求内 get_db 被认证依赖、业务依赖、路由处理器各引用一次也只解析一次,全程同一个连接——这是请求级事务一致性的基础。执行多次的两种情况:一是 use_cache=False,每次引用都新建,典型事故是写事务的 session 和读校验的 session 不是同一个,校验通过提交却失败;二是带参数的依赖(如 Depends(paginator) 传不同 page),参数不同缓存键就不同,各解析一次——这通常是对的,但要意识到它已经不是一个实例。缓存作用域是一次请求,跨请求不共享,不要在依赖里放请求间共享的可变状态。

```python
# file: code/03_Web后端开发/q1634_dep_cache.py
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
```

**追问**:
- 想让某依赖每次都新开怎么办?——use_cache=False 显式声明,但要能说清为什么需要两个实例。
- 缓存键包含子依赖吗?——键只由该依赖自身的可调用对象与参数决定,子依赖各自独立缓存,树上按需解析。
