"""BFF 并行聚合: 整体 deadline、单源超时与降级(标准库线程池)。"""
import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeout


def upstream(name, seconds, payload):
    time.sleep(seconds)
    return payload


def aggregate(deadline=0.4):
    calls = {
        "order": (0.10, {"id": "ord_1", "status": "paid"}),
        "recommend": (0.60, {"items": ["A1"]}),      # 超过容忍阈值 -> 降级
        "profile": (0.15, {"nickname": "王工"}),
    }
    pool = ThreadPoolExecutor(max_workers=len(calls))
    futures = {k: pool.submit(upstream, k, s, p) for k, (s, p) in calls.items()}
    data, degraded = {}, []
    for key, fut in futures.items():
        try:
            data[key] = fut.result(timeout=deadline)
        except FutureTimeout:
            degraded.append(key)
            data[key] = {"degraded": True}            # 缺省兜底, 页面照样能开
    pool.shutdown(wait=False)
    return data, degraded


data, degraded = aggregate()
print("聚合结果:", data)
print("降级源:", degraded)
print("要点: BFF 的 deadline 要小于端上超时留出传输余量; 降级要在响应里显式标注, 不许静默吞掉")
