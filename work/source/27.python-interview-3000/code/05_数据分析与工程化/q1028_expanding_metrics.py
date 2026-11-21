try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    values = [10, 12, 9, 15]
    run_sum = run_max = 0
    for i, v in enumerate(values):
        run_sum += v
        run_max = max(run_max, v)
        print(f"day{i} 累计 {run_sum} 历史最高 {run_max} 是否新高 {v == run_max}")
else:
    s = pd.Series([10, 12, 9, 15], index=pd.date_range("2026-01-01", periods=4, freq="D"))
    out = pd.DataFrame({
        "gmv": s,
        "cum_gmv": s.expanding().sum(),
        "cum_avg": s.expanding().mean().round(2),
        "hist_max": s.expanding().max(),
    })
    out["is_record"] = s >= out["hist_max"]
    print(out)
    # CUSUM 累积偏移,常用于漂移监控
    print("cusum:", s.sub(s.mean()).cumsum().round(2).tolist())
