---
title: "[Q5151] __missing__ 协议原理：defaultdict、Counter 与自定义映射"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5151 · __missing__ 协议原理：defaultdict、Counter 与自定义映射

难度：P7 ｜ 标签：`__missing__`、defaultdict、Counter、映射协议

**问**：`defaultdict`、`Counter`、`OrderedDict` 对"缺失 key"的行为为什么各不相同？`__missing__` 在映射协议里处于什么位置（与 `__getitem__`、`dict.get`、`in` 的关系）？如何用它实现"读不写入"的惰性加载字典？

**答**：
结论：`__missing__(self, key)` 是 `dict` 子类专用的钩子——**只在 `d[key]` 形式（`__getitem__`）且查不到时被调用**；`get()`、`in`、`keys()` 都不经过它。三个内置差异：① `defaultdict.__missing__` 会调用 `default_factory` 并**把结果写入 dict**（副作用是插入）；② `Counter.__missing__` 返回 0 且**不插入**（读安全）；③ 普通 `dict` 没有 `__missing__`，直接抛 KeyError。注意 `dict.get(k)` 永远不会触发 `default_factory`，这是"配置字典默认值不生效"事故的高频根因。

取舍：用 `defaultdict` 求"写式默认"（分组累积）最省事，但会让只读操作污染字典（顺手塞满垃圾 key）；需要"读式默认"（缓存未命中计算但不缓存结果）时继承 dict 实现 `__missing__` 返回计算值而不写入。另一个取舍：`__missing__` 是 Python 层方法，只对 `dict` 子类生效，不能给普通 dict 实例打补丁（`typing.TypedDict` 等运行时也不走它）。

实战：实现惰性加载配置/资源池时，在 `__missing__` 里加载并**有条件写入**（可加 LRU 上限或负缓存）；并发场景下 `__missing__` 不自带锁，多线程同时 miss 会重复加载，需要外层锁或单飞（singleflight）。

```python
from collections import Counter, OrderedDict

class LazyDict(dict):
    """读式默认：缺失时计算，不写回 dict"""
    def __missing__(self, key):
        print(f"  [compute] {key}")
        return key.upper()          # 返回但不插入

class GroupDict(dict):
    """写式默认：等价 defaultdict(list)"""
    def __missing__(self, key):
        v = self[key] = []
        return v

d = LazyDict()
print("getitem :", d["alpha"])          # 触发 __missing__，返回 ALPHA
print("keys after __getitem__:", list(d))   # 仍为空 —— 没写入
print("get     :", d.get("beta"))        # None —— get 不走 __missing__
print("in      :", "beta" in d)          # False —— in 不走 __missing__

g = GroupDict()
g["items"].append(1)                    # 触发 __missing__ 并插入 []
print("group  :", g)

c = Counter("aab")
print("counter miss:", c["z"])           # 0，不插入
print("counter keys:", list(c))

# OrderedDict 的 move_to_end 式 missing（3.x 实现：缺 key 返回 default=None 语义由调用方决定）
od = OrderedDict(a=1)
try:
    od["missing"]
except KeyError as e:
    print("OrderedDict raises KeyError:", e.args[0])
```

**追问一**：为什么 `defaultdict` 的 `default_factory` 抛异常时表现如何？——`__missing__` 里 factory 调用异常会原样抛出（不包 KeyError），且字典不残留部分状态；若 factory 返回可变对象被调用方修改后再写回，无原子性问题（单线程），多线程下 `d[k]` 的 check-then-insert 在 C 层一次性完成（`__missing__` 同步调用），所以 defaultdict 天然比"手动 if k not in d"少一次竞态。

**追问二**：`__missing__` 与 `dict.__getitem__` 的 C 实现顺序是什么？——`subscript` 先走 fast path（哈希命中直接返回），miss 后检查类型是否有 `__missing__`（`PyDict_GetItem` 失败 → `dict_subscript` 调用 slot）；这意味着**高频命中的读不受 hook 影响**，只有 miss 才付出 Python 层调用成本，因此惰性字典热路径开销接近原生 dict。

## 背诵要点
- `__missing__` 只由 `d[key]`（`__getitem__` miss）触发；`get()`/`in`/迭代都不走它——defaultdict 配 `get()` 不生效是经典事故。
- defaultdict 的 missing 会写入（写式默认），Counter 返回 0 不写入（读式默认），自定义按需选边。
- `__missing__` 是 Python 层钩子、仅 dict 子类可用；并发 miss 需要外层锁/单飞。

## 复盘追问
- 一个用 `defaultdict(list)` 做分组的服务，接口里顺手 `d.get(k)` 读了个不存在的 key 返回 None，但日志统计却发现字典无限增长，如何定位与根治？（定位：遍历 key 集合比对预期；根治：读路径换 `__missing__` 读式默认或显式 `in` 判断）
- 如何给惰性加载字典加上"并发单飞 + 失败负缓存"？说出关键结构。（per-key Future/锁表 + 失败时短 TTL 标记，讨论异常传播）
