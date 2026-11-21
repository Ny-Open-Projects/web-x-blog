# -*- coding: utf-8 -*-
"""线程对账: 期望清单与实际清单, 泄漏无处藏身。

- 线程泄漏的形态: 每来一个任务就 new 一个线程, 用完不收;
- 对账审计: threading.enumerate 的实际名单对照期望名单, 差集即泄漏;
- 配合峰值采样: 线程数的历史高点, 是无界并发最直白的证据。
"""
import threading
import time

EXPECTED = {"main", "monitor", "worker-0", "worker-1"}
peak_samples = []
stop_sampler = threading.Event()


def monitor():
    while not stop_sampler.is_set():
        peak_samples.append(threading.active_count())
        time.sleep(0.03)


def long_worker():
    time.sleep(3.0)                      # 长命 worker: 全程都在名单上


def batch_worker():
    time.sleep(0.4)                      # 短命任务线程: 等着被对账


def leaky_batch():
    """反面教材: 每个任务开一个线程, 不 join 不复用。"""
    for i in range(5):
        threading.Thread(target=batch_worker, name="task-%d" % i,
                         daemon=True).start()


def audit():
    actual = {t.name for t in threading.enumerate()}
    return sorted(actual - EXPECTED), sorted(EXPECTED - actual)


if __name__ == "__main__":
    threading.current_thread().name = "main"
    mon = threading.Thread(target=monitor, name="monitor", daemon=True)
    mon.start()
    for i in range(2):
        threading.Thread(target=long_worker, name="worker-%d" % i,
                         daemon=True).start()

    leaky_batch()
    time.sleep(0.15)                     # task-* 线程已在名单上
    leaked, missing = audit()
    print("审计一: 泄漏线程 %s, 缺失线程 %s" % (leaked, missing))
    print("峰值线程数:", max(peak_samples) if peak_samples else 1)

    for t in threading.enumerate():      # 处置: 收尸
        if t.name.startswith("task-"):
            t.join()
    leaked2, missing2 = audit()
    stop_sampler.set()
    mon.join()
    print("收尸后审计: 泄漏 %s, 缺失 %s" % (leaked2, missing2))
    print("要点: 泄漏的本质是'只有创建没有生命周期管理', 审计把账对平")
