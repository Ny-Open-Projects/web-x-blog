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
