"""RFM 分段跨期稳定性: 转移矩阵 Jaccard 与降级滞回"""

F1 = {"u1": 12, "u2": 2, "u3": 8, "u4": 1, "u5": 5, "u6": 15,
      "u7": 3, "u8": 6, "u9": 20, "u10": 1, "u11": 4, "u12": 7}
F2 = {"u1": 13, "u2": 3, "u3": 7, "u4": 1, "u5": 6, "u6": 14,
      "u7": 4, "u8": 6, "u9": 18, "u10": 2, "u11": 5, "u12": 5}
HI = 6        # 高频阈值: F>=6
MARGIN = 1    # 降级滞回: 高频用户 F 回落到 HI-MARGIN 以内不降级


def seg(f):
    if f >= HI:
        return "高频"
    return "中频" if f >= 3 else "低频"


def seg_hyst(prev, f):
    if prev == "高频" and f >= HI - MARGIN:
        return "高频"
    return seg(f)


def jaccard(a, b):
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 1.0


if __name__ == "__main__":
    raw = {u: seg(f) for u, f in F1.items()}
    raw2 = {u: seg(f) for u, f in F2.items()}
    hyst2 = {u: seg_hyst(raw[u], f) for u, f in F2.items()}
    labels = ["高频", "中频", "低频"]
    matrix = {(a, b): 0 for a in labels for b in labels}
    for u in F1:
        matrix[(raw[u], raw2[u])] += 1
    print("原始转移矩阵(行=上月, 列=本月):")
    for a in labels:
        print("  " + a + ": " + ", ".join(f"{b} {matrix[(a, b)]}" for b in labels))
    flips_raw = sum(1 for u in F1 if raw[u] != raw2[u])
    flips_hyst = sum(1 for u in F1 if raw[u] != hyst2[u])
    hi1 = {u for u, s in raw.items() if s == "高频"}
    j_raw = jaccard(hi1, {u for u, s in raw2.items() if s == "高频"})
    j_hyst = jaccard(hi1, {u for u, s in hyst2.items() if s == "高频"})
    print(f"换段人数: 原始 {flips_raw}, 加滞回 {flips_hyst}; 高频集合 Jaccard: {j_raw:.2f} -> {j_hyst:.2f}")
    assert flips_hyst < flips_raw and j_hyst > j_raw, "滞回应降低抖动"
    print("要点: 边界上的用户在两期之间反复横跳, 降级加一段缓冲带, 升级即时生效")
