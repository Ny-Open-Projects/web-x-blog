try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    df = pd.DataFrame({
        "ts": pd.date_range("2026-01-01", periods=6, freq="D"),
        "amount": [100, np.nan, np.nan, 160, np.nan, 200],
        "city": ["BJ", None, "SH", None, "SZ", "BJ"],
    })
    print(df.dropna(subset=["city"]).shape)          # 按关键列删
    print(df["amount"].fillna(0).tolist())           # 业务填 0
    print(df["amount"].ffill().tolist())             # 时序向前填充
    print(df["amount"].interpolate().round(1).tolist())  # 线性插值
    print(df.assign(city=df["city"].fillna("unknown")).isna().sum().to_dict())

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        amounts = [100, None, None, 160, None, 200]
        filled = []
        last = None
        for v in amounts:            # ffill 的标准库等价实现
            if v is not None:
                last = v
            filled.append(last)
        print("ffill:", filled)
        print("fill 0:", [0 if v is None else v for v in amounts])
