---
title: [AIC-663] 团队 AI 效能度量，北极星指标该选什么？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-663：团队 AI 效能度量，北极星指标该选什么？

**答**：
- 结论先行：**北极星指标应反映「AI 带来的真实业务价值」，而不是「AI 使用量」**——推荐「单位时间有效交付价值」（如每周通过评审且 7 天存活的功能点数），而非「AI 生成代码行数」「调用次数」这类易作弊的虚荣指标。
- 为什么不用行数/调用量：代码行数可被 AI 灌水（AI 爱写冗长代码），调用量可被刷（开着不用也算）；它们衡量「投入」不衡量「产出」（Goodhart 定律，AIC-681）。
- 好的北极星指标特征：1) **与业务价值相关**：交付速度、质量、稳定性；2) **抗作弊**：难以通过表面行为刷高；3) **可分解**：能拆成团队/个人可行动的子指标；4) **平衡质量**：必须带质量约束（如「有效交付」已排除上线后回滚的代码）。
- 配套护栏指标：北极星之外必须有「缺陷逃逸率」「回滚率」「7 天存活率」作护栏——防止「交付变快但质量崩盘」的提效幻觉（AIC-305）。
- 追问钩子：为什么「7 天存活率」要纳入北极星而不仅是护栏？——因为它定义了什么是「有效交付」：写完就算交付是虚的，7 天后还在生产环境稳定跑的功能才是真交付；把存活率内嵌进交付定义，指标天然抗「写完就崩」的作弊。

```typescript
type Delivery = { points: number; tested: boolean; reviewPassed: boolean; survived7d: boolean; reverted: boolean };

function northStar(deliveries: Delivery[]): number {
  // 有效交付 = 通过评审 + 测试 + 7天存活 + 未回滚
  const effective = deliveries.filter(d =>
    d.reviewPassed && d.tested && d.survived7d && !d.reverted);
  return effective.reduce((s, d) => s + d.points, 0);
}

const week = [
  { points: 5, tested: true, reviewPassed: true, survived7d: true, reverted: false },  // 有效
  { points: 8, tested: true, reviewPassed: true, survived7d: false, reverted: true },  // 回滚，不算
  { points: 3, tested: false, reviewPassed: true, survived7d: true, reverted: false }, // 没测，不算
];
console.log(northStar(week) === 5); // 只算真正有效的 5 点
```
