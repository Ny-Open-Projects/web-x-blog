---
title: "[Q5237] 自定义 __eq__ 后 __hash__ 的失效：不可哈希的连锁反应"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5237 · 自定义 __eq__ 后 __hash__ 的失效：不可哈希的连锁反应

难度：P6 ｜ 标签：__eq__、__hash__、不可哈希、hash None、dict/set 键、dataclass eq、等值契约

**问**：为什么自定义类一旦定义了 `__eq__`，实例就变得不可哈希？语言层面是怎么实现这个"失效"的（`__hash__` 被置为什么）？dataclass 的 `eq=True` 与 `frozen=True` 在哈希上分别做什么？恢复可哈希的正确姿势有哪些、各自的语义风险是什么？

**答**：
结论：这是语言规范的**等值契约**：`a == b` 成立则 `hash(a) == hash(b)` 必须成立（否则 dict/set 的桶定位崩坏，Q1297）。默认继承自 object 的 `__eq__` 是恒等比较（同一对象才相等），与之配对的是基于 `id()` 的默认 `__hash__`，两者天然一致。当你自定义 `__eq__`（改为按值比较），默认 `__hash__` 与新相等语义**必然失配**——按值相等的两个对象 id 不同、哈希不同。CPython 的实现是在类创建时做静态检查：**类体内定义了 `__eq__` 而未定义 `__hash__`，就把 `__hash__` 置为 None**——`A.__hash__ is None`，实例调用 `hash(a)` 抛 TypeError: unhashable type。连锁反应面很宽：进 set、当 dict 键、被 dedupe（`list(set(items))`）、进 lru_cache 的参数（Q5168）、collections.Counter 统计——全部在运行时炸。恢复姿势三种：①**显式 `__hash__ = None`**：声明"这个类就是不可哈希的"，语义清晰；②**自定义 `__hash__`**：必须只用参与 `__eq__` 的不可变字段计算（用可变字段做哈希源是内容漂移事故，Q1297）；③**`frozen=True` dataclass**（或手写 `__hash__`）：eq=True 默认置 `__hash__ = None`，加 frozen 后自动生成基于全部字段的哈希——dataclass 的规则：eq=True, frozen=False → 不可哈希；frozen=True → 生成 `__hash__`。

取舍：a) 值语义对象（Money、Point、Config 快照）：eq + hash 一同实现，或 dataclass(frozen=True)；b) 有身份语义的实体（ORM 行对象、任务对象）：只按 id 相等是常态，若业务要求自定义 `__eq__`，必须同时决定哈希策略，不能留 None 了事——留 None 会把 set/dedupe 的调用点变成运行期地雷；c) 哈希源选择：用不可变字段（元组化），避免 list/dict 字段——要参与哈希就转 tuple/frozenset；d) 继承链陷阱：父类定义了 `__eq__` 和 `__hash__`，子类**新增可参与相等的字段**而忘了重定义 `__hash__` → 相等的两个子类实例哈希不同（契约崩），子类必须同步重算；e) `__hash__ = object.__hash__` 恢复默认恒等哈希：与按值 `__eq__` 配对违反契约，值相等的两个对象进 set 会变成两个成员——这是比 unhashable 更隐蔽的错。

实战：事故形态是"配置对比服务把两个等值 Config 对象放进 set 求差集，`__hash__ = object.__hash__` 恢复写法让 set 里出现两个'相等'成员，diff 结果翻倍——根治为 dataclass(frozen=True) 让 hash 自动生成，diff 语义随等值契约恢复"。下面实测失效机制与三种恢复姿势。

