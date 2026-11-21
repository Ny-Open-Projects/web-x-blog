try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    values = [10.0, 11.0, 11.0, 30.0, 12.0]
    alpha = 0.5
    ema = values[0]
    for v in values:
        ema = alpha * v + (1 - alpha) * ema
        print(round(ema, 2), end=" ")
    print("\n标准库递推即 adjust=False 语义")
else:
    s = pd.Series([10, 11, 11, 30, 12], dtype="float64")
    out = pd.DataFrame({
        "raw": s,
        "ewm_span4": s.ewm(span=4, adjust=False).mean().round(2),
        "ewm_hl2": s.ewm(halflife=2).mean().round(2),
        "sma3": s.rolling(3, min_periods=1).mean().round(2),
    })
    print(out)
