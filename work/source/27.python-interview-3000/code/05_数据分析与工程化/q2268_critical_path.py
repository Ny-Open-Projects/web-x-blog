"""调度关键路径与松弛时间: 找出拖慢整条管道的瓶颈任务"""

DUR = {"extract": 20, "ods_load": 15, "dwd_clean": 40, "dim_sync": 10,
       "dws_agg": 25, "ads_report": 10}
DEPS = {
    "ods_load": ["extract"], "dwd_clean": ["ods_load"], "dim_sync": ["ods_load"],
    "dws_agg": ["dwd_clean", "dim_sync"], "ads_report": ["dws_agg"],
}


def topo_order():
    indeg = {t: len(DEPS.get(t, [])) for t in DUR}
    order, ready = [], [t for t in DUR if indeg[t] == 0]
    while ready:
        t = ready.pop()
        order.append(t)
        for u, ups in DEPS.items():
            if t in ups:
                indeg[u] -= 1
                if indeg[u] == 0:
                    ready.append(u)
    return order


def cpm():
    order = topo_order()
    est, eft = {}, {}
    for t in order:
        est[t] = max((eft[u] for u in DEPS.get(t, [])), default=0)
        eft[t] = est[t] + DUR[t]
    project = max(eft.values())
    lst = {}
    for t in reversed(order):
        downs = [u for u, ups in DEPS.items() if t in ups]
        lft = min((lst[u] for u in downs), default=project)
        lst[t] = lft - DUR[t]
    slack = {t: lst[t] - est[t] for t in order}
    return est, slack, project


if __name__ == "__main__":
    est, slack, project = cpm()
    print(f"整条管道最早完成: {project} 分钟")
    print(f"{'任务':<12}{'最早开始':>8}{'松弛':>6}  判定")
    for t in sorted(est, key=lambda x: est[x]):
        tag = "关键路径" if slack[t] == 0 else f"可延误 {slack[t]} 分钟"
        print(f"{t:<12}{est[t]:>8}{slack[t]:>6}  {tag}")
    print("要点: 优化只花在松弛为 0 的任务上; 关键路径会随优化移动, 每轮优化后重算")
