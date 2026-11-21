try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    idx = pd.date_range("2026-01-01 00:00", periods=60, freq="min")
    df = pd.DataFrame({"req": np.arange(60)}, index=idx)
    down = df.resample("5min").agg(req_sum=("req", "sum"),
                                   req_max=("req", "max"))
    print(down)                          # 下采样:5 分钟窗口
    up = df.resample("30s").ffill()
    print(len(up), "rows after upsample")  # 上采样 + 前向填充

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        from collections import defaultdict
        buckets = defaultdict(int)
        for minute in range(60):         # 5 分钟窗口求和
            buckets[minute // 5 * 5] += minute
        print(dict(sorted(buckets.items())))
