---
title: [WCN-298] Figma（设计）到 WC（代码）的自动化链路实践？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-298：Figma（设计）到 WC（代码）的自动化链路实践？
**答**：
- Figma 组件与 WC 组件一一映射（命名约定 ds-button ↔ ds-button）。
- token 双向：Figma variables ↔ tokens.json 同步（设计改 token → PR 自动生成）。
- 标注即验收：Figma dev mode 标注 token 名，实现用同 token——review 时对账。
- 不追求像素级自动生成代码：生成「结构骨架 + token 引用」，交互逻辑人写。

```javascript
// Figma variable → token 映射
figma.variables.forEach(v => tokens[mapName(v.name)] = v.value);
// ds-button/btn-primary → --ds-btn-primary
r
```
