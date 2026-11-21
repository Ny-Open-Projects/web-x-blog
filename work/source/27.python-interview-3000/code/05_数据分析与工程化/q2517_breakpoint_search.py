"""断点网格搜索: 最小段保护, 防止尾部小段硬凑出假断点"""


def fit_sse(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    var = sum((x - mx) ** 2 for x in xs)
    slope = cov / var if var else 0.0
    return sum((y - (my - slope * mx + slope * x)) ** 2 for x, y in zip(xs, ys))


def search_break(xs, ys, min_seg):
    """网格搜索最优断点, 每段至少 min_seg 个点, 返回 断点 SSE 改善"""
    sse_all = fit_sse(xs, ys)
    best_k, best_sse = None, sse_all
    for k in range(min_seg, len(xs) - min_seg + 1):
        sse = fit_sse(xs[:k], ys[:k]) + fit_sse(xs[k:], ys[k:])
        if sse < best_sse:
            best_k, best_sse = k, sse
    return best_k, 1 - best_sse / sse_all


MONTHS = list(range(1, 31))
# 真实断点在第 18 个月, 叠加确定性伪噪声
CONV = [0.08 * m + 0.08 * (((m * 11) % 7) - 3) / 3 for m in range(1, 19)]
CONV += [1.44 + 0.16 * (m - 18) + 0.08 * (((m * 11) % 7) - 3) / 3 for m in range(19, 31)]


def to_month(k):
    return f"{2024 + (k - 1) // 12}-{(k - 1) % 12 + 1:02d}"


if __name__ == "__main__":
    k_g, gain_g = search_break(MONTHS, CONV, min_seg=8)
    print(f"干净数据 min_seg=8: 断点在第 {k_g} 个月 {to_month(k_g)}, SSE 下降 {gain_g:.0%}")
    assert k_g == 18, f"应定位到第 18 个月, 实际 {k_g}"
    # 月末大促制造一个极端异常点, 再看两种搜索的表现
    noisy = CONV[:]
    noisy[-1] += 1.5
    k_u, gain_u = search_break(MONTHS, noisy, min_seg=2)
    k_p, gain_p = search_break(MONTHS, noisy, min_seg=8)
    print(f"含月末异常点 min_seg=2: 断点跳到第 {k_u} 个月, SSE 下降 {gain_u:.0%} -> 尾部 2 个点的假断点")
    assert k_u >= 25, "无保护时应被异常点吸到尾部"
    print(f"含月末异常点 min_seg=8: 断点在第 {k_p} 个月, SSE 下降 {gain_p:.0%} -> 小段硬凑被禁止")
    assert k_p <= len(MONTHS) - 8, "有保护时不可能选出超短尾段"
    print("要点: 最小段保护保证不为你制造假断点, 但异常值要先行清洗, 否则长段也会被拉偏")
