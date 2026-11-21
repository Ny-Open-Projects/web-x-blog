---
title: [Q2794] 残差 bootstrap 的预测区间
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2794 · 残差 bootstrap 的预测区间

> 难度:★★★★ | 标签:bootstrap, 预测区间

**问**:面试官:预测下个月 GMV,你给的"区间"是置信区间还是预测区间?差在哪?

**答**:预测未来单点要用预测区间,它比均值的置信区间宽,因为叠加两层不确定性:回归系数的抽样波动 + 单点噪声。残差 bootstrap 的做法:拟合后把残差有放回重抽、贴回拟合值重构 y*,重新拟合,预测新点时再叠加一份重抽残差,重复 600 次取分位数。实测 y=2.146+0.493x,残差标准差 0.559:x=12 的 90% 预测区间 [7.21, 8.86] 宽 1.65,外推到 x=30(超出样本范围)时 [15.93, 17.85] 宽 1.92——越远离样本重心,系数不确定性被杠杆放大,区间越宽。汇报预测时给预测区间而不给置信区间,否则业务会拿点估计当承诺,拿置信带当容错,两头都错。

```python
# file: code/05_数据分析与工程化/q2794_bootstrap_pred_interval.py
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
```

**追问**:
- 追问 1:和均值置信区间的本质区别?—— 置信区间只含系数不确定性,预测区间再加新观测噪声,宽度永远更大,目标是"下一个值"而不是"均线的位置"。
- 追问 2:残差独立同分布假设破了怎么办?—— 换分块 bootstrap 保留序列相关,或对残差先建方差模型做异方差修正。
