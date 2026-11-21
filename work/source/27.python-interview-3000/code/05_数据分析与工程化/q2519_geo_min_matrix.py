"""地理聚类的最小距离矩阵: haversine 全对距离与贪心合并"""

import math

SITES = [
    ("朝阳仓", 39.920, 116.470), ("通州仓", 39.910, 116.490),
    ("亦庄仓", 39.900, 116.480), ("海淀仓", 40.000, 116.300),
    ("昌平仓", 40.010, 116.310), ("大兴仓", 39.730, 116.340),
    ("房山仓", 39.720, 116.350), ("顺义仓", 40.130, 116.650),
]
THRESHOLD_KM = 8.0


def haversine_km(lat1, lon1, lat2, lon2):
    r = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(a))


def dist_matrix(points):
    n = len(points)
    d = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            km = haversine_km(points[i][1], points[i][2], points[j][1], points[j][2])
            d[i][j] = d[j][i] = km
    return d


def greedy_clusters(points, d, threshold_km):
    clusters = [[i] for i in range(len(points))]
    while len(clusters) > 1:
        best = None
        for a in range(len(clusters)):
            for b in range(a + 1, len(clusters)):
                pair_min = min(d[i][j] for i in clusters[a] for j in clusters[b])
                if best is None or pair_min < best[0]:
                    best = (pair_min, a, b)
        if best[0] > threshold_km:
            break
        _, a, b = best
        clusters[a].extend(clusters[b])
        del clusters[b]
    return clusters


if __name__ == "__main__":
    d = dist_matrix(SITES)
    n = len(SITES)
    assert all(d[i][j] == d[j][i] for i in range(n) for j in range(n)), "矩阵应对称"
    assert all(d[i][i] == 0.0 for i in range(n)), "对角线必须为 0"
    print("站点 0 的距离行: " + ", ".join(f"{SITES[j][0]} {d[0][j]:.1f}km" for j in range(1, n)))
    for i in range(n):
        nn = min((d[i][j], j) for j in range(n) if j != i)
        print(f"  {SITES[i][0]} 最近邻 {SITES[nn[1]][0]} {nn[0]:.1f}km")
    clusters = greedy_clusters(SITES, d, THRESHOLD_KM)
    print(f"贪心合并(阈值 {THRESHOLD_KM}km, 簇间距离取最小对) 得到 {len(clusters)} 个簇:")
    for c in clusters:
        print("  " + " + ".join(SITES[i][0] for i in c))
    assert len(clusters) < n, "阈值应能合并出簇"
    print("要点: 最近邻只看单点, 聚类看簇间最小距离; 复杂度 O(n^2) 起步, 大规模需网格索引")
