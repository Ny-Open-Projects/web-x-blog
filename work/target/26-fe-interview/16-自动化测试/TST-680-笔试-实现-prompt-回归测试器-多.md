---
title: [TST-680] 笔试：实现 prompt 回归测试器（多模型 / 多 temperature 稳定性）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-680：笔试：实现 prompt 回归测试器（多模型 / 多 temperature 稳定性）

**题目**：实现 promptRegression(cases,models,temps,call,{runs})。对每个模型×temperature 组合，每条 case 跑 runs 次，输出必须全一致且等于 expected 才算通过；返回每组合通过率、是否全部稳定、最差组合。

**答**：
- 对每条 golden case 在每个模型 × 每个 temperature 下运行 N 次。
- 稳定性 = 输出完全一致的比例；一致性低于阈值即判失败。
- 输出每个组合的通过率与最不稳定 case。

```javascript
async function promptRegression(cases, models, temps, call, { runs = 3 } = {}) {
  const results = [];
  for (const model of models) for (const t of temps) {
    let consistent = 0;
    for (const c of cases) {
      const outs = [];
      for (let i = 0; i < runs; i++) outs.push(JSON.stringify(await call(model, t, c.input)));
      if (new Set(outs).size === 1 && outs[0] === JSON.stringify(c.expected)) consistent++;
    }
    results.push({ model, temp: t,
      rate: +(consistent / cases.length).toFixed(2) });
  }
  return {
    results,
    stable: results.every(r => r.rate >= 0.9),
    worst: results.sort((a, b) => a.rate - b.rate)[0],
  };
}
```

**评分点**：
- 三层循环（模型×温度×case×runs）完整
- 一致性判定严格（全等）
- 通过率与最差组合输出
- 异步调用处理正确
