try:
    import pandas as pd
except ImportError:
    pd = None

def spread(values):
    """自定义极差聚合:标准库里也用同一套逻辑演示"""
    return max(values) - min(values)

if pd is None:
    from collections import defaultdict
    rows = [("华东", 10), ("华东", 25), ("华北", 40), ("华北", 50)]
    g = defaultdict(list)
    for region, amount in rows:
        g[region].append(amount)
    for region, values in g.items():
        print(region, spread(values), sum(values))
else:
    df = pd.DataFrame({
        "region": ["华东", "华东", "华北", "华北"],
        "amount": [10, 25, 40, 50],
    })
    # 多函数聚合产生 MultiIndex 列
    out = df.groupby("region").agg({"amount": [spread, "sum", "mean"]})
    print(out.columns.tolist())
    # 拍平列名再导出
    out.columns = ["_".join(map(str, c)) for c in out.columns]
    print(out.reset_index())
