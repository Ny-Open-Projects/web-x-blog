try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from collections import defaultdict
    rows = [("bj", 10), ("bj", 25), ("sh", 5), ("sh", 6)]
    g = defaultdict(list)
    for city, amount in rows:
        g[city].append(amount)
    print("组级筛选:仅保留合计>=30 的组 ->", {k: v for k, v in g.items() if sum(v) >= 30})
else:
    df = pd.DataFrame({
        "user": ["u1", "u1", "u1", "u2"],
        "event": ["view", "cart", "pay", "view"],
        "amount": [10, 25, 5, 6],
    })
    # 组级筛选:只保留组内 amount 合计 >= 30 的组
    big = df.groupby("user").filter(lambda g: g["amount"].sum() >= 30)
    print(big, end="\n\n")
    # 组内序号:用户行为序列编号,并取每个用户第一条事件
    df = df.sort_values(["user", "event"])
    df["seq"] = df.groupby("user").cumcount() + 1
    first_event = df[df.groupby("user").cumcount() == 0]
    print(df, end="\n\n")
    print(first_event)
