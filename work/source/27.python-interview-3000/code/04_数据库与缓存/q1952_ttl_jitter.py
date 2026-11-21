"""多级 TTL 抖动: 过期散布与回源峰值实测"""
import random
import statistics

random.seed(42)

def expiry_times(n, base, jitter):
    """jitter 为 0 全部同一时刻过期; 大于 0 时过期点均匀散布在 base 到 base 加 jitter"""
    return [base + random.random() * jitter for _ in range(n)]

def max_overlap(expiries, window=1.0):
    """同一 window 秒内同时过期的最大数量 近似雪崩强度"""
    expiries = sorted(expiries)
    best, j = 0, 0
    for i in range(len(expiries)):
        while expiries[j] < expiries[i] - window:
            j += 1
        best = max(best, i - j + 1)
    return best

n = 5000
same = expiry_times(n, 300, 0)
uni = expiry_times(n, 300, 60)      # L2 redis: 基础 300 秒加 0 到 60 秒抖动
n_l1 = 800                          # L1 只放热点子集 量级远小于 L2
l1 = expiry_times(n_l1, 30, 10)     # L1 本地: 基础 30 秒加 0 到 10 秒抖动
print("无抖动         最大同窗过期:", max_overlap(same), "/ 5000")
print("均匀抖动 60 秒 最大同窗过期:", max_overlap(uni), "/ 5000")
print("L1 热点子集    最大同窗过期:", max_overlap(l1), "/ 800")

stdev = statistics.pstdev(uni)
print(f"均匀抖动的过期点标准差 {stdev:.1f} 秒 过期从脉冲变成均匀雨")

def refill_rate(expiries, total_seconds=380):
    counts = [0] * total_seconds
    for e in expiries:
        counts[int(e)] += 1
    return max(counts), sum(counts) / total_seconds

print("无抖动   峰值回源每秒:", refill_rate(same)[0])
peak, avg = refill_rate(uni)
print(f"均匀抖动 峰值回源每秒: {peak}  平均 {avg:.1f} 削峰 {refill_rate(same)[0] / peak:.0f} 倍")
print("结论: TTL 必须加抖动把过期打散 多级缓存把一次雪崩拆成两级小峰 L1 的 TTL 与抖动都要小于 L2")
