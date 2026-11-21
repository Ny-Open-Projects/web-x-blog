---
title: [Q1635] 缓存命中的 yield 依赖只进出一次
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1635 · 缓存命中的 yield 依赖只进出一次

> 难度:★★★☆ | 标签:FastAPI, 依赖注入

**问**:被缓存命中的 yield 依赖,setup 和 teardown 各执行几次?清理发生在什么时候?

**答**:一次。yield 依赖首次解析时执行 setup 并把生成器登记;后续引用走缓存命中,不再进入生成器;请求结束、响应发送完毕后,框架按登记栈倒序执行 teardown——后申请的资源先释放,比如先开事务再开连接,就要先提交事务再还连接。两个易错点:一是以为多次引用会多次 setup,结果在 setup 里做了重复计数;二是在 teardown 里假设还有请求上下文,实际上响应已经发出,teardown 只做资源释放,不做业务收尾。异常传播上,处理函数抛错时 teardown 仍会执行,生成器里用 try/finally 包住清理逻辑才可靠。

```python
# file: code/03_Web后端开发/q1635_yield_cache.py
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
```

**追问**:
- teardown 顺序能自定义吗?——顺序由依赖树解析与登记顺序决定,想要确定顺序就控制依赖声明结构。
- yield 后抛异常会怎样?——异常向上传播,清理逻辑放 finally 才保证执行,别指望 yield 之后的代码必然跑到。
