"""指标领先滞后的互相关扫描: 找 B 落后 A 几天"""
import math

N = 60


def pn(t, a=17, m=13):
    """确定性伪噪声, 范围约 -1 到 1"""
    return ((t * a) % m - (m - 1) / 2) / ((m - 1) / 2)


def series():
    a = [100 + 8 * math.sin(2 * math.pi * t / 7) + 0.8 * pn(t) for t in range(N)]
    b = [0.9 * a[t - 3] + 0.5 * pn(t + 5) if t >= 3 else 100 + 0.5 * pn(t)
         for t in range(N)]
    return a, b


def zscore(xs):
    m = sum(xs) / len(xs)
    sd = (sum((x - m) ** 2 for x in xs) / len(xs)) ** 0.5
    return [(x - m) / sd for x in xs]


def xcorr(a, b, max_lag):
    """正滞后 L 表示 B 比 A 晚 L 天, 用对齐段的相关系数"""
    za, zb = zscore(a), zscore(b)
    out = {}
    for lag in range(-max_lag, max_lag + 1):
        if lag >= 0:
            xs, ys = za[:N - lag], zb[lag:]
        else:
            xs, ys = za[-lag:], zb[:N + lag]
        n = len(xs)
        r = sum(x * y for x, y in zip(xs, ys)) / n
        out[lag] = r
    return out


if __name__ == "__main__":
    a, b = series()
    corr = xcorr(a, b, 7)
    print("滞后 L 与相关系数 (B 比 A 晚 L 天):")
    for lag in range(-7, 8):
        bar = "#" * int(max(corr[lag], 0) * 40)
        print(f"  L={lag:+d}  r={corr[lag]:+.3f}  {bar}")
    peak = max(corr, key=lambda k: corr[k])
    print(f"相关峰在 L={peak}, r={corr[peak]:.3f} -> B 是 A 的滞后指标, 时滞 {peak} 天")
    assert peak == 3, "构造数据 B 滞后 A 三天, 峰应在 +3"
    assert corr[3] > corr[0] + 0.1, "峰值应显著高于同期相关"
    print("要点: 领先滞后用互相关找峰, 判读时先固定口径再谈因果, 领先指标才有预警价值")
