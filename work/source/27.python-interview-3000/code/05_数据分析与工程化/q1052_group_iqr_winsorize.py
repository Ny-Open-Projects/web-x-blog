try:
    import pandas as pd
except ImportError:
    pd = None

if pd is None:
    from collections import defaultdict
    rows = [("bj", 10), ("bj", 12), ("bj", 11), ("bj", 500), ("sh", 8), ("sh", 9), ("sh", 40)]
    g = defaultdict(list)
    for city, v in rows:
        g[city].append(v)
    for city, values in g.items():
        s = sorted(values)

        def q(p):
            i = p * (len(s) - 1)
            lo, hi = int(i), min(int(i) + 1, len(s) - 1)
            return s[lo] + (s[hi] - s[lo]) * (i - lo)
        q1, q3 = q(0.25), q(0.75)
        iqr = q3 - q1
        low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        print(city, "边界", round(low, 2), round(high, 2), "盖帽后", [min(max(v, low), high) for v in values])
else:
    df = pd.DataFrame({
        "city": ["bj", "bj", "bj", "bj", "sh", "sh", "sh"],
        "amount": [10, 12, 11, 500, 8, 9, 40],
    })
    q1 = df.groupby("city")["amount"].transform(lambda s: s.quantile(0.25))
    q3 = df.groupby("city")["amount"].transform(lambda s: s.quantile(0.75))
    iqr = q3 - q1
    df["amount_capped"] = df["amount"].clip(q1 - 1.5 * iqr, q3 + 1.5 * iqr)
    print(df)
