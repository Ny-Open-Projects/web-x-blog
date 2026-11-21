"""上游并发连接上限与准入排队: 有界等待加超时快速失败(纯标准库)。"""
import threading
import time


class ConcurrencyGate:
    """全局并发上限 + 有界等待队列: 排不上队立即返回, 宁可 503 不可拖死。

    max_inflight 限制同时在飞的上游调用数, max_waiting 限制排队长度。
    """

    def __init__(self, max_inflight=2, max_waiting=2, acquire_timeout=0.5):
        self.max_inflight = max_inflight
        self.max_waiting = max_waiting
        self.acquire_timeout = acquire_timeout
        self.slots = threading.BoundedSemaphore(max_inflight)
        self.waiting = 0
        self.lock = threading.Lock()

    def call(self, fn):
        with self.lock:
            if self.waiting >= self.max_waiting:
                return {"status": 503, "note": "队列已满, 直接拒绝"}
            self.waiting += 1
        try:
            acquired = self.slots.acquire(timeout=self.acquire_timeout)
        finally:
            with self.lock:
                self.waiting -= 1
        if not acquired:
            return {"status": 503, "note": "排队超时, 快速失败"}
        try:
            return {"status": 200, "result": fn()}
        finally:
            self.slots.release()


def slow_upstream():
    time.sleep(0.2)                      # 模拟慢上游
    return "upstream-data"


gate = ConcurrencyGate(max_inflight=2, max_waiting=1, acquire_timeout=0.1)
results = []
threads = []
for i in range(6):                       # 6 个并发打一个上限为 2 的门
    t = threading.Thread(target=lambda i=i: results.append((i, gate.call(slow_upstream))))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

results.sort()
ok = [r for _, r in results if r["status"] == 200]
rejected = [r for _, r in results if r["status"] == 503]
print("成功数:", len(ok), " 拒绝数:", len(rejected))
assert len(ok) == 6 - len(rejected) and len(rejected) >= 2
print("拒绝样本:", rejected[0]["note"])
print("要点: 上限保护的是自己不被慢上游拖垮, 排队长度加超时把故障变成快速失败而不是雪崩")
