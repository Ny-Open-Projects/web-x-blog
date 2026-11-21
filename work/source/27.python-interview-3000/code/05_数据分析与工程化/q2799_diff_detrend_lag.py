"""共趋势伪相关: 差分消趋势后才能看到真实时滞"""
import math

N = 60


def pn(t, a=17, m=13):
    return ((t * a) % m - (m - 1) / 2) / ((m - 1) / 2)


def series():
    a = [0.8 * t + 5 * math.sin(2 * math.pi * t / 7) + 0.4 * pn(t) for t in range(N)]
    b = [0.8 * t + 4 * math.sin(2 * math.pi * (t - 2) / 7) + 0.4 * pn(t + 11)
         for t in range(N)]
    return a, b


def zscore(xs):
    m = sum(xs) / len(xs)
    sd = (sum((x - m) ** 2 for x in xs) / len(xs)) ** 0.5
    return [(x - m) / sd for x in xs]


def xcorr_peak(a, b, max_lag):
    za, zb = zscore(a), zscore(b)
    corr = {}
    for lag in range(0, max_lag + 1):
        xs, ys = za[:N - lag], zb[lag:]
        corr[lag] = sum(x * y for x, y in zip(xs, ys)) / len(xs)
    peak = max(corr, key=lambda k: corr[k])
    return peak, corr


def diff(xs):
    return [xs[i] - xs[i - 1] for i in range(1, len(xs))]


if __name__ == "__main__":
    a, b = series()
    raw_peak, raw = xcorr_peak(a, b, 7)
    print("原始序列互相关:")
    for lag in range(0, 8):
        print(f"  L={lag}  r={raw[lag]:+.3f}")
    print(f"原始序列相关峰在 L={raw_peak}, 全部滞后都高 -> 共同上升趋势支配了相关")
    da, db = diff(a), diff(b)
    d_peak, dc = xcorr_peak(da, db, 7)
    print("一阶差分后互相关:")
    for lag in range(0, 8):
        print(f"  L={lag}  r={dc[lag]:+.3f}")
    print(f"差分后相关峰移到 L={d_peak} -> 真实时滞是 B 比 A 晚 {d_peak} 天")
    assert raw_peak == 0, "共趋势下原始互相关峰应停在 0"
    assert d_peak == 2, "差分消趋势后峰应落在真实时滞 2"
    assert dc[2] > 0.8, "差分后周期成分的相关应很高"
    print("要点: 两条都在涨的序列怎么算都相关, 先差分或去趋势, 互相关的峰才有资格谈领先滞后")
