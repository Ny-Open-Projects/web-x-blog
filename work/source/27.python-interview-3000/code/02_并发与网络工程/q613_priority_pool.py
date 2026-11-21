import itertools
import queue
import threading
import time

results: list = []
executed_order: list = []


class PriorityWorkerPool:
    def __init__(self, workers: int = 2) -> None:
        self._q: queue.PriorityQueue = queue.PriorityQueue()
        self._seq = itertools.count()
        self._stop = threading.Event()
        self._workers = [
            threading.Thread(target=self._run, daemon=True) for _ in range(workers)
        ]
        for w in self._workers:
            w.start()

    def submit(self, priority: int, name: str, fn) -> None:
        self._q.put((priority, next(self._seq), name, fn))  # seq 防函数比较

    def _run(self) -> None:
        while not self._stop.is_set():
            try:
                prio, seq, name, fn = self._q.get(timeout=0.5)
            except queue.Empty:
                continue
            executed_order.append(name)
            fn()
            self._q.task_done()

    def shutdown(self) -> None:
        # 先排空队列再停机: 若先 set stop, worker 可能在两次 get 之间
        # 直接退出, 队列里留下未处理任务, join() 永久阻塞(经典关停竞态)
        self._q.join()
        self._stop.set()


def job(name: str) -> None:
    time.sleep(0.05)
    results.append(name)


if __name__ == "__main__":
    pool = PriorityWorkerPool(workers=1)  # 单 worker 顺序清晰
    # 先提交低优先级, 再提交 VIP: VIP 只能插队"还在队列里"的任务
    for i in range(5):
        pool.submit(priority=10, name=f"normal-{i}", fn=lambda n=f"normal-{i}": job(n))
    # 等 worker 取走第一个任务(取走即脱离队列, VIP 抢不过它)
    deadline = time.monotonic() + 2
    while len(executed_order) < 1 and time.monotonic() < deadline:
        time.sleep(0.001)
    pool.submit(priority=1, name="vip", fn=lambda: job("vip"))
    pool.shutdown()
    print("执行顺序:", executed_order)
    assert executed_order[0] == "normal-0", "已被 worker 取走的任务无法被抢占"
    assert executed_order[1] == "vip", "VIP 应插队到队列中剩余任务之前"
    assert executed_order[2:] == [f"normal-{i}" for i in range(1, 5)]
    print("PriorityQueue 语义验证通过")
