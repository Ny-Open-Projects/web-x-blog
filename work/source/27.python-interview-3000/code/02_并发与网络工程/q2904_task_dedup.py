# -*- coding: utf-8 -*-
"""任务去重的本地实现: 排队/在途去重 + 完成台账 TTL。

- admit(key): 在途或台账内 -> 拒绝; 否则登记在途并放行;
- finish(key): 移出在途, 记入完成台账, TTL 过期后才允许重跑;
- 台账在每次 admit 时顺带修剪, 长期运行不涨内存;
- 指纹: 对 payload 做哈希, 相同内容的任务天然同 key。
"""
import hashlib
import threading
import time


class DedupGate:
    """去重闸门: 在途集合 + 带 TTL 的完成台账。"""

    def __init__(self, ttl=0.4):
        self.ttl = ttl
        self._lock = threading.Lock()
        self._inflight = set()
        self._done = {}                # key -> 完成时刻
        self.blocked = 0

    def _prune(self, now):
        for k in [k for k, t in self._done.items() if now - t > self.ttl]:
            del self._done[k]

    def admit(self, key):
        with self._lock:
            now = time.monotonic()
            self._prune(now)
            if key in self._inflight or key in self._done:
                self.blocked += 1      # 已排队不重排, 已完成不重跑
                return False
            self._inflight.add(key)
            return True

    def finish(self, key):
        with self._lock:
            self._inflight.discard(key)
            self._done[key] = time.monotonic()


def fingerprint(payload):
    """任务指纹: 同内容同 key。"""
    return hashlib.sha256(payload).hexdigest()[:12]


if __name__ == "__main__":
    gate = DedupGate(ttl=0.4)
    q = []
    qlock = threading.Lock()
    processed = []
    processed_once = {}

    def producer(pid):
        for i in range(15):            # 3 个生产者各投 15 个, 内容大量重叠
            key = fingerprint(("job-%d" % (i % 8)).encode())
            if gate.admit(key):
                with qlock:
                    q.append(key)

    def worker():
        while True:
            with qlock:
                if not q:
                    return
                key = q.pop(0)
            time.sleep(0.01)           # 干活
            with processed_once_lock:
                processed_once[key] = processed_once.get(key, 0) + 1
            gate.finish(key)

    processed_once_lock = threading.Lock()
    ps = [threading.Thread(target=producer, args=(i,)) for i in range(3)]
    ws = [threading.Thread(target=worker) for _ in range(2)]
    for t in ps + ws:
        t.start()
    for t in ps:
        t.join()
    for t in ws:
        t.join()

    print("投放 45 次, 唯一 key 8 个, 实际入队处理 %d 次, 去重拦截 %d 次"
          % (sum(processed_once.values()), gate.blocked))
    assert len(processed_once) == 8
    assert all(v == 1 for v in processed_once.values()), "有 key 被处理多次"
    assert gate.blocked == 37

    # TTL 过期后, 同一 key 允许重新执行 (重跑窗口)
    time.sleep(0.5)
    key = fingerprint(b"job-0")
    readmitted = gate.admit(key)
    if readmitted:
        gate.finish(key)
    print("TTL 过期后重投 job-0: admit=%s (到期允许重跑)" % readmitted)
    assert readmitted
    print("要点: 去重 = 在途集合 + TTL 台账, 拦的是重复劳动不是新任务")
