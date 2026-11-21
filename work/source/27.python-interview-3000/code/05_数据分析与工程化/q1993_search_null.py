"""搜索无结果率:整体比率与空转 query 前缀粗聚类"""

LOGS = [
    ("iPhone 手机壳", 12), ("iphone 壳", 8), ("蓝牙耳机", 30), ("無线耳机", 0),
    ("无线耳机", 25), ("充电器", 18), ("苹果充电线", 0), ("苹果 data线", 0),
    ("手机支架", 7), ("折叠支架", 2), ("隐私贴膜", 0), ("钢化膜", 44),
    ("耳机包", 0), ("耳机收纳包", 3), ("游戏手柄", 9), ("ns2 手柄", 0),
]


def null_rate(logs):
    zeros = [q for q, c in logs if c == 0]
    return len(zeros) / len(logs), zeros


def prefix_cluster(queries, width=2):
    groups = {}
    for q in queries:
        groups.setdefault(q[:width], []).append(q)
    return sorted(groups.items(), key=lambda kv: -len(kv[1]))


if __name__ == "__main__":
    rate, zeros = null_rate(LOGS)
    print(f"无结果率 {rate:.0%}({len(zeros)}/{len(LOGS)} 条 query 零结果)")
    for pre, qs in prefix_cluster(zeros):
        print(f"  前缀[{pre}] x{len(qs)}: {qs}")
    print("要点:零结果 query 按前缀粗聚再人工归并,繁简与大小写变体提示要先做归一化;头部类目优先补词库与同义词;无结果率看周趋势,单日受运营活动扰动")
