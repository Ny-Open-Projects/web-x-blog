---
title: "[Q6252] Depends 的请求级缓存与覆盖：use_cache 的 key、子依赖复用与 lru_cache 陷阱"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6252 · Depends 的请求级缓存与覆盖：use_cache 的 key、子依赖复用与 lru_cache 陷阱

难度：P7 ｜ 标签：FastAPI、Depends、use_cache、dependency_overrides、请求级单例、lru_cache、依赖图

基线：库知识卡，代码用标准库模拟 FastAPI 的依赖缓存 key 与 override 匹配规则。

**问**：一个接口的依赖树是 `get_current_user → get_db → get_settings`，同一个请求里三个地方都声明了 `Depends(get_db)`，监控却显示一次请求建了 3 个数据库会话；测试里用 `app.dependency_overrides[get_db] = fake_db` 覆盖成功，换成 `@lru_cache` 包了一层的 `get_db_cached` 后覆盖就失效了，测试打到了真库。`Depends` 的"请求级单例"是怎么实现的？cache key 到底是什么？override 又按什么匹配？

**答**：

- **结论**：FastAPI 在一次请求内维护一个 `dependency_cache`，key 是 **`(dependency_callable, tuple(sorted(security_scopes)))`**——同一个可调用对象、同一组安全作用域，只解析一次，后续直接拿缓存；子依赖也走同一个 cache，所以 `get_db` 被三处 `Depends` 引用只会执行一次。`use_cache=False` 让这次解析**跳过读缓存**（但仍会写？实现上是"不参与缓存"，每次重新调用），用于"每次都要新值"的依赖（如分页参数解析、一次性 token 校验）。`dependency_overrides` 是一个以**原始可调用对象为 key** 的 dict：路由里声明的是哪个对象，就覆盖哪个对象；一旦你用 `lru_cache`/`functools.partial`/装饰器把 `get_db` 包成了另一个对象，路由引用的是包装后的对象，覆盖原函数自然不生效。此外 cache key 含 `params` 吗？不含——同一依赖带不同参数（比如 `Depends(get_settings, env="a")` 与 `env="b"`）在 FastAPI 里是不同的依赖对象（`Depends` 实例不同），不会被错误合并，但你自己写的工厂函数要注意。

- **取舍**：a) 请求级单例是默认：DB session、当前用户、租户配置这类"一次请求内应共享"的资源必须靠它，否则会出现多个 session 各自开事务、互相看不到未提交数据；b) `use_cache=False` 要慎用：它只该给"必须是新实例"的依赖（如每次调用都要读最新配置/生成一次性 nonce），滥用会把单例拆成多份，抵消依赖注入的意义；c) override 的纪律：测试里覆盖"路由实际引用的那个对象"，最好在 `conftest` 里集中定义依赖对象、禁止在路由里临时包一层；d) 生成器依赖（`yield`）的清理顺序是**逆依赖顺序**，且发生在响应之后；override 成普通函数会跳过清理，测试里要显式断言资源已释放。

- **实战**：事故形态是"一次请求三个 session，库存扣减看不见"——三个子模块各自 `Depends(get_db)`，本应共享同一个 session，但其中一个模块把 `get_db` 用 `@lru_cache` 包了一层（想"优化"连接创建），导致依赖图里出现两个不同的 callable，cache 各建一份；库存模块在 session A 扣减未提交，订单模块在 session B 查询看不到，误判"库存不足"回滚。修复：删除 `lru_cache`，连接池本身已经是单例，不需要再缓存 session 工厂；测试里加一条断言"一次请求内 `get_db` 调用次数 == 1"；override 统一指向 `deps.get_db` 这个对象，包装函数只做参数绑定、不改变依赖身份。

