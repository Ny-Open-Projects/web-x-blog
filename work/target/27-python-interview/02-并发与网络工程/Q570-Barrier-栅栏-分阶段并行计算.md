---
title: [Q570] Barrier 栅栏:分阶段并行计算
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q570 · Barrier 栅栏:分阶段并行计算

> 难度:★★☆ | 标签:Barrier, 同步, 并行

**问**:Barrier 和 Event/Condition 有什么区别?什么场景必须用栅栏?

**答**:Barrier 是"集合点":n 个线程都调 wait 后才一起放行,适合多阶段流水线——每阶段所有线程完成后才进入下一阶段,例如并行模拟里"所有体素更新完才交换边界"。Event 是单向广播开关,Condition 是围绕共享状态的等待/通知,都不表达"凑齐 n 个"的语义。Barrier 还带超时和 `abort()`:任何一个线程 wait 超时,栅栏进入 broken 状态,所有等待者立刻抛 `BrokenBarrierError`,避免整组永久卡死,这正是它比手动 CountDownLatch 更适合错误处理的地方。

```python
# file: code/02_并发与网络工程/q570_barrier.py
import random
import threading
import time

barrier = threading.Barrier(3, timeout=1.0)  # 3 个线程一组, 最多等 1 秒


def phase_worker(name: str, slow: bool = False) -> None:
    for phase in range(3):
        delay = 2.0 if slow and phase == 1 else random.uniform(0.05, 0.15)
        time.sleep(delay)
        print(f"{name} 完成阶段 {phase}")
        try:
            barrier.wait()  # 集合点: 全员到齐才进下一阶段
        except threading.BrokenBarrierError:
            print(f"{name} 阶段 {phase} 栅栏失效, 整组退出")
            return


if __name__ == "__main__":
    print("--- 正常场景 ---")
    ts = [threading.Thread(target=phase_worker, args=(f"w{i}",)) for i in range(3)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()

    print("--- 超时场景: w9 太慢, 全组 broken ---")
    barrier2 = threading.Barrier(3, timeout=0.5)

    def worker2(name: str, slow: bool) -> None:
        try:
            for phase in range(2):
                if slow:
                    time.sleep(1.5)  # 远超栅栏超时
                barrier2.wait()
            print(f"{name} 全部完成")
        except threading.BrokenBarrierError:
            print(f"{name} 检测到栅栏失效, 中止")

    ts = [
        threading.Thread(target=worker2, args=("a", False)),
        threading.Thread(target=worker2, args=("b", False)),
        threading.Thread(target=worker2, args=("slow", True)),
    ]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
```

**追问**:1) Barrier 和 CountDownLatch 的本质区别?——latch 是一次性倒计数(等事件),Barrier 是可复用的集合点(等人),且 broken 语义让整组能协同失败。2) broken 的传播机制?——一方超时/退出→ barrier 置 broken → 其他等待者全部 BrokenBarrierError 抛出;reset() 恢复新代;这让「部分成员失联」不会永久卡死全组(Q572 的回退思想)。3) 分阶段并行的工程要点?——每阶段 barrier(action) 汇总;action 要短(长动作拖全员,Q582 呼应);阶段间数据交换用锁内共享结构。4) 生产陷阱?——成员数与 parties 不匹配永久等待;broken 后不 reset 复用;action 里做重活;超时为零死等。

---
