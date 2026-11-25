---
title: [AIC-674] 跨团队比 AI 效能，怎么避免「不公平对比」？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-674：跨团队比 AI 效能数据，怎么避免不公平对比？

**答**：
- 结论先行：**跨团队对比前必须「归一化」——不同团队的业务复杂度、代码库成熟度、人员构成天差地别，直接比绝对数是误导**（AIC-670 对照混淆）。
- 归一化的维度：1) **任务复杂度加权**：把交付点按复杂度分级（简单1/中等2/复杂3），比「加权交付点」而非原始数；2) **基线对齐**：比「相对自身基线的提升率」而非绝对值——一个从 10 提到 15（+50%）的团队比从 100 提到 110（+10%）的团队进步更大；3) **人员构成**：新老比例不同会影响学习效率；4) **代码库成熟度**：老系统（存量债务多）的提效空间天然小于新项目。
- 对比的正确姿势：1) **同类团队比**：业务线相似、技术栈相似的团队之间比；2) **看趋势不看排名**：A 队本月比上月进步多少，比「A 队第一 B 队第二」更有 actionable 信息；3) **分享实践而非施压**：对比的目的是发现「谁的做法值得学」，不是给落后团队扣分——否则会诱发数据造假。
- 追问钩子：为什么「比提升率」比「比绝对值」更公平？——因为绝对值受起点影响巨大；一个基线很低的团队（因为历史债务重）即使进步巨大，绝对值仍可能落后；比提升率承认了「起点不同」，衡量的是「AI 对你有多大帮助」——这才是 AI 效能度量的本意。

```typescript
type Team = { name: string; baseline: number; current: number; complexityFactor: number };

function fairCompare(teams: Team[]) {
  return teams.map(t => ({
    name: t.name,
    absolute: t.current,
    normalized: t.current / t.complexityFactor,   // 复杂度归一
    improvementRate: (t.current - t.baseline) / t.baseline, // 相对自身基线
  })).sort((a, b) => b.improvementRate - a.improvementRate); // 按提升率排，而非绝对值
}

const teams = [
  { name: '老系统组', baseline: 10, current: 15, complexityFactor: 3 }, // 提升50%
  { name: '新项目组', baseline: 100, current: 110, complexityFactor: 1 }, // 提升10%
];
const r = fairCompare(teams);
console.log(r[0].name === '老系统组'); // 按提升率，老系统组第一
console.log(r[0].absolute < r[1].absolute); // 但绝对值更低 —— 绝对排名会误判
```
