try:
    import pandas as pd
    from pandas.api.types import CategoricalDtype
except ImportError:
    pd = None

if pd is None:
    order = ["低", "中", "高"]
    rows = [("u1", "中"), ("u2", "高"), ("u3", "低")]
    for user, level in sorted(rows, key=lambda x: order.index(x[1])):
        print(user, level)
else:
    lvl = CategoricalDtype(["低", "中", "高"], ordered=True)
    df = pd.DataFrame({"user": ["u1", "u2", "u3"], "level": ["中", "高", "低"]})
    df["level"] = df["level"].astype(lvl)
    print(df.sort_values("level"), end="\n\n")
    print("min/max:", df["level"].min(), df["level"].max())
    print("比较过滤 高于中:", df[df["level"] > "中"]["user"].tolist())
