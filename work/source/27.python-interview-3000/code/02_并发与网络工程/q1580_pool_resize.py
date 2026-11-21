"""线程池动态扩缩: 标准库池是定死的, 自己写一个能伸缩的。

ThreadPoolExecutor 的 max_workers 固定; 高峰需要更多手, 低谷想省内存。
自研要点:
- 扩容: 有积压且没有闲手 -> 孵化新 worker, 直到上限;
- 缩容: worker 空闲超时, 且总数超过下限 -> 自动退出;
- 关闭: 哨兵值排空队列, 存量任务做完再收摊。
"""
import queue
import threading
import time


class ResizablePool:
    def __init__(self, min_workers=2, max_workers=4, idle_timeout=0.25):
        self.q = queue.Queue()
        self.min_workers = min_workers
        self.max_workers = max_workers
        self.idle_timeout = idle_timeout
        self.mu = threading.Lock()
        self.busy = 0
        self.total = 0
        self.peak_busy = 0
        self.results = []
        for _ in range(min_workers):
            self._spawn()

    def _spawn(self):
        self.total += 1
        threading.Thread(target=self._worker, daemon=True,
                         name="w%d" % self.total).start()

    def _worker(self):
        while True:
            try:
                item = self.q.get(timeout=self.idle_timeout)
            except queue.Empty:
                with self.mu:
                    if self.total > self.min_workers:
                        self.total -= 1     # 缩容: 多余的手自动退出
                        return
                continue
            with self.mu:
                self.busy += 1
                self.peak_busy = max(self.peak_busy, self.busy)
            time.sleep(0.1)                 # 模拟任务耗时
            self.results.append(item)
            with self.mu:
                self.busy -= 1

    def drain(self, items):
        for it in items:
            self.q.put(it)
        deadline = time.monotonic() + 5
        while time.monotonic() < deadline:
            with self.mu:
                # 扩容: 有积压且全员在忙
                if self.total < self.max_workers and self.busy == self.total \
                        and not self.q.empty():
                    self._spawn()
            if self.q.empty() and self.busy == 0:
                break
            time.sleep(0.02)
        # 等待多余 worker 空闲退出
        end = time.monotonic() + 2
        while time.monotonic() < end:
            with self.mu:
                if self.total == self.min_workers:
                    break
            time.sleep(0.05)
        return self.peak_busy


def main():
    pool = ResizablePool(min_workers=2, max_workers=4)
    print("初始 worker 数:", pool.total)
    peak = pool.drain(["task-%d" % i for i in range(8)])
    print("完成 %d 个任务, 忙碌峰值: %d" % (len(pool.results), peak))
    print("收缩后 worker 数:", pool.total)
    assert len(pool.results) == 8, "所有任务都应完成"
    assert peak >= 3, "突发时应扩容到 3 个以上忙碌 worker"
    assert pool.total == 2, "低谷后应收缩回下限"
    print("结论: 扩容看'积压 + 无闲手', 缩容看'空闲超时 + 超出下限'")


if __name__ == "__main__":
    main()
