---
title: [Q5054] array 与 list 存大规模数值的内存容量账
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5054 · array 与 list 存大规模数值的内存容量账

> 难度:★★★ | 标签:array, list, 内存, 容量规划, sys.getsizeof

**问**：要在内存里放 1000 万个采样点（int64），产品经理拍脑袋说"1000 万个数字才几十 MB 吧"。用 list 和用 `array` 各要多少内存？为什么差这么多？什么时候该换 bytes/array，什么时候必须留 list？

**答**：list 存的是**指针数组**：每个元素 8 字节指向一个独立 int 对象，而一个小 int 对象自身约 28 字节（头部 16 + 值），且除 -5~256 的缓存整数外每个都是独立分配。所以 1000 万 int ≈ 1000 万×(8+28) ≈ 360MB——"几十 MB"差了一个数量级。`array('l')` 是 C 数组语义：连续定长存储，每元素固定 8 字节，1000 万 ≈ 80MB，缩小 4.5 倍；范围更小的值还能更省（`'b'` 1 字节、`'h'` 2 字节、`'f'` 4 字节）。纯同类型数值/布尔序列（传感器采样、向量、bitmap）用 array/bytes；需要混类型、含 None、频繁增删中间元素或被 GC 单独管理的业务对象，才用 list。中间档还有 bytes/bytearray（1 字节粒度）。第三方的 numpy 不在本题范围，但面试时可以点一句：向量化计算场景 array 只是省内存，numpy 才省计算。

```python
# file: code/01_语言核心与底层/q5054_array_vs_list.py
import sys
from array import array

N = 1_000_000

# 1) list: 指针数组 + 每个 int 独立对象
lst = list(range(N))
per_int = sys.getsizeof(999)          # 小整数对象约 28B
est = sys.getsizeof(lst) + per_int * N
print(f"list {N} 个 int ≈ {est/1024/1024:.0f}MB  (指针8B + int对象{per_int}B)")
print("list 自身结构仅:", sys.getsizeof(lst), "B, 大头在元素对象")

# 2) array('l'): C 数组, 每元素定长 8B
arr = array("l", range(N))
print(f"array('l') {N} 个 int64 = {sys.getsizeof(arr)/1024/1024:.1f}MB")

# 3) 更窄类型更省
small = array("b", bytes(N))          # 每元素 1B
print(f"array('b') {N} 个字节值 = {sys.getsizeof(small)/1024/1024:.1f}MB")

# 4) 容量账口诀
print("口径: list = 8B 指针 + 元素对象头; array = typecode 定长; bytes = 1B")
print("选型: 纯数值大序列 array/bytes; 混合类型/含 None/要放业务对象 list")
```

**追问**：1) `array` 支持 `int` 之外混一个 None 吗？——不支持，类型码定死后只能放对应类型，混入任何其他类型直接 TypeError；这是"省内存"的代价，也是天然 schema 约束。2) `memoryview` 在这套账里扮演什么角色？——零拷贝视图，`memoryview(arr)[k]` 不复制就能按类型读定长元素，跨 buffer 切片也不产生新分配，配合 array 可做无拷贝的分段处理。3) Python 3.12 的 `PyLong` 有什么变化影响这笔账？——3.12 起小整数内部表示优化（`_PyLong` 布局更紧凑），但"每值一个对象 + 指针数组"的 list 结构性开销不变，账的量级结论不变。

## 背诵要点
- list 存 1000 万 int ≈ 360MB（8B 指针 × N + 每个独立 int 对象约 28B）；array('l') ≈ 80MB。
- array 类型码：b=1B、h=2B、f=4B、l/q=8B；bytes 是 1 字节粒度的极致紧凑。
- 纯同类型数值用 array/bytes；混合类型/含 None/业务对象才用 list。

## 复盘追问
- 你们哪个接口/任务在内存里放了"指针数组陷阱"式的数据？怎么发现的？（提示：tracemalloc 按分配点聚合，list 指针结构+int 对象两个分配源相加）
- 采样数据从 list 换成 array 后，计算路径要不要重写？（提示：array 支持 buffer 协议，循环可原样跑；sum/max 等走迭代略慢于 list 缓存路径，向量化交给 numpy）
