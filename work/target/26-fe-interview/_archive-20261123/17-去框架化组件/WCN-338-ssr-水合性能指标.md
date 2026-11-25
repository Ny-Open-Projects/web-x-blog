---
title: [WCN-338] 元素水合的性能指标定义（比 TTI 更细）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-338：元素水合的性能指标定义（比 TTI 更细）？
**答**：
- 元素级指标：define 完成 / hydrate 完成 / interactive（首交互响应）三时刻。
- 聚合：页面「全部关键元素 interactive」时刻 = 元素级 TTI。
- 采集：元素生命周期打点上报（tag × 时刻）。
- 预算：关键元素 interactive < 2s（P75），超预算按元素归因优化。

```javascript
performance.mark(`ds:${tag}:defined`);
performance.mark(`ds:${tag}:interactive`);   // 首次事件响应后
report(performance.getEntriesByType('mark').filter(m => m.name.startsWith('ds:')));
r
```
