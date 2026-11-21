import heapq
import time
from collections import deque


class Kernel:
    """curio 风格内核: 任务是生成器, yield trap 请求内核服务。"""

    def __init__(self) -> None:
        self._ready: deque = deque()
        self._sleeping = []  # (deadline, seq, task)
        self._seq = 0
        self._results = {}

    def add(self, tid: int, gen) -> None:
        self._ready.append((tid, gen))

    def run(self) -> dict:
        current_time = time.monotonic
        while self._ready or self._sleeping:
            # 1. 唤醒到期任务
            now = current_time()
            while self._sleeping and self._sleeping[0][0] <= now:
                _, _, (tid, gen) = heapq.heappop(self._sleeping)
                self._ready.append((tid, gen))
            # 2. 跑一个就绪任务直到它 yield trap
            if not self._ready:
                if self._sleeping:
                    delay = max(0.0, self._sleeping[0][0] - current_time())
                    time.sleep(min(delay, 0.01))  # 真实内核会 epoll 等待
                continue
            tid, gen = self._ready.popleft()
            try:
                trap = gen.send(None)
            except StopIteration as e:
                self._results[tid] = e.value
                continue
            # 3. 内核裁决 trap
            if trap[0] == "sleep":
                self._seq += 1
                heapq.heappush(
                    self._sleeping, (current_time() + trap[1], self._seq, (tid, gen))
                )
            elif trap[0] == "checkpoint":
                self._ready.append((tid, gen))  # 立即重新排队
        return self._results


def task_a(kernel: Kernel) -> int:
    for i in range(3):
        yield ("sleep", 0.03)
        print(f"task_a 步骤 {i}")
    return "a-done"


def task_b(kernel: Kernel) -> str:
    for i in range(2):
        yield ("checkpoint",)  # 显式可取消点: 换其他任务跑
        print(f"task_b 步骤 {i}")
    return "b-done"


if __name__ == "__main__":
    k = Kernel()
    k.add(1, task_a(k))
    k.add(2, task_b(k))
    t0 = time.perf_counter()
    results = k.run()
    print("结果:", results, f"耗时 {time.perf_counter() - t0:.2f}s")
