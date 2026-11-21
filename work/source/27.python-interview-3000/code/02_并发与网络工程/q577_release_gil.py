import ctypes
import ctypes.util
import threading
import time

path = ctypes.util.find_library("c") or ("libc.so.6" if sys.platform != "darwin" else "libc.dylib")
libc = ctypes.CDLL(path or "libc.so.6")  # CDLL: 调用期间释放 GIL
libc.usleep.argtypes = [ctypes.c_uint]

SPIN_SECONDS = 0.5
iterations = [0]
stop = threading.Event()


def python_spin() -> None:
    """纯 Python 忙循环, 用来探测 GIL 是否可用。"""
    while not stop.is_set():
        iterations[0] += 1


if __name__ == "__main__":
    import sys
    if sys.platform == "darwin":
        path = ctypes.util.find_library("libc.dylib") or "/usr/lib/libc.dylib"
    else:
        path = ctypes.util.find_library("c") or "libc.so.6"
    libc = ctypes.CDLL(path)
    libc.usleep.argtypes = [ctypes.c_uint]

    spinner = threading.Thread(target=python_spin, daemon=True)
    spinner.start()

    iterations[0] = 0
    t0 = time.perf_counter()
    libc.usleep(300000)  # 0.3s 的 C 阻塞调用: 释放 GIL
    c_blocking = iterations[0] / (time.perf_counter() - t0)

    iterations[0] = 0
    t0 = time.perf_counter()
    n = 3000000
    libc.rand.restype = ctypes.c_int
    for _ in range(n):  # 大量微小 C 调用: 每次调用都要抢 GIL
        libc.rand()
    c_many = iterations[0] / (time.perf_counter() - t0)

    stop.set()
    spinner.join()
    print(f"C 阻塞调用期间 Python 循环推进率: {c_blocking:,.0f} 次/秒")
    print(f"海量微小 C 调用期间推进率:      {c_many:,.0f} 次/秒")
    print("结论: 单次长 C 调用释放 GIL, 频繁短调用反而加剧 GIL 争抢")
