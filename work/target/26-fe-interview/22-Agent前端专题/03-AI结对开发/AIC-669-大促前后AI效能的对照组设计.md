---
title: [AIC-669] 怎么设计「大促前后」的 AI 效能对照组？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-669：想证明 AI 真的提效了，对照组怎么设计？

**答**：
- 结论先行：**对照组的目的是排除「混淆变量」——PR 周期变短可能是需求简单了、人手熟了，而非 AI 的功劳**（AIC-302 归因）。好的对照让「只有 AI 这个变量不同」。
- 对照设计三选一：1) **前后对照**（同一团队引入 AI 前后）——最简单，但混淆变量最多（需求/人员/季节都在变），要选「同期对比」（去年大促 vs 今年大促）并控制项目复杂度；2) **组间对照**（AI 组 vs 非 AI 组）——同时间段、相似项目、相似人员构成，但现实中难以随机分配；3) **任务级对照**（同类任务 AI 做 vs 人工做）——控制任务复杂度，最可信但样本少。
- 必须控制的变量：团队规模、需求复杂度、人员经验、截止压力（大促本身就是强干扰）、代码库成熟度。
- 看什么指标：交付前置时间、缺陷逃逸率、7 天存活率——速度和质量一起看，避免「提效幻觉」。
- 统计严谨性：样本要够大，看趋势不看单点；大促是极端场景，结论要标注「仅适用大促类高强度场景」，别过度泛化。
- 追问钩子：为什么「同期对比」（去年 vs 今年大促）比「引入 AI 前后一个月对比」更有说服力？——因为前者控制了「季节性/大促节奏」这个最大混淆变量——大促本身会让团队进入高压高效状态，前后一个月的对比会把「大促效应」误算成「AI 效应」；同期对比抵消了季节因素。

```typescript
type Cohort = { name: string; aiUsed: boolean; leadTimeH: number; escapeRate: number; complexity: number };

function compareCohorts(a: Cohort, b: Cohort) {
  // 复杂度差异 > 20% 时对照不可信
  const confounded = Math.abs(a.complexity - b.complexity) / Math.max(a.complexity, b.complexity) > 0.2;
  return {
    valid: !confounded,
    leadTimeDiff: b.leadTimeH - a.leadTimeH,
    escapeRateDiff: b.escapeRate - a.escapeRate,
    reason: confounded ? '复杂度差异过大，对照不可信' : '可用于归因',
  };
}

const lastYear: Cohort = { name: '去年大促', aiUsed: false, leadTimeH: 20, escapeRate: 0.1, complexity: 100 };
const thisYear: Cohort = { name: '今年大促', aiUsed: true, leadTimeH: 12, escapeRate: 0.14, complexity: 105 };
const r = compareCohorts(lastYear, thisYear);
console.log(r.valid === true);            // 复杂度接近，对照可用
console.log(r.leadTimeDiff === -8);        // 前置时间缩短8h
console.log(r.escapeRateDiff === 0.04);    // 但逃逸率上升4% —— 提效幻觉信号
```
