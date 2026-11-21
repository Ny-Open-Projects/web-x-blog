"""聚类停止阈值: 用合并距离序列的肘部替代拍脑袋"""

import math

SITES = [
    ("朝阳仓", 39.920, 116.470), ("通州仓", 39.910, 116.490),
    ("亦庄仓", 39.900, 116.480), ("海淀仓", 40.000, 116.300),
    ("昌平仓", 40.010, 116.310), ("大兴仓", 39.730, 116.340),
    ("房山仓", 39.720, 116.350), ("顺义仓", 40.130, 116.650),
]


def haversine_km(lat1, lon1, lat2, lon2):
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def merge_distances(points):
    """逐步合并最近的两个簇, 记录每次合并时的簇间最小距离"""
    d = [[haversine_km(p[1], p[2], q[1], q[2]) for q in points] for p in points]
    clusters = [[i] for i in range(len(points))]
    history = []
    while len(clusters) > 1:
        best = None
        for a in range(len(clusters)):
            for b in range(a + 1, len(clusters)):
                pair_min = min(d[i][j] for i in clusters[a] for j in clusters[b])
                if best is None or pair_min < best[0]:
                    best = (pair_min, a, b)
        history.append((best[0], len(clusters) - 1))
        _, a, b = best
        clusters[a].extend(clusters[b])
        del clusters[b]
    return history


def elbow_threshold(history):
    """取相邻合并距离比值最大的一跳之后作为阈值"""
    best_i, best_ratio = 1, 1.0
    for i in range(1, len(history)):
        prev = max(history[i - 1][0], 1e-9)
        ratio = history[i][0] / prev
        if ratio > best_ratio:
            best_i, best_ratio = i, ratio
    return (history[best_i - 1][0] + history[best_i][0]) / 2, best_ratio


if __name__ == "__main__":
    history = merge_distances(SITES)
    print("合并距离序列(距离, 合并后簇数):")
    for dist, k in history:
        print(f"  合并到 {k} 簇时距离 {dist:.1f}km")
    thr, ratio = elbow_threshold(history)
    print(f"肘部: 最大跳变 x{ratio:.1f}, 建议阈值取 {thr:.1f}km")
    assert ratio > 2, "本例应存在明显肘部"
    kept = sum(1 for dist, _ in history if dist <= thr)
    print(f"按该阈值停止合并, 得到 {kept} 个簇; 与按 5km 拍脑袋相比有数据依据")
    print("要点: 肘部找的是'合并成本突然变贵'的位置, 那之后合并的都是跨商圈硬凑")
