"""综合演练: 上游变慢引发的超时雪崩与止血(纯标准库模拟)。"""


def simulate(latencies, pool_size, timeout_ms, queue_wait_limit_ms=1000.0,
             arrival_gap_ms=10.0):
    """槽位模型: 每个请求占用一个 worker 槽至完成或超时, 超限即网关拒绝。"""
    slot_free = [0.0] * pool_size
    stats = {"ok": 0, "timeout": 0, "rejected": 0, "max_wait": 0.0}
    for i, lat in enumerate(latencies):
        arrive = i * arrival_gap_ms
        slot = min(range(pool_size), key=lambda k: slot_free[k])
        start = max(arrive, slot_free[slot])
        wait = start - arrive
        stats["max_wait"] = max(stats["max_wait"], wait)
        if wait > queue_wait_limit_ms:
            stats["rejected"] += 1               # 排队过久, 网关直接 502
            continue
        if lat > timeout_ms:
            stats["timeout"] += 1                # 上游超时, 占槽 timeout_ms 后释放
            slot_free[slot] = start + timeout_ms
        else:
            stats["ok"] += 1
            slot_free[slot] = start + lat
    return stats


LATENCIES = [50.0] * 10 + [800.0] * 10 + [3000.0] * 20
POOL = 4
GAP = 100.0                                        # 每 100ms 到达一个请求

no_timeout = simulate(LATENCIES, POOL, timeout_ms=60000.0, arrival_gap_ms=GAP)
with_timeout = simulate(LATENCIES, POOL, timeout_ms=300.0, arrival_gap_ms=GAP)

print("无上游超时 timeout=60s:", no_timeout)
print("有上游超时 timeout=300ms:", with_timeout)

assert no_timeout["rejected"] > 0, "无超时止血时必然出现排队溢出"
assert with_timeout["rejected"] == 0, "快速超时让槽位回收, 队列不再堆积"
assert with_timeout["timeout"] == 30 and with_timeout["ok"] == 10
assert no_timeout["max_wait"] > with_timeout["max_wait"]

print()
print("因果链: 上游变慢 -> worker 槽被占满 -> 后续请求排队 -> 排队超过网关容忍 -> 502 面扩大")
print("止血链: 上游调用设 300ms 超时 -> 槽位按时回收 -> 队列不堆积 -> 错误快速可见且可重试")
verdict = ("止血有效: 牺牲部分超时数, 换取零排队溢出与更小的最大等待"
           if with_timeout["rejected"] < no_timeout["rejected"] else "参数仍需调整")
print("判定:", verdict)
print("要点: 雪崩的本质是 慢 把资源池拖穿, 止血靠三件套 上游超时 池上限 快速失败, "
      "超时预算要逐层对齐, 让最上游先于网关放弃")
