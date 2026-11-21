---
title: [Q5037] copyreg 与 pickle 的长期持久化兼容契约
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5037 · copyreg 与 pickle 的长期持久化兼容契约

> 难度:★★★★ | 标签:pickle, copyreg, 兼容性, 事故复盘

**问**：用 pickle 做长期持久化（落盘/进缓存）为什么会在半年后爆炸？`copyreg`（`__reduce__`/`__getstate__`）如何建立兼容契约？类改名、字段增删分别怎么处理？

**答**：pickle 存的是**对象图 + 按引用还原**：记录的是类的"模块路径+类名"，还原时在**当前代码里**找类再用当前 `__setstate__`/属性赋值填充。所以旧数据的敌人不是 pickle 格式，而是**你的类在演化**：类改名/移模块 → `AttributeError: Can't get attribute 'MyClass'`（最常见的半年后爆炸）；字段删除/改名 → 新 `__init__` 签名对不上旧状态；新增字段 → 旧数据缺 key。兼容契约三层：1) **协议版本钉死**（`pickle.dumps(x, protocol=5)`，load 时先读协议号）；2) **`__reduce__` 显式化**——不要靠默认"按构造函数重建"，改成"按稳定函数名 + 显式 state dict"还原，函数名成为兼容锚点；3) **`__setstate__` 做字段补默认/迁移**——旧数据进来先归一化。**copyreg.pickle(obj_type, reduce_fn)** 把这套契约注册成类型级规则，还支持 `copyreg.pickle` 的 dispatch 表与 extension registry（缩短类路径）。取舍：与 schema 化协议（protobuf）相比 pickle 契约靠纪律维持，**长期数据（>1 个发布周期）应上 schema 协议**；pickle 只适合"读方与写方同版本部署"的场景。

```python
# file: code/01_语言核心与底层/q5037_copyreg_contract.py
import copyreg
import pickle

# 1) 兼容契约: 显式 __reduce__ + __setstate__, 不依赖默认重建
class Order:
    __version__ = 2

    def __init__(self, order_id: str, amount: int, currency: str = "CNY"):
        self.order_id = order_id
        self.amount = amount
        self.currency = currency      # v2 新增字段, v1 数据没有

    def __reduce__(self):
        # 锚点: 模块级稳定函数名 + (版本, state) —— 类改名不影响还原
        return (_restore_order, (self.__version__,
                                 {"order_id": self.order_id,
                                  "amount": self.amount,
                                  "currency": self.currency}))

def _restore_order(version: int, state: dict) -> "Order":
    """还原入口: 兼容层集中在这里, 类演化只改这一处."""
    if version == 1:                  # v1 -> v2 迁移: 补默认值
        state.setdefault("currency", "CNY")
        state.setdefault("amount", state.pop("price", 0))
    return Order(**state)

copyreg.pickle(Order, lambda o: o.__reduce__())   # 注册为类型级规则
Order.__reduce__ = Order.__reduce__               # (示例中已显式定义, copyreg 负责 dispatch)

# 2) 正常往返
o = Order("A1", 99)
blob = pickle.dumps(o, protocol=5)
r = pickle.loads(blob)
print("往返 OK:", r.order_id, r.amount, r.currency)

# 3) 模拟"半年前的 v1 数据": 没有新字段、字段名不同
v1_state = (1, {"order_id": "OLD1", "price": 500})
v1_blob = pickle.dumps(v1_state, protocol=2)
ver, state = pickle.loads(v1_blob)
old = _restore_order(ver, state)
print("v1 数据迁移还原:", old.order_id, old.amount, old.currency)

# 4) 类改名事故复现: 默认 pickle(未建契约)按类路径还原
class Legacy:
    pass

bad = pickle.dumps(Legacy(), protocol=5)
del Legacy
import sys
sys.modules[__name__].__dict__.pop("Legacy", None)  # 名字已不存在
try:
    pickle.loads(bad)
except AttributeError as e:
    print("默认 pickle 的改名爆炸:", str(e)[:60], "...")
```

**追问**：1) `copyreg.pickle()` 与自己写 `__reduce__` 的关系？——`copyreg` 注册类型级 reducer（等价于给不可改代码的第三方类型补契约），自己类直接定义 `__reduce__` 即可；两者都走 pickle 的 reduce 协议。2) 为什么协议号要显式钉死？——默认协议随 Python 版本抬升（3.8→5），旧版本读者解不了新协议；钉住 5 并在存储里带版本元数据是双向兼容的地基。3) pickle 长期持久化的替代？——protobuf/msgpack + 显式 schema 迁移，或干脆存 JSON + 版本号字段；pickle 留给"同版本一起发布"的临时态（如进程内缓存、任务参数）。

## 背诵要点
- pickle 还原按"类路径 + 当前代码"，旧数据的敌人是类演化：改名→AttributeError，增删字段→签名错配。
- 契约三件套：协议号钉死、`__reduce__` 显式锚点（稳定函数名）、`__setstate__`/还原函数做迁移。
- 长于一个发布周期的数据用 schema 协议；pickle 限同版本部署场景。

## 复盘追问
- 半年后的今天 "Can't get attribute 'Order'" 爆了，你的应急读取顺序是什么（旧代码/兼容 stub/重写数据）？
- 团队规范该在哪一层强制"pickle 不落长期存储"——code review、CI 扫描还是封装层？
