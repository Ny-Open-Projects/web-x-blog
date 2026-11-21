---
title: [Q411] PEP 703 free-threading:去掉 GIL 之后靠什么保证安全?
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q411 · PEP 703 free-threading:去掉 GIL 之后靠什么保证安全?

> 难度:★★★★★ | 标签:PEP 703, free-threading, 并发

**问**:free-threaded 构建(3.13+,`python3.13t`)是怎么做到不要 GIL 的?引用计数怎么办?为什么官方说"依赖 GIL 隐式线程安全的代码会坏"?3.14 的状态是什么?

**答**:PEP 703 方案分三件事:引用计数改成**偏向读写(biased reference counting)**——对象挂一个偏向线程做无原子操作的自然计数,其他线程走原子慢路径;把 GIL 拆成细粒度锁,内存分配器 per-thread、`dict`/`list` 内部加锁,同时许多容器操作用惰性删除(先标记后清理)避免长持锁;对象头里的 GC 头与锁信息合并。代价是无竞争时单线程性能有损(3.13 早期约 40%,3.13t+ 持续优化中),所以以独立 ABI(`python3.13t`,带 `_t` 后缀)发布,与 GIL 版不能装同一个扩展二进制。PEP 779 在 3.14 把 free-threading 提升为官方 "supported"(非默认)阶段。风险点:过去依赖"一个字节码不会被打断"的代码(如无锁的单 check-then-act、靠 GIL 串行化的 `dict` 批量操作)在 free-threading 下会出现真正的数据竞争,必须显式加 `threading.Lock` 或改用不可变数据。

```python
# file: code/01_语言核心与底层/q411_free_threading_check.py
import sys
import threading

# 判断运行在哪种构建:free-threading 构建下 sys._is_gil_enabled() 可为 False
print("version:", sys.version)
is_ft = getattr(sys, "_is_gil_enabled", None)
if is_ft is not None:
    print("GIL enabled:", is_ft())
else:
    print("no _is_gil_enabled -> 普通含 GIL 构建")

# 无论哪种构建,这段 check-then-act 都不是原子的
# 在 free-threading 下竞争窗口更大,正确做法是加锁
lock = threading.Lock()
seen = set()

def check_and_add(n):
    with lock:                    # 去掉锁,free-threading 下可能出现覆盖
        seen.add(n)

threads = [threading.Thread(target=check_and_add, args=(i % 50,)) for i in range(1000)]
[t.start() for t in threads]
[t.join() for t in threads]
print("unique:", len(seen))
```

**追问**:1) 如何让自己的 C 扩展同时支持两种构建?——free-threading 下必须声明 `Py_mod_gil = Py_MOD_GIL_NOT_USED`,并消除模块级全局可变状态,否则解释器会在导入时告警。2) `PYTHON_GIL=0/1` 环境变量做什么?——运行期强制开/关 GIL;对依赖不安全扩展的程序,free-threading 构建可退回启用 GIL。
