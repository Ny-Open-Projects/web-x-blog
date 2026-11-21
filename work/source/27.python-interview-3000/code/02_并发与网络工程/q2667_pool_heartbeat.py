# -*- coding: utf-8 -*-
"""进程池任务的进度心跳: 父进程怎么知道子进程没卡死。

- 任务函数把"平安报文"写进 multiprocessing.Queue, 父进程持续捞取;
- 父进程给每个任务记最近心跳时刻, 超过阈值没声音就告警;
- 结果 Future 只能告诉你"完成没有", 心跳才能告诉你"还活着没有"。
"""
import multiprocessing as mp
import time
from queue import Empty

HB_Q = None                              # 子进程侧的全局心跳队列


def hb_init(q):
    global HB_Q
    HB_Q = q


def beat(name):
    HB_Q.put(("beat", name, time.time()))


def progress_task(name):
    beat(name)
    for _ in range(6):
        time.sleep(0.1)
        beat(name)                       # 每 0.1s 报一次平安
    return name + ":ok"


def silent_task(name):
    time.sleep(1.0)                      # 假装卡死: 全程一声不吭
    return name + ":done"


if __name__ == "__main__":
    q = mp.Queue()
    with mp.Pool(2, initializer=hb_init, initargs=(q,)) as pool:
        specs = [("progress-1", progress_task), ("silent-1", silent_task)]
        results = {n: pool.apply_async(fn, (n,)) for n, fn in specs}

        last_beat = {n: time.time() for n in results}   # 起点也算时刻
        warned = set()
        while any(not r.ready() for r in results.values()):
            try:
                kind, name, ts = q.get(timeout=0.1)
                last_beat[name] = ts
            except Empty:
                pass
            now = time.time()
            for n, r in results.items():
                seen = last_beat.get(n)
                if (not r.ready() and seen is not None
                        and now - seen > 0.4 and n not in warned):
                    warned.add(n)
                    print("告警: %s 已 %.1fs 无心跳, 疑似卡死"
                          % (n, now - seen))

    print("心跳收尾: progress-1 持续报平安, silent-1 全程静默")
    print("结果回传:", {n: r.get() for n, r in results.items()})
