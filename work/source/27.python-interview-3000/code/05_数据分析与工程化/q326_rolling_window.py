try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False                      # 未装 pandas: 走下面的纯手写降级路径

def demo_pandas():
    idx = pd.date_range("2026-01-01", periods=14, freq="D")
    s = pd.Series(np.arange(1, 15, dtype=float), index=idx)
    print(s.rolling(7, min_periods=3).mean().round(2).tolist())
    print(s.expanding().sum().tail(3).tolist())
    # 按时间窗口:适合有不连续日期的表
    print(s.rolling("7D").mean().round(2).tail(3).tolist())

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        vals = list(range(1, 15))
        for i in range(len(vals)):       # 7 日滚动均值的朴素实现
            win = vals[max(0, i - 6): i + 1]
            print(round(sum(win) / len(win), 2))
