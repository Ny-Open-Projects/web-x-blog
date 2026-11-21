---
title: [Q2654] Condition.wait_for 超时等待:醒来必查谓词,超时也要拿证据
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2654 · Condition.wait_for 超时等待:醒来必查谓词,超时也要拿证据

> 难度:★★ | 标签:Condition, 超时等待, 谓词

**问**:Condition.wait() 挂起等条件,条件一直不来怎么办?超时之后能直接当条件不成立吗?

**答**:wait_for(predicate, timeout) 是带超时的谓词等待:内部循环重查谓词,帮你挡掉虚假唤醒与迟到通知;返回值就是谓词现值,超时拿到 False 也要以谓词现值为准。实测:生产者迟到但赶在预算内就等到,预算耗尽返回 False,之后再取还能取到迟到的包裹——超时返回不影响条件后续成立。

- 裸 wait() 醒来必须自己 while 重查谓词,wait_for 把这个模式固化了;

- 超时不是异常而是快速失败,调用方拿到 False 就去走降级路径;

- 超时时长要显著大于正常到达时间,否则会把慢而正常的操作误判为失败;

- 超时后条件仍可能成立,是否重试由业务决定,原语只负责如实报告。

```python
# file: code/02_并发与网络工程/q2654_cond_wait_for.py
# -*- coding: utf-8 -*-
"""Condition.wait_for 的超时等待: 醒来必查谓词, 超时也要拿证据。

- wait_for(pred, timeout) 内部循环重查谓词, 帮你挡掉虚假唤醒;
- 返回值就是谓词现值: True 表示条件成立, False 表示到点仍不成立;
- 超时不是异常, 是"拿不到就带着证据返回"的快速失败。
"""
import threading
import time


class Box:
    """最小的一次性信箱: item 非空即谓词成立。"""

    def __init__(self):
        self.cv = threading.Condition()
        self.item = None

    def put(self, v):
        with self.cv:
            self.item = v
            self.cv.notify_all()

    def take(self, timeout):
        with self.cv:
            ok = self.cv.wait_for(lambda: self.item is not None, timeout)
            if ok:
                v, self.item = self.item, None
                return v, True
            # 到点仍为空: 谓词现值就是证据, 不能想当然当它有货
            return None, False


if __name__ == "__main__":
    # 场景一: 生产者迟到但赶在预算内, 消费者等到货
    box1 = Box()
    results = {}

    def late_producer():
        time.sleep(0.15)
        box1.put("包裹")

    threading.Thread(target=late_producer).start()
    t0 = time.perf_counter()
    results["s1"], results["s1_ok"] = box1.take(timeout=0.5)
    results["s1_wait"] = time.perf_counter() - t0
    print("场景一: 等到 %r, 谓词=%s, 实等 %.2fs" %
          (results["s1"], results["s1_ok"], results["s1_wait"]))

    # 场景二: 没有生产者, 到点超时, 谓词为 False
    box2 = Box()
    t0 = time.perf_counter()
    v, ok = box2.take(timeout=0.2)
    elapsed = time.perf_counter() - t0
    print("场景二: 拿到 %r, 谓词=%s, 实等 %.2fs(约等于预算)" % (v, ok, elapsed))

    # 场景三: 超时后货又到了, 证明"超时返回"不影响之后取货
    def very_late_producer():
        time.sleep(0.3)
        box2.put("迟到的包裹")

    threading.Thread(target=very_late_producer).start()
    v, ok = box2.take(timeout=0.05)      # 先超时一次
    v2, ok2 = box2.take(timeout=1.0)     # 再等一次
    print("场景三: 第一次取 %r(ok=%s), 第二次取 %r(ok=%s)" % (v, ok, v2, ok2))
```

**追问**:1) wait_for 超时后锁还持有吗?——持有,它和 wait 一样在返回前重新拿到锁,出 with 块才释放。2) 谓词抛异常会怎样?——异常原样抛出,调用方应保证谓词是纯函数,不抛、不阻塞。3) 底层机制:wait_for 怎么挡虚假唤醒?——实现是循环"谓词为假就 wait(剩余预算)",无论被 notify 还是超时唤醒都重查谓词,只有谓词为真或预算耗尽才返回;notify_all 唤醒多个等待者时,大家各自重查,不会因别人抢先把货拿走而误判。4) 生产陷阱?——谓词里做 IO 或再拿别的锁,持锁阻塞拖死整个 Condition;超时预算小于正常到达时间,慢而正常的操作被误判失败;把 False 当"永远不成立",漏掉稍后重试的机会。

---
