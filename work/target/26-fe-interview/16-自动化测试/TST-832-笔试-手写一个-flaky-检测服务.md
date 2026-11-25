---
title: [TST-832] 笔试：手写一个「flaky 检测服务」，根据历史执行记录计算不稳定分数
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-832：笔试：手写一个「flaky 检测服务」，根据历史执行记录计算不稳定分数
**答**：
- 需求：实现 flakyScore(history) —— history 是每条用例的 {id, results:boolean[]} 数组，输出 flaky 分数与判定。
- 规则：分数 = 结果不一致次数 / 相邻结果对比次数；分数 > 0.1 判为 flaky。
- 边界：结果不足 2 次返回 0（数据不足）；全通过或全失败分数为 0（稳定），需单独标记 alwaysFail。

```javascript
function flakyScore(records) {
  return records.map(r => {
    const seq = r.results || [];
    if (seq.length < 2) return { id: r.id, score: 0, verdict: '数据不足' };
    let flips = 0;
    for (let i = 1; i < seq.length; i++) if (seq[i] !== seq[i - 1]) flips++;
    const score = Number((flips / (seq.length - 1)).toFixed(3));
    const alwaysFail = seq.every(v => v === false);
    return {
      id: r.id, score,
      verdict: alwaysFail ? 'alwaysFail' : score > 0.1 ? 'flaky' : 'stable',
    };
  });
}
console.log(flakyScore([
  { id: 'A', results: [true, true, true, true] },
  { id: 'B', results: [true, false, true, false] },
  { id: 'C', results: [false, false, false] },
])); // A stable, B flaky(1.0), C alwaysFail

// 单点结果不足的用例不会被误判
console.log(flakyScore([{ id: 'D', results: [true] }])); // 数据不足
```
**评分点**：
- 分数算法：相邻结果翻转次数 / 对比次数，正确区分「不稳定」与「稳定失败」。
- 数据不足（<2 次）返回 0 并标记，避免误判。
- alwaysFail 单独标记，因为 flaky 分数低但其实是真失败。
- 输出 verdict 可执行，体现 flaky 治理自动化的落地。
