---
title: [Q1799] bytes/bytearray/memoryview 三态转换与只读边界
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1799 · bytes/bytearray/memoryview 三态转换与只读边界

> 难度:★★★☆☆ | 标签:缓冲区协议, 二进制, 内存

**问**:bytes、bytearray、memoryview 之间的转换哪些拷贝、哪些不拷贝?写与 resize 的边界在哪?

**答**:转换矩阵记三行:① bytes -> bytearray 拷贝、-> memoryview 零拷贝视图;② bytearray -> memoryview 零拷贝、-> bytes 拷贝出只读快照;③ 视图回 bytes/bytearray 都拷贝,视图切片不拷贝(Q493 讲零拷贝用法,本题给转换与读写边界)。写边界:只有底层可变且视图可写才能写——bytes 的视图只读,赋值抛 TypeError;对 bytearray 的视图写会写穿到底层。resize 边界最常踩:存在未释放视图时 bytearray 禁止扩缩(抛 BufferError),必须先 mv.release() 或让视图离开作用域。进阶用 memoryview.cast 换格式重解释(比如按 h 把字节流当 short 数组读),全程零拷贝,这是 struct.unpack_from 之外的第二条协议解析路径。

```python
# file: code/01_语言核心与底层/q1799_buffer_trio.py
"""bytes/bytearray/memoryview 三态转换矩阵与只读边界。"""
import struct


def conversion_matrix():
    b = bytes([72, 105])       # bytes:不可变
    ba = bytearray(b)          # bytes -> bytearray:拷贝
    mv = memoryview(ba)        # bytearray -> memoryview:零拷贝视图
    snap = bytes(mv)           # 视图 -> bytes:拷贝出快照
    ba2 = bytearray(mv)        # 视图 -> bytearray:拷贝
    return b, ba, snap, bytes(ba2), snap == bytes(ba)


def view_write_through():
    ba = bytearray(b"hello")
    mv = memoryview(ba)
    mv[0] = ord("H")           # 写视图,写穿到底层
    return ba


def readonly_boundary():
    mv = memoryview(b"immutable")   # bytes 的视图只读
    try:
        mv[0] = 88
    except TypeError as e:
        return "只读视图被拦截: " + str(e)[:30]
    return "写成功了?不可能"


def resize_block():
    ba = bytearray(b"12345")
    mv = memoryview(ba)
    result = None
    try:
        ba.extend(b"678")      # 有活动视图时禁止 resize
    except BufferError as e:
        result = "有视图时禁止 resize: " + str(e)[:22]
    finally:
        mv.release()           # 释放视图后恢复可变
        ba.extend(b"678")
    return result, ba


def struct_view():
    raw = bytearray(struct.pack("<2h", 7, -9))
    shorts = memoryview(raw).cast("h")   # 视图重解释,不拷贝
    return list(shorts), bytes(raw)


if __name__ == "__main__":
    b, ba, snap, snap2, eq = conversion_matrix()
    print("转换矩阵:", b, ba, snap, snap2, "快照相等:", eq)
    print("视图写穿:", view_write_through())
    print(readonly_boundary())
    print(resize_block())
    print("cast 重解释:", struct_view())
```

**追问**:1) 为什么视图活着的 bytearray 连 extend 都不行?——缓冲区协议把内存地址交给了外部持有者,移动或扩容会让对方拿到悬空指针,CPython 选择直接禁止导出中的 resize。2) 三态的职责分工?——bytes 只读快照、bytearray 可变缓冲、memoryview 零拷贝视图;bytes(ba) 拷贝、mv(ba) 引用;选型按「是否需要修改」与「是否需要零拷贝」。3) 视图的进一步操作?——cast() 改解释格式(int/float 视图)、release() 释放导出、与 struct/numpy 互操作;持有期间所有 resize 被 BufferError 挡住(Q493)。4) 生产陷阱?——大缓冲误转 bytes 双倍内存;忘 release 导致 BufferError 隐藏真实泄漏;循环里反复拼接 bytes 应换 bytearray。
