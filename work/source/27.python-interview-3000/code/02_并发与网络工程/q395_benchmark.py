"""单机压测脚本:并发采样 + QPS + 延迟分位数。"""
import concurrent.futures as cf
import random
import statistics
import time
import urllib.request

TARGET = "https://httpbin.org/get"


def one_request():
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(TARGET, timeout=5) as resp:
            resp.read(1024)
        return time.perf_counter() - start, None
    except Exception as e:
        return time.perf_counter() - start, repr(e)


def percentile(sorted_data, p):
    if not sorted_data:
        return 0.0
    idx = min(int(len(sorted_data) * p / 100), len(sorted_data) - 1)
    return sorted_data[idx]


def benchmark(total=20, workers=5):
    with cf.ThreadPoolExecutor(max_workers=workers) as pool:
        results = list(pool.map(lambda _: one_request(), range(total)))
    latencies = sorted(d for d, _ in results)
    errors = [e for _, e in results if e]
    duration = sum(latencies)  # 近似总时间(串行累加口径, 单机粗估)
    qps = total / (sum(latencies) / workers) if workers else 0
    print(f"请求数 {total} 并发 {workers} 错误 {len(errors)}")
    print(f"avg {statistics.mean(latencies)*1000:.0f}ms "
          f"p50 {percentile(latencies, 50)*1000:.0f}ms "
          f"p95 {percentile(latencies, 95)*1000:.0f}ms "
          f"p99 {percentile(latencies, 99)*1000:.0f}ms")
    print(f"估算 QPS ~ {qps:.1f}")
    if errors:
        print("错误示例:", errors[0])


if __name__ == "__main__":
    benchmark(total=20, workers=5)
