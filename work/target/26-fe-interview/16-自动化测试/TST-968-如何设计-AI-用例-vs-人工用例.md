---
title: [TST-968] 如何设计「AI 用例 vs 人工用例」的可靠性对照实验，而不是凭感觉说 AI 不行？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-968：如何设计「AI 用例 vs 人工用例」的可靠性对照实验，而不是凭感觉说 AI 不行？
**答**：
- 结论：用同任务对照——同一批需求分别由 AI 和工程师写用例，在相同环境跑同样的轮次，对比 flake 率、缺陷发现数、维护成本。
- 控制变量：相同代码版本、相同测试框架、相同运行时长；样本量足够（多轮）避免偶然。
- 指标：缺陷检出率、flake 率、一周后存活率、单用例维护工时。
- 追问钩子：AI 用例缺陷检出率略低但维护成本高一倍，你会怎么给出「是否引入」的结论？

```javascript
function compareReliability(ai, human) {
  const metric = (g) => ({
    detectRate: +(g.bugsFound / g.totalBugs).toFixed(2),
    flakeRate: +(g.flakyRuns / g.runs).toFixed(2),
    survival: +(g.survived / g.total).toFixed(2),
    maintainCost: +(g.maintainHours / g.total).toFixed(2),
  });
  const a = metric(ai), h = metric(human);
  return {
    ai: a, human: h,
    verdict: a.detectRate >= h.detectRate * 0.9 && a.maintainCost <= h.maintainCost
      ? '可引入' : '需改进或限量使用',
  };
}
console.log(compareReliability(
  { bugsFound: 8, totalBugs: 10, flakyRuns: 3, runs: 100, survived: 18, total: 30, maintainHours: 6 },
  { bugsFound: 9, totalBugs: 10, flakyRuns: 1, runs: 100, survived: 28, total: 30, maintainHours: 3 }
).verdict); // '需改进或限量使用'
```
