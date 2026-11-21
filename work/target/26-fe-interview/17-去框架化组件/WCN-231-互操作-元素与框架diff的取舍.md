---
title: [WCN-231] 什么时候「不」应该用 Web Components（反向决策）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-231：什么时候「不」应该用 Web Components（反向决策）？
**答**：
- 单框架团队 + 无跨框架需求：WC 的互操作收益为零，付出的是 DX 损失（无框架生态工具）。
- 强依赖框架运行时特性的组件（Suspense 流式/RSC 数据传递）——WC 难以对齐。
- 复杂状态联动密集的页面级组件——框架响应式更高效。
- 决策记分卡：跨框架消费数/长寿命预期/设计系统统一度 三项打分，低分不迁。

```javascript
const scorecard = {
  crossFramework: 0,      // 只有 React 用 → 0 分
  longevity: 4,           // 10 年寿命 → 高
  designSystem: 3,        // 统一设计系统 → 中
  verdict: '总分 7/12：暂不迁移，保持 React 实现',
};
r
```
