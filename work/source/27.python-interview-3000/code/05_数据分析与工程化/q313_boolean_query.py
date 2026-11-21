try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    df = pd.DataFrame({"a": [1, 5, 10, 15], "b": [2, 3, 4, 5], "c": list("abcd")})
    mask = (df["a"] > 2) & (df["b"] < 5)
    print(df[mask]["c"].tolist())              # 布尔索引
    print(df.query("a > 2 and b < 5")["c"].tolist())
    threshold = 10
    print(df.query("a > @threshold")["c"].tolist())  # 引用外部变量
    print(df[~df["c"].isin(["a", "b"])]["c"].tolist())  # 取反 + isin

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        rows = [{"a": 1, "b": 2, "c": "a"}, {"a": 5, "b": 3, "c": "b"},
                {"a": 10, "b": 4, "c": "c"}, {"a": 15, "b": 5, "c": "d"}]
        print([r["c"] for r in rows if r["a"] > 2 and r["b"] < 5])
