"""同期群引擎:按入群键 x 月龄透视任意指标,pandas 与标准库双实现"""
try:
    import pandas as pd
except ImportError:
    pd = None

EVENTS = [
    # user, signup_month, order_month, amount
    ("u1", "2025-01", "2025-01", 100),
    ("u1", "2025-01", "2025-02", 80),
    ("u2", "2025-01", "2025-01", 200),
    ("u3", "2025-02", "2025-02", 150),
    ("u3", "2025-02", "2025-03", 90),
    ("u4", "2025-02", "2025-03", 60),
]


def month_diff(a, b):
    """b 相对 a 的月龄,格式 YYYY-MM"""
    ya, ma = int(a[:4]), int(a[5:7])
    yb, mb = int(b[:4]), int(b[5:7])
    return (yb - ya) * 12 + (mb - ma)


def cohort_table_stdlib(events, max_age=2):
    """行=同期群,列=月龄,单元格=指标聚合;留存同理把值换成人数即可"""
    agg, sizes = {}, {}
    for user, signup, order, amount in events:
        age = month_diff(signup, order)
        agg[(signup, age)] = agg.get((signup, age), 0) + amount
        sizes.setdefault(signup, set()).add(user)
    cohorts = sorted({k[0] for k in agg})
    print("cohort\t" + "\t".join(f"M{m}" for m in range(max_age + 1)) + "\t用户数")
    for c in cohorts:
        row = [agg.get((c, m), 0) for m in range(max_age + 1)]
        print(c + "\t" + "\t".join(str(v) for v in row) + f"\t{len(sizes[c])}")


if pd is None:
    print("标准库降级:cohort 消费金额矩阵")
    cohort_table_stdlib(EVENTS)
else:
    df = pd.DataFrame(EVENTS, columns=["user", "signup", "order", "amount"])
    df["month_idx"] = df.apply(lambda r: month_diff(r["signup"], r["order"]), axis=1)
    pivot = df.pivot_table(index="signup", columns="month_idx", values="amount",
                           aggfunc="sum", fill_value=0)
    print(pivot)
    print("各 cohort 用户数:", df.groupby("signup")["user"].nunique().to_dict())
