"""从日请求量倒推峰值 QPS(纯标准库)。"""


def peak_qps(daily_requests, peak_hour_ratio=0.10, minute_factor=3.0):
    hour_qps = daily_requests * peak_hour_ratio / 3600
    return round(hour_qps * minute_factor)


print("日请求 500 万 ->", peak_qps(5_000_000), "QPS 设计值")
print("日请求 50 万 ->", peak_qps(500_000), "QPS 设计值")
print("大促 10 倍日量 ->", peak_qps(50_000_000), "QPS 设计值")
print("建议:按设计值做阶梯压测,确认延迟拐点高于它")
