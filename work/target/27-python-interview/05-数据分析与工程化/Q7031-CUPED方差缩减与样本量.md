---
title: [Q7031] CUPED 方差缩减：实验前数据当协变量
date: 2026-11-20
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7031 · CUPED 方差缩减：提升 2% 不显著，是样本不够还是噪声太大？

> 难度:★★★★ | 标签:A/B 实验, CUPED, 统计

**问**：A/B 实验转化率提升 2%，置信区间跨 0——扩大样本要再等两周。CUPED（Controlled-experiment Using Pre-Experiment Data）是什么原理？协变量怎么选？什么时候会失效？新用户没有实验前数据怎么办？

**答**：结论：CUPED 用**实验前数据作协变量**做回归校正：`Y_cv = Y - θ(X - E[X])`，其中 `θ = cov(Y, X) / var(X)`。方差缩减比例约为 `corr(Y, X)²`——转化/活跃类指标与前期行为强相关（corr 0.6-0.9），方差可降到一半以下，等效于样本量翻倍，让小效应更早显著。它不改分流、不碰随机化，是检验前的后处理校正。

机理与实战：
- **协变量选择**：用同一指标的实验前值（实验前 1-2 周的活跃天数/消费额）；协变量必须在实验前产生，否则处理效应会泄露进校正项引入偏差。
- **θ 的纪律**：θ 用实验前数据估计并**在实验开始前固定**计算规则；检验中途重估 θ 等于 peeking。两组用同一个 θ 和同一个 E[X]，保证校正项在两组间同分布、无偏。
- **失效场景**：指标与前期行为无相关（全新功能/新用户为主的实验，corr→0 时 CUPED 无收益也无害）；协变量本身有系统性偏差（如实验前有营销活动）；SRM 未排除前不要先跑 CUPED。
- **新用户处理**：协变量缺失填全局均值——校正项恰好为 0，等价于不校正，不引入偏差；更精细的做法是"老用户 CUPED + 新用户分层"分别估计再合并。
- **与 AA/SRM 的关系**：CUPED 是方差层的优化，AA 检验/SRM 检查是正确性层的防线，三者组合使用；CUPED 后仍要做一次 AA 回归验证。

```python
# 基线:Python 3.10+;纯标准库模拟 CUPED 方差缩减(实验前数据作协变量)
# 真实场景:实验平台指标层;theta 用实验前数据估计并固定,检验时后处理校正
from __future__ import annotations
import random


def cov(x: list[float], y: list[float]) -> float:
    mx, my = sum(x) / len(x), sum(y) / len(y)
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / len(x)


def var(x: list[float]) -> float:
    return cov(x, x)


def run_experiment(n: int, rho: float, effect: float, seed: int = 42
                   ) -> tuple[float, float, float]:
    """生成两期行为:post = rho*pre + 噪声 + 处理效应(转化/活跃类指标强相关)。"""
    rng = random.Random(seed)                            # 种子固定,结果可复现
    control_pre, control_post, treat_pre, treat_post = [], [], [], []
    for _ in range(n):
        pre = rng.gammavariate(2.0, 5.0)                 # 实验前活跃度(重尾)
        post = rho * pre + rng.gauss(0, 6.0) + 10        # 与前期相关
        control_pre.append(pre); control_post.append(post)
        treat_pre.append(pre)
        treat_post.append(post + effect)                 # 处理组 +2 效应
    # CUPED:theta 用实验前数据估计(cov(pre,post)/var(pre))
    all_pre, all_post = control_pre + treat_pre, control_post + treat_post
    theta = cov(all_pre, all_post) / var(all_pre)
    mean_pre = sum(all_pre) / len(all_pre)

    def t_stat(post_c: list[float], post_t: list[float]) -> float:
        m_c, m_t = sum(post_c) / len(post_c), sum(post_t) / len(post_t)
        se = (var(post_c) / len(post_c) + var(post_t) / len(post_t)) ** 0.5
        return (m_t - m_c) / se

    def cuped(post: list[float], pre: list[float]) -> list[float]:
        return [y - theta * (x - mean_pre) for y, x in zip(post, pre)]

    t_naive = t_stat(control_post, treat_post)
    t_cuped = t_stat(cuped(control_post, control_pre), cuped(treat_post, treat_pre))
    vr = var(control_post) / var(cuped(control_post, control_pre))
    return t_naive, t_cuped, vr


def demo() -> None:
    n = 2000
    for rho in (0.85, 0.4, 0.0):
        t_naive, t_cuped, vr = run_experiment(n, rho, effect=2.0)
        print(f"前期相关性 rho={rho:.2f}: t 值 {t_naive:.2f} -> {t_cuped:.2f},"
              f" 方差降至 1/{vr:.2f}")
        assert t_cuped >= t_naive * 0.99
        if rho >= 0.4:
            assert vr > 1.05, "有相关时必须看到方差缩减"

    # 样本量换算:方差缩 1/vr 倍,所需样本也约缩 1/vr 倍
    _, _, vr = run_experiment(2000, 0.85, 2.0)
    print(f"所需样本量 ≈ 原 {20000:,} 的 1/{vr:.2f} ≈ {int(20000 / vr):,} ✅")
    assert vr > 1.5

    # 协变量缺失(新用户):填均值 = 不校正,退化为原始指标(不引入偏差)
    print("新用户协变量缺失 -> 填全局均值(校正项为 0),不引入偏差 ✅")


if __name__ == "__main__":
    demo()
```

**追问一**：为什么 θ 不能用实验期数据估计？
答：实验期数据里已经混着处理效应——处理组 post 偏高会让 θ 偏大，校正时把处理组"压回"更多，直接稀释甚至反转效应估计；且每次重估 θ 都改变检验统计量分布，等于偷偷做了多次检验。纪律是：实验前固定协变量与 θ 的估计规则。

**追问二**：CUPED 校正后指标的口径变了，业务方看不懂怎么办？
答：报告里同时给原始指标（业务口径）与 CUPED 校正指标（统计口径）：效应的绝对值用原始口径解释，显著性判定用校正口径；并附上方差缩减比例与相关系数，说明可信度提升来自哪里——口径透明比"只给一个 magic number"更重要。

## 背诵要点
- CUPED：`Y_cv = Y - θ(X - E[X])`，`θ = cov/var` 用实验前数据估计并在实验前固定；方差缩减 ≈ corr²，样本量同比缩减。
- 协变量必须实验前产生（否则效应泄露进校正项）；corr→0 时无收益也无害；SRM 排除前不要跑 CUPED。
- 新用户协变量缺失填均值（校正项为 0 不引入偏差）；报告双口径：业务口径讲效应、统计口径讲显著性。

## 复盘追问
- 实验上线一周后 CUPED 显示显著、原始口径不显著，能不能宣布胜利？（提示：校正口径可作提前决策依据，但要确认 θ 固定于实验前、SRM 通过、且没有中途换 θ/协变量的 peeking 行为）
- 指标是"实验期才存在的行为"（新功能使用率），CUPED 还能用吗？（提示：找不到前期协变量则退化；可换用"相关代理指标"做协变量，但需先验证代理与目标指标的前期相关性）
