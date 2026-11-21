"""连接池监控指标: 在用 空闲 等待与超时"""
import threading
import time
from collections import deque

class MonitoredPool:
    def __init__(self, size=4):
        self.size = size
        self.idle = deque(range(size))
        self.in_use = 0
        self.waiting = 0
        self.cond = threading.Condition()
        self.metrics = {"acquired": 0, "wait_timeout": 0, "wait_ms": []}
    def acquire(self, timeout=0.03):
        start = time.monotonic()
        deadline = start + timeout
        with self.cond:
            self.waiting += 1
            ok = True
            while not self.idle:
                remain = deadline - time.monotonic()
                if remain <= 0:
                    ok = False
                    break
                self.cond.wait(remain)
            self.waiting -= 1
            if not ok:
                self.metrics["wait_timeout"] += 1
                raise TimeoutError("pool exhausted")
            self.metrics["wait_ms"].append((time.monotonic() - start) * 1000)
            conn = self.idle.popleft()
            self.in_use += 1
            self.metrics["acquired"] += 1
            return conn
    def release(self, conn):
        with self.cond:
            self.in_use -= 1
            self.idle.append(conn)
            self.cond.notify()

pool = MonitoredPool(size=4)
errors = []

def worker(n):
    try:
        c = pool.acquire(timeout=0.03)
        time.sleep(0.01)
        pool.release(c)
    except TimeoutError:
        errors.append(n)

threads = [threading.Thread(target=worker, args=(i,)) for i in range(20)]
for t in threads:
    t.start()
for t in threads:
    t.join()

m = pool.metrics
waits = sorted(m["wait_ms"])
p95 = waits[int(len(waits) * 0.95) - 1] if waits else 0.0
print(f"20 并发 4 连接: 成功 {m['acquired']}  等待超时 {m['wait_timeout']}  剩余空闲 {len(pool.idle)}  在用 {pool.in_use}")
print(f"等待时长 p95 {p95:.1f} ms  超时错误 {len(errors)} 个")
print("结论: 连接池必看五个数 在用 空闲 等待线程 等待超时 等待分位 超时上升先查慢查询再考虑扩池")
