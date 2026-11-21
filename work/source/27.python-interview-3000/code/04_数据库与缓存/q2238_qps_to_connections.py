"""QPS 到连接数: Little 定律换算加峰值与安全系数"""

def connections_needed(qps, avg_latency_ms, peak_factor=3.0, safety=1.5):
    concurrency = qps * avg_latency_ms / 1000.0     # 平均并发 = QPS x 占用时长
    return concurrency * peak_factor * safety, concurrency

rows = [("点查    ", 3000, 2.0),
        ("列表页  ", 800, 30.0),
        ("复杂报表", 50, 2000.0)]
print("场景       QPS   平均延迟ms  均值并发  建议连接数")
total = 0.0
for name, qps, lat in rows:
    need, avg = connections_needed(qps, lat)
    total += need
    print("%s %6d %8.0f %10.1f %10.0f" % (name, qps, lat, avg, need))
print("合计建议 %.0f 个连接, 还要对照 max_connections 与每连接内存成本" % total)
print("并发上涨先查占用时长: 长事务与慢查询才是元凶, 加连接只是推迟雪崩")
