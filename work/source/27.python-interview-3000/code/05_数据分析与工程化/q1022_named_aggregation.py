try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from collections import defaultdict
    rows = [("华东", 10, "o1"), ("华东", 20, "o2"), ("华北", 40, "o3")]
    total, cnt, mx = defaultdict(float), defaultdict(int), defaultdict(lambda: float("-inf"))
    for region, amount, _ in rows:
        total[region] += amount
        cnt[region] += 1
        mx[region] = max(mx[region], amount)
    for region in sorted(total):
        print(region, total[region], total[region] / cnt[region], cnt[region], mx[region])
else:
    df = pd.DataFrame({
        "region": ["华东", "华东", "华北", "华北"],
        "order_id": ["o1", "o2", "o3", "o4"],
        "amount": [10, 20, 40, 50],
    })
    out = df.groupby("region").agg(
        total_amount=("amount", "sum"),
        avg_amount=("amount", "mean"),
        n_orders=("order_id", "count"),
        max_amount=("amount", "max"),
    )
    print(out.reset_index())
