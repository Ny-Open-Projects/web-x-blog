try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False

def demo_pandas():
    df = pd.DataFrame({
        "dept": ["A", "A", "B", "B", "B"],
        "salary": [100, 200, 150, 250, 300],
    })
    agg = df.groupby("dept")["salary"].agg(["mean", "max"])
    print(agg)                                   # 每组一行
    df["dept_avg"] = df.groupby("dept")["salary"].transform("mean")
    df["ratio"] = df["salary"] / df["dept_avg"]  # 组内占比
    df["rank"] = df.groupby("dept")["salary"].rank(ascending=False)
    print(df)

if __name__ == "__main__":
    if PANDAS:
        demo_pandas()
    else:
        rows = [("A", 100), ("A", 200), ("B", 150), ("B", 250), ("B", 300)]
        groups = {}
        for d, s in rows:
            groups.setdefault(d, []).append(s)
        for d, s in rows:            # transform 的标准库等价
            avg = sum(groups[d]) / len(groups[d])
            print(d, s, "dept_avg=", avg, "ratio=", round(s / avg, 2))
