try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from datetime import date
    values = {date(2026, 1, 5): 10, date(2026, 1, 11): 20, date(2026, 1, 12): 30}
    # 周一起点口径:01-05 属于 01-05 那周,01-12 起新周
    print("01-05 与 01-11 同周,01-12 开新周")
    print({str(k): v for k, v in values.items()})
else:
    s = pd.Series(
        range(1, 15),
        index=pd.date_range("2026-01-05", periods=14, freq="D"),  # 01-05 是周一
    )
    print("默认 W-SUN 标签在周日:")
    print(s.resample("W-SUN").sum(), end="\n\n")
    print("周一起点,label=left 标签在周一:")
    print(s.resample("W-MON", label="left").sum())
