---
title: [TST-676] LLM-as-judge 的结果可信度怎么保障？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-676：LLM-as-judge 的结果可信度怎么保障？

**答**：
- 结论：多模型投票 + 多次采样 + 置信度门槛，三者缺一不可。
- 同一用例跑 3 个模型，2/3 一致才采信；不一致升级人工。
- 定期用「黄金集」（人工标注样本）校准模型，统计准确率漂移。
- 追问钩子：三个模型一致但答案是错的，你怎么发现？

```javascript
function juryDecide(votes, { threshold = 0.7 } = {}) {
  const yes = votes.filter(v => v.pass && v.confidence >= threshold).length;
  const ratio = yes / Math.max(1, votes.length);
  return {
    pass: ratio >= 2 / 3,
    ratio: +ratio.toFixed(2),
    escalate: ratio > 0 && ratio < 2 / 3,
  };
}
```
