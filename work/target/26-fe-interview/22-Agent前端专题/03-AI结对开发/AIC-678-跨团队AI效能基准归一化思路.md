---
title: [AIC-678] 想做跨团队 AI 效能基准，归一化怎么做？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-678：想做跨团队 AI 效能基准，归一化怎么做？

**答**：
- 结论先行：**归一化的目标是让「不同背景的团队可比」——核心是「比相对提升」而非「比绝对数值」，并用复杂度系数对齐任务难度**（AIC-674 跨团队对比）。
- 三个归一化维度：1) **复杂度系数**：给每个团队的任务按难度分级，算「复杂度加权交付点」= Σ(功能点×难度系数)；2) **基线归一**：每队指标除以自身引入 AI 前的基线，得到「提升倍数」——消除起点差异；3) **规模归一**：按人天、按迭代周期归一化，消除团队规模差异。
- 基准的形式：与其给「绝对排名」，不如给「分位带 + 实践标签」——如「提升率 P50=30%，P75=50%」并标注高提升团队的实践（如「A 队用了任务卡模板」）——目的是传播实践而非制造排名压力。
- 数据可信度：归一化前先确认数据口径一致（什么算「有效交付」各队理解是否相同）——口径不统一，归一化就是在精致地计算错误数据。
- 追问钩子：为什么基准要「传播实践」而非「制造排名」？——因为排名会激励各队优化数字（古德哈特定律），而「看谁做得好 + 学他的做法」激励的是真实改进；基准的终极价值是组织学习，不是绩效考核。

```typescript
type TeamData = {
  name: string; points: number; complexityCoeff: number;
  baseline: number; personDays: number; practice?: string;
};

function normalizeBenchmark(teams: TeamData[]) {
  return teams.map(t => {
    const weighted = t.points * t.complexityCoeff;
    const perPersonDay = weighted / Math.max(1, t.personDays);
    const improvement = (perPersonDay - t.baseline) / Math.max(0.001, t.baseline);
    return { name: t.name, normalized: perPersonDay, improvement, practice: t.practice };
  }).sort((a, b) => b.improvement - a.improvement);
}

const teams = [
  { name: 'A队', points: 20, complexityCoeff: 1.5, baseline: 2, personDays: 20, practice: '任务卡模板' },
  { name: 'B队', points: 40, complexityCoeff: 0.8, baseline: 3, personDays: 30 },
];
const r = normalizeBenchmark(teams);
console.log(r[0].name === 'A队'); // A队提升率更高（复杂度加权+基线归一后）
console.log(r[0].practice === '任务卡模板'); // 基准附带可学实践
```
