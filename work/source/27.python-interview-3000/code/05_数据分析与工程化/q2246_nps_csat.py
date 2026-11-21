"""NPS 与 CSAT 口径:分类规则、分群加权与样本量提示"""

RAW_NPS = [
    # 分群, 推荐题打分 0-10
    ("新用户", 9), ("新用户", 10), ("新用户", 7), ("新用户", 6),
    ("老用户", 9), ("老用户", 10), ("老用户", 10), ("老用户", 8),
    ("老用户", 5), ("老用户", 3),
]
RAW_CSAT = [5, 4, 3, 5, 2]          # 满意度题打分 1-5
SEG_WEIGHT = {"新用户": 0.6, "老用户": 0.4}   # 真实用户结构


def nps(scores):
    n = len(scores)
    if n == 0:
        return None
    promoters = sum(1 for s in scores if s >= 9)
    detractors = sum(1 for s in scores if s <= 6)
    return 100.0 * (promoters - detractors) / n


def csat(scores_1_5):
    if not scores_1_5:
        return None
    return 100.0 * sum(1 for s in scores_1_5 if s >= 4) / len(scores_1_5)


if __name__ == "__main__":
    by_seg = {}
    for seg, s in RAW_NPS:
        by_seg.setdefault(seg, []).append(s)
    weighted = 0.0
    for seg, scores in by_seg.items():
        seg_nps = nps(scores)
        weighted += SEG_WEIGHT[seg] * seg_nps
        print(f"{seg}: n={len(scores)} NPS={seg_nps:.1f} 真实占比={SEG_WEIGHT[seg]:.0%}")
    raw = nps([s for _, s in RAW_NPS])
    print(f"未加权 NPS={raw:.1f}, 按真实结构加权 NPS={weighted:.1f}, 偏差 {weighted - raw:+.1f} 分")
    print(f"CSAT(4-5 分占比) = {csat(RAW_CSAT):.1f}%, 与 NPS 是两个口径不可互替")
    print("要点: 被动者 7-8 分不计分但占样本; 加权系数来自用户结构表; 分群 n<30 只看趋势不打分")
