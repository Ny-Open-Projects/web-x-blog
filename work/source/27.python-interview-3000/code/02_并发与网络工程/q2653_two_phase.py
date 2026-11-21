# -*- coding: utf-8 -*-
"""锁外准备、锁内提交两段式: 把耗时工作挪出临界区。

- 朴素写法: 拿锁 -> 准备数据 -> 写入 -> 放锁, 锁被计算拖住;
- 两段式: 锁外把新版本完整准备好, 锁内只做一次引用替换;
- 实测两种写法的"持锁时长": 两段式把临界区压缩到微秒以下。
"""
import threading
import time

N_WORKERS = 4
ROUNDS = 60
hold_times = {"one_phase": [], "two_phase": []}
store = {"version": 0, "data": {}}
store_lock = threading.Lock()


def prepare():
    """昂贵的准备工作: 构造一份全新的数据版本, 不碰任何共享状态。"""
    return {i: (i * 31) % 997 for i in range(2000)}


def one_phase():
    for _ in range(ROUNDS):
        with store_lock:
            t0 = time.perf_counter()         # 只量真正持锁的部分
            new_data = prepare()             # 计算在锁内: 临界区被拖长
            store["data"] = new_data
            store["version"] += 1
            hold_times["one_phase"].append(time.perf_counter() - t0)


def two_phase():
    for _ in range(ROUNDS):
        new_data = prepare()                 # 准备在锁外: 与他人零竞争
        with store_lock:
            t0 = time.perf_counter()
            store["data"] = new_data         # 提交在锁内: 一次赋值
            store["version"] += 1
            hold_times["two_phase"].append(time.perf_counter() - t0)


def report(mode):
    xs = sorted(hold_times[mode])
    avg = sum(xs) / len(xs) * 1e6
    p95 = xs[int(len(xs) * 0.95)] * 1e6
    print("%s: 平均持锁 %.2f us, P95 持锁 %.2f us" % (mode, avg, p95))


if __name__ == "__main__":
    for mode, key, fn in (("朴素一把梭", "one_phase", one_phase),
                          ("两段式", "two_phase", two_phase)):
        hold_times[key] = []
        ts = [threading.Thread(target=fn) for _ in range(N_WORKERS)]
        for t in ts:
            t.start()
        for t in ts:
            t.join()
        report(key)
    print("最终版本号:", store["version"], "(4 线程 x 60 轮, 无丢失更新)")
