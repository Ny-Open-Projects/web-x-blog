---
title: [Q2122] 进程池任务的优雅取消:Future.cancel 的生效窗口
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2122 · 进程池任务的优雅取消:Future.cancel 的生效窗口

> 难度:★★★ | 标签:ProcessPoolExecutor, cancel, 优雅停机

**问**:用户点停止时,进程池里还有 8 个任务:已在跑的 2 个、排队的 6 个,哪些能取消?

**答**:只有未开始的排队任务能取消;已在跑的 cancel 返回 False,进程没有外部中断任务的正道。

- cancel 成功的 future 进入 CANCELLED 状态,result 抛 CancelledError;

- 在途任务只能等它自然结束,或用子进程级手段(SIGKILL worker)代价更高;

- 批量停止的标准姿势:取消全部排队者,等在途者排干,超时再降级;

- 提交时给任务内部传停止标志,是让"不可取消"变"可取消"的协作式方案。

```python
# file: code/02_并发与网络工程/q2122_pool_task_cancel.py
# -*- coding: utf-8 -*-
"""进程池任务的优雅取消: Future.cancel 的生效窗口。

- 未开始的 pending 任务可 cancel; 已在跑的任务 cancel 返回 False, 只能等待;
- cancel 后的 future 状态是 CANCELLED, result 会抛 CancelledError;
- 批量取消时先留出在途任务, 取消排队者, 是进程池唯一体面的刹车。
"""
import multiprocessing
import os
import time
import concurrent.futures as cf

ctx = multiprocessing.get_context("fork")


def work(n):
    time.sleep(0.3)
    return n * 2


def main():
    ex = cf.ProcessPoolExecutor(max_workers=2, mp_context=ctx)
    try:
        futs = [ex.submit(work, i) for i in range(8)]
        time.sleep(0.1)            # 头两个任务已进入执行
        cancelled, pending = [], []
        for f in futs[2:]:
            (cancelled if f.cancel() else pending).append(f)
        print("排队任务取消成功:", len(cancelled), "个")
        print("已在跑无法取消:", len(pending), "个, 状态:",
              [f.running() for f in futs[:2]])
        kept = [f.result() for f in futs[:2]] + \
               [p.result() for p in pending]
        print("实际拿到结果:", kept)
        try:
            cancelled[0].result()
            print("意外: 取消的任务居然有结果")
        except cf.CancelledError:
            print("取消任务的 result 抛 CancelledError, 符合预期")
    finally:
        ex.shutdown(wait=True)


if __name__ == "__main__":
    main()
```

**追问**:1) multiprocessing.Pool 有取消吗?——没有 future 级取消,要用进程池外的任务表自己记账;这是 executor API 的优势。2) 已取消的任务会把队列堵住吗?——不会,worker 取到任务前就跳过了,队列立即瘦身。3) 「在途任务只能等」的工程化解法?——任务内部停止标志(协作式,Q1574):提交时传 flag,任务循环检查;子进程级 SIGKILL worker(代价:池要重建 worker,3.11 的 max_tasks_perchild 模式配合)——「提交时带停止钩子」是进程池取消的正道。4) 批量停止的次序与超时?——先 cancel 全部排队者(立即生效,队列瘦身)→等在途者(带 deadline)→超时降级(SIGKILL 或放弃);与线程池 shutdown 的三档(Q1305)、TaskGroup 取消树同构——「先取消未开始,再等待已开始,超时降级」是取消的通用次序。5) 生产陷阱?——以为 cancel 能停掉在跑任务(返回 False);等在途无超时(永不返回);SIGKILL worker 不重建(池容量缺口);取消任务的结果没人消费(CancelledError 静默);multiprocessing.Pool 无 future 级取消还硬写(用 executor API)。

---
