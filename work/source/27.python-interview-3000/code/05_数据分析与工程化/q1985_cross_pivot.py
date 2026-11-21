"""双维度交叉透视:标准库手写 pivot,含行列边际与行占比"""

try:
    import pandas as pd
except ImportError:
    pd = None

ORDERS = [
    ("自然流量", "工作日", 320), ("自然流量", "周末", 410),
    ("付费投放", "工作日", 560), ("付费投放", "周末", 380),
    ("老客召回", "工作日", 150), ("老客召回", "周末", 260),
    ("付费投放", "工作日", 90),   # 同格多行,演示先聚合再成表
]


def pivot(rows, row_idx, col_idx, agg=sum):
    cols, grid = [], {}
    for r in rows:
        rk, ck = r[row_idx], r[col_idx]
        if ck not in cols:
            cols.append(ck)
        grid.setdefault(rk, {}).setdefault(ck, []).append(r[2])
    table = {rk: {ck: agg(grid[rk][ck]) if ck in grid[rk] else 0
                  for ck in cols} for rk in grid}
    return table, cols


def with_margins(table, cols):
    out = {rk: dict(row) for rk, row in table.items()}
    for rk in out:
        out[rk]["合计"] = sum(out[rk][c] for c in cols)
    cols_all = cols + ["合计"]
    out["总计"] = {c: sum(out[rk][c] for rk in table) for c in cols_all}
    return out, cols_all


if __name__ == "__main__":
    table, cols = pivot(ORDERS, 0, 1)
    full, cols_all = with_margins(table, cols)
    print("渠道 x 时段 订单数:")
    print(f"{'渠道':<8}" + "".join(f"{c:>8}" for c in cols_all))
    for rk, row in full.items():
        print(f"{rk:<8}" + "".join(f"{row[c]:>8}" for c in cols_all))
    print("行占比(占本渠道):")
    for rk in table:
        total = full[rk]["合计"]
        print(f"{rk:<8}" + "".join(f"{full[rk][c] / total:>8.0%}" for c in cols))
    print("要点:同格多行先聚合再成表;边际合计用于核对总量;占比单独成表,别和绝对值混在一张矩阵里")
    if pd is not None:
        df = pd.DataFrame(ORDERS, columns=["channel", "bucket", "orders"])
        pv = pd.pivot_table(df, index="channel", columns="bucket",
                            values="orders", aggfunc="sum",
                            margins=True, fill_value=0)
        print("pandas 视角:")
        print(pv)
