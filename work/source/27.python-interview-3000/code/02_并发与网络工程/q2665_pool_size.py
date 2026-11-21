# -*- coding: utf-8 -*-
"""池大小的实测标定: 核数翻倍的收益递减曲线。

- CPU 密集任务的池大小不该拍脑袋, 应该实测加速比曲线;
- 物理 core 之前接近线性, 超线程之后收益骤减甚至回落;
- 标定方法: 固定任务总量, 从 1 倍核数爬到 2 倍, 记录墙钟时间。
"""
import multiprocessing as mp
import os
import time


def burn(n):
    x = 0
    for i in range(n):
        x = (x * 31 + i) % 1000003
    return x


if __name__ == "__main__":
    TASKS = 8
    N = 1200000
    cores = os.cpu_count()
    print("os.cpu_count() =", cores)

    t0 = time.perf_counter()
    burn(N)
    single = time.perf_counter() - t0
    print("单任务耗时: %.2fs -> 任务总量约 %.1fs 核时" % (single, TASKS * single))

    print("%-8s %-12s %-8s" % ("workers", "wall", "speedup"))
    best = None
    for w in (1, 2, 4, 8):
        with mp.Pool(w) as pool:
            t0 = time.perf_counter()
            pool.map(burn, [N] * TASKS)
            wall = time.perf_counter() - t0
        speedup = TASKS * single / wall
        print("%-8d %-12s %.2fx" % (w, "%.2fs" % wall, speedup))
        if best is None or wall < best[1]:
            best = (w, wall)
    print("实测最优池大小: %d 个进程(cpu_count 只能当起点, 不能当结论)"
          % best[0])
