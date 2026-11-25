---
title: [SCN-717] SLA 看板的改进项追踪闭环（问题→改进项→验证）怎么做？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-717：改进项追踪闭环怎么做？
**答**：
- 闭环链路：复盘产出改进项（负责人/期限/目标指标）→ 看板关联追踪（该指标改善情况）→ 到期自动检查 → 完成后指标确实改善则闭环，未改善打回重开。
- 防形式主义：改进项必须绑定「可验证的指标变化」（如 checkout LCP P95 从 3.2s 降到 2.8s），不能只写「优化性能」。
- 看板呈现：指标卡上的「改进中」角标 + 改进项列表（含进度与到期）；到期未完成自动升级提醒 owner 上级。
- 复盘沉淀：闭环的改进项自动进案例库（触发条件/方案/效果数据），下同类问题先查库。
- 追问钩子：怎么证明指标改善是改进项带来的而不是流量变化——改善声明要求附对照（同期流量/版本维度切片），不满足对照条件标「待验证」。

```javascript
const improvement = {
  create: ({ metricKey, target, deadline, owner }) => ({   // 必须绑定可验证目标
    validate: () => target.d && target.from,               // 从 X 到 Y
    onDue: async () => {
      const delta = await metrics.compare(metricKey, deadline, '-30d');
      return delta.achieved ? close(delta) : escalate(owner);   // 未达成升级
    },
    verification: 'must include traffic/version control slice',  // 对照要求
  }),
};
```
