try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, index=["x", "y", "z"])
    print(df.loc["y", "a"])      # 标签取单值 -> 2
    print(df.iloc[1, 0])         # 位置取单值 -> 2
    print(df.at["z", "b"])       # 标签取标量(快) -> 6
    print(df.iat[2, 1])          # 位置取标量(快) -> 6
    print(df.loc[df["a"] > 1, "b"].tolist())  # 布尔索引 + 列选择
    print(df.iloc[0:2].index.tolist())        # 位置切片左闭右开

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        rows = [{"a": 1, "b": 4}, {"a": 2, "b": 5}, {"a": 3, "b": 6}]
        labels = ["x", "y", "z"]
        print("loc y,a =", rows[labels.index("y")]["a"])
        print("iloc 1,0 =", rows[1]["a"])
