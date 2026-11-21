"""Q2838 并发工具的竞速聚合:预算内前 k 个成功结果先到先得。

多个等价数据源并发查询时,不必等全员返回:设定预算和需要的成功数 k,
谁先成功用谁,凑够 k 个立刻收摊,慢的和失败的按失败清单留痕。相比
逐个串行重试,尾延迟从「最慢者」变成「第 k 快者」。
"""

import time
from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
    TimeoutError as FuturesTimeout,
)


def race_aggregate(jobs, want, deadline_s):
    """jobs: [(name, fn)],fn 返回值即结果或抛异常。返回 (成功, 失败)。"""
    results, failures = [], []
    ex = ThreadPoolExecutor(max_workers=len(jobs))
    try:
        futs = {ex.submit(fn): name for name, fn in jobs}
        end = time.monotonic() + deadline_s
        try:
            for fut in as_completed(futs, timeout=deadline_s):
                name = futs[fut]
                try:
                    results.append((name, fut.result()))
                    if len(results) >= want:
                        break
                except Exception as exc:
                    failures.append((name, type(exc).__name__))
        except FuturesTimeout:
            failures.append(("<deadline>", "FuturesTimeout"))
    finally:
        ex.shutdown(wait=False, cancel_futures=True)
    return sorted(results), failures, time.monotonic() < end


def slow_source():
    time.sleep(0.6)
    return "slow"


def fast_source_a():
    time.sleep(0.01)
    return "dataA"


def fast_source_b():
    time.sleep(0.03)
    return "dataB"


def broken_source():
    raise RuntimeError("源挂了")


def main():
    jobs = [
        ("slow", slow_source),
        ("fast_a", fast_source_a),
        ("fast_b", fast_source_b),
        ("broken", broken_source),
    ]
    t0 = time.monotonic()
    results, failures, within = race_aggregate(jobs, want=2, deadline_s=0.2)
    cost = time.monotonic() - t0
    assert [n for n, _ in results] == ["fast_a", "fast_b"], results
    assert ("broken", "RuntimeError") in failures, failures
    assert within is True and cost < 0.2, (within, cost)  # 没等慢源
    print("前2个成功:", results)
    print("失败留痕:", failures)
    print("耗时 %.3fs,慢源未被等待" % cost)


if __name__ == "__main__":
    main()
