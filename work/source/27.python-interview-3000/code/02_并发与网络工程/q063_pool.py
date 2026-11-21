import multiprocessing
import os
import time


def square(n: int) -> int:
    return n * n


def slow_square(n: int) -> int:
    time.sleep(0.1)
    print(f"子进程 {os.getpid()} 处理 {n}")
    return n * n


if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, range(10))
        print("map 结果:", results)

        async_results = [pool.apply_async(slow_square, (i,)) for i in (3, 5, 7)]
        print("异步提交后可先做别的事")
        print("apply_async 结果:", [r.get() for r in async_results])
    print("with 退出即 pool.close + join")
