"""问卷偏差校正: 事后分层加权与有效样本量"""

RESPONDENTS = [
    # 年龄段, 满意度 1-5
    ("18-25", 5), ("18-25", 4), ("18-25", 5), ("18-25", 4), ("18-25", 5),
    ("26-40", 4), ("26-40", 4), ("26-40", 3),
    ("40+", 3), ("40+", 2),
]
POP_SHARE = {"18-25": 0.2, "26-40": 0.45, "40+": 0.35}

if __name__ == "__main__":
    by_seg = {}
    for seg, s in RESPONDENTS:
        by_seg.setdefault(seg, []).append(s)
    total = len(RESPONDENTS)
    weighted_sum, weight_sum, sq_sum = 0.0, 0.0, 0.0
    print(f"{'年龄段':<8}{'样本占比':>8}{'总体占比':>8}{'权重':>6}{'段内均值':>8}")
    for seg, scores in by_seg.items():
        share = len(scores) / total
        w = POP_SHARE[seg] / share
        seg_mean = sum(scores) / len(scores)
        weighted_sum += w * seg_mean * len(scores)
        weight_sum += w * len(scores)
        sq_sum += w * w * len(scores)
        print(f"{seg:<8}{share:>8.0%}{POP_SHARE[seg]:>8.0%}{w:>6.2f}{seg_mean:>8.2f}")
    weighted = weighted_sum / weight_sum
    raw = sum(s for _, s in RESPONDENTS) / total
    ess = weight_sum * weight_sum / sq_sum
    print(f"未加权满意度 {raw:.2f}, 加权后 {weighted:.2f}, 年轻样本高估 {raw - weighted:.2f} 分")
    print(f"有效样本量 {total} -> {ess:.1f}, 加权让区间变宽是诚实的代价")
