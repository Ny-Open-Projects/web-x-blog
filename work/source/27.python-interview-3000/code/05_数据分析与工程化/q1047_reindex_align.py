try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    a = {"01-01": 10, "01-02": 20, "01-05": 50}
    b = {"01-01": 2, "01-03": 3, "01-05": 5}
    days = ["01-01", "01-02", "01-03", "01-04", "01-05"]
    for d in days:
        print(d, "a =", a.get(d), "b =", b.get(d))
else:
    a = pd.Series([10, 20, 50], index=pd.to_datetime(["2026-01-01", "2026-01-02", "2026-01-05"]))
    b = pd.Series([2, 3, 5], index=pd.to_datetime(["2026-01-01", "2026-01-03", "2026-01-05"]))
    full = pd.date_range("2026-01-01", "2026-01-05")
    a2 = a.reindex(full, method="ffill")
    b2 = b.reindex(full)
    print(pd.DataFrame({"a_ffill": a2, "b_raw": b2, "ratio": (a2 / b2).round(2)}))
