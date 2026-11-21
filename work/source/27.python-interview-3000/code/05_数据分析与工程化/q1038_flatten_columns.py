try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    print("标准库演示:把 (列, 函数) 元组拼成单层列名")
    cols = [("amount", "sum"), ("amount", "mean")]
    print(["_".join(map(str, c)) for c in cols])
else:
    df = pd.DataFrame({
        "region": ["华东", "华东", "华北", "华北"],
        "amount": [10, 20, 30, 40],
    })
    g = df.groupby("region").agg({"amount": ["sum", "mean"]})
    print("双层列:", g.columns.tolist(), end="\n\n")
    g.columns = ["_".join(map(str, c)) for c in g.columns]
    print(g.reset_index())
