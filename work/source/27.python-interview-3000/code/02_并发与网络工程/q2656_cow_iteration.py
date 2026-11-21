# -*- coding: utf-8 -*-
"""写时复制的遍历安全: 边遍历边改的 RuntimeError 与快照替换。

- 读者正在 for 循环里遍历 dict, 写者插入新键 -> RuntimeError;
- 写时复制: 写者复制整表、改完一次性换引用, 读者拿着旧引用安心遍历;
- 复制成本随表增长, 所以写时复制适合"读多写少 + 表不大"的场景。
"""
import threading
import time

errors = [0]
rounds = [0]
stop = threading.Event()


def bare_reader(table):
    """直接遍历共享 dict: 撞上写入就抛 RuntimeError。"""
    while not stop.is_set():
        rounds[0] += 1
        try:
            for k in table:
                _ = table[k]         # 读每个值
        except RuntimeError as e:
            errors[0] += 1


def cow_reader(holder):
    """取一次引用当快照, 遍历的是不可变副本。"""
    while not stop.is_set():
        snap = dict(holder["snap"])  # 取引用 + 局部快照
        for k in snap:
            _ = snap[k]


if __name__ == "__main__":
    # 阶段一: 裸遍历共享 dict, 写者同时插键
    table = {i: i for i in range(8)}
    r = threading.Thread(target=bare_reader, args=(table,))
    r.start()
    for i in range(100, 160):
        table[i] = i                 # 边遍历边改
        time.sleep(0.0005)
    stop.set()
    r.join()
    print("裸遍历: %d 轮里撞出 %d 次 RuntimeError" % (rounds[0], errors[0]))

    # 阶段二: 写时复制, 读者只碰快照
    holder = {"snap": {i: i for i in range(8)}}
    writer_lock = threading.Lock()
    err2 = [0]

    def cow_writer():
        for i in range(100, 160):
            new = dict(holder["snap"])   # 复制旧版本
            new[i] = i                   # 在副本上改
            with writer_lock:
                holder["snap"] = new     # 一次性原子换引用
            time.sleep(0.0005)

    stop2 = threading.Event()
    rounds2 = [0]

    def cow_reader2():
        while not stop2.is_set():
            rounds2[0] += 1
            try:
                for k, v in list(holder["snap"].items()):
                    _ = v
            except RuntimeError:
                err2[0] += 1

    w = threading.Thread(target=cow_writer)
    r2 = threading.Thread(target=cow_reader2)
    w.start()
    r2.start()
    w.join()
    stop2.set()
    r2.join()
    print("写时复制: %d 轮遍历, RuntimeError %d 次, 最终键数 %d"
          % (rounds2[0], err2[0], len(holder["snap"])))
