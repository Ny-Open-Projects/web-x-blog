---
title: [WCN-618] 如何衡量元素库的「总体拥有成本（TCO）」并建立性能预算？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-618：如何衡量元素库的「总体拥有成本（TCO）」并建立性能预算？

**答**：
- 结论：TCO = 接入成本 + 运行时成本 + 维护成本；性能预算是其中「运行时成本」的可量化抓手（体积/INP/CLS/内存）。
- 做法：体积按 gzip 设预算并在 CI 门禁；运行时用 RUM 采 INP/长任务；维护成本用升级耗时与故障数度量。
- 追问钩子：预算_superfluous 怎么办？要区分「预算是护栏不是天花板」——偶发超标需评审豁免机制，避免团队为达标而造假。

```javascript
const BUDGET = {
  bundleGzipKB: 30,   // 单组件 gzip 上限
  inpMs: 200,         // 交互响应 P75
  cls: 0.1,           // 布局偏移
  memoryDeltaMB: 5,   // 挂载 100 实例的内存增量
};
function checkBudget(metrics) {
  return Object.entries(BUDGET).map(([k, limit]) => ({
    metric: k, limit, actual: metrics[k],
    pass: metrics[k] <= limit,
  }));
}
console.log(checkBudget({
  bundleGzipKB: 28, inpMs: 180, cls: 0.05, memoryDeltaMB: 4,
})); // 全部 pass：进入发布门禁
```
