---
title: [AIC-729] 多模型 A/B 实验中如何控制变量与归因
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-729：多模型 A/B 实验中如何控制变量与归因

**答**：
- 结论先行：多模型 A/B 要「只变模型这一件事」——prompt、上下文、采样参数、评测集必须完全一致，否则无法把差异归因到模型本身。
- 控制要点：1) 固定随机种子与 temperature 降低波动；2) 同一批任务同时跑两组；3) 用配对比较（同一任务两组结果对比）而非分组均值，减少任务难度差异干扰。
- 归因陷阱：模型 API 可能静默升级；观测窗口太短会碰巧遇到简单任务；需记录模型版本号与时间戳。
- 追问钩子：为什么配对比较比分组均值更可信？——它消除了「任务本身难度」这个混杂变量，差异更纯粹来自模型。

```javascript
// 配对 A/B：同一任务跑两组，统计净胜
function pairedAB(tasks, runA, runB, judge) {
  let aWin = 0, bWin = 0, tie = 0;
  for (const t of tasks) {
    const [ra, rb] = [runA(t), runB(t)];       // 同任务、同 prompt、仅模型不同
    const w = judge(ra, rb);
    if (w === 'A') aWin++; else if (w === 'B') bWin++; else tie++;
  }
  return { aWin, bWin, tie, winner: aWin > bWin ? 'A' : bWin > aWin ? 'B' : 'tie' };
}
console.log(pairedAB([1, 2, 3], t => t + 1, t => t, (a, b) => a > b ? 'A' : 'B'));
// { aWin:3, bWin:0, tie:0, winner:'A' }
```
