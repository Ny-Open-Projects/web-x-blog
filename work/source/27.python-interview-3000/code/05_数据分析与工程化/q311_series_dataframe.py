try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    s = pd.Series([10, 20, 30], index=["a", "b", "c"], name="score")
    df = pd.DataFrame({
        "city": ["BJ", "SH", "SZ"],
        "score": [88, 92, 79],
    }, index=["r1", "r2", "r3"])
    print(type(s.values), s.dtype, s.index.tolist())
    print(df.shape, df.columns.tolist(), df.dtypes.to_dict())
    print(df["score"])          # 取出一列就是 Series

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        # 标准库降级:Series 概念上就是 值 + 标签索引 的组合
        series = dict(zip(["a", "b", "c"], [10, 20, 30]))
        dataframe = {"city": ["BJ", "SH", "SZ"], "score": [88, 92, 79]}
        print("Series-like:", series)
        print("DataFrame-like columns:", {k: len(v) for k, v in dataframe.items()})
