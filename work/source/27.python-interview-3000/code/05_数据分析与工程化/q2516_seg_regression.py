"""分段回归: 用两段最小二乘检测结构性变化"""


def fit_line(xs, ys):
    """一元最小二乘, 返回斜率 截距 残差平方和"""
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    var = sum((x - mx) ** 2 for x in xs)
    slope = cov / var if var else 0.0
    intercept = my - slope * mx
    sse = sum((y - (intercept + slope * x)) ** 2 for x, y in zip(xs, ys))
    return slope, intercept, sse


MONTHS = list(range(1, 25))
# 前 12 个月转化率平缓爬坡, 第 13 个月起渠道算法改版斜率抬升
CONV = [2.0, 2.2, 2.1, 2.4, 2.3, 2.6, 2.5, 2.7, 2.8, 2.7, 3.0, 3.1,
        3.0, 3.4, 3.6, 3.5, 3.9, 4.1, 4.0, 4.4, 4.5, 4.4, 4.8, 5.0]


def segment_gain(xs, ys, k):
    """在 k 处切成两段的 SSE 改善比例"""
    _, _, sse_all = fit_line(xs, ys)
    _, _, sse_a = fit_line(xs[:k], ys[:k])
    _, _, sse_b = fit_line(xs[k:], ys[k:])
    return 1 - (sse_a + sse_b) / sse_all


if __name__ == "__main__":
    slope, _, sse_all = fit_line(MONTHS, CONV)
    gain = segment_gain(MONTHS, CONV, 12)
    s_a, _, _ = fit_line(MONTHS[:12], CONV[:12])
    s_b, _, _ = fit_line(MONTHS[12:], CONV[12:])
    print(f"单段拟合: 斜率 {slope:.3f}, SSE {sse_all:.2f}")
    print(f"两段拟合: 前段斜率 {s_a:.3f}, 后段斜率 {s_b:.3f}, SSE 下降 {gain:.0%}")
    assert gain > 0.5, "改版数据应检出结构性变化"
    print(f"解读: 斜率从 {s_a:.2f} 翻倍到 {s_b:.2f}, 第 13 个月是政策/算法变更点")
    # 反例: 平稳带噪声的数据不应误报
    stable = [3.0 + 0.05 * m + 0.04 * ((m % 3) - 1) for m in MONTHS]
    gain_s = segment_gain(MONTHS, stable, 12)
    print(f"平稳对照数据 SSE 仅下降 {gain_s:.0%}, 不应触发告警")
    assert gain_s < 0.2, "平稳数据不应误报结构变化"
    print("要点: 分段回归把'感觉变了'变成可检验的 SSE 下降, 前后斜率各自解释两个时代")
