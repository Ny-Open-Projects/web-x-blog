import threading
import time

def cpu_bound(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

def io_like(duration):
    time.sleep(duration)   # sleep 会释放 GIL,模拟阻塞 IO

if __name__ == "__main__":
    N = 1_000_000    # 演示规模缩小,保证脚本秒级跑完

    t0 = time.perf_counter()
    cpu_bound(N)
    cpu_bound(N)
    print("CPU 串行:", round(time.perf_counter() - t0, 3), "s")

    t0 = time.perf_counter()
    threads = [threading.Thread(target=cpu_bound, args=(N,)) for _ in range(2)]
    for t in threads: t.start()
    for t in threads: t.join()
    print("CPU 多线程,通常更慢:", round(time.perf_counter() - t0, 3), "s")

    t0 = time.perf_counter()
    threads = [threading.Thread(target=io_like, args=(0.3,)) for _ in range(4)]
    for t in threads: t.start()
    for t in threads: t.join()
    print("IO 多线程,约等于单个耗时:", round(time.perf_counter() - t0, 3), "s")
