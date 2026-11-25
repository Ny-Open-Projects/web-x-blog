---
title: [TST-671] AI 测试助手的端到端价值怎么评测（不只看采纳率）？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-671：AI 测试助手的端到端价值怎么评测（不只看采纳率）？

**答**：
- 结论：价值 = 节省时长 + 缺陷发现增量 − 误报处理成本，四项都要量化。
- 用 A/B 对照：一组用助手一组不用，比较单位时间的有效缺陷数与回归时长。
- 采纳率高但缺陷发现没提升，说明生成的是「有效但无价值」的测试。
- 追问钩子：助手让测试数量翻倍但评审成本也翻倍，你怎么算净收益？

```javascript
function valueScore({ savedMin, bugsFound, falsePositives, reviewMin, rate = 1 }) {
  const net = savedMin * rate + bugsFound * 20
    - falsePositives * 5 - reviewMin;
  return { net, positive: net > 0,
    roi: +(net / Math.max(1, reviewMin)).toFixed(2) };
}
console.log(valueScore({ savedMin: 100, bugsFound: 2,
  falsePositives: 10, reviewMin: 60 }));
```
