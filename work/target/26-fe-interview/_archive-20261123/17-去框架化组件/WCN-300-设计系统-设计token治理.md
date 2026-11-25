---
title: [WCN-300] token 的命名与治理（避免 token 膨胀/别名混乱）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-300：token 的命名与治理（避免 token 膨胀/别名混乱）？
**答**：
- 三层命名：基础层（primitive：blue-500）→ 语义层（semantic：color-action-primary）→ 组件层（component：btn-bg，可选）。
- 消费只允许语义层以上——基础层直用会锁死主题。
- 膨胀治理：季度 token 审计（使用计数为零的删除）、新增需理由（为何现有不够）。
- 弃用映射：删除 token 先保留别名一个版本（var(--old, var(--new))）。

```javascript
/* 基础 */ --ds-blue-500: #165DFF;
/* 语义（消费层用这个） */ --ds-color-action: var(--ds-blue-500);
/* 组件（可选） */ --ds-btn-bg: var(--ds-color-action);
r
```
