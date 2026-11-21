---
title: [Q5014] 描述符协议深水区：__set_name__ 与优先级链
date: 2026-11-19
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5014 · 描述符协议深水区：__set_name__ 与优先级链

> 难度:★★★ | 标签:描述符, 元编程

**问**：`__set_name__` 在什么时机被调用、解决什么问题？data descriptor（定义 `__set__`/`__delete__`）与 non-data descriptor（只有 `__get__`）在属性查找优先级上差在哪——为什么 `cached_property` 并发下会出问题？

**答**：`__set_name__(owner, name)` 在**类体创建时**（type 构建流程的 `type.__new__` 里）对每个出现在类体中的描述符调用一次，把「我在哪个类的哪个名字下」传给描述符——解决描述符无法预知自己绑定名的老问题（如 ORM 列、验证器自动注册）。优先级链：**实例 `__dict__` vs 描述符**——data descriptor > 实例 `__dict__` > non-data descriptor > 类属性回退。所以：① `__slots__` 能挡实例 dict，因为槽描述符是 data descriptor；② 函数（non-data）可以被实例 dict 里的同名属性覆盖；③ `functools.cached_property` 是 **non-data**：第一次访问算完写进**实例 dict**，之后实例 dict 优先——但并发下多个线程同时首次访问会**各算一遍**（读类属性→算→写 dict 之间存在窗口），非幂等计算会重复执行甚至出错；要线程安全就得自己包锁或改用 data-descriptor 实现。

```python
# 全部标准库，任何 3.x 版本可跑
import functools, threading

class Validator:
    """演示 __set_name__：自动记住绑定名，无需手传字段名。"""
    def __init__(self, minlen: int):
        self.minlen, self.name = minlen, None
    def __set_name__(self, owner, name):
        self.name = name                      # 类创建时调用一次
        print(f"__set_name__: {owner.__name__}.{name}")
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self                       # 类访问返回描述符本身
        return obj.__dict__[self.name]
    def __set__(self, obj, value):
        if len(value) < self.minlen:
            raise ValueError(f"{self.name} 最少 {self.minlen} 字符")
        obj.__dict__[self.name] = value       # data descriptor 里写实例 dict 是惯用法

class User:
    name = Validator(minlen=3)                # 输出 __set_name__: User.name

u = User()
u.name = "alice"                              # 触发 __set__
try:
    u.name = "ab"
except ValueError as e:
    print("拦截:", e)

# 优先级链实测：non-data 描述符可被实例 dict 覆盖，data 不能
class NonData:
    def __get__(self, obj, objtype=None):
        return "from descriptor"
class Demo:
    attr = NonData()
d = Demo()
print(d.attr)                                 # from descriptor
d.__dict__["attr"] = "from instance dict"
print(d.attr)                                 # from instance dict（non-data：实例优先）

class Demo2:
    attr = Validator(minlen=1)                # data descriptor（有 __set__）
d2 = Demo2(); d2.attr = "x"
d2.__dict__["attr"] = "hijack"
print(d2.attr)                                # x —— data descriptor 优先，劫持无效

# cached_property 并发窗口演示
class Service:
    @functools.cached_property
    def config(self):
        return {"id": threading.get_ident()}  # 用线程 id 观测重复计算
s = Service()
results = []
def worker():
    results.append(s.config)
ts = [threading.Thread(target=worker) for _ in range(8)]
[t.start() for t in ts]; [t.join() for t in ts]
print("cached_property 并发首次访问算了几遍:", len({r["id"] for r in results}), "遍（>1 即窗口存在）")
```

**追问**：1) `cached_property` 为什么不做 data descriptor？——做成 data（带 `__set__`）就没法让实例 dict 缓存生效（data 永远优先），缓存逻辑要全部塞进 `__get__` 自己管理字典，复杂且失去「实例级缓存即属性」的简洁；代价就是接受首次并发重复计算。2) `__slots__` 的槽描述符为什么必须 data？——槽值不存在实例 dict（没有 dict），`__set__`/`__delete__` 直接操作槽内存储；若只有 `__get__`，实例 dict 覆盖机制会找不到 dict。3) 类访问 `User.name` 返回描述符本身有什么用？——迁移/自省场景：ORM 用它拿列定义，Pydantic 用它收集字段元信息。

## 背诵要点
1. `__set_name__` 在类创建时由 type 机制调用一次，描述符借此自动感知绑定名。
2. 优先级：data descriptor > 实例 dict > non-data descriptor > 类属性；`__slots__` 依赖 data 优先级。
3. `cached_property` 是 non-data：首次并发访问有重复计算窗口，非幂等计算要加锁。

## 复盘追问
1. 为什么 data descriptor 优先于实例 dict 是语言设计而非实现细节？（提示：保证不变量——若实例可覆盖验证器，约束形同虚设）
2. 怎么给 cached_property 加线程安全又不大改接口？（提示：类级锁包首次计算，算完写实例 dict；或自己实现双检锁）
