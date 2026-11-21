---
title: [Q2126] maxtasksperchild:进程池的定期换班
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2126 · maxtasksperchild:进程池的定期换班

> 难度:★★★ | 标签:multiprocessing.Pool, maxtasksperchild, worker 回收

**问**:进程池的 worker 会一直活着吗?怎么防止一个写了内存泄漏的任务把池子拖死?

**答**:maxtasksperchild 让 worker 干满 N 个任务就退出、换新进程接班,用重建成本隔离坏状态。

- 实测 8 个任务配 maxtasksperchild=2,出现 4 个不同 pid;

- 不设上限时 pid 几乎不变,worker 长期存活;

- 适合隔离内存泄漏、释放第三方 C 库的内部状态;

- 代价是每 N 个任务一次进程重建,进程创建与导入成本要算进吞吐。

```python
# file: code/02_并发与网络工程/q2126_maxtasksperchild.py
# -*- coding: utf-8 -*-
"""maxtasksperchild: 进程池的定期换班。

- maxtasksperchild 让 worker 干满 N 个任务后退出换新进程;
- 目的是隔离内存泄漏、释放第三方库的坏状态, 代价是重建进程的固定开销;
- 实测: 8 个任务配 maxtasksperchild=2, 出现至少 4 个不同 pid。
"""
import multiprocessing
import os

ctx = multiprocessing.get_context("fork")


def task(i):
    return os.getpid()


def main():
    pool = ctx.Pool(processes=2, maxtasksperchild=2)
    try:
        pids = pool.map(task, range(8))
    finally:
        pool.close()
        pool.join()
    print("8 个任务的执行进程:", pids)
    distinct = len(set(pids))
    print("不同 pid 数:", distinct, "-> 每干 2 个任务就换班一次")

    pool2 = ctx.Pool(processes=2)   # 不限任务数
    try:
        pids2 = pool2.map(task, range(8))
    finally:
        pool2.close()
        pool2.join()
    print("不限换班的执行进程:", pids2)
    print("不限换班的不同 pid 数:", len(set(pids2)),
          "-> 明显少于换班版, worker 长期存活")

    print("ProcessPoolExecutor 在 3.11+ 用 max_tasks_per_child 提供同能力")


if __name__ == "__main__":
    main()
```

**追问**:1) ProcessPoolExecutor 怎么设?——3.11 起有 max_tasks_per_child 参数,标准库两个池终于对齐。2) 换班会不会丢正在跑的任务?——不会,worker 只在任务间隙退出,回收的是"干完 N 个"的进程。3) 换班成本怎么算进吞吐?——每次重建=进程创建+模块导入+连接重建;任务越轻、N 越小,重建占比越高;经验:重建成本 < 单任务耗时的 10% 才划算;「换班频率」与「泄漏速率」匹配(泄漏严重 N 小,无泄漏 N 大或不设)。4) 与健康探活/对象池的配套?——换班治「进程级坏状态」,连接池的 validator 治「连接级坏状态」(Q1849);两级卫生机制叠加;重建时 in-flight 任务不丢(worker 只在任务间隙退出,Q2126 原问)。5) 生产陷阱?——N 太小(重建风暴,吞吐崩);第三方 C 库状态没随换班清(泄漏仍在);换班不重建连接池(新进程旧连接?不可能,但会重复建连,要配连接预热);误把换班当泄漏修复(泄漏在任务代码里,换班只是延缓);ProcessPoolExecutor 3.11 前无此参数(用 multiprocessing.Pool 或手动重建)。

---
