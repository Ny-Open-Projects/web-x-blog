"""次关键链: 扰动下的第二瓶颈与关键链翻盘测试"""

TASKS = {
    "pull_orders":  (20, []),
    "pull_pay":     (15, []),
    "clean_orders": (25, ["pull_orders"]),
    "clean_pay":    (10, ["pull_pay"]),
    "join_trade":   (20, ["clean_orders", "clean_pay"]),
    "agg_shop":     (12, ["join_trade"]),
    "agg_category": (15, ["join_trade"]),
    "load_report":  (10, ["agg_shop", "agg_category"]),
    "push_alert":   (5,  ["load_report"]),
}


def all_chains(tasks):
    """枚举起点到终点的全部任务链, 返回按总时长降序的列表"""
    deps_of = {t: v[1] for t, v in tasks.items()}
    succ = {t: [s for s in tasks if t in deps_of[s]] for t in tasks}
    roots = [t for t in tasks if not deps_of[t]]
    chains = []

    def dfs(node, path):
        kids = succ[node]
        if not kids:
            chains.append(list(path))
            return
        for k in kids:
            path.append(k)
            dfs(k, path)
            path.pop()

    for r in roots:
        dfs(r, [r])
    return sorted(chains, key=lambda c: -sum(tasks[t][0] for t in c))


def chain_len(chain):
    return sum(TASKS[t][0] for t in chain)


if __name__ == "__main__":
    chains = all_chains(TASKS)
    top = chains[0]
    second = chains[1]
    gap = chain_len(top) - chain_len(second)
    print("全部链路按时长降序 top3:")
    for c in chains[:3]:
        print(f"  {chain_len(c):>3} 分钟  {' -> '.join(c)}")
    print(f"关键链 {chain_len(top)} 分钟, 次关键链 {chain_len(second)} 分钟, 只差 {gap} 分钟")
    assert "agg_category" in top, "本例关键链应走类目聚合支线"
    assert "agg_shop" in second, "次关键链应是商店聚合支线"
    # 翻盘测试: 关键链上的独占任务缩短 4 分钟, 次关键链立即上位
    TASKS["agg_category"] = (11, ["join_trade"])
    chains2 = all_chains(TASKS)
    new_top = chains2[0]
    print(f"把 agg_category 从 15 压到 11 分钟后, 新关键链: {' -> '.join(new_top)} ({chain_len(new_top)} 分钟)")
    assert "agg_shop" in new_top, "压缩 4 分钟超过 3 分钟的差距, 关键链应翻转到商店支线"
    print("要点: 只盯着一条关键链的排期是脆的, 次关键链差距小于常规波动时, 瓶颈随时换位")
