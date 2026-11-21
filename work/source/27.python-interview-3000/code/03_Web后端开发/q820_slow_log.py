
lat = [12, 15, 11, 300, 14, 900, 13, 16, 12, 14]
lat.sort()

def percentile(data: list, p: int) -> float:
    k = max(0, min(len(data) - 1, int(round(p / 100 * (len(data) - 1)))))
    return data[k]

print("p50:", percentile(lat, 50))
print("p95:", percentile(lat, 95))
print("p99:", percentile(lat, 99))
print("慢请求样本:", [x for x in lat if x > 200])
