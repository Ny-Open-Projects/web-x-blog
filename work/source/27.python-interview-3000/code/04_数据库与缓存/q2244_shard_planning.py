"""分片数规划: 容量与吞吐双约束取最大, 向上取 2 的幂"""

def plan_shards(total_rows, rows_per_shard, peak_qps, qps_per_shard):
    by_cap = -(-total_rows // rows_per_shard)      # 向上取整
    by_qps = -(-peak_qps // qps_per_shard)
    n = max(by_cap, by_qps)
    p = 1
    while p < n:
        p <<= 1
    return by_cap, by_qps, p

scenarios = [("今天",   200000000, 2000000, 50000, 8000),
             ("一年后", 800000000, 2000000, 150000, 8000),
             ("三年后", 3000000000, 2000000, 400000, 8000)]
print("阶段     容量约束  吞吐约束  建议分片")
for name, rows_, rps, qps, qpsp in scenarios:
    cap, thr, p = plan_shards(rows_, rps, qps, qpsp)
    print("%-4s %10d %9d %8d" % (name, cap, thr, p))
print("容量约束主导时优先做归档与治理, 分片数取 2 的幂便于翻倍扩容")
