"""帕累托分析:按累计占比 80% 划 A 类做 ABC 分层,指导运营与库存优先级"""

try:
    import pandas as pd
except ImportError:
    pd = None

SALES = {"SKU-A": 4200, "SKU-B": 2600, "SKU-C": 1900, "SKU-D": 1200,
         "SKU-E": 900, "SKU-F": 600, "SKU-G": 400, "SKU-H": 250,
         "SKU-I": 180, "SKU-J": 90}


def abc_classify(items, a_cut=0.8, b_cut=0.95):
    """按金额降序累计,A:累计<=80%,B:<=95%,其余 C"""
    total = sum(items.values())
    ordered = sorted(items.items(), key=lambda x: -x[1])
    out, cum = [], 0.0
    for sku, amt in ordered:
        cum += amt
        share = cum / total
        cls = "A" if share <= a_cut else ("B" if share <= b_cut else "C")
        out.append((sku, amt, amt / total, share, cls))
    return out


if pd is None:
    print("标准库降级:帕累托 ABC 分层")
    rows = abc_classify(SALES)
    total = sum(SALES.values())
    print(f"{'SKU':<8}{'金额':>8}{'单品占比':>10}{'累计占比':>10}  类别")
    for sku, amt, s, cum, cls in rows:
        print(f"{sku:<8}{amt:>8}{s:>10.1%}{cum:>10.1%}  {cls}")
    for c in "ABC":
        n = sum(1 for r in rows if r[4] == c)
        amt = sum(r[1] for r in rows if r[4] == c)
        print(f"{c} 类:{n} 个 SKU,贡献 {amt / total:.1%} 金额")
else:
    df = pd.DataFrame(sorted(SALES.items(), key=lambda x: -x[1]),
                      columns=["sku", "amount"])
    total = df["amount"].sum()
    df["item_share"] = df["amount"] / total
    df["cum_share"] = df["amount"].cumsum() / total
    df["cls"] = pd.cut(df["cum_share"], bins=[0, 0.8, 0.95, 1.0],
                       labels=["A", "B", "C"], include_lowest=True)
    print(df.to_string(index=False))
    print(df.groupby("cls")["amount"].agg(["count", "sum"]))
