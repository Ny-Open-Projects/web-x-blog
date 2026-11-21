try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    rows = [("bj", 1, 10), ("bj", 2, 20), ("sh", 1, 30)]
    wide = {}
    for city, month, v in rows:
        wide[(city, month)] = v
    cities = sorted({c for c, _ in wide})
    months = sorted({m for _, m in wide})
    for c in cities:
        print(c, [wide.get((c, m), None) for m in months])
else:
    long = pd.DataFrame({
        "city": ["bj", "bj", "sh", "sh"],
        "month": [1, 2, 1, 2],
        "sales": [10, 20, 30, 40],
    })
    wide = long.pivot(index="city", columns="month", values="sales")
    print(wide, end="\n\n")
    print(wide.stack(), end="\n\n")
    print(wide.stack().unstack(level="month"))
