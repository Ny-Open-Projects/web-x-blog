try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    ts = pd.Series(pd.to_datetime([
        "2026-01-01 08:00:00", "2026-06-01 08:00:00"]))
    s_utc = ts.dt.tz_localize("UTC")           # 赋予时区
    print(s_utc.dt.tz_convert("Asia/Shanghai").tolist())
    # 混合时区字符串解析:统一到 UTC
    mixed = pd.Series(["2026-01-01 08:00+08:00", "2026-01-01 00:00+00:00"])
    parsed = pd.to_datetime(mixed, format="ISO8601", utc=True)
    print(parsed.tolist())

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        from datetime import datetime, timezone, timedelta
        dt = datetime(2026, 1, 1, 8, 0, tzinfo=timezone(timedelta(hours=8)))
        print(dt.astimezone(timezone.utc).isoformat())  # localize/convert 等价
