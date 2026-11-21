try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    rows = {("华东", "A"): 10, ("华东", "B"): 20, ("华北", "A"): 30}
    print("华东层:", {k: v for k, v in rows.items() if k[0] == "华东"})
    print("华东-A:", rows.get(("华东", "A")))
else:
    df = pd.DataFrame({
        "region": ["华东", "华东", "华北"],
        "product": ["A", "B", "A"],
        "amount": [10, 20, 30],
    })
    mi = df.set_index(["region", "product"]).sort_index()
    print(mi, end="\n\n")
    print(mi.xs("华东", level="region"), end="\n\n")
    print(mi.xs(("华东", "B")), end="\n\n")
    print(mi.xs("A", level="product", drop_level=False))
