"""残差 bootstrap 的预测区间: 不止均值置信带, 还要覆盖新观测的噪声"""
import random

N = 24
XS = list(range(1, N + 1))
# 确定性构造: y = 2 + 0.5x + 伪噪声
YS = [2 + 0.5 * x + 0.9 * (((x * 37) % 13) - 6) / 6 for x in XS]


def ols(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    var = sum((x - mx) ** 2 for x in xs)
    b = cov / var
    a = my - b * mx
    resid = [y - (a + b * x) for x, y in zip(xs, ys)]
    return a, b, resid


def pred_interval(xs, ys, x_new, level=0.90, boots=600, seed=7):
    """残差 bootstrap: 重抽残差重构 y 再拟合, 预测时再叠加一份新噪声"""
    a, b, resid = ols(xs, ys)
    rng = random.Random(seed)
    lo_q = (1 - level) / 2 * 100
    preds = []
    for _ in range(boots):
        ys_b = [a + b * x + resid[rng.randrange(len(resid))] for x in xs]
        a_b, b_b, resid_b = ols(xs, ys_b)
        y_pred = a_b + b_b * x_new + resid_b[rng.randrange(len(resid_b))]
        preds.append(y_pred)
    preds.sort()
    lo = preds[int(len(preds) * lo_q / 100)]
    hi = preds[min(len(preds) - 1, int(len(preds) * (1 - lo_q / 100)))]
    return a + b * x_new, lo, hi


if __name__ == "__main__":
    a, b, resid = ols(XS, YS)
    print(f"拟合: y = {a:.3f} + {b:.3f}x, 残差标准差 {((sum(r * r for r in resid) / (N - 2)) ** 0.5):.3f}")
    for x_new, tag in [(6, "样本密集区"), (12, "中段"), (30, "超出样本外推")]:
        yhat, lo, hi = pred_interval(XS, YS, x_new)
        print(f"x={x_new:2d} {tag}: 点预测 {yhat:.2f}, 90% 预测区间 [{lo:.2f}, {hi:.2f}], 宽度 {hi - lo:.2f}")
    _, lo_m, hi_m = pred_interval(XS, YS, 12)
    _, lo_e, hi_e = pred_interval(XS, YS, 30)
    assert hi_e - lo_e > hi_m - lo_m, "超出样本范围处的预测区间应更宽"
    yhat12 = a + b * 12
    assert lo_m - 0.6 <= yhat12 <= hi_m + 0.6, "区间应以点预测为中心"
    print("要点: 预测区间 = 回归不确定 + 单点噪声, 比均值的置信带更宽, 越远离样本重心越宽")
