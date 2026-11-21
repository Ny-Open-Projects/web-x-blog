"""指标突降归因:维度贡献分解 + 乘法口径的因子替换拆解"""
try:
    import pandas as pd
except ImportError:
    pd = None

YESTERDAY = {"华东": 1200, "华南": 800, "华北": 600, "海外": 400}
TODAY = {"华东": 900, "华南": 820, "华北": 100, "海外": 380}


def dimension_contribution(prev, curr):
    """按维度算贡献:该维度降幅 / 总降幅,先定位大头再二次下钻"""
    total_drop = sum(prev.values()) - sum(curr.values())
    if total_drop == 0:
        return {}
    return {
        k: {"drop": prev[k] - curr[k], "share": (prev[k] - curr[k]) / total_drop}
        for k in prev
    }


def multiplicative_breakdown(uv_p, uv_c, cvr_p, cvr_c, aov_p, aov_c):
    """GMV = UV x CVR x AOV,逐因子替换:每步只换一个因子,交互项归到最后一步"""
    gmv_prev = uv_p * cvr_p * aov_p
    d_uv = uv_c * cvr_p * aov_p - gmv_prev
    d_cvr = uv_c * cvr_c * aov_p - uv_c * cvr_p * aov_p
    d_aov = uv_c * cvr_c * aov_c - uv_c * cvr_c * aov_p
    return {"uv": d_uv, "cvr": d_cvr, "aov": d_aov, "total": uv_c * cvr_c * aov_c - gmv_prev}


if pd is None:
    print("标准库降级:维度贡献分解")
    contrib = dimension_contribution(YESTERDAY, TODAY)
    for k, v in sorted(contrib.items(), key=lambda x: -x[1]["drop"]):
        print(f"  {k}: 下降 {v['drop']:.0f} 占总降幅 {v['share']:.1%}")
    print("乘法口径因子替换:", multiplicative_breakdown(10000, 9800, 0.04, 0.032, 120, 121))
else:
    df = pd.DataFrame({
        "region": list(YESTERDAY),
        "gmv_prev": list(YESTERDAY.values()),
        "gmv_curr": list(TODAY.values()),
    })
    df["drop"] = df["gmv_prev"] - df["gmv_curr"]
    df["share"] = df["drop"] / df["drop"].sum()
    print(df.sort_values("drop", ascending=False).to_string(index=False))
