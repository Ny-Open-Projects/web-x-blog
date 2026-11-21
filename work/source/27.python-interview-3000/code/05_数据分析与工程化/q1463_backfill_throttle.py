"""回填限速:令牌桶控制回填吞吐,优先级队列保证实时任务先走"""

import heapq
import itertools

BUCKET_CAPACITY = 3      # 每个调度周期可用的回填令牌数
REFILL_PER_TICK = 2

JOBS = [
    # 优先级数字越小越先执行, 0=实时 5=回填, 任务名, 耗时令牌
    (0, "rt_dashboard", 1),
    (5, "bf_2024_01", 2),
    (5, "bf_2024_02", 2),
    (0, "rt_alert", 1),
    (5, "bf_2024_03", 1),
]


def scheduler(jobs, ticks=4):
    tokens = BUCKET_CAPACITY
    seq = itertools.count()
    heap = [(p, next(seq), name, cost) for p, name, cost in jobs]
    heapq.heapify(heap)
    executed, deferred = [], []
    for _ in range(ticks):
        tokens = min(BUCKET_CAPACITY, tokens + REFILL_PER_TICK) if _ else tokens
        progressed = True
        while progressed and heap:
            progressed = False
            candidates = []
            while heap:
                candidates.append(heapq.heappop(heap))
            for idx, (p, _, name, cost) in enumerate(candidates):
                if p == 0 or cost <= tokens:
                    if p == 0:
                        executed.append(name)       # 实时任务不受令牌限制
                    else:
                        tokens -= cost
                        executed.append(name)
                    candidates = candidates[:idx] + candidates[idx + 1:]
                    progressed = True
                    break
            for item in candidates:
                heapq.heappush(heap, item)
        else:
            break
    while heap:
        deferred.append(heapq.heappop(heap)[2])
    return executed, deferred


if __name__ == "__main__":
    executed, deferred = scheduler(JOBS)
    print("执行顺序:", executed)
    print("延后执行:", deferred)
    print("要点:回填永远让路实时,限速用令牌桶而不要拍脑袋 sleep")
