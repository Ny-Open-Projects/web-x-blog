---
title: [Q5577] free-threading 下 threading 原语的演进
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5577 · free-threading 下 threading 原语的演进

> 难度:★★★★ | 标签:版本演进, free-threading, 3.13

**问**：3.13 自由线程构建（PEP 703，`--disable-gil`）下，`threading.Lock/RLock/Condition/Queue/Barrier` 的语义变了吗？为什么 free-threading 下"用 GIL 兜底的锁省略代码"全成了事故？deferred reference counting 与 `mimalloc` 在里面扮演什么角色？迁移已有多线程代码的检查清单是什么？

**答**：结论：free-threading 构建里 GIL 没了，**threading 原语的 API 语义不变（照常可用且行为一致），但"Python 层面的操作是原子的"这条隐含保证消失了**——CPython 里 `dict[key]=v`、`list.append` 单字节码看似原子（GIL 兜底），free-threading 下可被并发交错，所有依赖该隐含保证的代码都要补显式锁（对应 01 类 Q5002 的 dict/list 安全边界）。原语逐个看：a) `Lock/RLock` 本来就是真锁（底层 pthread mutex/semaphore），free-threading 下行为一致、且从"性能税"变成"必需品"；b) `queue.Queue` 内部自己持锁，仍是线程安全首选；c) `threading.Event/Condition` 语义不变；d) **不再存在"GIL 竞争"概念，但出现新瓶颈**：原语基于系统 futex/mutex，高争用下上下文切换成本真实化，之前被 GIL"串行化掩盖"的争用会显形。实现侧关键演进：**deferred reference counting + biased reference counting**——多线程下每对象 refcount 不再是单一整数（任何线程随手 refcount++ 都会 cache line 弹跳），3.13 用每线程本地引用计数 + 延迟释放，搭配 mimalloc 的线程本地分配器把 malloc 争用也消掉；副作用是对象回收有延迟（`gc` 收尾），观测 refcount 的调试技巧（`sys.getrefcount`）在 free-threading 下数值波动更大。迁移清单：a) grep 所有"无锁共享可变状态"（模块级 dict/list/计数器、双重检查锁的单例）；b) `functools.lru_cache` 等隐式共享结构确认版本；c) benchmark 用 `PYTHON_GIL=0`/`-X gil=0` 与 per-interpreter GIL（Q5501）分别跑，警惕解释器构建差异。

```python
# file: code/02_并发与网络工程/q5577_freethreading.py
import sys, threading, time

def gil_enabled():
    # 3.13+: sys._is_gil_enabled(); 3.12 无此 API, 用 flags 兜底
    if hasattr(sys, "_is_gil_enabled"):
        return sys._is_gil_enabled()
    return not bool(getattr(sys.flags, "gil", 0) or 0) if False else True  # 3.12 视为默认 GIL

print("解释器:", sys.version.split()[0], "| GIL 当前启用:", gil_enabled())
FREE = hasattr(sys, "_is_gil_enabled") and not sys._is_gil_enabled()

# 1) 危险模式: "GIL 兜底"的读改写, free-threading 下必须显式锁
counter = {"n": 0}
lock = threading.Lock()

def bump_plain():
    for _ in range(200_000):
        counter["n"] += 1          # 读改写非原子! GIL 下碰巧多数安全, ft 下必错

def bump_safe():
    for _ in range(200_000):
        with lock:
            counter["n"] += 1

ts = [threading.Thread(target=bump_safe) for _ in range(4)]
[t.start() for t in ts]; [t.join() for t in ts]
print("显式锁结果:", counter["n"], "(准确)")

if not FREE:
    counter["n"] = 0
    ts = [threading.Thread(target=bump_plain) for _ in range(4)]
    [t.start() for t in ts]; [t.join() for t in ts]
    print("无锁模式在 GIL 构建下: ", counter["n"], "(碰运气, ft 构建下会丢计数)")

# 2) queue.Queue 自带锁: 两代构建都安全
from queue import Queue
q = Queue(); done = []
def worker():
    while True:
        it = q.get()
        if it is None: break
        done.append(it); q.task_done()
t = threading.Thread(target=worker, daemon=True); t.start()
for i in range(1000): q.put(i)
q.join(); q.put(None)
print("Queue 生产消费:", len(done))

# 3) 迁移守则输出
print("迁移清单: 共享可变状态全量加锁 / 双检锁单例复查 / lru_cache 版本行为 / 基准跑 gil=0 与 per-interpreter")
```

**追问**：1) free-threading 下 `dict.get` 真的不原子吗？——CPython 的 free-threading 构建对内置容器做了**细粒度内部锁**（dict/list 有 per-object locking），单个操作本身仍安全；危险的是**复合操作**（get 后 set、遍历中修改），内部锁不覆盖跨调用的逻辑原子性，还是要应用层锁——所以更准确的说法是"单操作安全、序列不安全"。2) 与 per-interpreter GIL（PEP 684/734，Q5501）什么关系？——两个互补方向：free-threading 是全进程无 GIL（共享堆、细粒度锁，调试难度最大）；subinterpreters 是每解释器一把 GIL（隔离更彻底，IPC 走共享内存），按隔离需求选型而非性能迷信。3) 为什么 free-threading 构建单线程会变慢？——去掉了 GIL 后所有对象操作都要走延迟回收与本地计数协议，单线程路径多了分支与屏障；官方口径约 5-10% 单线程开销，所以 3.13 把它做成可选构建而非默认。

## 背诵要点
- free-threading（3.13 PEP 703，可选构建）：threading 原语 API 不变，消失的是"GIL 兜底隐式原子性"——单操作有内部细粒度锁、复合操作必须显式锁。
- 实现侧三件套：deferred/biased reference counting + mimalloc 线程本地分配器；代价是单线程约 5-10% 开销、refcount 观测不稳定。
- 迁移清单：无锁共享状态全量加锁、复合操作（get-then-set）排查、与 per-interpreter GIL 按隔离需求选型（Q5501）。

## 复盘追问
- 你们的代码里有多少"碰巧没出事"的无锁共享写？如果明天切 free-threading 构建会炸几处？（提示：先用本卡 bump_plain 模式 grep 模块级可变全局，再排双检锁与缓存失效逻辑）
- 基准测试里 free-threading 构建的吞吐曲线在几线程处开始收益递减？瓶颈是争用还是调度？（提示：对比 py-spy 火焰图中 mutex 等待帧占比，回看 Q5566 的 switch interval 时代账本已不适用）
