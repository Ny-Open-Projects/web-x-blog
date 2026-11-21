try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    import bisect
    quotes = [(10, 9.9), (20, 10.1), (40, 10.4)]
    times = [t for t, _ in quotes]
    for trade_t in (12, 25, 45):
        i = bisect.bisect_right(times, trade_t) - 1
        if i >= 0:
            print(f"成交 {trade_t}s 匹配报价 {quotes[i]}")
else:
    quotes = pd.DataFrame({
        "ts": pd.to_datetime(["10:00:00", "10:00:20", "10:00:40"]),
        "price": [9.9, 10.1, 10.4],
    }).sort_values("ts")
    trades = pd.DataFrame({
        "ts": pd.to_datetime(["10:00:12", "10:00:25", "10:00:45"]),
        "qty": [100, 200, 50],
    }).sort_values("ts")
    m = pd.merge_asof(trades, quotes, on="ts", direction="backward", tolerance=pd.Timedelta("30s"))
    print(m)
