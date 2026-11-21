"""分区键选择:按查询模式的谓词组合估算扫描分区数,选平均扫得最少的键"""

PARTITIONS = 60  # 候选键基数,如 60 天
QUERIES = [
    {"dt": None, "city": None},   # 全表扫
    {"dt": 1, "city": None},      # 按天
    {"dt": None, "city": 1},      # 按城市
    {"dt": 7, "city": 1},         # 天 + 城市
]


def scanned(filter_card, key):
    """扫描数 = 命中谓词的维度相乘;查询没带的维度只能全扫"""
    n = 1
    for col in key:
        c = filter_card.get(col)
        n *= PARTITIONS if c is None else c
    return n


def evaluate(candidates):
    rows = []
    for key in candidates:
        costs = [scanned(q, key) for q in QUERIES]
        rows.append((key, costs, sum(costs) / len(costs)))
    return sorted(rows, key=lambda r: r[2])


if __name__ == "__main__":
    candidates = [["dt"], ["city"], ["dt", "city"]]
    for key, costs, avg in evaluate(candidates):
        print(f"分区键 {key}: 各查询扫描 {costs}, 平均 {avg:.0f} 分区")
    best = evaluate(candidates)[0][0]
    print(f"推荐分区键: {best}")
    print("要点:分区键来自查询模式而不是建表习惯;高频等值谓词放前,范围谓词放后;两级分区当心笛卡尔放大与空目录元数据负担")
