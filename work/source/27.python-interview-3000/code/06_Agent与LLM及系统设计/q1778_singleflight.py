"""同 query 并发合并:singleflight 让相同 key 的并发请求共享一次执行与结果。"""
import threading
import time


class Singleflight:
    def __init__(self):
        self._lock = threading.Lock()
        self._inflight = {}

    def do(self, key, fn):
        with self._lock:
            if key in self._inflight:
                event, box = self._inflight[key]     # 跟随者:共享首到者执行
                follower = True
            else:
                event, box = threading.Event(), {"result": None, "error": None}
                self._inflight[key] = (event, box)
                follower = False
        if follower:
            event.wait(timeout=5)
            if box["error"] is not None:
                raise box["error"]
            return box["result"]
        try:
            box["result"] = fn()                     # 只有首到者执行
            return box["result"]
        except Exception as e:
            box["error"] = e                         # 异常同样广播给跟随者
            raise
        finally:
            with self._lock:
                self._inflight.pop(key, None)
                event.set()


CALLS = {"n": 0}
CALL_LOCK = threading.Lock()


def slow_lookup(key):
    with CALL_LOCK:
        CALLS["n"] += 1
    time.sleep(0.15)                                 # 模拟慢调用,给并发窗口
    return "value:" + key


if __name__ == "__main__":
    sf = Singleflight()
    gate = threading.Barrier(4)
    results = []

    def worker(key):
        gate.wait(timeout=5)                         # 四线程同时对同一 key 发起
        results.append(sf.do(key, lambda: slow_lookup(key)))

    threads = [threading.Thread(target=worker, args=("q1",)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join(timeout=5)

    assert len(results) == 4 and all(r == "value:q1" for r in results)
    assert CALLS["n"] == 1, "相同 key 的 4 个并发请求只执行 1 次底层调用"

    assert sf.do("q2", lambda: slow_lookup("q2")) == "value:q2"
    assert CALLS["n"] == 2, "不同 key 各自执行"
    print("singleflight 通过:同 key 并发合并执行共享结果,不同 key 互不影响")
