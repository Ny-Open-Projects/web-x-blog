"""容量评估估算器: 从行数与增长推导磁盘 水位 内存 连接数"""
GB = 1024 ** 3


def estimate(name, rows_now, daily_growth, retention_days, row_bytes,
             provisioned_gb, index_factor=1.5, replicas=2, hot_ratio=0.2,
             buffer_gb=8.0, peak_qps=5000, ms_per_query=5.0, disk_water=0.75):
    rows_peak = rows_now + daily_growth * retention_days
    data_gb = rows_peak * row_bytes * index_factor / GB      # 数据 + 索引
    disk_gb = data_gb * (1 + replicas)                       # 主从各一份
    growth_gb_day = daily_growth * row_bytes * index_factor * (1 + replicas) / GB
    used_ratio = disk_gb / provisioned_gb
    days_left = (provisioned_gb * disk_water - disk_gb) / growth_gb_day
    hot_gb = data_gb * hot_ratio
    est_hit = min(1.0, buffer_gb / hot_gb) if hot_gb else 1.0
    conns = int(peak_qps * ms_per_query / 1000 * 2)          # 2 倍安全系数
    print("[%s]" % name)
    print("  保留期峰值 %.0f 万行, 数据+索引 %.1f GB, 含副本落盘 %.1f GB"
          % (rows_peak / 1e4, data_gb, disk_gb))
    print("  磁盘水位 %.0f%%, 到 %.0f%% 水位线还剩约 %.0f 天"
          % (used_ratio * 100, disk_water * 100, days_left))
    print("  热数据 %.1f GB vs 缓冲池 %.1f GB -> %s, 估算命中率 %.0f%%"
          % (hot_gb, buffer_gb,
             "全内存" if hot_gb <= buffer_gb else "装不下", est_hit * 100))
    print("  峰值连接数约 %d (QPS %d x 单查询 %.0fms x 2 倍安全系数)"
          % (conns, peak_qps, ms_per_query))
    return {"disk_gb": disk_gb, "days_left": days_left, "conns": conns}


a = estimate("订单库 A", rows_now=8e7, daily_growth=3e5, retention_days=365,
             row_bytes=300, provisioned_gb=600)
b = estimate("日志库 B", rows_now=2e8, daily_growth=2e6, retention_days=90,
             row_bytes=800, provisioned_gb=3000, buffer_gb=16, peak_qps=800)
assert a["conns"] > 0 and b["days_left"] < a["days_left"]
print("结论: 容量三问——磁盘到水位还有几天, 热集进不进得了内存, 连接数够不够")
