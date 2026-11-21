# -*- coding: utf-8 -*-
"""多进程日志汇聚: 子进程日志经 Queue 回传父进程统一落盘。

- 子进程只挂一个 QueueHandler: 日志记录被 pickle 后送进队列;
- 父进程跑 QueueListener 角色: 单点收日志、统一格式、统一输出;
- 好处: 不抢同一个日志文件, 格式一处可改, 也不会写花。
"""
import logging
import logging.handlers
import multiprocessing as mp
import sys
import time
from multiprocessing import Process, Queue


def listener_proc(q, counter):
    relay = logging.getLogger("relay")
    relay.setLevel(logging.INFO)
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(logging.Formatter("[来自 %(name)s] %(message)s"))
    relay.addHandler(h)
    n = 0
    while True:
        rec = q.get()
        if rec is None:                  # 收工哨兵
            break
        relay.handle(rec)
        n += 1
    counter.value = n


def worker_init(q):
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.addHandler(logging.handlers.QueueHandler(q))


def wjob(i):
    logging.getLogger("worker.%d" % (i % 2)).info("task %d done", i)
    return i


if __name__ == "__main__":
    q = Queue()
    counter = mp.Value("i", 0)
    lp = Process(target=listener_proc, args=(q, counter), daemon=True)
    lp.start()

    with mp.Pool(2, initializer=worker_init, initargs=(q,)) as pool:
        pool.map(wjob, range(8))

    time.sleep(0.3)                      # 等子进程的记录飞到队列
    q.put(None)
    lp.join(timeout=3)
    print("listener 汇聚了 %d 条日志(应为 8)" % counter.value)
