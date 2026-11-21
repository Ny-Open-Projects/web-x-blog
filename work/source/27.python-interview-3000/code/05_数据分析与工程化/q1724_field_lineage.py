"""字段级血缘:目标字段到来源字段的映射与反查,变更影响评估的基础"""

LINEAGE = {
    ("dws", "user_pay_d", "amt_7d"): [
        ("dwd", "pay_order_d", "pay_amount", "sum where dt>=today-6"),
        ("dwd", "pay_order_d", "status", "filter paid"),
    ],
    ("dws", "user_pay_d", "order_cnt_7d"): [
        ("dwd", "pay_order_d", "order_id", "count distinct where dt>=today-6"),
    ],
    ("ads", "vip_board", "pay_users_7d"): [
        ("dws", "user_pay_d", "amt_7d", "count where amt_7d>0"),
    ],
}


def downstream(field):
    """反查:某字段被哪些下游字段使用,含传递闭包"""
    direct = {tgt for tgt, srcs in LINEAGE.items()
              if field in [(s[0], s[1], s[2]) for s in srcs]}
    all_down = set(direct)
    changed = True
    while changed:
        changed = False
        for tgt, srcs in LINEAGE.items():
            if tgt not in all_down and any(s[:3] in all_down for s in srcs):
                all_down.add(tgt)
                changed = True
    return sorted(all_down)


if __name__ == "__main__":
    tgt = ("dws", "user_pay_d", "amt_7d")
    print(f"目标字段 {tgt} 的直接上游:")
    for db, tb, col, rule in LINEAGE[tgt]:
        print(f"  <- {db}.{tb}.{col}  规则: {rule}")
    field = ("dwd", "pay_order_d", "pay_amount")
    print(f"反查 {field} 的影响面(含传递): {downstream(field)}")
    print("要点:表级血缘够排期,字段级才能回答'改这个列影响谁';血缘随 SQL 解析自动生成,手工维护必然漂移")
