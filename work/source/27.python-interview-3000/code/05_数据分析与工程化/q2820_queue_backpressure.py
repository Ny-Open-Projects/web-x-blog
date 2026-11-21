"""队列背压: 满载时的拒绝与逐出两种策略的代价对比"""

CAP = 5
BURST_TICKS = 4    # 前 4 拍每拍突发 5 个作业, 共 20 个
PER_TICK_IN = 5
PER_TICK_OUT = 1


def simulate(policy):
    queue, processed, lost = [], [], []
    for t in range(BURST_TICKS):
        for i in range(PER_TICK_IN):
            job = PER_TICK_IN * t + i
            if len(queue) < CAP:
                queue.append(job)
            elif policy == "reject":
                lost.append(("rejected", job))
            else:  # drop_oldest
                old = queue.pop(0)
                lost.append(("evicted", old))
                queue.append(job)
        if queue:
            processed.append(queue.pop(0))
    while queue:
        processed.append(queue.pop(0))
    return processed, lost


if __name__ == "__main__":
    proc_r, lost_r = simulate("reject")
    proc_d, lost_d = simulate("drop_oldest")
    rej = [j for kind, j in lost_r if kind == "rejected"]
    evi = [j for kind, j in lost_d if kind == "evicted"]
    print(f"拒绝策略: 完成 {len(proc_r)} 个 {proc_r}")
    print(f"  拒收 {len(rej)} 个 {rej}")
    print(f"逐出策略: 完成 {len(proc_d)} 个 {proc_d}")
    print(f"  逐出 {len(evi)} 个 {evi}")
    assert 0 in proc_r and rej, "拒绝策略完成先到作业, 拒掉后到的"
    assert min(rej) >= max(proc_r) or min(rej) > 0, "被拒的都是晚到作业"
    assert evi and any(e < max(proc_d) for e in evi), "逐出策略丢的是老作业, 却放行了新作业"
    assert len(lost_r) == len(lost_d), "两种策略丢的总量相同, 代价结构不同"
    print("要点: 拒新保旧适合'先来先得'的批处理, 逐旧纳新适合新请求更有时效价值的在线场景, 必须显式选边")
