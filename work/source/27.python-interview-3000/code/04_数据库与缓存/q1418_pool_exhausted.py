"""连接池打满: 借用超时与等待队列的最小模型"""
import queue
import threading
import time

class Pool:
    def __init__(self, size, timeout=0.2):
        self.free = queue.LifoQueue()
        for _ in range(size):
            self.free.put("conn")
        self.timeout = timeout
    def acquire(self):
        try:
            return self.free.get(timeout=self.timeout)
        except queue.Empty:
            raise RuntimeError("PoolError: 连接池已满 等待超时")
    def release(self, c):
        self.free.put(c)

pool = Pool(5)
results = {"ok": 0, "fail": 0}
lock = threading.Lock()

def worker():
    try:
        c = pool.acquire()
        time.sleep(0.05)
        pool.release(c)
        with lock:
            results["ok"] += 1
    except RuntimeError:
        with lock:
            results["fail"] += 1

ts = [threading.Thread(target=worker) for _ in range(20)]
for t in ts:
    t.start()
for t in ts:
    t.join()
print(f"池大小 5, 并发 20: 成功 {results['ok']}, 超时失败 {results['fail']}")
print("处置: 泄漏根治 + 容量按峰值占用估算 + 消灭慢命令这个放大器")