```python
# 模拟 FastAPI 依赖缓存: key=(callable, scopes), 子依赖共享, override 按对象匹配
import functools

class Container:
    def __init__(self):
        self.cache = {}
        self.calls = []
        self.overrides = {}

    def resolve(self, dep, use_cache=True, scopes=()):
        key = (dep, tuple(sorted(scopes)))
        if use_cache and key in self.cache:
            return self.cache[key]
        real = self.overrides.get(dep, dep)
        self.calls.append(real.__name__)
        value = real(self) if getattr(real, "__needs_container__", False) else real()
        if use_cache:
            self.cache[key] = value
        return value

SETTINGS = {"env": "prod"}

def get_settings():
    return SETTINGS                      # 同一个对象, 便于验证缓存命中

def get_current_user():
    return {"id": 7}

# 1) 同一 callable + 同 scopes -> 请求级单例
c = Container()
a = c.resolve(get_current_user)
b = c.resolve(get_current_user)
print("→ 两次 Depends 同一依赖:", a is b, "| 调用次数:", c.calls.count("get_current_user"))
assert a is b
assert c.calls.count("get_current_user") == 1

# 2) use_cache=False: 每次都重新执行
c2 = Container()
x = c2.resolve(get_settings)
y = c2.resolve(get_settings, use_cache=False)
z = c2.resolve(get_settings, use_cache=False)
print("→ use_cache=False 调用次数:", c2.calls.count("get_settings"))
assert x is y is z is not None          # 值可能相同
assert c2.calls.count("get_settings") == 3   # 1 次缓存 + 2 次强制

# 3) scopes 不同 -> 不同 cache key, 重新解析
c3 = Container()
c3.resolve(get_settings, scopes=("admin",))
c3.resolve(get_settings, scopes=("user",))
assert c3.calls.count("get_settings") == 2
# 4) override 按对象匹配
c4 = Container()
fake_calls = []
def fake_settings():
    fake_calls.append(1)
    return {"env": "test"}
c4.overrides[get_settings] = fake_settings
got = c4.resolve(get_settings)
print("→ override 生效:", got, "| fake 调用:", len(fake_calls))
assert got == {"env": "test"} and len(fake_calls) == 1
# 5) lru_cache 包装后是另一个对象, 覆盖原函数不生效
@functools.lru_cache(maxsize=None)
def get_settings_cached():
    return {"env": "prod-cached"}

c5 = Container()
c5.overrides[get_settings] = fake_settings
val = c5.resolve(get_settings_cached)
print("→ 覆盖原始函数后, 路由引用的是 lru_cache 包装对象:", val)
assert val == {"env": "prod-cached"}      # fake 没生效
c5.overrides[get_settings_cached] = fake_settings
assert c5.resolve(get_settings_cached) == {"env": "prod-cached"}  # 已缓存, 新 override 不回溯
c6 = Container(); c6.overrides[get_settings_cached] = fake_settings
assert c6.resolve(get_settings_cached) == {"env": "test"}         # 请求前覆盖才生效

# 6) 请求级单例的边界: 新请求 = 新容器 = 新缓存
new_request = Container()
assert new_request.resolve(get_current_user) is not a
print("→ 跨请求不共享缓存:", new_request.resolve(get_current_user))
```

**追问一**：为什么 cache key 要包含 security scopes，而不是简单的 `id(dep)`？—— `Depends` 可以带 `Security(..., scopes=["admin"])`，同一个依赖在不同 scopes 下可能有不同的授权结果（比如 `get_current_user` 要求 admin 时校验失败应抛 403，而普通用户通过）；如果只按 callable 缓存，先解析的宽松结果会被后续严格请求复用，造成越权。把 scopes 排序后拼进 key，保证"同一依赖 + 同一授权要求"才复用。参数不在 key 里，是因为带不同参数的 `Depends` 在路由定义时就是不同的 `Depends` 对象（call 相同但 `Depends` 实例不同）；如果你用工厂函数返回闭包，每个闭包是不同 callable，自然也是不同 key。

**追问二**：生成器依赖的 `yield` 之后清理，和 `use_cache=False` 混用会怎样？—— 生成器依赖在 `yield` 前是"创建"，`yield` 后是"清理"，FastAPI 用 `AsyncExitStack` 按解析顺序压栈、请求结束时逆序弹出。如果同一个生成器依赖被 `use_cache=False` 解析两次，就会有**两个实例、两次清理**，它们各自持有独立资源（两个 session、两个锁），业务代码以为共享却实际不共享；如果只解析一次，清理也只发生一次。坑在于"清理抛异常"：逆序弹出时一个清理失败会中断后续清理，所以清理逻辑要自己 try/except，不能假设前面的资源一定还活着。

## 背诵要点

- 依赖缓存 key 是 `(callable, sorted(scopes))`，同一请求内同 key 只执行一次；子依赖共享同一个 cache，`use_cache=False` 跳过缓存。
- `dependency_overrides` 以原始 callable 为 key；用 `lru_cache`/`partial` 包一层后路由引用的是新对象，覆盖原函数无效。
- 请求级单例随请求容器销毁；生成器依赖按逆序清理，解析两次就有两份资源与两次清理。

## 复盘追问

- 一次请求建了 3 个 session，最可能是什么原因？（同一依赖被包装成不同 callable、或用了 use_cache=False、或跨了不同请求容器）
- 测试里 override 不生效怎么排查？（打印路由 dependant.call 与 overrides 的 key 是否是同一对象；lru_cache/装饰器会换对象）
