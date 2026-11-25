---
title: "[Q5096] dict.fromkeys 共享可变值事故复盘"
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5096 · dict.fromkeys 共享可变值事故复盘

难度：P6 | 标签：事故复盘 | dict.fromkeys | 可变默认

**问**：一个"按租户聚合指标"的初始化代码 `dict.fromkeys(tenants, [])`，上线后所有租户的数据混到了一起。根因是什么？还有哪些写法踩同一个坑？正确的几种替代分别适用什么场景？

**答**：
结论：`dict.fromkeys(keys, value)` 的 value **只求值一次**，所有 key 共享同一个对象引用。对不可变值（int/str/tuple）无害，对 list/dict/set 这类可变值就是"一个默认桶被全体共享"，任何一处 append 都改了"所有人"的桶。这与可变默认参数是同一族问题：共享的可变默认值。
取舍与替代：① 键值初始化用推导式 `{k: [] for k in keys}`，每次新建列表，语义最直白；② 已有 key 集合、想避免重复构建用 `dict.setdefault(k, [])` 或 `collections.defaultdict(list)`，适合增量聚合；③ 值是不可变时 fromkeys 仍是好写法（`fromkeys(keys, 0)`）。
实战：把"fromkeys + 可变值"写进 lint/评审红线；事故排查特征是"只有第一个被写入的租户有数据"或"所有 key 数据相同"——先查初始化是否共享引用。

```python
from collections import defaultdict

tenants = ["a", "b", "c"]

# 事故复现：所有租户共享同一个 list 对象
bad = dict.fromkeys(tenants, [])
print("共享同一对象:", all(v is bad["a"] for v in bad.values()))
bad["a"].append(1)
print("改 a 却全变了:", bad)  # {'a': [1], 'b': [1], 'c': [1]}

# 姿势1：推导式逐 key 新建（正确且直白）
ok1 = {k: [] for k in tenants}
ok1["a"].append(1)
print("推导式:", ok1)

# 姿势2：defaultdict 增量聚合
ok2 = defaultdict(list)
ok2["a"].append(1); ok2["a"].append(2); ok2["b"].append(3)
print("defaultdict:", dict(ok2))

# 姿势3：setdefault 适合 key 动态到达的场景
ok3: dict = {}
for t, v in [("a", 10), ("b", 20), ("a", 30)]:
    ok3.setdefault(t, []).append(v)
print("setdefault:", ok3)

# fromkeys 的正确用法：不可变值
zeros = dict.fromkeys(tenants, 0)
zeros["a"] += 1
print("不可变值安全:", zeros)

# 坑的变体：列表推导里用 [ [] ] * n 同样共享
rows = [[]] * 3
rows[0].append("x")
print("[[]]*n 共享:", rows)
rows_ok = [[] for _ in range(3)]
rows_ok[0].append("x")
print("推导式版:", rows_ok)

# 可运行断言：共享性检测
def is_shared(d):
    vals = list(d.values())
    return len(set(map(id, vals))) != len(vals)
assert is_shared(bad) and not is_shared(ok1)
print("断言通过：fromkeys 共享、推导式独立")
```

**追问 1**：为什么 Python 不让 fromkeys 对每个 key 重新求值？
- 追问 2 层：fromkeys 是 dict 的 C 级类方法，签名是 (iterable, value=None)，value 是已求值对象；要惰性求值得用工厂函数，标准库没提供该形式。
- 追问 3 层：同理 `dict.fromkeys(keys, bytearray())`、`threading.Event()` 之类都要逐 key 构造，fromkeys 全部踩坑。

**追问 2**：defaultdict 与 setdefault 的取舍？
- 追问 2 层：defaultdict 访问也会创建 key（副作用是查询性访问会膨胀 dict），setdefault 只在显式写入时创建；只读判断用 `d.get(k)` 不触发创建。
- 追问 3 层：defaultdict 的工厂在 pickle 时会丢（旧版本），跨进程传递聚合结果要转回普通 dict。

## 背诵要点
1. fromkeys 的 value 只求值一次、全 key 共享引用，可变值必然互相污染。
2. 逐 key 构造用 `{k: [] for k in keys}`；增量聚合用 defaultdict/setdefault；不可变值才用 fromkeys。
3. `[[]] * n` 是同一坑的乘法变体，共享性可用 id 集合检测。

## 复盘追问
1. 事故为什么没被单测抓住？——单测常只写单租户断言，共享引用要靠"多 key 相互独立"的断言才暴露。
2. 如果值是可变但需要冻结快照（如共享配置 list）怎么办？——转 tuple 或 `MappingProxyType`，把共享从事故变成特性。
