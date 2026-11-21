"""下游影响查询器:字段级血缘反查,按引用类型分级处置"""

EDGES = [
    ("ods_orders.user_id", "dwd_orders.user_id", "直接引用"),
    ("dwd_orders.user_id", "dws_user_day.user_id", "直接引用"),
    ("dwd_orders.user_id", "dws_user_day.distinct_users", "聚合引用"),
    ("dws_user_day.user_id", "ads_retention.user_col", "直接引用"),
    ("dws_user_day.distinct_users", "ads_dash.dau_card", "直接引用"),
    ("ods_orders.amount", "dwd_orders.pay_amount", "直接引用"),
]


def impact(source, edges):
    """BFS 反查下游,输出每节点的深度与入边引用类型"""
    adj = {}
    for src, dst, kind in edges:
        adj.setdefault(src, []).append((dst, kind))
    out, queue, seen = [], [(source, 0, "")], {source}
    while queue:
        node, depth, incoming = queue.pop(0)
        if node != source:
            out.append((node, incoming, depth))
        for dst, kind in adj.get(node, []):
            if dst not in seen:
                seen.add(dst)
                queue.append((dst, depth + 1, kind))
    return out


if __name__ == "__main__":
    print("变更 ods_orders.user_id 的影响面:")
    for node, kind, depth in impact("ods_orders.user_id", EDGES):
        grade = "必须适配" if kind == "直接引用" else "需回归验证"
        print(f"  {'  ' * (depth - 1)}<- {node} [{kind}] {grade}")
    print("要点:字段级血缘在任务上线时自动登记,别靠人肉补;直接引用要改代码,聚合引用要重算验证;血缘覆盖不全时,影响面结论必须带'可能遗漏'声明")
