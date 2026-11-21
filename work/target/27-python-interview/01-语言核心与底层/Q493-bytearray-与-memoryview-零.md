---
title: [Q493] bytearray 与 memoryview:零拷贝处理
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q493 · bytearray 与 memoryview:零拷贝处理

> 难度:★★★★ | 标签:内存, 二进制

**问**:处理大块二进制数据时,bytes、bytearray、memoryview 三者怎么配合?

**答**:bytes 不可变,适合存与哈希;bytearray 可变,适合就地拼装(避免 bytes 反复拼接的拷贝);memoryview 是零拷贝窗口——对同一块缓冲创建多个视图、切片不复制、struct.unpack_from 直接按偏移读,协议解析和环形缓冲区靠它把拷贝次数压到最低。切片视图写穿到底层(mv[0]=9 会改 bytearray),所以释放前底层不能 resize。性能敏感代码的检查点:是否在热循环里 bytes += 、是否有大切片仅为了读几个字节——都可以换成视图与 unpack_from。

```python
# file: code/01_语言核心与底层/q493_memoryview_zero_copy.py
import struct

if __name__ == "__main__":
    payload = bytearray(b"\x00" * 8)
    view = memoryview(payload)
    view[0:4] = b"\x01\x02\x03\x04"       # 写穿到底层缓冲
    print("payload:", payload.hex())

    struct.pack_into(">I", payload, 4, 1024)
    print("parsed:", struct.unpack_from(">I", payload, 4))

    mv = view[0:4]                        # 切片不拷贝,共享同一块内存
    mv[0] = 9
    print("after view write, payload[0]:", payload[0])

    ro = bytes(payload)                   # 真正的拷贝在这里才发生
    print("snapshot:", ro.hex(), len(ro))
    mv.release()                          # 先释放子视图
    view.release()                        # 再释放父视图,底层才可 resize
```

**追问**:1) memoryview 持有期间对 bytearray resize 会怎样?——抛 BufferError:现有导出未释放,底层缓冲被视图锁定;必须先 release 所有视图,这也是「忘 release」导致 BufferError 的根因。2) memoryview 为什么零拷贝?——通过 buffer 协议 export 直接引用底层内存,切片也是视图不复制;代价是生命周期绑定——视图活着底层就不能动。3) buffer 协议的底层结构?——exporter(实现 __buffer__)向 view 提供 Py_buffer(指针、format、shape);bytes/bytearray/array/numpy 都是 exporter,struct.unpack_from 可直接读视图。4) 生产陷阱?——视图未 release 导致 bytearray 缩容失败、BufferError 隐藏真实泄漏;把 view 传给 C 扩展后底层对象先死(必须保引用);只读 bytes 上误用 cast 写入。
