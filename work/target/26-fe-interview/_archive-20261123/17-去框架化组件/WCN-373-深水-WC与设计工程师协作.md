---
title: [WCN-373] Design Engineer 角色在 WC 体系中的职责与工作流？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-373：Design Engineer 角色在 WC 体系中的职责与工作流？
**答**：
- 职责：设计到实现的「语义翻译」（token 化/动效规格/微交互）+ 元素打磨（动画/边界态）。
- 工作流：设计稿 → 设计工程师实现原型（真实元素）→ 工程接手补齐（测试/边缘）。
- 工具链：设计工程师用同一元素库（文档站 playground）迭代——设计与实现零翻译损耗。
- 产出物：motion 规范/边界态清单/微交互 demo 进元素文档。

```javascript
const deRole = {
  duty: ['语义翻译（token/动效）', '微交互打磨', '边界态清单'],
  flow: '原型（真元素）→ 工程补齐',
  output: 'motion 规范 + demo 进文档站',
};
r
```
