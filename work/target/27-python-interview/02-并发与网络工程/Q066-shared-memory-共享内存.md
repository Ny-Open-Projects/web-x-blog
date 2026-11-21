---
title: [Q066] shared_memory 共享内存
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q066 · shared_memory 共享内存

> 难度:★★★ | 标签:multiprocessing, shared_memory, 零拷贝

**问**:multiprocessing.shared_memory 如何使用?和 Queue 传数据相比优势在哪?

**答**:SharedMemory 在操作系统层面开一块命名共享内存,多个进程通过名字 attach,数据不经 pickle 序列化,适合传大块二进制数据(如图像帧)。通常配 NumPy 的 `np.ndarray(buffer=shm.buf)` 使用;用完必须 close 并由最后一方 unlink 释放——否则退出时 resource_tracker 会报 "leaked shared_memory objects" 警告。缺点是不自带同步,需配 Lock 使用。注意 memoryview 切片赋值要求左右字节数完全一致,短一截都会抛 ValueError。

```python
# file: code/02_并发与网络工程/q066_shared_memory.py
import multiprocessing
import multiprocessing.shared_memory as shm


def child(name: str, size: int) -> None:
    existing = shm.SharedMemory(name=name)
    try:
        # 读取父进程写入的数据
        data = bytes(existing.buf[:size])
        print("child 读到:", data.decode())
        existing.buf[:5] = b"CHILD"  # 回写(切片长度必须与数据等长)
    finally:
        existing.close()


if __name__ == "__main__":
    block = shm.SharedMemory(create=True, size=10)
    try:
        block.buf[:10] = b"PARENTDATA"  # 10 字节, 与切片等长
        p = multiprocessing.Process(target=child, args=(block.name, 10))
        p.start()
        p.join()
        print("parent 读回:", bytes(block.buf[:10]).decode())
    finally:
        # close + unlink 成对出现, 避免 resource_tracker 报泄漏
        block.close()
        block.unlink()  # 最后由创建者释放
```

**追问**:
- 为什么必须有人 unlink?——共享内存块由操作系统管理,进程全退出也不自动回收;约定「最后一个使用者 unlink」,否则泄漏到重启,resource_tracker 会报 leaked 警告。
- 怎么和 NumPy 零拷贝配合?——`np.ndarray(shape, dtype, buffer=shm.buf)` 直接映射;形状和 dtype 等元数据要另外传,通常走 Pipe/Queue 一起发。
- shared_memory 的同步怎么做?——本身不带锁,配 `multiprocessing.Lock` 保护写侧;只读共享(单写多读)可以不加。

---
