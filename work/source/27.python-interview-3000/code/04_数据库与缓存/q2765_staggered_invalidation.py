"""批量失效的错峰实测: 同刻删除把回源挤成尖峰, 随机散布削平"""
import random
from collections import Counter

random.seed(42)
N, BACKFILL_MS, TICK_MS, WINDOW_MS = 1000, 20.0, 50.0, 2000.0

def profile(label, delays):
    loads = Counter(int(d // TICK_MS) for d in delays)
    peak = max(loads.values())
    total_ticks = max(loads) + 1
    avg = N / total_ticks
    print("%s: %d 个 tick, 峰值单 tick 回源 %d 个 (约 %.0f ms 回源压力), 均值 %.0f 个"
          % (label, total_ticks, peak, peak * BACKFILL_MS, avg))

profile("同刻失效", [0.0] * N)
profile("错峰失效", [random.uniform(0, WINDOW_MS) for _ in range(N)])
print("错峰的本质: 把确定性尖峰摊成背景噪音, 代价是失效完成时间从 0 变成窗口长")
