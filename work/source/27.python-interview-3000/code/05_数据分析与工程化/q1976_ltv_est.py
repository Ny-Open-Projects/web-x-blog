"""LTV 粗估:留存曲线加权 ARPU,观察不满时按留存衰减外推并给区间"""

try:
    import pandas as pd
except ImportError:
    pd = None

# 观测到 M6 的月度留存率与各月人均收入
RETENTION = [1.00, 0.42, 0.31, 0.26, 0.23, 0.21, 0.19]
ARPU = [30.0, 18.0, 14.0, 12.0, 10.0, 9.0, 8.0]
HORIZON = 12


def extrapolate(series, target_len, tail_ratio):
    """尾部按固定环比衰减外推到目标期数,用于截断观测的粗估"""
    out = list(series)
    while len(out) < target_len:
        out.append(out[-1] * tail_ratio)
    return out[:target_len]


def ltv(retention, arpu):
    return sum(r * a for r, a in zip(retention, arpu))


if __name__ == "__main__":
    obs = ltv(RETENTION, ARPU)
    arpu_flat = extrapolate(ARPU, HORIZON, 1.0)   # ARPU 按最近一月持平
    base = ltv(extrapolate(RETENTION, HORIZON, 0.85), arpu_flat)
    low = ltv(extrapolate(RETENTION, HORIZON, 0.70), arpu_flat)
    high = ltv(extrapolate(RETENTION, HORIZON, 0.95), arpu_flat)
    print(f"观测到 M6 的 LTV: {obs:.1f} 元(只信观测期)")
    print(f"外推到 M12(ARPU 持平): 基准 {base:.1f} 元,区间 [{low:.1f}, {high:.1f}] 元")
    print(f"外推增量占粗估 {1 - obs / base:.0%},投放 ROI 判断用保守下界 {low:.1f} 元")
    print("要点:ARPUx寿命公式只做数量级判断;不确定性主要来自留存衰减,衰减系数用老 cohort 校准;报告必须带区间与观测期标注")
    if pd is not None:
        df = pd.DataFrame({"month": range(len(RETENTION)),
                           "ret": RETENTION, "arpu": ARPU})
        df["contrib"] = df["ret"] * df["arpu"]
        print("pandas 视角: 累计 LTV 到 M6 =", round(df["contrib"].sum(), 1))
