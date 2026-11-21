# -*- coding: utf-8 -*-
"""进程池的 pickle 税: 传参与回传都要过序列化这道关。

- 池的每次调用: 参数 pickle 后发给子进程, 结果 pickle 后传回来;
- 大数据当参数传: 双程 pickle 税可能超过计算本身;
- 改传"生成指令"(只传 N), 让子进程自己造数据, 税就没了。
"""
import pickle
import time
from multiprocessing import Pool

N = 2000000


def sum_squares(data):
    """传数据: 参数是一整个大列表。"""
    return sum(x * x for x in data)


def sum_squares_lite(n):
    """传指令: 只传一个整数, 数据在子进程现场生成。"""
    return sum(x * x for x in range(n))


if __name__ == "__main__":
    data = list(range(N))
    payload = pickle.dumps(data)
    print("数据方案参数体积: %.1f MB" % (len(payload) / 1e6))
    print("指令方案参数体积: 0.0 MB (一个 int)")

    with Pool(2) as pool:
        t0 = time.perf_counter()
        r1 = pool.apply(sum_squares, (data,))
        tax_time = time.perf_counter() - t0

        t0 = time.perf_counter()
        r2 = pool.apply(sum_squares_lite, (N,))
        lite_time = time.perf_counter() - t0

    print("传数据: 结果=%s, 耗时 %.2fs" % (r1, tax_time))
    print("传指令: 结果=%s, 耗时 %.2fs" % (r2, lite_time))
    print("结果一致:", r1 == r2, "/ 指令方案提速 %.1f 倍"
          % (tax_time / lite_time))
