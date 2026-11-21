"""异常检测基线带:按星期几取历史分位带,出带才告警"""

import random

random.seed(7)
HIST = []  # 28 天历史:周末高、工作日低
for day in range(28):
    dow = day % 7
    base = [110, 112, 115, 113, 120, 165, 158][dow]
    HIST.append(base + random.randint(-6, 6))

TODAY_DOW = 0      # 今天周一
TODAY_VALUE = 138  # 明显高于历史周一


def quantile(xs, q):
    s = sorted(xs)
    pos = (len(s) - 1) * q
    lo, hi = int(pos), min(int(pos) + 1, len(s) - 1)
    frac = pos - lo
    return s[lo] * (1 - frac) + s[hi] * frac


def band_for_dow(hist, dow, lo_q=0.1, hi_q=0.9):
    xs = hist[dow::7]
    return quantile(xs, lo_q), quantile(xs, hi_q)


if __name__ == "__main__":
    print("星期几基线带 p10-p90:")
    names = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    for d, name in enumerate(names):
        lo, hi = band_for_dow(HIST, d)
        mark = "  <- 今天" if d == TODAY_DOW else ""
        print(f"  {name}: [{lo:.0f}, {hi:.0f}]{mark}")
    lo, hi = band_for_dow(HIST, TODAY_DOW)
    out = TODAY_VALUE > hi or TODAY_VALUE < lo
    print(f"今天 {TODAY_VALUE}: 基线带 [{lo:.0f}, {hi:.0f}] -> {'出带,告警并人工复核' if out else '带内,正常'}")
    lo_all, hi_all = quantile(HIST, 0.1), quantile(HIST, 0.9)
    print(f"对照:全局固定带 [{lo_all:.0f}, {hi_all:.0f}] 会把每个周末都误报")
    print("要点:基线带按周期分量分别构造,同分布才可比;带取 p10-p90,出带只代表异常候选,告警还要叠加持续时间条件")
