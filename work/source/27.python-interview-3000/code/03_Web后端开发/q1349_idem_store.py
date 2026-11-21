"""幂等键存储:并发首请求只执行一次,其余重放(纯标准库)。"""
import threading
import time


class IdempotencyStore:
    def __init__(self, ttl_seconds=300):
        self.ttl = ttl_seconds
        self.records = {}            # key -> {"result": .., "expires": ..}
        self.locks = {}              # key -> Lock,实现单飞
        self.guard = threading.Lock()

    def _key_lock(self, key):
        with self.guard:
            return self.locks.setdefault(key, threading.Lock())

    def execute(self, key, work):
        """返回 (result, replayed):只有持锁者真正执行 work。"""
        lock = self._key_lock(key)
        with lock:
            now = time.monotonic()
            rec = self.records.get(key)
            if rec and rec["expires"] > now:
                return rec["result"], True
            result = work()
            self.records[key] = {"result": result, "expires": now + self.ttl}
            return result, False


store = IdempotencyStore()
calls = []
barrier = threading.Barrier(2)


def do_work(tag):
    calls.append(tag)
    time.sleep(0.05)                 # 模拟业务耗时,放大并发窗口
    return f"order-{tag}"


def worker(tag):
    barrier.wait()                   # 两个请求同时发起
    result, replayed = store.execute("pay-1", lambda: do_work(tag))
    print(f"worker-{tag}: result={result} replayed={replayed}")


threads = [threading.Thread(target=worker, args=(i,)) for i in (1, 2)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("业务执行次数:", len(calls), "必须为 1")
