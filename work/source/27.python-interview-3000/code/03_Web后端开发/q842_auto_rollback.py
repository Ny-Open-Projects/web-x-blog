
def decide(metrics: dict, thresholds: dict) -> str:
    if metrics["error_rate"] > thresholds["error_rate"]:
        return "回滚: 错误率超标"
    if metrics["p99_ms"] > thresholds["p99_ms"]:
        return "回滚: 延迟超标"
    if metrics["sample_count"] < thresholds["min_sample"]:
        return "继续观察: 样本不足"
    return "放量"

th = {"error_rate": 0.01, "p99_ms": 800, "min_sample": 100}
print(decide({"error_rate": 0.002, "p99_ms": 500, "sample_count": 500}, th))
print(decide({"error_rate": 0.05, "p99_ms": 500, "sample_count": 500}, th))
print(decide({"error_rate": 0.002, "p99_ms": 500, "sample_count": 10}, th))
