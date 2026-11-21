---
title: [Q5002] 3.13/3.14 free-threading 下 dict/list 线程安全语义边界
date: 2026-11-18
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5002 · 3.13/3.14 free-threading 下 dict/list 线程安全语义边界

> 难度:★★★ | 标签:free-threading, 线程安全, PEP 703

**问**：free-threaded 构建（`python3.13t`）去掉 GIL 后，`dict` 和 `list` 的哪些操作还是线程安全的？「单个方法调用是原子的」这条 GIL 时代的老经验还剩多少？check-then-act 为什么必坏？怎么在压测里证明？

**答**：结论：free-threading 下 **单次容器方法的调用不会损坏内部结构**（dict/list 内部有细粒度锁，迭代器靠惰性删除保证不崩），但 **「原子性」不再延伸到组合操作**——GIL 时代「一个字节码序列不可被打断」的隐式保证被收紧为「单个操作内部一致」，任何跨操作的状态依赖都可能出竞争。具体边界：1) `d[k]=v`、`d[k]`、`L.append(x)` 本身安全（数据不坏），但两个线程 `d[k]=v1` 与 `d[k]=v2` 的最终值不确定；2) `d.get(k) → 判断 → d[k]=...` 这类 check-then-act 从「碰巧安全」变成「明确竞争」，`setdefault`/`update` 这种单调用完成的复合语义才是安全写法；3) **迭代期间被并发修改**：GIL 下会抛 RuntimeError（dict 大小变化），free-threading 下同样有并发修改保护，但语义是「尽力检测」，不能当同步原语用；4) 计数器场景 `d[k] += 1` 是读-改-写三步，必须加 `threading.Lock`。实战：事故复盘模式是「GIL 版跑半年没事，换 3.13t 后偶发重复写入/丢计数」——上线 free-threading 前要做两件事：用 `threading` 压测工具放大竞争窗口（多线程高频写同一 key），以及用 `TSAN` 式思维审计所有 check-then-act。

```python
# 基线:Python 3.13t(free-threaded 构建)演示竞争;GIL 版运行时同样可跑,
# 但竞争窗口小,可能看不到丢计数——这正是「GIL 隐式安全」的欺骗性。
import threading

N_THREADS, N_INC = 8, 50_000
counter: dict[str, int] = {}
lock = threading.Lock()

def unsafe_inc():
    for _ in range(N_INC):
        counter["k"] = counter.get("k", 0) + 1   # 读-改-写,三步非原子

def safe_inc():
    for _ in range(N_INC):
        with lock:
            counter["k"] = counter.get("k", 0) + 1

def run(fn):
    counter.clear()
    ts = [threading.Thread(target=fn) for _ in range(N_THREADS)]
    for t in ts: t.start()
    for t in ts: t.join()
    return counter.get("k", 0)

print("unsafe:", run(unsafe_inc), "/", N_THREADS * N_INC)  # 3.13t 下 < 期望
print("safe:  ", run(safe_inc),   "/", N_THREADS * N_INC)  # 恒等于期望
```

**追问**：
1) 单方法「数据不坏」的机制是什么？代价呢？——PEP 703 给容器内部加细粒度锁并用惰性删除（先标记后清理）缩短持锁时间；代价是无竞争路径也要付同步开销，单线程性能 3.13 早期损失约 40%，后续版本持续收窄。
2) `collections.Counter` / `queue.Queue` 在 free-threading 下安全吗？——`queue.Queue` 内部自带锁，安全；`Counter` 的 `+=` 一样是三步操作，不安全。判断标准不是类型，是「一次调用是否完成读改写」。
3) 怎么迁移存量代码？——先跑 `python -X thread_safety` 类压测（自由线程构建自带的竞争检测思路），把 check-then-act 改成单调用原子操作（setdefault、put-if-absent 风格）或显式锁；跨多步的不变量（转账）用锁或改队列串行化。
