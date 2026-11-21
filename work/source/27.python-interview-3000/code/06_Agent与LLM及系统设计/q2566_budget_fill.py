"""Q2566 注入预算的按优先级装填:装得下才进上下文,丢弃要可解释。"""


def fill(items, budget):
    kept, dropped = [], []
    used = 0
    for it in sorted(items, key=lambda x: (-x["priority"], x["cost"])):
        if it["cost"] <= budget - used:
            kept.append(it["name"])
            used += it["cost"]
        else:
            dropped.append(it["name"])
    return kept, dropped, used


def main():
    items = [
        {"name": "系统策略", "priority": 3, "cost": 100},
        {"name": "长文档A", "priority": 1, "cost": 500},
        {"name": "长文档B", "priority": 1, "cost": 200},
        {"name": "历史摘要", "priority": 2, "cost": 150},
    ]
    kept, dropped, used = fill(items, 600)
    assert kept == ["系统策略", "历史摘要", "长文档B"], kept
    assert dropped == ["长文档A"], dropped
    assert used == 450, used
    # 预算充裕时低优先级也能进
    kept2, dropped2, used2 = fill(items, 1200)
    assert dropped2 == [] and used2 == 950
    print("预算 600 装入:", kept, "用量", used)
    print("预算 600 丢弃:", dropped)
    print("预算 1200 全部装入,用量", used2)


if __name__ == "__main__":
    main()
