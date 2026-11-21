---
title: [Q5041] 重写 __eq__ 忘 __hash__：去重失效事故复盘
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5041 · 重写 __eq__ 忘 __hash__：去重失效事故复盘

> 难度:★★★ | 标签:eq, hash, 事故复盘, set, 不变式

**问**：生产上遇到一个事故：给订单类重写了 `__eq__` 之后，`set` 去重和 `dict` 查找行为全变了，同一对象"查不到自己"。这类问题的根因是什么？语言层面的不变式是什么？如何系统性防住？

**答**：根因是 Python 的 hash/equality 不变式：**`a == b` 为真的两个对象必须有相同的 `hash(a) == hash(b)`**。当你定义了 `__eq__`，解释器会把 `__hash__` 置为 `None`（实例变不可哈希，`set`/`dict` 直接 TypeError）；而如果你又随手定义了 `__hash__` 但它不满足与 `__eq__` 的一致性（比如基于可变字段、或基于 id 而 `__eq__` 基于值），就会出现"相等但分桶不同 → set 里出现两个'相等'元素"或"同值对象查不到"的事故。三条防线：1) **用 dataclass/equatable 工具自动生成**：`@dataclass(eq=True)` 默认同时生成两者且 frozen 时 hash 基于字段（可变类加 `eq=True` 不生成 hash，避免可变 hash）；2) 可变对象**绝不要**把 hash 建在可变字段上（Q1297 的内容漂移问题）；3) CI 加静态检查/单测不变式断言（相等必同桶、去重往返一致）。事故复盘要点：这类 bug 只在大数据量或跨进程（重新构造对象）路径暴露，小单测里 `==` 通过就上线，正是漏测 set/dict 路径的典型。

```python
# file: code/01_语言核心与底层/q5041_eq_hash.py
class OrderBad:
    """事故版: 重写 __eq__ 后默认 __hash__ 被置 None"""
    def __init__(self, oid):
        self.oid = oid

    def __eq__(self, other):
        return isinstance(other, OrderBad) and self.oid == other.oid

o = OrderBad(1)
try:
    {o}
except TypeError as e:
    print("事故1: 不可哈希 ->", str(e)[:45])

class OrderWorse:
    """事故版: 手写 __hash__ 与 __eq__ 不一致 (hash 用 id, eq 用值)"""
    def __init__(self, oid):
        self.oid = oid

    def __eq__(self, other):
        return isinstance(other, OrderWorse) and self.oid == other.oid

    def __hash__(self):
        return id(self)          # 每个实例桶都不同

a, b = OrderWorse(1), OrderWorse(1)
print("事故2: a==b:", a == b, "| 进了同一个set吗:", len({a, b}))  # 2 个"相等"元素

class OrderGood:
    """修复版: hash 与 eq 基于同一不可变字段集"""
    __slots__ = ("oid",)
    def __init__(self, oid):
        self.oid = oid

    def __eq__(self, other):
        return isinstance(other, OrderGood) and self.oid == other.oid

    def __hash__(self):
        return hash(self.oid)

x, y = OrderGood(1), OrderGood(1)
print("修复: a==b:", x == y, "| set 长度:", len({x, y}),
      "| dict 命中:", {x: "v"}[y])

# CI 不变式断言: 相等必同桶 + 去重往返一致
def check_invariant(cls, samples):
    for p in samples:
        for q in samples:
            if p == q:
                assert hash(p) == hash(q), f"{cls.__name__} 违反不变式"
    assert len(set(samples)) == len({s.oid for s in samples})

check_invariant(OrderGood, [OrderGood(i) for i in range(10)])
print("不变式断言通过")
```

**追问**：1) 为什么定义 `__eq__` 后 CPython 会把 `__hash__` 置为 None 而不是保留默认（基于 id）？——保留默认会造成更隐蔽的事故：值相等但被当作两个 key（正是 OrderWorse 手写复现的行为）；置为 None 让错误**尽早**在 TypeError 处爆炸，符合 fail-fast。2) `frozen=True` 的 dataclass 为什么能安全生成 `__hash__`？——字段不可变保证 hash 稳定；可变 dataclass 默认 `eq=True, frozen=False` 时不生成 hash（`__hash__` 置 None），把"可变对象做 key"的风险挡在门外。3) 跨进程/跨机器场景还要注意什么？——hash 只在单进程内有意义（PYTHONHASHSEED 随机化，Q535），分布式去重必须基于规范化的 key（规范化序列化）而不是对象的 hash。

## 背诵要点
- 定义 `__eq__` 后 `__hash__` 被置 None（实例不可哈希）；不变式：相等必同 hash。
- 手写 hash 与 eq 基于不同字段 → set 出现重复/查不到，事故只在大数据量暴露。
- 可变对象禁止把 hash 建在可变字段上；dataclass frozen=True 才自动生成安全 hash。

## 复盘追问
- 上线前的哪条单测/CI 检查能在最早期拦住这类 eq/hash 不一致？（提示：不变式断言可写成通用 property test）
- 如果事故是"同一订单在 set 里出现两次"，你的排查顺序是什么？（提示：先 `type(o).__hash__ is None`，再 diff `__eq__` 与 `__hash__` 用到的字段集）
