try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from datetime import datetime
    raw = ["2026-01-05", "2026/01/06", "not-a-date"]
    for v in raw:
        try:
            print(v, "->", datetime.strptime(v, "%Y-%m-%d").date())
        except ValueError:
            try:
                print(v, "->", datetime.strptime(v, "%Y/%m/%d").date())
            except ValueError:
                print(v, "-> NaT(脏数据进审计表)")
else:
    raw = pd.Series(["2026-01-05", "2026/01/06", "05-01-2026", "not-a-date"])
    parsed = pd.to_datetime(raw, errors="coerce")
    out = pd.DataFrame({"raw": raw, "parsed": parsed})
    print(out)
    print("脏值数量:", parsed.isna().sum())
    print("显式 format 提示:01-05 这类要用 dayfirst 与来源方约定")
