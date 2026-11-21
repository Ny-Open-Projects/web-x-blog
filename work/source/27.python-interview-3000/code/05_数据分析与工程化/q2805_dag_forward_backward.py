"""DAG 的前推后推: 最早最晚时刻与零松弛关键链"""

TASKS = {
    # 任务: 时长, 依赖
    "pull_orders":   (20, []),
    "pull_pay":      (15, []),
    "clean_orders":  (25, ["pull_orders"]),
    "clean_pay":     (10, ["pull_pay"]),
    "join_trade":    (20, ["clean_orders", "clean_pay"]),
    "agg_shop":      (30, ["join_trade"]),
    "agg_category":  (15, ["join_trade"]),
    "load_report":   (10, ["agg_shop", "agg_category"]),
    "push_alert":    (5,  ["load_report"]),
}


def topo_sort(tasks):
    indeg = {t: 0 for t in tasks}
    succ = {t: [] for t in tasks}
    for t, (_, deps) in tasks.items():
        for d in deps:
            succ[d].append(t)
            indeg[t] += 1
    ready = sorted(t for t, d in indeg.items() if d == 0)
    order = []
    while ready:
        t = ready.pop(0)
        order.append(t)
        for s in succ[t]:
            indeg[s] -= 1
            if indeg[s] == 0:
                ready.append(s)
        ready.sort()
    assert len(order) == len(tasks), "DAG 存在环"
    return order, succ


def forward_backward(tasks):
    order, succ = topo_sort(tasks)
    es, ef = {}, {}
    for t in order:
        dur, deps = tasks[t]
        es[t] = max((ef[d] for d in deps), default=0)
        ef[t] = es[t] + dur
    finish = max(ef.values())
    ls, lf = {}, {}
    for t in reversed(order):
        _, _ = tasks[t]
        lf[t] = min((ls[s] for s in succ[t]), default=finish)
        ls[t] = lf[t] - tasks[t][0]
    slack = {t: ls[t] - es[t] for t in tasks}
    return es, ef, ls, lf, slack, finish, order


if __name__ == "__main__":
    es, ef, ls, lf, slack, finish, order = forward_backward(TASKS)
    print(f"工程总完工 T = {finish} 分钟")
    print(f"{'任务':<14}{'时长':>4}{'ES':>5}{'EF':>5}{'LS':>5}{'LF':>5}{'松弛':>5}  关键")
    for t in order:
        dur = TASKS[t][0]
        mark = " *" if slack[t] == 0 else ""
        print(f"{t:<14}{dur:>4}{es[t]:>5}{ef[t]:>5}{ls[t]:>5}{lf[t]:>5}{slack[t]:>5}{mark}")
    critical = [t for t in order if slack[t] == 0]
    print("关键链:", " -> ".join(critical))
    assert finish == 110, "总完工应为 110 分钟"
    assert critical == ["pull_orders", "clean_orders", "join_trade",
                        "agg_shop", "load_report", "push_alert"], "关键链应走商品域长链"
    assert slack["agg_category"] == 15 and slack["pull_pay"] == 20, "旁支松弛应符合手算"
    print("要点: 前推算最早时刻, 后推算最晚时刻, 松弛为零的任务串起来就是关键链, 压工期只压它")
