try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    print("标准库演示:日期归入账期")
    from datetime import date
    for d in (date(2026, 2, 20), date(2026, 3, 1)):
        print(d, "->", f"{d.year}-{d.month:02d}")
else:
    q = pd.period_range("2026Q1", periods=4, freq="Q")
    print("季度:", q.tolist())
    print("季度 -> 期初月:", q.asfreq("M", how="start").tolist())
    print("Q1 期末时刻:", q[0].to_timestamp(how="end"))
    ts = pd.Timestamp("2026-03-15")
    print("时刻 -> 月账期:", ts.to_period("M"), "季账期:", ts.to_period("Q"))
