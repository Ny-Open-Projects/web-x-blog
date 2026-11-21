"""渠道质量评分:秩归一抗离群,多指标加权合成综合分"""

try:
    import pandas as pd
except ImportError:
    pd = None

CHANNELS = {
    "搜索":   {"cvr": 0.032, "ret7": 0.41, "aov": 156, "roi": 2.1},
    "信息流": {"cvr": 0.018, "ret7": 0.29, "aov": 98,  "roi": 1.4},
    "社交裂变": {"cvr": 0.027, "ret7": 0.46, "aov": 88,  "roi": 3.8},
    "应用商店": {"cvr": 0.041, "ret7": 0.38, "aov": 141, "roi": 1.9},
}
WEIGHTS = {"cvr": 0.3, "ret7": 0.3, "aov": 0.2, "roi": 0.2}


def rank_norm(values):
    """秩归一:映射到 0-1,离群值只占一个名次,不拉伸整条轴"""
    order = sorted(range(len(values)), key=lambda i: values[i])
    rank = [0.0] * len(values)
    for pos, idx in enumerate(order):
        rank[idx] = pos / (len(values) - 1) if len(values) > 1 else 0.5
    return rank


def score_channels(channels, weights):
    names = list(channels)
    norms = {}
    for k in weights:
        vals = [channels[c][k] for c in names]
        norms[k] = dict(zip(names, rank_norm(vals)))
    out = {}
    for c in names:
        total = sum(norms[k][c] * w for k, w in weights.items())
        out[c] = (total, {k: round(norms[k][c], 2) for k in weights})
    return out


if __name__ == "__main__":
    scored = score_channels(CHANNELS, WEIGHTS)
    for c, (s, detail) in sorted(scored.items(), key=lambda kv: -kv[1][0]):
        print(f"{c:<6} 综合分 {s:.2f}  各项秩 {detail}")
    print("要点:合成前统一指标方向(成本类取倒数);min-max 会被 roi=3.8 这种离群值压扁其他渠道,秩归一不拉伸但有名次并列风险;权重必须评审留痕,别让调权重变成调结论")
    if pd is not None:
        df = pd.DataFrame(CHANNELS).T
        print("pandas 视角(原始指标):")
        print(df)
