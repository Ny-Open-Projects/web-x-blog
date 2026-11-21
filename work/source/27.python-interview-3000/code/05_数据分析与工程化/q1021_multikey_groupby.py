try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    # 标准库降级:多键分组求和,输出平铺行
    from collections import defaultdict
    rows = [("华东", "A", 10), ("华东", "B", 20), ("华东", "A", 5), ("华北", "A", 40)]
    agg = defaultdict(float)
    for region, product, amount in rows:
        agg[(region, product)] += amount
    for key in sorted(agg):
        print(key[0], key[1], agg[key])
else:
    df = pd.DataFrame({
        "region": ["华东", "华东", "华东", "华北", "华北"],
        "product": ["A", "A", "B", "A", "B"],
        "amount": [10, 20, 5, 40, 50],
    })
    # 默认 as_index=True,分组键进 MultiIndex
    multi = df.groupby(["region", "product"])["amount"].sum()
    print(multi, end="\n\n")
    # 平铺方案一:as_index=False,键回到普通列,报表场景首选
    print(df.groupby(["region", "product"], as_index=False)["amount"].sum(), end="\n\n")
    # 平铺方案二:事后 reset_index 还原
    print(multi.reset_index())
