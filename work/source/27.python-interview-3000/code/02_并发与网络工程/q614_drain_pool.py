import queue
import threading
import time


class DrainablePool:
    def __init__(self, workers: int = 3) -> None:
        self._q: queue.Queue = queue.Queue()
        self._accepting = True
        self._processed = 0
        self._lock = threading.Lock()
        self._ws = [
            threading.Thread(target=self._run, daemon=True) for _ in range(workers)
        ]
        for w in self._ws:
            w.start()

    def submit(self, fn) -> None:
        if not self._accepting:
            raise RuntimeError("pool closed: 拒绝新任务")
        self._q.put(fn)

    def _run(self) -> None:
        while True:
            fn = self._q.get()
            if fn is None:  # 毒丸
                return
            fn()
            with self._lock:
                self._processed += 1

    def shutdown(self, drain_timeout: float = 0.5) -> dict:
        self._accepting = False
        deadline = time.monotonic() + drain_timeout
        while self._q.qsize() > 0 and time.monotonic() < deadline:
            time.sleep(0.02)
        dropped = 0
        while True:  # 清空剩余并计数
            try:
                self._q.get_nowait()
                dropped += 1
            except queue.Empty:
                break
        for _ in self._ws:
            self._q.put(None)
        for w in self._ws:
            w.join(timeout=2)
        return {"processed": self._processed, "dropped": dropped}


def job(i: int) -> None:
    time.sleep(0.01)


if __name__ == "__main__":
    pool = DrainablePool(workers=3)
    for i in range(300):
        pool.submit(lambda i=i: job(i))
    t0 = time.monotonic()
    stats = pool.shutdown(drain_timeout=0.4)
    print(f"完成 {stats['processed']}, 明确丢弃 {stats['dropped']}, "
          f"关闭耗时 {time.monotonic() - t0:.2f}s")
    assert stats["processed"] + stats["dropped"] == 300
