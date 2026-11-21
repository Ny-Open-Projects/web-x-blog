---
title: [Q7065] 数据作业云成本账与 Spot 策略
date: 2026-11-20
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7065 · 数据作业云成本账与 Spot 策略

难度：P6 | 标签：成本工程、Spot、容量规划、数据管道

**问**：月度数据作业的 EC2/云主机账单超预算 3 倍。"全部换 Spot 实例"为什么不是标准答案？怎么给每类作业算成本账、定资源策略？

**答**：
- **结论**：成本账公式：月成本 = 单价 × 时长 + 期望中断次数 × 单次重跑代价 + SLA 风险定价。Spot 折扣 60-70%，但中断率 10-15% 意味着长作业几乎必然被杀：如果作业可断点续跑且重跑便宜，Spot 净赚；如果重跑 4 小时还可能二次中断、错过下游 SLA，损失吃掉全部折扣。正确姿势是分账：批处理/重跑友好任务 → Spot + checkpoint；关键路径（按时交付的日报/训练）→ 包年/预留 + 固定窗口；弹性尖峰（临时回填）→ Spot 自动扩容 + 任务幂等。
- **取舍**：预留/包年是确定性溢价：单价降 30-40% 但锁容量，适合负载基线；Spot 是风险折扣，需要任务架构配合（checkpoint、幂等、重试上限）。事故复盘常见根因是"用按需跑批"——没人算账，默认选项最贵。
- **实战**：落地三步：① 按作业打标签（任务名/负责人/关键性），账单可归因，否则治理无从下手；② 每类作业记录"时长-中断率-重跑代价"三参数，进成本模型自动化选型；③ 作业内存 compute 层可换（Docker 化），才能在策略间迁移。 checkpoint 设计是 Spot 化的前置条件：没有 checkpoint 的 6 小时作业换 Spot 等于赌博。

```python
"""数据作业云成本账：按需 vs 抢占式 vs 包年，含中断重跑成本。"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Plan:
    name: str
    hourly: float        # 每小时单价
    reliability: float   # 不被中断的概率
    rerun_cost: float    # 单次中断的重跑代价（小时数折算的钱）

def monthly_cost(plan: Plan, hours: int) -> float:
    base = plan.hourly * hours
    interruptions = hours * (1 - plan.reliability)          # 期望中断次数
    return base + interruptions * plan.rerun_cost

plans = [
    Plan("on-demand", 1.00, 1.0, 0.0),
    Plan("spot",      0.30, 0.85, 0.30 * 2),   # 中断后重跑 2 小时的量
    Plan("reserved",  0.60, 1.0, 0.0),
]
HOURS = 24 * 30
for p in plans:
    print(f"{p.name:>10}: {monthly_cost(p, HOURS):8.1f} 元/月")

def choose(plans, hours, sla_penalty_per_interruption_hour):
    scored = [(p.name, monthly_cost(p, hours)
               + sla_penalty_per_interruption_hour * hours * (1 - p.reliability))
              for p in plans]
    return min(scored, key=lambda x: x[1])

print("带 SLA 风险定价后的选择:", choose(plans, HOURS, sla_penalty_per_interruption_hour=0.5))
print("结论：Spot 便宜的前提是可断点续跑且重跑代价低；关键路径才谈包年/预留")
```

**追问链**：
1. 追问一层：Spot 化的作业，checkpoint 间隔怎么定？——间隔 = 可接受的最大重复计算时间，通常 5-15 分钟；间隔太小 checkpoint IO 占比高（自身就是成本），太大则中断重跑代价上升，两边要进成本模型平衡。
2. 追问二层：为什么"账单打标签"是成本治理的第一步而不是选实例？——无法归因的账单无法定位"谁贵了、为什么贵"；标签齐全后才能按作业维度做预算、告警与选型实验。

**背诵要点**：
1. 成本账 = 单价×时长 + 中断期望×重跑代价 + SLA 风险定价。
2. 分账策略：可续跑批处理上 Spot，关键路径包年，尖峰回填弹性 Spot+幂等。
3. Spot 化前置条件是 checkpoint 与幂等；账单先打标签再谈优化。

**复盘追问**：
1. Spot 中断率从 10% 涨到 40%，作业频繁重跑错过 SLA，短期怎么止血？（关键作业切回按需，长期做 checkpoint 改造）
2. 为什么"人均成本"和"作业成本"两个视角都重要？（前者管预算归因，后者管技术选型，混着看会做出互相矛盾的决策）
