"""singleflight: 同 key 并发回源合并为一次"""
import threading
import time

class SingleFlight:
    def __init__(self):
        self.inflight = {}
        self.lock = threading.Lock()

    def do(self, key, loader):
        with self.lock:
            if key in self.inflight:             # 已有同伴在加载
                fut = self.inflight[key]
                owner = False
            else:
                fut = {"event": threading.Event(), "value": None,
                       "error": None, "waiters": 0}
                self.inflight[key] = fut
                owner = True
            if not owner:
                fut["waiters"] += 1
        if owner:
            try:
                fut["value"] = loader()
            except Exception as e:
                fut["error"] = e
            finally:
                fut["event"].set()
                with self.lock:
                    self.inflight.pop(key, None)
        fut["event"].wait()
        if fut["error"]:
            raise fut["error"]
        return fut["value"]

if __name__ == "__main__":
    calls = []
    sf = SingleFlight()

    def slow_loader():
        time.sleep(0.3)                          # 模拟 DB 查询
        calls.append(1)
        return "db-result"

    results = []
    def worker():
        results.append(sf.do("hot:key", slow_loader))
    ts = [threading.Thread(target=worker) for _ in range(8)]
    [t.start() for t in ts]
    [t.join() for t in ts]
    print(f"8 个并发请求 -> DB 实际调用 {len(calls)} 次, 结果一致: {len(set(results)) == 1}")
