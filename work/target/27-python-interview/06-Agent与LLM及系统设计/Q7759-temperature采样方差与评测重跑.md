---
title: "[Q7759] 同一评测跑了三遍分数不一样：temperature 采样与评测的方差治理"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7759 · 同一评测跑了三遍分数 82%/85%/79%：temperature 采样与评测的方差治理

难度：P6 ｜ 标签：LLM 评测、temperature、采样方差、复现性、置信判断

基线：Python 3.12；用加权随机模拟 temperature 0 与 0.9 的输出分布，演示评测通过率的波动与重跑次数决策。

**问**：跑评测集对比新旧提示词：旧版 82%、新版 85%，准备宣布改进有效；重跑一遍变成 79% vs 84%，结论反过来了。评测结论为什么这么不稳？temperature 该设多少、每条样本该跑几次？什么样的提升幅度才敢说"真的变好了"？

**答**：
- **结论**：温度 > 0 时每次生成都从分布里采样，评测分数是**随机变量的观测值**：50 条样本、单条通过概率 82% 时，三遍跑出 78%~86% 完全正常——单次评测的分数波动（采样方差）远大于提示词之间的真实差异，拿单次结果做 go/no-go 就是在掷硬币。治理三件套：① **固定采样参数做对比**： temperature=0（贪心解码）最可复现，适合回归对比与生产确定性场景；② **重跑取分布**：温度 > 0 的评测每条样本跑 N 次（通常 3~5）取通过率，报出区间而不是单值；③ **按样本量算分辨力**：50 条样本根本分不清 82% vs 85%（差异在噪声内），要么加大样本量、要么承认"看不出差异"。温度参数的选择本身是产品决策：创意类任务高温，抽取/工具调用类低温——评测要**模拟生产配置**，用 t=0 评测却以 t=0.7 上线，测的就不是上线的东西。
- **取舍**：① t=0 也有残余不确定性（服务端 batch、非正式的温度语义、模型版本抖动），严格回归仍要跑 2~3 遍确认零漂移；② 重跑次数与样本量是一对预算旋钮：样本少就多跑几次，样本多单次即可；③ 分数接近时不要硬比——给"无显著差异"留出口，把精力放到困难子集上；④ 对比实验要**同评测集同参数同时间窗**，混入模型版本变化就是混淆变量。
- **实战**：① 评测报告固定输出：n、通过率、每条样本的多次运行方差、与基线的差值区间；② go/no-go 规则前置写死（如"提升 > 5pp 且下界 > 0 才算通过"），防止事后解释；③ 生产与评测的温度配置进同一份配置表，禁止"评测一套上线一套"；④ 高方差样本（每次跑结果都不同的 case）单独归档，它们通常是提示词歧义的信号。

```python
"""采样方差与评测治理：temperature 模拟 + 重跑次数与样本量决策。"""
import random
import statistics


def sample_outcome(p_pass: float, temp: float, rng: random.Random) -> bool:
    """temperature 越高, 单次输出越接近分布本身的随机性。"""
    jitter = 0.0 if temp == 0 else temp * 0.12      # 模拟高温采样噪声
    return rng.random() < min(1.0, p_pass + rng.uniform(-jitter, jitter))


def run_eval(p: float, n: int, temp: float, times: int, seed: int) -> list[float]:
    rng = random.Random(seed)
    return [sum(sample_outcome(p, temp, rng) for _ in range(n)) / n
            for _ in range(times)]


def decide(old: list[float], new: list[float], min_pp: float = 5.0) -> str:
    diff = statistics.mean(new) - statistics.mean(old)
    spread_old = max(old) - min(old)
    spread_new = max(new) - min(old)
    noise = max(spread_old, spread_new)
    if abs(diff) < noise:
        return f"差异 {diff * 100:.1f}pp < 噪声 {noise * 100:.1f}pp -> 无显著差异, 不宜宣布"
    if diff >= min_pp / 100:
        return f"提升 {diff * 100:.1f}pp 超过噪声与门限 -> 通过"
    return f"变化 {diff * 100:.1f}pp 未达门限 {min_pp}pp -> 观察或加大样本"


if __name__ == "__main__":
    N = 50
    print("单次评测的波动 (n=50, 真实通过率 82%, temperature=0.7):")
    for i, s in enumerate(run_eval(0.82, N, 0.7, 3, seed=11), 1):
        print(f"  第{i}遍: {s:.0%}")
    print("\ntemperature=0 的回归对比 (真实 82% vs 85%):")
    old = run_eval(0.82, N, 0.0, 3, seed=42)
    new = run_eval(0.85, N, 0.0, 3, seed=42)
    print(f"  旧版: {[f'{s:.0%}' for s in old]} | 新版: {[f'{s:.0%}' for s in new]}")
    print("  判定:", decide(old, new))
    print("\n样本量对分辨力的影响 (真实差 3pp, t=0.7, 各跑5遍取均值):")
    for n in (50, 300, 2000):
        o = run_eval(0.82, n, 0.7, 5, seed=7)
        w = run_eval(0.85, n, 0.7, 5, seed=7)
        d = statistics.mean(w) - statistics.mean(o)
        print(f"  n={n:>5}: 均值差 {d * 100:+.1f}pp {'(仍在噪声内)' if abs(d) < 0.05 else '(可分辨)'}")
    print("\n结论：温度>0 的评测分数是随机变量; 单次结果不可做 go/no-go,")
    print("      报区间不报单值; 差异小于噪声时诚实说'看不出', 别硬比")
```

**追问一**：temperature=0 就完全确定了吗？

→ 解析：不是 100% 确定。多数 API 供应商的 t=0 只保证"取概率最高的 token"，但工程层面仍有扰动源：batch 内并发导致的数值舍入差异、模型服务商的版本静默更新、不同推理后端（GPU 型号/量化）的浮点差异、以及多 token 采样在 logit 几乎并列时的翻转。所以 t=0 的复现是"近似确定"：严格回归要跑 2~3 遍确认零漂移，跨时间窗的对比要校验模型版本号（Q7680 默认参数漂移的教训）。把 t=0 当"降低方差的主要手段"，而不是"绝对可复现的保证"。

**追问二**：重跑 3~5 次取平均就够了，还是该算真正的置信区间？

→ 解析：对 go/no-go 决策，跑 3~5 次看波动范围是廉价的工程做法，能挡住大多数误判；但样本量小（<100 条）且版本差异小时（2~3pp），经验波动范围会低估不确定性，应该上二项比例的置信区间（Wilson 区间最稳）：50 条样本 82% 的 95% 区间是 [69%, 90%]，一眼就能看出"根本分辨不了 82% vs 85%"。实践分层：日常迭代用重跑均值 + 前置规则；重大升级（换模型/换架构）用完整区间与样本量规划（A161 的统计功效思路），把"多少样本才够"在实验前算出来，而不是跑完再补救。
