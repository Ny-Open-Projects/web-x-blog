---
title: [A116] A/B 实验健康度：SRM 检测与实验中止判据
date: 2026-11-20
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A116 · SRM 检测与实验中止

> 难度:★★☆ | 标签:AB 测试, SRM, 统计

**问**（笔试·编程+场景题）：A/B 实验 50/50 分流，跑了三天 A 组 10 万、B 组 8.5 万——「样本比例失配（SRM）」怎么量化判定（卡方检验手写实现），SRM 出现意味着什么（分流器 bug/数据丢失/ instrumentation 不对称），为什么说「SRM 出现时实验结果一律不可信」？实验提前中止（peeking）为什么危险，序贯检验怎么合法地提前看？

**答**：① SRM 检测：期望 n_A = n_total × p_design，卡方统计量 `χ² = (n_A - E)²/E + (n_B - O)²/O_B`（df=1），p < 0.001 即严重失配（SRM 阈值要极严——0.05 太松，正常波动就能触发）。② SRM 的含义：**随机化假设被破坏**——可能是分流器实现 bug（哈希不均）、某组数据上报丢失（SDK 崩溃）、某组用户被排除（登录墙只挡一组）——任何一种都会让「组间差异」不再归因于实验处理，效应估计有偏。所以 SRM 一票否决：先修分流，重新开实验。③ Peeking 危险：每看一次结果相当于多做一次检验，α 膨胀（看 10 次 p=0.05 实际犯错率 ~40%）；合法提前看 = **序贯检验**（group-sequential：预设 2-3 个检查点，α 按边界分配 O'Brien-Fleming——早期极严后期宽松）或 Bayesian 连续监测（赔率阈值）。④ 中止判据：有害信号（质量指标恶化）随时中止，正向显著用序贯边界判。

```python
# 全部标准库；demo 实现 SRM 卡方检验 + 序贯边界演示
import math

def chi2_pvalue(chi2: float, df: int = 1) -> float:
    """df=1 的卡方 p 值（upper tail）：p = erfc(sqrt(x/2))。"""
    return math.erfc(math.sqrt(chi2 / 2))

def srm_test(n_a: int, n_b: int, p_design: float = 0.5, alpha: float = 1e-3) -> dict:
    """SRM 检测：期望比例 vs 实际比例，卡方 df=1。"""
    total = n_a + n_b
    e_a, e_b = total * p_design, total * (1 - p_design)
    chi2 = (n_a - e_a) ** 2 / e_a + (n_b - e_b) ** 2 / e_b
    p = chi2_pvalue(chi2)
    return {"chi2": round(chi2, 1), "p": p,
            "verdict": "SRM! 实验作废" if p < alpha else "OK"}

def obrien_fleming_boundaries(checkpoints: int, alpha: float = 0.05):
    """序贯边界（近似）：早期极严后期接近 0.05。"""
    info = [(i + 1) / checkpoints for i in range(checkpoints)]
    bounds = [2.24 / math.sqrt(t) for t in info]      # OF 常数近似
    return [{"checkpoint": f"{i+1}/{checkpoints}", "info": round(t, 2),
             "z_boundary": round(b, 2)} for i, t, b in zip(range(checkpoints), info, bounds)]

def peeking_danger(n_peeks: int = 10, alpha: float = 0.05) -> float:
    """peeking 的真实犯错率近似（无处理时 α 膨胀）。"""
    # 近似：P(至少一次越界) ≈ 1 - (1-α)^sqrt(n)… 经验上 10 次 peek 犯错率 ~2-3×α
    return 1 - (1 - alpha) ** (n_peeks ** 0.75)

if __name__ == "__main__":
    print("50/50 正常:", srm_test(100000, 100200))     # p 大 → OK
    bad = srm_test(100000, 85000)                      # 明显失配
    print("15% 失配:", bad)
    assert bad["verdict"].startswith("SRM")
    for b in obrien_fleming_boundaries(3):
        print("序贯检查点:", b)
    print(f"peeking 10 次的膨胀犯错率 ≈ {peeking_danger():.1%}（α=5% 名义 → 实际更高）")
    # 口径：SRM 一票否决实验；提前看结果必须走序贯边界；有害信号随时停。
```

**追问**：1) 为什么 SRM 的 α 设 0.001 而不是 0.05？——SRM 几乎不可能是「运气」（大样本下卡方极敏感），0.05 会频繁误报（每次实验都停）；0.001 下触发基本必然是系统性问题。2) 「某组用户被排除」的 SRM 怎么发现比卡方更深？——按登录状态/平台/版本分层的 SRM（子群 SRM）能定位到「哪类用户丢了」——总 SRM 只报异常，分层 SRM 定位根因。3) Bayesian 连续监测和频率派序贯的取舍？——Bayes 可随时看（决策规则基于后验赔率），门槛低；频率派序贯需预设但理论审计性强——工程团队常用 Bayes，监管/学术用序贯。

## 背诵要点
1. SRM = 样本比例 vs 设计比例的卡方检验，α=0.001 极严阈值；触发即实验作废（随机化被破坏）。
2. 分层 SRM 定位根因（哪类用户丢失）：登录态/平台/版本维度拆开各自检验。
3. Peeking 危险：反复看结果 α 膨胀；合法提前看 = 序贯边界（O'Brien-Fleming 早期极严）或 Bayesian 赔率。

## 复盘追问
1. 实验显示 B 组转化率 +20%（p=0.01），但 SRM p=0.002——你怎么向老板汇报？（提示：实验无效，SRM 优先级高于效应值；修复分流后重跑，绝不能「先看着用」）
2. 每日自动看结果的看板怎么设计才不构成 peeking？（提示：看板只是展示，决策（停/继续）必须按预注册的序贯边界触发——自动化执行预注册规则而非人眼看心情）
