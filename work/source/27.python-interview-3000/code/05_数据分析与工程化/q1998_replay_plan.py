"""故障重放:从故障任务反查下游闭包,拓扑分层给出重放批次"""

DAG = {
    "ods_orders": ["dwd_orders"],
    "ods_users": ["dwd_users"],
    "dwd_orders": ["dws_shop_day", "ads_funnel"],
    "dwd_users": ["dws_shop_day"],
    "dws_shop_day": ["ads_gmv", "ads_funnel"],
    "ads_gmv": [],
    "ads_funnel": [],
}
FAILED = ["ods_orders"]


def downstream(dag, starts):
    """沿边正向 BFS,求故障任务的受影响下游闭包(含自身)"""
    seen, stack = set(), list(starts)
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        stack.extend(dag.get(node, []))
    return seen


def topo_batches(sub_dag):
    """Kahn 分层:同层任务可并行重放"""
    indeg = {n: 0 for n in sub_dag}
    for vs in sub_dag.values():
        for v in vs:
            indeg[v] += 1
    layer = sorted(n for n, d in indeg.items() if d == 0)
    batches = []
    while layer:
        batches.append(layer)
        nxt = []
        for u in layer:
            for v in sub_dag[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    nxt.append(v)
        layer = sorted(nxt)
    return batches


if __name__ == "__main__":
    closure = downstream(DAG, FAILED)
    sub = {n: [v for v in DAG.get(n, []) if v in closure] for n in closure}
    print(f"故障: {FAILED} -> 受影响闭包 {len(closure)} 个任务: {sorted(closure)}")
    for i, batch in enumerate(topo_batches(sub), 1):
        print(f"  重放批次{i}(可并行): {batch}")
    print("要点:先求闭包再分层,同层并行、层间串行;重放期间冻结下游取数,全部完成后校验水位与行数再解冻;闭包外任务不动,避免重放扩大化")
