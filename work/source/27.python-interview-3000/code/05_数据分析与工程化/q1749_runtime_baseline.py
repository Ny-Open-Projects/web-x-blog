"""任务耗时基线:中位数与 MAD 做稳健基线,劣化超阈值才告警,不追每次抖动"""

HISTORY = [720, 735, 710, 760, 725, 740, 715, 730]   # 近 8 次运行秒数
TODAY_RUN = 980
ALARM_SLACK = 6.0


def median(xs):
    s = sorted(xs)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


def baseline(history):
    med = median(history)
    mad = median([abs(x - med) for x in history])
    return med, mad


def check(value, med, mad, slack):
    if mad == 0:
        mad = max(1.0, med * 0.01)  # 历史完全一致时给 1% 兜底
    limit = med + slack * mad * 1.4826  # 1.4826 把 MAD 校正到正态 sigma
    return limit, value > limit


if __name__ == "__main__":
    med, mad = baseline(HISTORY)
    limit, bad = check(TODAY_RUN, med, mad, ALARM_SLACK)
    print(f"基线中位数 {med:.0f}s, MAD {mad:.1f}s, 劣化阈值 {limit:.0f}s")
    print(f"本次运行 {TODAY_RUN}s ->", "告警:疑似劣化,先查数据量环比再查代码" if bad else "正常")
    _, still_ok = check(760, med, mad, ALARM_SLACK)
    print(f"对照:历史波动 760s ->", "告警" if still_ok else "正常(不狼来了)")
    print("要点:基线用中位数+MAD 抗离群,均值+σ会被一次慢跑污染;告警附上行数环比,区分'数据量变大'与'代码劣化'")
