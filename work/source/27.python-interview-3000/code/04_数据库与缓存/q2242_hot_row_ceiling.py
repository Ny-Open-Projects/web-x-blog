"""热点行写入天花板: 行锁串行化, 分桶是唯一出路"""
import random

def ceiling_qps(lock_ms, buckets=1):
    """单行持锁 L 毫秒 -> 每秒最多 1000/L 次, 分桶乘 N"""
    return 1000.0 / lock_ms * buckets

print("单行持锁 5ms -> 该行写入上限 %.0f QPS, 与实例数无关" % ceiling_qps(5))
for b in (1, 10, 100):
    print("拆成 %3d 个桶 -> 上限 %6.0f QPS" % (b, ceiling_qps(5, b)))

random.seed(1)
BUCKETS, ops = 10, 1000
counts = [0] * BUCKETS
for _ in range(ops):
    counts[random.randrange(BUCKETS)] += 1
print("均匀散列下最热桶承担 %d%% 写, 接近线性打散" % (max(counts) * 100 // ops))
print("代价: 读要聚合全桶 扣减要挑桶重试防负余额 一致性窗口等于聚合周期")
