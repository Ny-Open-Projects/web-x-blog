import queue
import threading
import time


class PolicyPool:
    """带饱和策略的线程池: Abort / CallerRuns / DiscardOldest。"""

    def __init__(self, workers: int, queue_size: int, policy: str) -> None:
        self._q: queue.Queue = queue.Queue(maxsize=queue_size)
        self._policy = policy
        self._workers = [
            threading.Thread(target=self._run, daemon=True) for _ in range(workers)
        ]
        for w in self._workers:
            w.start()

    def submit(self, fn) -> None:
        try:
            self._q.put_nowait(fn)
        except queue.Full:
            if self._policy == "abort":
                raise RuntimeError("队列已满, Abort 策略: 拒绝任务")
            elif self._policy == "caller_runs":
                print("[饱和] CallerRuns: 提交线程自己执行")
                fn()  # 背压: 提交被拖慢
            elif self._policy == "discard_oldest":
                try:
                    self._q.get_nowait()  # 丢最老的
                    self._q.put_nowait(fn)
                    print("[饱和] DiscardOldest: 丢弃旧任务")
                except queue.Empty:
                    pass

    def _run(self) -> None:
        while True:
            fn = self._q.get()
            if fn is None:
                return
            fn()


def job(i: int) -> None:
    time.sleep(0.05)  # 模拟耗时任务


if __name__ == "__main__":
    for policy in ("abort", "caller_runs", "discard_oldest"):
        print(f"--- 策略: {policy} ---")
        pool = PolicyPool(workers=2, queue_size=2, policy=policy)
        ok = 0
        for i in range(8):
            try:
                pool.submit(lambda i=i: job(i))
                ok += 1
            except RuntimeError as e:
                print(f"[饱和] Abort: 第 {i} 个任务被拒绝 ({e})")
        time.sleep(0.8)
        pool._q.put(None)
        print(f"提交成功 {ok}/8, 队列剩余 {pool._q.qsize()}")
