---
title: [Q2246] NPS 与 CSAT:口径规则与分群加权
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2246 · NPS 与 CSAT:口径规则与分群加权

> 难度:★★☆☆ | 标签:NPS, 问卷口径

**问**:领导让你出 NPS 和 CSAT 两个数,你会怎么算?问卷回收的样本结构和真实用户结构不一致时要不要处理?

**答**:NPS 是推荐者占比减贬损者占比,0-6 分是贬损者、7-8 是被动者不计分、9-10 是推荐者;CSAT 是 4-5 分(满意)占全部打分的比例,两个指标回答不同问题,NPS 量忠诚度、CSAT 量当次体验,不能互相替代。实测里新用户 NPS 25 分、老用户 16.7 分,问卷回收却偏向老用户,未加权 NPS 20 分,按真实用户结构加权后是 21.7 分——样本结构偏斜必须做分群加权,权重来自用户结构表而不是问卷本身。样本量要报告:分群回收少于 30 份只看趋势不打分;加权后要同时给有效样本量,区间变宽是诚实的代价。

```python
# file: code/05_数据分析与工程化/q2246_nps_csat.py
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
```

**追问**:
- 追问 1:被动者那么大一群,不计分合理吗?—— 合理,NPS 只关心推荐意愿的极性,被动者反映在样本量与追问题目里,而不是硬塞进分数。
- 追问 2:为什么同一批人 CSAT 高但 NPS 低?—— CSAT 评单次触点、NPS 评整体关系,当次体验好不代表愿意推荐,两者背离本身就是分析结论。
