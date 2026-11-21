---
title: [Q5060] __index__ 协议与切片下标的分派原理
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5060 · `__index__` 协议与切片下标的分派原理

> 难度:★★★ | 标签:__index__, __int__, operator.index, 切片, 协议

**问**：自定义类实现了 `__int__` 却当不了下标，`seq[MyInt()]` 报 TypeError。切片/下标背后到底调什么？`__index__` 和 `__int__` 为什么分成两个协议？哪些内建行为走 `__index__`？

**答**：CPython 对"当索引用"走的是 `operator.index()`，对应协议方法 `__index__`——切片、下标、`slice`、序列重复 `[0]*n`、`hex()`/`bin()`/`oct()`、`bytes(n)` 预分配等全部只认它。与 `__int__` 分开的原因是**语义纯度**：`__int__` 表达"可以有损转成 int"（`int(3.9)`=3，浮点也能转），而索引要求**无损的整数身份**——`seq[3.0]` 必须报错而不是悄悄当 3 用，否则 `seq[2.9]` 这类错误会被静默吞掉。所以 numpy 生态当年推动 PEP 357 加入 `__index__`：自定义"整数标记"类只要实现 `__index__` 就能穿透所有内建索引路径。规则口诀：**做索引用 `__index__`，做转换用 `__int__`；`__index__` 必须返回精确 int（返回别的会被 `operator.index` 再收窄或报 TypeError）**。反向关系：一个类实现 `__index__` 后 `int(obj)` 也走它（`__int__` 缺省 fallback 到 `__index__`），但反之不成立。3.12 之后这个分派稳定不变，只是错误信息更精确（提示你该实现 `__index__`）。

```python
# file: code/01_语言核心与底层/q5060_index_protocol.py
import operator

class OnlyInt:
    def __int__(self):
        return 2          # 只有转换, 没有整数身份

class GoodIndex:
    def __index__(self):
        return 2          # 完整整数身份

seq = list("abcdef")

# 1) 下标/切片只认 __index__
try:
    seq[OnlyInt()]
except TypeError as e:
    print("仅 __int__ 做下标 -> TypeError:", e)
print("__index__ 做下标:", seq[GoodIndex()])
print("operator.index 才是真实入口:", seq[operator.index(GoodIndex())])

# 2) 走 __index__ 的内建行为全景
print("列表重复:", [0] * GoodIndex())
print("hex/bin:", hex(GoodIndex()), bin(GoodIndex()))
print("bytes 预分配:", len(bytes(GoodIndex())), "字节")
print("切片对象:", seq[slice(GoodIndex())])

# 3) int() 对两者都可用: __int__ 缺省时 fallback __index__
print("int() 转换:", int(OnlyInt()), int(GoodIndex()))

# 4) 反例: __index__ 返回非 int 会被拒
class Bad:
    def __index__(self):
        return 2.0
try:
    operator.index(Bad())
except TypeError as e:
    print("__index__ 返回 float -> TypeError:", e)
```

**追问**：1) `float` 为什么不实现 `__index__`？——正是为了把 `seq[3.0]` 变成显式错误：float 有损转 int 的语义与"无损索引"冲突，PEP 357 刻意不收编；用户要自己 `int(3.0)` 表明意图。2) `slice` 对象里的参数走 `__index__` 吗？——走，`slice(a, b)` 在被应用到序列时对 start/stop/step 各调 `operator.index()`（`slice.__index__` 化发生在 `PySlice_AdjustIndices`），所以自定义索引类能无缝用于切片。3) `bool` 当索引的行为？——`bool` 是 `int` 子类，天然有 `__index__`，`seq[True]` 等价 `seq[1]`；这也是"bool 是 int"这条历史设计在索引层的直接后果。

## 背诵要点
- 索引/切片/重复/hex/bin/bytes 预分配全部走 `operator.index()` → `__index__`，不认 `__int__`。
- `__index__` = 无损整数身份（必须返回精确 int），`__int__` = 可有损转换；`int()` 在无 `__int__` 时 fallback 到 `__index__`。
- `seq[3.0]` 报 TypeError 是刻意设计（PEP 357）：防止 `seq[2.9]` 类错误被静默截断。

## 复盘追问
- 你们某个包装类（如强类型 ID）当过 dict key 或下标吗？缺 `__hash__`/`__index__` 时的表现是什么？（提示：dict key 走 `__hash__`/`__eq__` 与本题无关；下标场景会 TypeError，补 `__index__` 或实现 `__hash__` 要评审语义）
- `__index__` 返回超大整数（如 2**64）在切片上会怎样？（提示：切片会按 Python int 正常钳制到序列长度，不溢出；但转 C 层的地方（如 array 下标）受边界检查保护，仍不会越界访问）
