---
title: "[Q6167] 任务队列乐观锁 CAS 与 ABA 防线"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6167 · 任务队列乐观锁 CAS 与 ABA 防线

难度：P7 ｜ 标签：乐观锁、CAS、ABA、任务队列、并发认领

**问**：不用 `SELECT ... FOR UPDATE SKIP LOCKED`（Q6007 已覆盖），能否用"版本号 CAS"做任务认领？两个 worker 同时读 `owner=None` 再写自己的名字，为什么会发生"两人都以为认领成功、后写覆盖前写"的更新丢失？CAS（`UPDATE ... WHERE version=? AND owner IS NULL`）为什么能防住？版本号被回收重置时 ABA 问题怎么产生、怎么防？失败重试的退避该怎么设计？

**答**：
结论：乐观锁的核心是"**读时记下版本，写时带版本做条件更新，只有版本未变才写成功**"——`UPDATE tasks SET owner=?, version=version+1 WHERE id=? AND version=?`。两个 worker 并发认领同一行时，都读到 `version=0`，第一个 CAS 成功（version→1），第二个的 `WHERE version=0` 不再匹配、更新 0 行，于是知道自己失败——这把"检查 + 写入"从两个步骤压缩成**一次原子条件写**，消除了"都检查通过再都写"的交错窗口。没有 CAS 的裸写就是典型更新丢失：两个 worker 都看到 `owner=None`，后写覆盖前写，两人都会执行同一任务且都以为自己拿到了。ABA 出现在"版本号被重置/复用"：任务完成后行被回收，version 错误地从 5 回到 5，新的 CAS 又用 5 做期望值，无法区分"这是旧世代还是新世代"——防线是**版本号单调递增永不复用**，或用 `(generation, version)` 复合标识、给行加唯一 `epoch`。CAS 失败后的重试要带**指数退避 + 抖动**（Q1335/Q824 覆盖退避策略），否则多 worker 在同一时刻重试会再次碰撞（重试风暴）。

取舍：乐观锁适合"冲突少、读多写少"的任务队列（大多数 worker 认领不同行），失败重试成本低于悲观锁的等待/死锁；高冲突热点单行场景用 CAS 会大量失败重试，反而不如 `SKIP LOCKED` 直接跳过被占行。与 Q6007 的 `SKIP LOCKED` 是两种思路：前者在**应用层做版本判定**，后者在**数据库层做行锁跳过**，互斥且不重复。

实战：事故形态是"两个 worker 同时认领同一任务，任务被执行两次（重复扣款/重复发邮件）"——排查看认领 SQL 有没有带版本/owner 条件、影响行数是否被检查。下面用 stdlib 模拟：无 CAS 的双认领覆盖、CAS 下只有一个成功、以及 ABA 风险与 generation 防线。

```python
from concurrent.futures import ThreadPoolExecutor
import threading, time

class Row:
    def __init__(self, version=0, owner=None):
        self.version = version
        self.owner = owner

# 1) 无 CAS：都看到 owner=None，交错后后写覆盖前写
bad = Row()
def claim_bad(worker, row):
    if row.owner is None:
        time.sleep(0.002)                 # 放大"检查与写入之间"的交错窗口
        row.owner = worker
        return True
    return False
with ThreadPoolExecutor(max_workers=2) as ex:
    print("no-CAS results:", list(ex.map(lambda w: claim_bad(w, bad), ["w1", "w2"])))
print("final owner:", bad.owner, " <- 两人都以为成功，后写覆盖")

# 2) CAS：比较并交换，只有一个成功（锁仅为模拟 DB 原子性）
lock = threading.Lock()
good = Row()
def claim_cas(worker, row):
    with lock:                             # 模拟一条原子 UPDATE 的临界区
        expected = row.version
        if row.owner is not None:
            return False
        row.version = expected + 1         # WHERE version=expected 成立才写
        row.owner = worker
        return True
with ThreadPoolExecutor(max_workers=2) as ex:
    print("CAS results  :", list(ex.map(lambda w: claim_cas(w, good), ["w1", "w2"])))
print("final owner:", good.owner, "version:", good.version)

# 3) ABA：版本被回收重置，CAS 无法区分世代
recycled = Row(version=5, owner="old")
recycled.owner, recycled.version = None, 5   # 错误地把 version 重置回 5
print("ABA: 新任务期望 version=5，与旧世代相同 -> 误判成功")
print("防线: 单调递增版本 / (generation, version) =", (2, 5))
```

**追问一**：为什么 CAS 一定要检查**影响行数**（`rowcount`）而不能只看 SQL 执行没报错？——因为 `UPDATE ... WHERE version=?` 在条件不满足时是**合法执行、只是更新 0 行**，不会抛异常；若代码只看"没报错就当成功"，两个 worker 都会认为自己认领成功，CAS 形同虚设。正确写法是 `if cursor.rowcount == 1: 认领成功 else: 重试/放弃`——这是乐观锁实现里最常见的一类 bug。

**追问二**：乐观锁+退避在极高冲突下为什么会退化成"重试风暴"？——因为多个失败 worker 若用固定间隔重试，会在同一时刻再次碰撞，反复失败；指数退避拉长间隔、抖动打散相位才能收敛（Q1335 的三种 jitter）。但即便如此，热点单行的冲突概率仍高，此时该换策略：用 `SKIP LOCKED` 跳过被占行去认领别的任务，或把任务按分片键打散到多行降低单点冲突——重试不是万能药，冲突率超过阈值就该换机制。

## 背诵要点
- CAS：`UPDATE ... WHERE version=? AND owner IS NULL`，靠版本未变才写成功，把检查+写入压成一次原子写。
- 必须检查 `rowcount==1`；无 CAS 的双认领会更新丢失、任务被执行两次。
- ABA：版本号重置复用会让 CAS 误判，防线是单调递增版本或 `(generation, version)`；高冲突用 SKIP LOCKED/分片替代重试。

## 复盘追问
- 两个 worker 同时认领同一任务导致重复执行，如何用"检查与写入交错窗口"定位并给出 CAS 修复？（rowcount 检查、版本条件更新、与 Q6007 SKIP LOCKED 的取舍）
- 为什么版本号不能回收复用？（ABA 问题，讨论单调递增/generation 复合键的防线）
