---
title: [TST-984] 按需拉起测试环境（spawn on demand）看着省钱，实际有哪些隐藏成本？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-984：按需拉起测试环境（spawn on demand）看着省钱，实际有哪些隐藏成本？
**答**：
- 结论：按需环境省「闲置成本」，但增加「拉起延迟」与「状态一致性」成本——环境冷启、依赖回填、数据准备都要算进去。
- 要点：拉起时间可能 3~10 分钟，直接拖慢反馈；每个环境要重新准备数据，容易与共享环境不一致。
- 折中：核心稳定环境常驻池 + 临时环境按需；用快照模板加速拉起。
- 追问钩子：按需环境每次都要重新造数据，导致同一用例在 A 环境过、B 环境挂，你怎么根治？

```javascript
function envCost({ idleHours, spawnMinutes, runsPerDay, dataPrepMinutes }) {
  const idleCost = idleHours * 0.5;          // 常驻闲置成本
  const spawnCost = runsPerDay * spawnMinutes / 60 * 1.0; // 按需拉起成本
  const dataCost = runsPerDay * dataPrepMinutes / 60 * 0.5;
  return {
    alwaysOn: +(idleCost).toFixed(2),
    onDemand: +(spawnCost + dataCost).toFixed(2),
    advice: spawnCost + dataCost < idleCost ? '按需更省' : '常驻池更划算',
  };
}
console.log(envCost({ idleHours: 16, spawnMinutes: 5, runsPerDay: 40, dataPrepMinutes: 3 }));
// { alwaysOn:8, onDemand:4.83, advice:'按需更省' }
```
