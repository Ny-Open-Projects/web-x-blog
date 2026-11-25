---
title: [Q7697] best-of-n 多候选生成的成本质量分界
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7697 · best-of-n 多候选生成的成本与质量分界

难度：P6 ｜ 标签：成本工程、best-of-n、采样、质量评估

基线：Python 3.9+；temperature 采样 n 候选；judge 模型或规则打分选优。

**问**：为了提升代码生成质量，团队把"生成一次"改成"生成 5 个候选再挑最好的"，质量确实好了，成本涨了 6 倍。best-of-n 的边际收益曲线长什么样？n 取几最划算？有没有比"无脑乘 n"更省钱的结构？

**答**：
- **结论**：best-of-n 的收益是**次序统计量的边际递减**：候选质量分布给定时，best-of-2 提升最陡，n=5 之后每加一个候选的提升通常只剩一半以下；而成本严格线性（n 倍生成费 + judge 费），所以"成本/质量"的分界点常在 n=3~4。更省钱的结构：(1) **best-of-n 只对"高风险请求"开**——用启发式（任务复杂度/历史失败率）决定 n，简单请求 n=1；(2) **自适应串行**（先生成 1 个，judge 低于阈值再补采）——期望成本远低于固定 n=5，因为大多数请求第一个就过线；(3) **pass@k 语义**：如果下游还有人工筛选，一次 n 个候选的价值 = pass@k 提升，不必全合格。
- **取舍**：judge 本身的可靠性是隐藏成本——judge 偏差会把"看起来好"的候选选出来（冗长偏好），等于花了 n 倍钱买到错的选择；所以选优标准要与真实质量指标对齐（离线评测校准 judge）。另外多候选带来的延迟问题：并行生成不增加墙钟时间，但吞吐占用翻倍，TPM 配额账要按 n 倍算。
- **实战**：算式——固定 n=5 的期望成本 = 5×生成价 + judge 价；自适应串行期望成本 = 1×生成价 + P(不过线)×(4×生成价) + judge 价×轮数，当首过率 70% 时约等于 2.4×生成价，省一半以上。

```python
# best-of-n 成本/收益账：固定 n vs 自适应串行（标准库可运行）。
def quality_gain(n: int, base: float = 0.55, cap: float = 0.88) -> float:
    """次序统计量近似的边际递减收益曲线。"""
    return min(cap, base + (cap - base) * (1 - 1 / n) * 0.9)

def cost_fixed(n: int, gen: float, judge: float) -> float:
    return n * gen + judge

def cost_adaptive(gen: float, judge: float, first_pass: float = 0.7,
                  max_n: int = 5) -> float:
    """先生成 1 个，judge 不过线再补采，最多 max_n。"""
    expected_gens = 0.0
    p_survive = 1.0
    for _ in range(max_n):
        expected_gens += p_survive          # 本轮生成的期望次数
        p_survive *= (1 - first_pass)       # 没过线的概率继续
    return expected_gens * gen + judge

if __name__ == "__main__":
    gen, judge = 0.004, 0.001
    prev_q, prev_c = quality_gain(1), cost_fixed(1, gen, judge)
    print(f"n=1: 质量 {prev_q:.2f}，成本 {prev_c:.3f}")
    for n in (2, 3, 5, 8):
        q, c = quality_gain(n), cost_fixed(n, gen, judge)
        marginal = (c - prev_c) / (q - prev_q) * 100  # 每多 1 分质量的边际成本
        print(f"n={n}: 质量 {q:.2f}，成本 {c:.3f}，边际 {marginal:.0f} 元/分")
        prev_q, prev_c = q, c
    print("自适应串行期望成本:", round(cost_adaptive(gen, judge), 3),
          "(首过率70%, 相当于固定 n≈2.4 的钱买接近 n=5 的质量)")
    # n=2 每提升 1 分质量约 3 元；n=3 起涨到 8 元；n=5 后 20 元+ ——
    # 边际成本陡增的分界在 n=3~4，之后是纯烧钱。
```

**追问**：
- 一层：为什么"并行 n 个"和"串行自适应"的质量上限一样但成本差一倍？→ 提示：自适应把"大概率首过"的信息变现了——只对困难请求付剩余的 n-1 次；代价是困难请求的延迟变长（串行轮次）。
- 二层：judge 怎么校准才不会"选错"？→ 提示：用已知优劣对（离线评测集）测 judge 一致率，必要时双 judge 投票；judge prompt 里防冗长/格式偏好。

**背诵要点**：
1. best-of-n 收益边际递减（best-of-2 最陡），成本线性 n 倍；单位质量成本拐点在 n=3~4。
2. 更省结构：高风险请求才开 best-of-n；自适应串行（首过率 70% 时成本 ≈ 固定 n=2.4）。
3. judge 偏差是隐藏成本，选优标准必须与真实指标对齐；TPM 配额按 n 倍入账。

**复盘追问**：
1. 为什么上线前没发现成本涨 6 倍？提示：新策略没有单独的成本标记维度；成本账要按功能开关分账。
2. 如果质量指标（人工采纳率）没变但费用降不下来，说明什么？提示：n=5 的增益被 judge 误差或下游筛选抵消，先修选优再谈降 n。
