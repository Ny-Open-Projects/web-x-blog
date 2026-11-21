try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False

def build_features(df):
    # 分箱:等频分 3 档
    df["amt_bin"] = pd.qcut(df["amt"], q=3, labels=["low", "mid", "high"])
    # 独热
    df = pd.get_dummies(df, columns=["city"], prefix="city")
    # 滞后特征:按用户按时间组内 shift,防泄露
    df = df.sort_values(["uid", "ts"])
    df["amt_prev"] = df.groupby("uid")["amt"].shift(1)
    df["amt_diff"] = df["amt"] - df["amt_prev"]
    return df

if __name__ == "__main__":
    if PANDAS:
        df = pd.DataFrame({
            "uid": [1, 1, 2, 2, 1],
            "ts": pd.to_datetime(["2026-01-01", "2026-01-02",
                                  "2026-01-01", "2026-01-02", "2026-01-03"]),
            "city": ["BJ", "BJ", "SH", "SH", "BJ"],
            "amt": [10.0, 30.0, 20.0, 25.0, 50.0],
        })
        print(build_features(df))
    else:
        print("标准库思路:排序后用 zip(cur, prev) 构造滞后列,分箱用边界列表判断")
