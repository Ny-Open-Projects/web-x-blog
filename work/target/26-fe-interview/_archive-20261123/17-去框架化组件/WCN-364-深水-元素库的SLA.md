---
title: [WCN-364] 元素库对业务方的服务 SLA 承诺？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-364：元素库对业务方的服务 SLA 承诺？
**答**：
- 缺陷响应：P0（不可用/a11y 致命）4h 修复或规避方案；P1 两个工作日。
- 需求响应：新组件/新属性需求评审 SLA（5 工作日给结论）。
- 兼容承诺：API 弃用至少一个大版本周期（≥ 3 个月）。
- 透明度：SLA 达成率公开看板——承诺才有约束。

```javascript
const sla = {
  p0: '4h fix-or-mitigate',
  p1: '2 工作日',
  feature: '5 工作日评审结论',
  deprecation: '≥ 1 major / ≥ 3 个月',
  dashboard: 'SLA 达成率公开',
};
r
```
