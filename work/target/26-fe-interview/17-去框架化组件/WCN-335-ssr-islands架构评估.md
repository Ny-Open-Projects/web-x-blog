---
title: [WCN-335] 元素级 islands 架构的适用性评估（什么时候值得）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-335：元素级 islands 架构的适用性评估（什么时候值得）？
**答**：
- 值得：内容为主 + 交互稀疏（文档站/营销页/电商详情）——JS 传输量大幅下降。
- 不值得：交互密集应用（后台管理）——几乎全是岛屿，架构开销无收益。
- 度量驱动：页面交互元素占比 > 60% → 全水合更简单；< 30% → islands 收益明显。
- 混合策略：按页面路由选择模式（详情页 islands / 后台全水合）——路由级决策。

```javascript
const decision = (interactivityRatio) =>
  interactivityRatio < 0.3 ? 'islands' :
  interactivityRatio > 0.6 ? 'full-hydrate' : 'hybrid（关键岛+整页水合）';
r
```
