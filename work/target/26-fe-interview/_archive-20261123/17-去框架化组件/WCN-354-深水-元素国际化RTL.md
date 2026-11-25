---
title: [WCN-354] RTL（阿拉伯语）在元素层的完整支持？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-354：RTL（阿拉伯语）在元素层的完整支持？
**答**：
- 逻辑属性：margin-inline/padding-inline-start/inset-inline——物理属性 lint 拦截。
- 方向感知：元素读宿主 dir 属性（:host([dir=rtl]) 选择器）自动镜像。
- 图标/箭头：方向性图标翻转（chevron），非方向性（logo）不翻。
- 验证：RTL 快照矩阵（每组件 RTL 快照 + 键盘流不变）。

```javascript
/* 元素内部 */
.item { padding-inline-start: var(--ds-space-2); }  /* 非 padding-left */
:host([dir="rtl"]) .arrow { transform: scaleX(-1); }
r
```
