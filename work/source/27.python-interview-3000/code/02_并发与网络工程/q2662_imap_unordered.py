# -*- coding: utf-8 -*-
"""imap_unordered 的完成序实测: 先跑完的先回来。

- map/imap: 结果严格按提交序产出, 慢任务挡住后面所有快任务的交付;
- imap_unordered: 谁先完成谁先产出, 长尾任务不再阻塞整批;
- 代价: 结果与输入的对应关系要自己带着编号走。
"""
import multiprocessing as mp
import time

WORKERS = 4


def job(i):
    """0 号是长尾: 睡 1.0s; 其余都是 0.05s 的快任务。"""
    time.sleep(1.0 if i == 0 else 0.05)
    return i


if __name__ == "__main__":
    with mp.Pool(WORKERS) as pool:
        pool.map(int, range(4))          # 预热: 排除 worker 启动噪声

        t0 = time.perf_counter()
        first_unordered = None
        arrival = []
        for r in pool.imap_unordered(job, range(12)):
            if first_unordered is None:
                first_unordered = time.perf_counter() - t0
            arrival.append(r)
        t_unordered = time.perf_counter() - t0

        t0 = time.perf_counter()
        first_ordered = None
        in_order = []
        for r in pool.imap(job, range(12)):
            if first_ordered is None:
                first_ordered = time.perf_counter() - t0
            in_order.append(r)
        t_ordered = time.perf_counter() - t0

    print("imap_unordered 到达序:", arrival)
    print("imap         到达序:", in_order)
    print("首个结果延迟: unordered %.2fs vs ordered %.2fs"
          % (first_unordered, first_ordered))
    print("总耗时:       unordered %.2fs vs ordered %.2fs"
          % (t_unordered, t_ordered))
    print("unordered 期间快结果已陆续交付, 长尾只在最后收一次")
