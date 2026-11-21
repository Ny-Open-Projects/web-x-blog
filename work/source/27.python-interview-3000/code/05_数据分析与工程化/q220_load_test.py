import statistics
import random


def percentile(sorted_lat: list[float], p: float) -> float:
    if not sorted_lat:
        return 0.0
    k = max(0, min(len(sorted_lat) - 1, int(len(sorted_lat) * p / 100)))
    return sorted_lat[k]


def summarize(latencies: list[float]) -> dict:
    s = sorted(latencies)
    return {
        "qps_like": round(len(s) / max(s) * 100, 2) if s else 0,
        "p50": percentile(s, 50),
        "p99": percentile(s, 99),
        "max": s[-1] if s else 0,
    }


def test_p99_not_hidden_by_average():
    data = [10.0] * 99 + [900.0]  # 长尾:平均值 18ms,p99 却很高
    r = summarize(data)
    assert statistics.mean(data) < 20
    assert r["p99"] == 900.0
