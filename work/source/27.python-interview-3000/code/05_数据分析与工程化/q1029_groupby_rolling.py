try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from collections import defaultdict
    rows = [("bj", 10), ("bj", 12), ("bj", 11), ("sh", 20), ("sh", 22), ("sh", 21)]
    g = defaultdict(list)
    for city, t in rows:
        g[city].append(t)
    for city, values in g.items():
        ma = [sum(values[max(0, i - 1):i + 1]) / len(values[max(0, i - 1):i + 1]) for i in range(len(values))]
        print(city, values, "ma2:", [round(x, 2) for x in ma])
else:
    df = pd.DataFrame({
        "city": ["bj", "bj", "bj", "sh", "sh", "sh"],
        "t": [10, 12, 11, 20, 22, 21],
    })
    # 写法一:链式 rolling 后拍平
    chained = df.groupby("city")["t"].rolling(2, min_periods=1).mean().reset_index()
    print(chained, end="\n\n")
    # 写法二:transform 对齐回原表,报表常用
    df["ma2"] = df.groupby("city")["t"].transform(lambda s: s.rolling(2, min_periods=1).mean())
    print(df)
