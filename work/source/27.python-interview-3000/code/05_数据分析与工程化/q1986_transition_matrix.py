"""跳转矩阵:页面序列转转移概率,找主流出页"""

SESSIONS = [
    ["首页", "列表", "详情", "下单"],
    ["首页", "列表", "详情"],
    ["首页", "详情", "下单"],
    ["首页", "列表"],
    ["首页", "活动", "列表", "详情", "下单"],
    ["首页", "活动"],
    ["首页", "列表", "详情"],
    ["首页", "详情"],
]


def transitions(sessions):
    cnt = {}
    for path in sessions:
        for a, b in zip(path, path[1:]):
            cnt[(a, b)] = cnt.get((a, b), 0) + 1
    return cnt


def row_normalize(cnt):
    totals = {}
    for (a, b), c in cnt.items():
        totals[a] = totals.get(a, 0) + c
    probs = {(a, b): c / totals[a] for (a, b), c in cnt.items()}
    return probs, totals


if __name__ == "__main__":
    cnt = transitions(SESSIONS)
    probs, totals = row_normalize(cnt)
    pages = sorted({p for path in SESSIONS for p in path})
    print("转移概率(行归一):")
    print("    " + "".join(f"{p:>6}" for p in pages))
    for a in pages:
        row = "".join(f"{probs.get((a, b), 0):>6.2f}" for b in pages)
        print(f"{a:<4}" + row)
    arrive = {}
    for path in SESSIONS:
        for p in path:
            arrive[p] = arrive.get(p, 0) + 1
    print("各页去向与流出:")
    for a in pages:
        outgoing = [(p, b) for (x, b), p in probs.items() if x == a]
        ends = sum(1 for path in SESSIONS if path[-1] == a)
        if not outgoing:
            print(f"  {a}: 终点页,到达 {arrive[a]} 次,全部会话在此结束")
            continue
        best = max(outgoing)
        print(f"  {a}: 到达 {arrive[a]} 次,最大去向 {best[1]} {best[0]:.0%},"
              f"会话在此结束 {ends / arrive[a]:.0%}")
    print("要点:转移矩阵按行归一,每行是一步的条件分布;流出率高的页是漏斗断点,优先修'最大去向占比低且流出率高'的页")