```python
# 自定义 __eq__ 后 __hash__ 的失效与恢复
class Point1:
    def __init__(self, x: int) -> None:
        self.x = x
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Point1) and self.x == other.x

class Point2(Point1):
    def __hash__(self) -> int:          # 恢复姿势一: 自定义哈希, 源只用参与 eq 的不可变字段
        return hash((self.__class__.__name__, self.x))

class Point3:
    __hash__ = None                     # 恢复姿势二: 显式声明不可哈希

print("[1] 定义 __eq__ 而未定义 __hash__: __hash__ 被置 None, 实例不可哈希")
a, b = Point1(1), Point1(1)
print("    Point1.__hash__ is None ->", Point1.__hash__ is None)
print("    a == b ->", a == b)
try:
    hash(a)
except TypeError as e:
    print("    hash(a) -> TypeError:", e)
try:
    {a, b}
except TypeError as e:
    print("    {a, b} -> TypeError:", e, "(set/dict键/lru_cache 全部连锁失效)")

print("[2] 恢复姿势一: 自定义 __hash__ (哈希源 = 参与 eq 的不可变字段)")
c, d = Point2(1), Point2(1)
print("    hash 相等:", hash(c) == hash(d), "| set 去重:", len({c, d}) == 1)

print("[3] 恢复姿势二: 显式 __hash__ = None 表达'该类不可哈希'的设计意图")
print("    Point3.__hash__ is None ->", Point3.__hash__ is None)

print("[4] 反模式: __hash__ = object.__hash__ 配按值 __eq__ -> 契约违反, set 里两个'相等'对象")
class Point4(Point1):
    __hash__ = object.__hash__          # 身份哈希 + 值相等: 危险组合
e1, e2 = Point4(1), Point4(1)
print("    e1 == e2 ->", e1 == e2, "| set 大小 ->", len({e1, e2}), "(应为 1 却得到 2, 静默错)")

print("[5] dataclass 规则: eq=True(默认) 置 hash=None; frozen=True 自动生成字段哈希")
from dataclasses import dataclass
@dataclass
class Money:
    amount: int
    currency: str
try:
    hash(Money(1, "CNY"))
except TypeError as e:
    print("    dataclass 默认 eq -> hash(Money) TypeError:", type(e).__name__)

@dataclass(frozen=True)
class FrozenMoney:
    amount: int
    currency: str
print("    frozen dataclass: hash(FrozenMoney(1,'CNY')) =", hash(FrozenMoney(1, "CNY")), "(可哈希)")
print("[6] 工程纪律: 动 __eq__ 必须同时决定 __hash__; 哈希源只用不可变字段; 子类加字段要同步重算 hash")
```

**追问一**：为什么语言要"自动置 None"而不是"自动生成一个按值的默认哈希"？—— 因为**没有正确的默认**：哈希源必须与相等语义一致，而解释器无法知道你的 `__eq__` 用了哪些字段、字段是否可变、是否含嵌套可变对象。若自动生成（比如 hash(tuple(self.__dict__.values()))），可变字段的值一改，对象就"逃出"原来的哈希桶——值相等的两个时刻哈希不同，dict/set 静默丢数据或重复（Q1297 的内容漂移事故）。置 None 的设计哲学：**让错误在最显式的位置爆发**——第一次进 set 就 TypeError，提示开发者做出明确的哈希决策，而不是埋一颗"大多数时候没事"的雷。这符合 Python"契约违反要可发现"的整体取向（同类：可变默认参数被字节码层面暴露出来让人看见，Q406）。

**追问二**：`hash()` 的随机化（PYTHONHASHSEED，Q5065）与自定义 `__hash__` 的交互要注意什么？—— 自定义 `__hash__` 若基于字符串字段，就继承了字符串哈希的进程级随机化：同一对象跨进程哈希值不同。三个注意点：①**自定义哈希不能落库/跨进程持久化**——哈希只在"本进程内的 dict/set 桶定位"有效，落库的应该是原始字段或业务摘要；②跨进程比对要用显式摘要（sha256.hexdigest()）而不是 hash()——两者语义完全不同，前者是稳定的内容指纹，后者是进程内定位符；③测试与并发场景：PYTHONHASHSEED 固定可复现桶碰撞路径（排 DoS 时有用），但不要因此把固定 seed 带到生产——那等于交出哈希碰撞 DoS 的钥匙。工程纪律一句话：hash() 只活在单进程内存里，出了进程边界就该换 hashlib。

## 背诵要点
- 类体定义 __eq__ 未定义 __hash__ → CPython 把 __hash__ 置 None，实例 unhashable，set/dict键/lru_cache 全连锁失效。
- 恢复三姿势：自定义 __hash__（源=参与 eq 的不可变字段）/ 显式 None 表达设计意图 / frozen dataclass 自动生成；object.__hash__ 配值相等是契约违反。
- 哈希只在本进程内存有效（受 PYTHONHASHSEED 随机化），跨进程比对用 hashlib 摘要。

## 复盘追问
- 自定义 __eq__ 后为什么不能默认生成哈希？（哈希源必须与相等语义一致，解释器无法推断；置 None 让错误显式爆发）
- set 里出现两个"相等"对象是什么事故形态？（__hash__ = object.__hash__ 配值 __eq__；哈希与相等失配，diff/dedupe 静默翻倍）
