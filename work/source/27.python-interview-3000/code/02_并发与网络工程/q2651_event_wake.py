# -*- coding: utf-8 -*-
"""Event 的并发唤醒实测: set 一声, 8 个等待者的唤醒时延展开。

- 8 个等待者都睡在 event.wait() 上, 主线程 set() 一次;
- 每个等待者记录从 set 到自己恢复运行的时延, 观察唤醒展开;
- 羊群效应: 全部 8 人被唤醒并抢锁, 但资源只有一份, 只有 1 人干成活。
"""
import threading
import time

N = 8
event = threading.Event()
ready = threading.Barrier(N + 1)     # 全员就位后再 set
wake_lat = [None] * N                # 每个等待者的唤醒时延
t_set = [0.0]
winner_lock = threading.Lock()
winner = []


def waiter(idx):
    ready.wait()
    event.wait()                     # 睡在 Event 上
    wake_lat[idx] = time.perf_counter() - t_set[0]
    # 资源只有一份: 只有第一个抢到名额的人算"干成活"
    with winner_lock:
        if not winner:
            winner.append(idx)


if __name__ == "__main__":
    ts = [threading.Thread(target=waiter, args=(i,)) for i in range(N)]
    for t in ts:
        t.start()
    ready.wait()
    time.sleep(0.05)                 # 确保它们都已睡在 event 上
    t_set[0] = time.perf_counter()
    event.set()                      # 一声哨响, 广播唤醒
    for t in ts:
        t.join()

    lat = sorted(x * 1000 for x in wake_lat if x is not None)
    print("各等待者唤醒时延 ms:", ["%.3f" % x for x in lat])
    print("最快 %.3f ms / 最慢 %.3f ms / 展开 %.3f ms"
          % (lat[0], lat[-1], lat[-1] - lat[0]))
    print("被唤醒人数: %d/%d, 真正干成活: %d 人"
          % (len(lat), N, len(winner)))

    # 对照: clear 之后再 set 才能再次广播, Event 是一次性闸门
    event.clear()
    second = threading.Event()
    blocked = []

    def late_waiter():
        blocked.append(event.wait(timeout=0.2))

    tl = threading.Thread(target=late_waiter)
    tl.start()
    tl.join()
    print("clear 后未 set, 新等待者 0.2s 超时返回:", blocked)
