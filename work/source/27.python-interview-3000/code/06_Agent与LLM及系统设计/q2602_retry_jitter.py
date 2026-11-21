"""Q2602 重试风暴的抖动实测:同刻重试压垮恢复期服务。

服务恢复瞬间,所有客户端的重试定时器同时到期,请求同刻砸下来
形成二次风暴;给每客户端的退避加随机抖动,把同一时刻的重试摊开
到一段时间上,单拍峰值大幅下降。
"""
import random
from collections import Counter


def arrivals(clients, jitter, seed):
    rng = random.Random(seed)
    ticks = Counter()
    for _ in range(clients):
        d = rng.randint(0, jitter) if jitter else 0
        ticks[d] += 1
    return ticks


def main():
    n = 100
    burst = arrivals(n, jitter=0, seed=1)
    smoothed = arrivals(n, jitter=9, seed=1)
    peak_burst = max(burst.values())
    peak_smooth = max(smoothed.values())
    assert peak_burst == n, peak_burst        # 全部同刻到站
    assert peak_smooth < peak_burst, peak_smooth
    reduction = round(100 * (1 - peak_smooth / peak_burst))
    assert reduction >= 60, reduction
    print("无抖动:第 0 拍同时到站", peak_burst, "个 ← 二次风暴")
    print("加 0-9 拍抖动:单拍峰值", peak_smooth, "个 ← 削峰", reduction, "%")
    print("各拍分布:", dict(sorted(smoothed.items())))


if __name__ == "__main__":
    main()
