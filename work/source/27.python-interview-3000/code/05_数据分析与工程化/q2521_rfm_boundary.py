"""RFM 分段边界: 分位数法与间隙法, 业务规则最后覆盖"""

try:
    import pandas as pd
except ImportError:
    pd = None

CUSTOMERS = [
    # id, R 天数(越小越近), F 次数, M 金额
    ("u1", 5, 12, 8600), ("u2", 40, 2, 700), ("u3", 12, 8, 4200),
    ("u4", 65, 1, 300), ("u5", 20, 5, 1500), ("u6", 8, 15, 9800),
    ("u7", 55, 3, 900), ("u8", 30, 6, 2400), ("u9", 3, 20, 15000),
    ("u10", 75, 1, 150), ("u11", 18, 4, 1100), ("u12", 25, 7, 3300),
]


def quantile_bounds(values, n_seg):
    """等分位切点: 按 rank 均分后取组内最大值作边界"""
    s = sorted(values)
    cuts = []
    for i in range(1, n_seg):
        idx = min(len(s) * i // n_seg, len(s) - 1)
        cuts.append(s[idx])
    return cuts


def gap_bounds(values, n_seg, min_side_ratio=0.25):
    """间隙法: 取最大间隔作切点, 且两侧样本都不得过少"""
    s = sorted(set(values))
    gaps = []
    for a, b in zip(s, s[1:]):
        left = sum(1 for v in values if v <= a)
        right = len(values) - left
        if left >= len(values) * min_side_ratio and right >= len(values) * min_side_ratio:
            gaps.append((b - a, a))
    gaps.sort(reverse=True)
    return sorted(a for _, a in gaps[:n_seg - 1])


def label(value, cuts, reverse=False):
    """reverse=True 时值越小段位越高, 例如 R"""
    seg = sum(1 for c in cuts if value > c)
    return seg if not reverse else (len(cuts) - seg)


if __name__ == "__main__":
    fs = [c[2] for c in CUSTOMERS]
    ms = [c[3] for c in CUSTOMERS]
    q_f, q_m = quantile_bounds(fs, 3), quantile_bounds(ms, 3)
    g_f, g_m = gap_bounds(fs, 3), gap_bounds(ms, 3)
    print(f"F 边界: 分位数法 {q_f}, 间隙法 {g_f}")
    print(f"M 边界: 分位数法 {q_m}, 间隙法 {g_m}")
    assert g_f != q_f, "两法在本例应给出不同边界"
    final_m = g_m if g_m else q_m
    vip = [c[0] for c in CUSTOMERS if c[3] >= 8000]
    counts = {}
    for cid, r, f, m in CUSTOMERS:
        seg_f = label(f, g_f)
        seg_m = label(m, final_m)
        tag = "超级用户" if m >= 8000 else f"F{seg_f}M{seg_m}"
        counts[tag] = counts.get(tag, 0) + 1
    print("业务规则覆盖: M>=8000 直接定为超级用户:", ",".join(vip))
    print("最终分布:", dict(sorted(counts.items())))
    if pd is not None:
        df = pd.DataFrame(CUSTOMERS, columns=["id", "R", "F", "M"])
        print("pandas 视角: F 三分位边界", df["F"].quantile([1 / 3, 2 / 3]).tolist())
    print("要点: 分位数保段数均衡, 间隙法找自然断档, 业务规则兜底, 三者写进口径字典")
