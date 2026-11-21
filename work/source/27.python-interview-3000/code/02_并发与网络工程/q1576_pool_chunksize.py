"""进程池 map 的分片账: chunksize 决定负载是否均匀。

Pool 内部有中央任务队列, worker 做完一件就领下一件, 但一次领的是"一整块":
块内串行、块是调度最小单位。重活被捆进同一大块时, 领到重块的 worker
独自加班, 其他 worker 提前收工。chunksize=1 让每件任务独立成块,
排队领取自然均衡, 代价是更高的分发开销。
"""
import multiprocessing as mp
import time

HEAVY = {4, 5, 6, 7, 12, 13, 14, 20, 21, 22}      # 重活按块边界聚集


def work(i):
    time.sleep(1.5 if i in HEAVY else 0.02)
    return i * i


def main():
    items = list(range(24))

    t0 = time.monotonic()
    with mp.Pool(4) as pool:
        pool.map(work, items, chunksize=8)    # 大块: 三件重活捆在一块
    t_chunk = time.monotonic() - t0

    t0 = time.monotonic()
    with mp.Pool(4) as pool:
        pool.map(work, items, chunksize=1)    # 单件: 领完一件再领一件
    t_single = time.monotonic() - t0

    print("chunksize=8 大块下发耗时: %.2fs" % t_chunk)
    print("chunksize=1 单件下发耗时: %.2fs" % t_single)
    assert t_single < t_chunk, "重活聚集成块时应是小分片更快"
    print("结论: 块是调度最小单位, 任务耗时不均用小分片; 极轻任务用大分片省开销")


if __name__ == "__main__":
    main()
