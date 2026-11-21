---
title: [Q423] __slots__ 与内存:每个实例省了什么?
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q423 · __slots__ 与内存:每个实例省了什么?

> 难度:★★★★☆ | 标签:__slots__, 内存, 性能

**问**:`__slots__` 到底砍掉了什么结构,能省多少内存?为什么说它顺便加快了属性访问?什么情况下 slots 类反而更费内存或者干脆报错?

**答**:普通对象的属性写在每实例的 `__dict__`(3.11 起是 key-sharing 的内联值数组,仍按实例存值),`__slots__` 让类型用固定槽位描述符替代 dict:每实例只存 N 个槽位指针,省掉整个 dict 开销(几十到上百字节/实例),百万级对象差距巨大。属性访问从 dict 哈希查找变为槽位偏移量直达,略快且 `__slots__` 类型不可动态加属性(拼写错误立刻 AttributeError,反而成优点)。坑:slots 与 `__dict__` 并存需要显式加 `'__dict__'` 进 slots(等于没省);多重继承两个带 slots 的基类(都有非空布局)会 TypeError;弱引用需显式 `'__weakref__'`;继承自无 slots 的基类时基类 dict 仍在,省内存效果打折;`dataclass(slots=True)`(3.10+)与 `__set_name__` 的组合在 3.12 前有已知交互 bug 的历史,升级注意。

```python
# file: code/01_语言核心与底层/q423_slots_memory.py
import sys
import tracemalloc

class Plain:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Slotted:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x, self.y = x, y

print("plain has dict:", Plain(1, 2).__dict__)
s = Slotted(1, 2)
print("slotted has dict:", hasattr(s, "__dict__"))          # False
try:
    s.z = 3
except AttributeError as e:
    print("blocked:", e)

tracemalloc.start()
plains = [Plain(i, i) for i in range(100_000)]
p_size = tracemalloc.get_traced_memory()[0]
del plains; tracemalloc.reset_peak()
slots_ = [Slotted(i, i) for i in range(100_000)]
s_size = tracemalloc.get_traced_memory()[0]
print("plain", round(p_size / 2**20, 1), "MB vs slotted", round(s_size / 2**20, 1), "MB")
print("per-instance delta:", sys.getsizeof(Plain(1, 2).__dict__), "bytes dict saved")
```

**追问**:1) 3.11 前后普通类实例内存为什么本来就有变化?——3.11 引入 key-sharing dict 内联布局(PEP 412 的延续),同形状实例共享键表,普通类已经省了一截,slots 的相对收益变小但稳定性(无哈希、预知偏移)仍胜出。2) slots 能与 dataclass 自动生成吗?——`@dataclass(slots=True)` 3.10+,注意它会把类重建出一个新类对象,装饰器叠加顺序有讲究。
