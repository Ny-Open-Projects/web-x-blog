---
title: [Q5120] range 惰性算术序列原理
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5120 · range 惰性算术序列原理

> 难度:★★★★☆ | 标签:原理深挖, range, 序列协议

**问**:`range(10**12)` 为什么不占内存？`range(0, 10**12)[999999999999]` 为什么瞬间返回？range 支持哪些"序列"操作而不物化任何元素，它是靠什么实现的？

**答**:结论：range 是**惰性算术序列**——对象只存 `start/stop/step` 三个整数，任何操作都靠公式即时计算：`len = max(0, (stop-start+step-1)//step)`（O(1)）；索引 `i` 处的值 = `start + i*step`（O(1)，且对负索引做 `+len` 归一）；成员判断 `in` 优先走算术路径（判断 `v` 是否落在区间内且 `(v-start) % step == 0`），**只有当 step 为浮点语义不可能时才退化线性**——实际上 range 全程 O(1)，`in` 从不线性扫描。它实现了完整序列协议（`__len__/__getitem__/__contains__`），且是**不可变类型**（没有 `__setitem__`），所以支持切片（返回新 range，同样 O(1) 参数运算）、`==`（按"展开后的序列"比较而非三元组，`range(0,5,3)==range(0,4,3)` 为 True）、`hash`（与展开元组同哈希，能进 dict 键）。设计取舍：三个 int 的对象头 + PyLong，`range(10**12)` 稳定 ~48 字节；代价是**只能表达等差数列**，且元素是每次新建的 int 对象（迭代时不缓存，`r[5] is r[5]` 为 False，仅小整数缓存叠加出巧合）。

```python
import sys

r = range(0, 10**12, 7)
print("内存(字节):", sys.getsizeof(r), "（三个整数，与区间大小无关）")

# O(1) 索引与长度
print("len:", len(r))                          # (10^12 - 0 + 6)//7
print("r[142857142856] =", r[142_857_142_856])  # 0 + i*7 瞬时返回（末元素）
print("r[-1] =", r[-1])                        # 负索引归一后同样 O(1)

# O(1) 成员判断：算术判定，不扫描
print("10**6 in r:", 10**6 in r)               # 区间内且 (v-start)%7==0
print("10**6+1 in r:", (10**6 + 1) in r)       # 步长不整除 -> False，仍然瞬间

# 切片返回新 range，仍是惰性三元组
s = r[100:200:2]
print("切片:", s, "内存:", sys.getsizeof(s))

# 相等按展开序列语义，不按三元组：0,3 与 0,3 展开相同
print("range(0,5,3) == range(0,4,3):", range(0, 5, 3) == range(0, 4, 3))

# 可哈希、可进 dict 键（与展开元组同哈希）
d = {range(3): "three"}
print("dict 命中:", d[range(0, 3)])

# 不可变：没有写路径
try:
    r[0] = 1
except TypeError as e:
    print("禁写:", e)

# 元素对象每次新建（小整数缓存的巧合除外）
big = range(10**9, 10**9 + 3)
print("r[0] is r[0]:", big[0] is big[0])       # False：每个元素即时新建 int
print("small:", [i for i in range(3)][0] is [i for i in range(3)][0])  # True：小整数缓存
```

**追问一层**:为什么 `range.__contains__` 能保证 O(1)，而 `list.__contains__` 只能线性？两者的"包含"语义差在哪（值相等 vs 身份+相等）？
**追二层**:`enumerate`、`itertools.count` 与 range 的惰性有何本质不同？为什么 `range` 能反复迭代而一次性生成器不能，这对"重复遍历"的代码契约意味着什么？

**背诵要点**
- range 只存 start/stop/step 三整数：len、索引、in、切片全部公式化 O(1)，内存与区间大小无关。
- 相等/哈希按"展开序列"语义（`range(0,10,3)==range(0,9,3)`）；类型不可变、可哈希。
- 元素每次新建 int 对象，小整数下 `is` 命中只是缓存巧合，不是缓存设计。

**复盘追问**
- 把 `range` 换成 `list(range(...))` 后内存翻了几千倍，这类错误常藏在哪？提示：函数参数默认 `list(range(N))` 或为 len() 而物化。
- 业务需要"等差数列 + 反复随机访问"时，range 与 numpy arange 的分界在哪？提示：范围超 int64 或需要向量运算时才引入第三方。
