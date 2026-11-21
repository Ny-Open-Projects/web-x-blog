import threading
import time

N = 10_000_000


def cpu_task() -> None:
    x = 0
    for i in range(N):
        x += i


def run_threads(n: int) -> None:
    threads = [threading.Thread(target=cpu_task) for _ in range(n)]
    start = time.perf_counter()
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return time.perf_counter() - start


if __name__ == "__main__":
    t1 = run_threads(1)
    t2 = run_threads(4)
    print(f"1 线程: {t1:.2f}s")
    print(f"4 线程: {t2:.2f}s  (受 GIL 限制, 几乎不加速甚至更慢)")
