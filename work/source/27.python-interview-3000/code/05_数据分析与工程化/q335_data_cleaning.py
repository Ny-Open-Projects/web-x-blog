try:
    import pandas as pd
    import numpy as np
    PANDAS = True
except ImportError:
    PANDAS = False

def clean(df):
    n0 = len(df)
    # 1 格式归一
    df["city"] = df["city"].str.strip().str.upper()
    df["amt"] = pd.to_numeric(df["amt"], errors="coerce")
    # 2 按业务键去重
    df = df.drop_duplicates(subset=["order_id"], keep="last")
    # 3 IQR 标记异常值(标记而非删除)
    q1, q3 = df["amt"].quantile([0.25, 0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    df["amt_outlier"] = (df["amt"] < lo) | (df["amt"] > hi)
    print(f"rows {n0} -> {len(df)}, outliers={int(df['amt_outlier'].sum())}")
    return df

if __name__ == "__main__":
    if PANDAS:
        df = pd.DataFrame({
            "order_id": [1, 2, 2, 3, 4],
            "city": [" BJ", "sh", " SZ ", "BJ", "gz"],
            "amt": ["10", "20", "20", "9999", "5"],
        })
        print(clean(df))
    else:
        rows = [(1, "BJ", 10), (2, "SH", 20), (2, "SH", 20), (3, "BJ", 9999)]
        seen, cleaned = set(), []
        for oid, city, amt in rows:      # 去重的标准库等价
            if oid not in seen:
                seen.add(oid)
                cleaned.append((oid, city.strip().upper(), amt))
        vals = sorted(c[2] for c in cleaned)
        q1, q3 = vals[len(vals) // 4], vals[3 * len(vals) // 4]
        iqr = q3 - q1
        for oid, city, amt in cleaned:
            flag = amt < q1 - 1.5 * iqr or amt > q3 + 1.5 * iqr
            print(oid, city, amt, "outlier" if flag else "ok")
