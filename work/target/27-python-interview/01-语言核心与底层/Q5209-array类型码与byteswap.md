---
title: "[Q5209] array.array 的 typecode 与 byteswap：跨端序二进制不要裸写"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5209 · array.array 的 typecode 与 byteswap：跨端序二进制不要裸写

难度：P6 ｜ 标签：array、typecode、byteswap、字节序、二进制协议

**问**：把一组 int 写进二进制文件，用 `array("l", data).tofile(f)`，本机读得好好的，换到另一台机器/另一种 CPU 后全变负数；另一个服务用 `array("i")` 当网络协议载荷，字段宽度在 Windows 上又对不上。`array` 的 typecode 到底保证什么？`byteswap()` 什么时候用？为什么二进制协议不该直接用它？

**答**：
结论：`array(typecode)` 的 `itemsize` 由 C 类型决定，**只有部分 typecode 是固定宽度**（`b/B` 1、`h/H` 2、`i/I` 通常 4、`q/Q` 8、`f` 4、`d` 8），`l/L` 是 C `long`，在 64 位 Unix 上常是 8 字节、Windows 上是 4 字节；字节序跟随本机（`sys.byteorder`）。`tobytes()` 直接吐本机内存布局，`frombytes()` 按本机解释；`byteswap()` 原地翻转每个元素的字节序，用来在读入外部数据后转换端序。

取舍：a) 本机临时缓存/数值计算用 `array` 很高效（连续内存、比 list 省）；b) 跨机/跨语言协议用 `struct` 或 `int.to_bytes(length, byteorder)` 固定宽度和端序，不要依赖 `array` 的 `l`/`L`；c) 必须在协议里用 array 时，选固定宽度 typecode（`i`/`q`/`d`），读写两端约定 `sys.byteorder` 或用 `byteswap()` 归一；d) `byteswap()` 是原地操作，会改变数组内容，别在共享缓冲区上随手调；e) 注意 `array('f')` 的 NaN/精度与 `struct` 的 `f` 行为一致，但跨平台浮点格式仍要确认 IEEE 754。

实战：事故形态是"行情快照用 `array('l')` 落盘，Linux 服务器写的 8 字节 long，Windows 分析机按 4 字节读，价格全错位；改成 `struct.pack('<q', ...)` 固定 8 字节小端后恢复"。下面演示 typecode 宽度、`tobytes`/`frombytes` 往返与 `byteswap` 的字节翻转。

```python
import sys
from array import array

a = array("i", [1, 0x01020304])
print("[1] typecode/itemsize:", a.typecode, a.itemsize,
      "byteorder:", sys.byteorder)
print("[2] tobytes:", a.tobytes().hex())

b = array("i")
b.frombytes(a.tobytes())
print("[3] frombytes 还原:", list(b))

a.byteswap()
print("[4] byteswap 后:", a.tobytes().hex(), list(a))

print("[5] 'l' 的宽度随平台变:", array("l").itemsize)
print("[6] 跨机协议用 struct/int.to_bytes 固定宽度，不用 array 裸写")
```

**追问一**：`array('i')` 一定是 4 字节吗？—— C 标准只保证 `int` 至少 2 字节，CPython 支持的平台上 `i` 基本都是 4 字节，但这不是语言级保证；`array` 文档给的是"minimum size"。要绝对固定宽度，用 `struct` 的 `i`/`q`（标准大小模式）或 `int.to_bytes`，并在代码里断言 `itemsize`。

**追问二**：`memoryview(array)` 能零拷贝读写吗？—— 可以，`memoryview(a)` 暴露连续缓冲区，支持切片、`cast()` 到其他格式；但 `cast` 不改变底层字节，只改解释方式，端序问题依旧存在。用 memoryview 做协议解析时要显式处理端序，且注意导出缓冲区期间不能 resize 原数组（会 `BufferError`）。

## 背诵要点
- `array` 的 `itemsize` 随 C 类型/平台变，`l/L` 在 Unix/Windows 宽度不同；字节序跟随本机。
- `tobytes`/`frombytes` 是本机布局；`byteswap()` 原地翻端序。
- 跨机协议用 `struct`/`int.to_bytes` 固定宽度和端序；array 只适合本机数值缓存。

## 复盘追问
- Linux 写的文件在 Windows 读出错位，为什么？（`long` 宽度 + 端序）
- `byteswap()` 能跨平台解决协议问题吗？（只能翻端序，宽度仍不保证）
