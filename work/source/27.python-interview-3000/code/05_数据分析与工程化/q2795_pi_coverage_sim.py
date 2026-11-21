"""预测区间的覆盖率校准: 蒙特卡洛验证名义 90% 是不是真 90%"""
import random


def ols(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    var = sum((x - mx) ** 2 for x in xs)
    b = cov / var
    a = my - b * mx
    return a, b, [y - (a + b * x) for x, y in zip(xs, ys)]


def bootstrap_pi(xs, ys, x_new, level, boots, rng):
    a, b, resid = ols(xs, ys)
    lo_q = (1 - level) / 2 * 100
    preds = []
    for _ in range(boots):
        ys_b = [a + b * x + resid[rng.randrange(len(resid))] for x in xs]
        a_b, b_b, resid_b = ols(xs, ys_b)
        preds.append(a_b + b_b * x_new + resid_b[rng.randrange(len(resid_b))])
    preds.sort()
    return preds[int(len(preds) * lo_q / 100)], preds[int(len(preds) * (100 - lo_q) / 100)]


if __name__ == "__main__":
    n, sims, boots, level = 30, 200, 300, 0.90
    master = random.Random(2026)
    covered = 0
    for s in range(sims):
        xs = list(range(1, n + 1))
        rnd = random.Random(1000 + s)
        ys = [1.5 + 0.6 * x + rnd.gauss(0, 2.0) for x in xs]
        truth = 1.5 + 0.6 * 15  # 新观测真值在回归线附近再叠一份噪声
        new_y = truth + master.gauss(0, 2.0)
        lo, hi = bootstrap_pi(xs, ys, 15, level, boots, master)
        if lo <= new_y <= hi:
            covered += 1
    emp = covered / sims
    print(f"模拟 {sims} 次, 每次 {boots} 次重抽样, 名义覆盖率 {level:.0%}")
    print(f"实测覆盖率 {emp:.1%} (覆盖 {covered}/{sims})")
    assert 0.80 <= emp <= 0.98, "残差 bootstrap 的实测覆盖率应接近名义值"
    print("要点: 名义 90% 不等于真 90%, 用固定种子的蒙特卡洛校准区间构造, 是发布前的自证动作")
