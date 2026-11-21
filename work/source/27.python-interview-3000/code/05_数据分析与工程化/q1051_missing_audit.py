try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    values = [1.0, None, None, 4.0, None, 6.0]
    last = None
    ffill = []
    for v in values:
        if v is not None:
            last = v
        ffill.append(last)
    print("前向填充:", ffill)
    print("缺失率:", sum(v is None for v in values) / len(values))
else:
    s = pd.Series(
        [1.0, None, None, 4.0, None, 6.0],
        index=pd.date_range("2026-01-01", periods=6, freq="D"),
    )
    print("缺失率:", round(s.isna().mean(), 3))
    print("ffill:", s.ffill().tolist())
    print("时间插值:", s.interpolate(method="time").round(2).tolist())
    print("限插 1 期:", s.interpolate(limit=1).tolist())
