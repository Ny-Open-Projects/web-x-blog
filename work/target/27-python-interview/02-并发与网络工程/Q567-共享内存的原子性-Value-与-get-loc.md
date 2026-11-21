---
title: [Q567] 共享内存的原子性:Value 与 get_lock
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q567 · 共享内存的原子性:Value 与 get_lock

> 难度:★★★☆ | 标签:multiprocessing, shared_memory, 原子性

**问**:multiprocessing.Value 是线程安全的吗?为什么锁了以后计数还是可能不对?

**答**:`Value` 单次读写由内部的 sysV/共享内存保证,但 `x.value += 1` 是"读-改-写"三步,进程之间随时可能被打断,所以必须用 `get_lock()` 把复合操作包成临界区。默认 `Value(typecode, lock=True)` 自带一把锁;若显式 `lock=False` 拿到的是纯共享内存,速度更快但要自己配锁。真正跨进程的"原子指令"在 Python 层没有暴露接口,工程上要么 Value+锁,要么改用单进程聚合后一次性写入。

```python
# file: code/02_并发与网络工程/q567_shared_atomic.py
import multiprocessing as mp

N = 20000  # 演示规模: 跨进程锁粒度重, 规模控制在 25s 内跑完


def unlocked_worker(val) -> None:
    for _ in range(N):
        v = val.value      # 读
        val.value = v + 1  # 写: 读-改-写之间可能被其他进程插入


def locked_worker(val) -> None:
    for _ in range(N):
        with val.get_lock():   # Value 自带的进程锁
            val.value += 1


def run(target, lock: bool) -> int:
    val = mp.Value("i", 0, lock=lock)
    ps = [mp.Process(target=target, args=(val,)) for _ in range(4)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    return val.value


if __name__ == "__main__":
    lost = run(unlocked_worker, lock=False)
    print(f"无锁结果: {lost} / 期望 {4 * N} (丢失 {4 * N - lost})")
    ok = run(locked_worker, lock=True)
    print(f"加锁结果: {ok} / 期望 {4 * N}")
    assert ok == 4 * N
```

**追问**:1) threading.Lock 能保护跨进程的 Value 吗?——不能,线程锁只在进程内有效,跨进程必须用 multiprocessing 提供的锁(基于信号量/文件锁实现)。2) Value/Array 的原子边界?——Value(typecode, lock=True) 的 get/set 是原子(带信号量);但「读改写」(v.value += 1)不是原子,要 with v.get_lock();Array 类似,整体修改靠锁。3) 与 Manager 的取舍?——Value/Array 共享内存快(零 IPC);Manager 代理慢(Q573)但支持任意对象;大块数据上 shared_memory(3.8+)。4) 生产陷阱?——裸 += 丢更新(经典);线程锁跨进程用;共享内存对象携带不可 pickle 状态;忘记 acquire 超时导致死等。

---
