---
title: [WCN-348] 一个真实演进案例：ds-table 从简单到复杂（API 兼容策略）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-348：一个真实演进案例：ds-table 从简单到复杂（API 兼容策略）？
**答**：
- v1：columns property + 基础渲染；v2 加排序/筛选（property 扩展 + 新事件，minor）。
- v3 虚拟滚动（渲染重构但 API 不变，patch/minor）——渲染可换 API 稳。
- v4 列插槽（slot/渲染函数二选一）——与 v3 渲染函数并存一个版本后弃用（major）。
- 教训：渲染级重构随时可做；API 面变更必须走弃用周期。

```javascript
const evolution = {
  v2: '+sort/filter (minor, 事件新增)',
  v3: '虚拟滚动渲染重构（API 不变）',
  v4: '列 slot 化：render fn 弃用一版本 → v5 移除 (major)',
};
r
```
