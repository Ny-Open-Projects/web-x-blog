---
title: [Q1576] 进程池 map 的分片账:chunksize 与负载不均
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1576 · 进程池 map 的分片账:chunksize 与负载不均

> 难度:★★☆☆ | 标签:multiprocessing, chunksize, 负载均衡

**问**:Pool.map 传了 24 个任务,4 个 worker,有个 worker 明显比别的慢一倍——和 chunksize 什么关系?

**答**:map 把任务按 chunksize 切成块,块是调度最小单位:worker 做完一整块才能领下一块,块内任务串行执行。默认 chunksize 按 ceil(n/(4*workers)) 算,24 任务 4 worker 是 2;如果重活恰好被捆进同一大块,领到重块的 worker 独自加班,其他 worker 提前收工。chunksize=1 让每件任务独立成块,worker 领完一件再领一件,负载自然均衡,代价是任务分发消息变多。经验:任务耗时不均(IO 调用、大小不一的文件)用小分片;任务极轻(微秒级计算)用大分片省分发开销。

```python
# file: code/02_并发与网络工程/q1576_pool_chunksize.py
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
```

**追问**:1) imap 和 map 谁更均衡?——map 把块塞进共享任务队列由 worker 动态领取;imap 是轮询分发,chunksize=1 也不保证动态均衡。2) map 与 imap 的调度差异的本质?——map 一次性把所有块丢进任务队列,worker 动态领取(领取即平衡);imap 按 chunksize 轮询分发,分发顺序固定,chunksize=1 才接近逐件分发;「动态领取」是负载均衡的关键,不是「分得小」就行。3) chunksize 怎么定量选?——粗估公式 chunksize ≈ n/(4×workers) 是「分发开销与均衡性」的折中起点;任务耗时方差大时直接 chunksize=1;任务极轻时大分片省 IPC——再以 worker 完成时间方差实测校准(各 worker 完成时间应接近)。4) 生产陷阱?——重活聚集在同一块(见原问);任务函数带大闭包,pickle 开销淹没计算;用 map 处理「任务间有顺序依赖」(进程池无共享状态,依赖要先拆解);异常在某个 chunk 里爆出后整批 map 中断,已完成的白算。

---
