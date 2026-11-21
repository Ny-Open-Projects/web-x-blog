---
title: [Q008] __slots__ 的作用与代价
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q008 · __slots__ 的作用与代价

> 难度:★★☆ | 标签:内存, 类

**问**:`__slots__` 为什么能省内存?它牺牲了什么?

**答**:默认情况下实例属性存在每个对象各自的 `__dict__` 中,字典带来灵活性也带来内存开销。声明 `__slots__` 后,属性通过固定槽位描述符访问,不再创建 `__dict__`,百万级小对象可省大量内存。代价包括:不能动态添加新属性、默认不能与多重继承含 `__dict__` 的类组合、需要 WeakSet 支持时要额外声明 `__weakref__`。

```python
# file: code/01_语言核心与底层/q008_slots.py
import sys

class Plain:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Slotted:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == "__main__":
    p = Plain(1, 2)
    s = Slotted(1, 2)
    print(hasattr(p, "__dict__"))  # True
    print(hasattr(s, "__dict__"))  # False
    print(sys.getsizeof(p) > sys.getsizeof(s))  # True

    try:
        s.z = 3
    except AttributeError as e:
        print("cannot add:", e)
```

**追问**:1) dataclass 支持 slots 吗?——支持,`@dataclass(slots=True)`(Python 3.10+)会自动生成 `__slots__`。2) __slots__ 的继承陷阱?——父类没定义 `__slots__` 时子类实例仍有 `__dict__`,省内存效果归零;两个都定义非空 slots 的类做多继承会报 multiple bases have instance lay-out conflict。3) 省了多少内存怎么验证?——单对象 `sys.getsizeof` 差异 + 全进程 `tracemalloc` 对比;注意 getsizeof 对普通实例不含 `__dict__` 本身的大小,容易低估差距。
