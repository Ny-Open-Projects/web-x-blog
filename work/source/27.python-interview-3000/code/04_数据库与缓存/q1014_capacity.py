"""缓存容量估算: payload -> 实际内存 -> 集群规格"""

def estimate(keys, avg_value_bytes, overhead=2.0, growth_months=6,
             monthly_growth=0.05, watermark=0.7):
    payload_gb = keys * avg_value_bytes / 1024 ** 3
    real_gb = payload_gb * overhead
    future = real_gb * (1 + monthly_growth) ** growth_months
    need = future / watermark
    return {"payload": payload_gb, "real": real_gb,
            "after_growth": future, "plan_with_watermark": need}

if __name__ == "__main__":
    plan = estimate(keys=50_000_000, avg_value_bytes=200)
    for k, v in plan.items():
        print(f"{k:>20}: {v:8.1f} GB")
    print("示例规格: 6 主 6 从(每主 16GB maxmemory)可承载, 水位 70% 告警")
    print("别忘了 fork 余量: 单实例 used 控制在 10GB 内降低 RDB 卡顿")
