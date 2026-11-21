"""工具调用 DAG:Kahn 分层拓扑排序,同层并行,环检测,失败传播标记 skip。"""
from collections import deque


def topo_layers(nodes, edges):
    indeg = {n: 0 for n in nodes}
    adj = {n: [] for n in nodes}
    for a, b in edges:
        adj[a].append(b)
        indeg[b] += 1
    queue = deque(sorted(n for n, d in indeg.items() if d == 0))
    layers, seen = [], 0
    while queue:
        layer = list(queue)
        queue.clear()
        seen += len(layer)
        layers.append(layer)
        for n in layer:
            for m in adj[n]:
                indeg[m] -= 1
                if indeg[m] == 0:
                    queue.append(m)
    if seen != len(nodes):
        raise ValueError("依赖图存在环,拒绝执行")
    return layers


def execute(plan, fail_at=None):
    layers = topo_layers(list(plan), [(a, b) for b, deps in plan.items() for a in deps])
    status, outputs = {}, {}
    for layer in layers:
        for n in layer:                        # 同层真实场景用线程池并行
            failed = n == fail_at
            dep_failed = any(status.get(d) in ("failed", "skipped") for d in plan[n])
            status[n] = "failed" if failed else ("skipped" if dep_failed else "ok")
            outputs[n] = None if status[n] != "ok" else f"{n} 的结果"
    return status, outputs


if __name__ == "__main__":
    plan = {
        "get_user": [],                        # 依赖:值是被依赖者
        "get_account": ["get_user"],
        "get_risk": ["get_user"],
        "check_limit": ["get_account", "get_risk"],
        "transfer": ["check_limit"],
        "notify": ["transfer"],
    }
    status, outputs = execute(plan)
    print("全成功:", status)
    assert status["transfer"] == "ok" and status["notify"] == "ok"

    status2, _ = execute(plan, fail_at="get_risk")
    print("get_risk 失败:", status2)
    assert status2["check_limit"] == "skipped" and status2["notify"] == "skipped"
    assert status2["get_account"] == "ok", "无关分支不受影响"

    try:
        topo_layers(["a", "b"], [("a", "b"), ("b", "a")])
    except ValueError as e:
        print("环检测:", e)
    print("DAG 调度器通过")
