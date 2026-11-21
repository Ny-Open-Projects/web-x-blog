try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from datetime import datetime
    stamps = [datetime(2026, 1, 1, h) for h in (8, 10, 12, 23, 1)]
    for t in stamps:
        ok = 9 <= t.hour <= 18
        print(t.strftime("%H:%M"), "营业时段" if ok else "非营业时段")
else:
    s = pd.Series(range(24), index=pd.date_range("2026-01-01", periods=24, freq="h"))
    print("营业时段行数:", len(s.between_time("09:00", "18:00")))
    print(s.at_time("12:00"), end="\n\n")
    print("跨零点 22 点到次日 2 点:", s.between_time("22:00", "02:00").index.strftime("%H:%M").tolist())
