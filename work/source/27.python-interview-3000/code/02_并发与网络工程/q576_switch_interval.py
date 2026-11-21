import sys
import threading
import time

counter = 0


def spin(n: int) -> None:
    global counter
    for _ in range(n):
        counter += 1  # 读-改-写, 依赖 GIL 切换时机决定竞态程度


def run(n_iter: int) -> tuple:
    global counter
    counter = 0
    ts = [threading.Thread(target=spin, args=(n_iter,)) for _ in range(4)]
    t0 = time.perf_counter()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    dt = time.perf_counter() - t0
    return counter, dt


if __name__ == "__main__":
    n = 100000
    for interval in (0.005, 0.001, 0.00005):
        sys.setswitchinterval(interval)
        got, dt = run(n)
        expected = 4 * n
        print(f"switchinterval={interval:<8} 结果 {got}/{expected} "
              f"丢失 {expected - got:>6} 耗时 {dt:.3f}s")
    sys.setswitchinterval(0.005)  # 恢复默认
