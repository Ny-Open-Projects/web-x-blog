---
title: [Q5131] __slots__ 类的 pickle 与弱引用失效事故
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5131 · __slots__ 类的 pickle 与弱引用失效事故

难度：P6 | 标签：__slots__、pickle、weakref、事故复盘

**问**：团队为省内存给热点数据类加了 `__slots__`，上线后出现两类诡异故障：`pickle.dumps` 对某些对象直接报错，另一处代码拿到的 `weakref.ref` 返回 None 导致缓存清理逻辑失效。为什么加了 `__slots__` 会同时影响 pickle 和 weakref？如何修复？

**答**：

**结论**：`__slots__` 会阻止 Python 为实例创建 `__dict__`，同时默认也不会创建 `__weakref__` 槽位。影响面有三处：(1) 默认 pickle 协议走 `__dict__`/`__reduce_ex__` 时拿不到实例状态，抛 `AttributeError` 或静默丢状态；(2) `weakref.ref(obj)` 抛 `TypeError: cannot create weak reference to ... object`；(3) 任何依赖 `vars(obj)`、`obj.__dict__` 的调试/序列化/ORM 代码全部失效。

**取舍**：修复方式按需求分层——需要弱引用就加 `"__weakref__"` 槽；需要 pickle 就实现 `__getstate__`/`__setstate__` 或用 `copyreg` 注册；两者都要就在 slots 里显式声明。省内存的收益仍在（实例从"对象头+__dict__"变成紧凑槽位数组），但不能把 slots 当纯优化无脑加。

**实战**：事故的根因几乎都是"类定义者"和"使用者"不是同一批人：加 slots 的人只跑了单元测试，而 pickle 落盘和弱引用缓存在集成链路里。上线前用 `hasattr(cls, '__getstate__')` 与 `weakref.ref(cls())` 做契约测试；dataclass(slots=True)（3.10+）同样有这两个坑，且 3.11 前 dataclass slots=True 会重新创建类导致 `super()` 语义变化。

```python
import pickle, weakref

class Bad:
    __slots__ = ("x",)
    def __init__(self, x): self.x = x

class Fixed:
    __slots__ = ("x", "__weakref__")
    def __init__(self, x): self.x = x
    def __getstate__(self):
        return (self.x,)                       # 槽位类需显式给出状态
    def __setstate__(self, state):
        self.x = state[0]

# 1) pickle 对比
try:
    pickle.dumps(Bad(1), protocol=5)
except Exception as e:
    print("Bad pickle ->", type(e).__name__, e)

b = pickle.loads(pickle.dumps(Fixed(42), protocol=5))
print("Fixed pickle ->", b.x)

# 2) weakref 对比
try:
    weakref.ref(Bad(1))
except TypeError as e:
    print("Bad weakref ->", e)

obj = Fixed(7)          # 必须持有强引用，临时对象会被立即回收
r = weakref.ref(obj)
print("Fixed weakref ->", r().x)
```

**追问 1**：为什么 slots 类在 `copyreg` 或 `__reduce__` 缺席时，protocol 2+ 有时又能 pickle 成功？
答：protocol 2 引入的 `__reduce_ex__` 会尝试走 `copyreg.__newobj__` + `__getstate__` 路径；slots 类没有 `__getstate__` 时 Python 3.11+ 内置了一个基于 slots 的默认 `__getstate__`（返回 `(None, slots_dict)`），所以新版本能 pickle 但旧版本（3.10 及更早）会失败——这是跨版本兼容事故的高发点。

**追问 2**：slots 继承链上父类没有 slots 会发生什么？
答：父类没有 `__slots__` 时父实例仍带 `__dict__`，子类 slots 白加，内存不降反升（多了槽位+dict 两份）；多继承两个都有非空 slots 的类会抛 `TypeError: multiple bases have instance lay-out conflict`。

**追问 3**：为什么 slots 类不能给实例动态加属性？
答：属性访问走描述符协议，slots 成员在类上表现为 `member_descriptor`，类里没有对应的 `__dict__` 存放新名字，赋值触发 `AttributeError`——除非 slots 里显式放进 `__dict__`。

## 背诵要点

- `__slots__` 默认不生成 `__dict__` 和 `__weakref__`，pickle 和 weakref 同时失效，要显式加 `"__weakref__"` 槽和 `__getstate__`。
- Python 3.11+ 给 slots 类补了默认基于 slots 的 `__getstate__`，pickle 行为跨版本不一致是兼容事故高发点。
- 父类无 slots、slots 多继承 layout 冲突、dataclass slots=True 重建类，是三个次生坑。

## 复盘追问

- 如果线上已落盘大量旧版本 pickle 数据，slots 升级后如何做数据迁移与灰度？(提示：copyreg 映射旧类路径 + 双读)
- slots 省下的内存如何量化验证？实例数多大时收益才显著？(提示：sys.getsizeof + 逐字段对比)
