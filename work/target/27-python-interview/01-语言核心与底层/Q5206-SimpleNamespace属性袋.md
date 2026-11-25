---
title: "[Q5206] types.SimpleNamespace：属性袋的相等、哈希与内存代价"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5206 · types.SimpleNamespace：属性袋的相等、哈希与内存代价

难度：P6 ｜ 标签：SimpleNamespace、属性容器、`__dict__`、可哈希、配置对象

**问**：测试里用 `SimpleNamespace(x=1)` 造配置对象，写进 `set` 时抛 `unhashable`；把两个内容相同的 namespace 当 dict 的 key，也失败。它和 dataclass、dict 到底差在哪？为什么它可比较却不可哈希？动态属性、`vars()`、pickle 的行为又是什么？

**答**：
结论：`SimpleNamespace` 是一个极薄的属性容器：属性存在实例 `__dict__` 里，`repr` 友好，`__eq__` 按 `__dict__` 比较，因此内容相同即相等；但它定义了 `__eq__` 却没定义 `__hash__`，所以**不可哈希**，不能当 set 元素/dict key。它没有 slots，每个实例都带一个 dict，内存比 dataclass(slots=True) 大；优点是零样板、可动态增删属性、pickle 直接可用。

取舍：a) 测试桩、临时配置、函数返回的"带字段的小对象"用 SimpleNamespace 最省事；b) 需要哈希/不可变/类型约束，用 `@dataclass(frozen=True)` 或 `NamedTuple`；c) 需要序列化契约/校验，用 Pydantic/dataclass，不要用裸 namespace 当 API 模型；d) 需要当 dict 用，直接用 dict，别为了点号访问包一层；e) 大量实例（百万级）别用 SimpleNamespace，`__dict__` 的内存开销会放大。

实战：事故形态是"缓存键用 SimpleNamespace 包装查询参数，运行到 `cache[key]` 时抛 `TypeError: unhashable type`，被上层 `except Exception` 吞掉，缓存永远 miss，DB QPS 翻倍"。下面演示相等、不可哈希、动态增删与 pickle 往返。

```python
import pickle
import sys
from types import SimpleNamespace

a = SimpleNamespace(x=1, y=2)
b = SimpleNamespace(x=1, y=2)

print("[1] repr:", a)
print("[2] 按属性字典相等:", a == b)
print("[3] vars 就是 __dict__:", vars(a) is a.__dict__)

try:
    hash(a)
except TypeError as e:
    print("[4] 可相等但不可哈希:", e)

a.z = 3
del a.x
print("[5] 动态增删:", vars(a))

c = pickle.loads(pickle.dumps(a))
print("[6] pickle 往返:", c, c == a)
print("[7] 每个实例都带 __dict__，比 slots 类重:", sys.getsizeof(a) > 0)
```

**追问一**：为什么 `__eq__` 会让对象不可哈希？—— Python 的数据模型规定：类如果定义了 `__eq__` 而没有显式定义 `__hash__`，`__hash__` 会被设为 `None`，因为"相等"通常意味着"可变"，可变对象做哈希键会破坏 dict/set 的不变式。要可哈希，就实现 `__hash__` 并保证参与相等的字段不可变（frozen dataclass 就是这么做的）。

**追问二**：`SimpleNamespace` 和 `argparse.Namespace` 有什么区别？—— 两者行为几乎一样，`argparse.Namespace` 是给命令行解析用的同型实现；`SimpleNamespace` 在 `types` 里更通用。它们都不是"配置框架"：没有类型校验、没有默认值合并、没有环境变量覆盖，生产配置还是用 dataclass/Pydantic + 显式加载逻辑。

## 背诵要点
- `SimpleNamespace` 属性存 `__dict__`，按 `__dict__` 相等；定义了 `__eq__` 所以不可哈希。
- 零样板、可动态增删、可 pickle；每实例带 dict，内存比 slots 类重。
- 要哈希/不可变用 frozen dataclass/NamedTuple；要契约用 Pydantic。

## 复盘追问
- `SimpleNamespace` 为什么不能做 dict key？（`__eq__` 导致 `__hash__ = None`）
- 百万级小对象为什么不该用它？（每实例一个 `__dict__`）
