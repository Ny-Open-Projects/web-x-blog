---
title: [WCN-290] 元素库的样式架构（Shadow 内样式与 token 的分层）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-290：元素库的样式架构（Shadow 内样式与 token 的分层）？
**答**：
- 层 1：reset/base（元素库全局一份 constructable stylesheet）。
- 层 2：元素结构样式（每元素内部，消费 token 变量）。
- 层 3：主题变量（宿主 :root/主题类，穿透进 shadow）。
- 原则：shadow 内不出现裸值（颜色/间距全部 var()），主题切换 = 只换变量不碰元素样式。

```javascript
const base = new CSSStyleSheet();
base.replaceSync(`:host { display: block; box-sizing: border-box; }
.button { background: var(--ds-btn-bg); padding: var(--ds-space-2); }`);
r
```
