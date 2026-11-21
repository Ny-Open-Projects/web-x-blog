try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from collections import defaultdict
    rows = [("bj", "A", 100), ("bj", "B", 100), ("bj", "C", 80), ("sh", "A", 90)]
    g = defaultdict(list)
    for city, product, amount in rows:
        g[city].append((amount, product))
    for city, items in g.items():
        items.sort(key=lambda x: -x[0])
        print(city, [(p, i + 1) for i, (a, p) in enumerate(items)])
else:
    df = pd.DataFrame({
        "city": ["bj", "bj", "bj", "sh"],
        "product": ["A", "B", "C", "A"],
        "amount": [100, 100, 80, 90],
    })
    df["rank_dense"] = df.groupby("city")["amount"].rank(method="dense", ascending=False)
    df["rank_first"] = df.groupby("city")["amount"].rank(method="first", ascending=False)
    df["rank_min"] = df.groupby("city")["amount"].rank(method="min", ascending=False)
    df["rank_pct"] = df.groupby("city")["amount"].rank(pct=True)
    print(df)
    top3 = df[df.groupby("city")["amount"].rank(method="first", ascending=False) <= 3]
    print(top3[["city", "product", "amount"]])
