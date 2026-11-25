---
title: [WCN-389] 当浏览器原生组件（如 dialog/input 新特性）覆盖元素库能力时的策略？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-389：当浏览器原生组件（如 dialog/input 新特性）覆盖元素库能力时的策略？
**答**：
- 评估：原生能力达元素库 80% 语义 → 元素变薄（包装原生 + 增强 a11y/样式）。
- 策略：渐进替换——元素内部实现换原生（API 不变，消费方无感）。
- 保留自研的理由：跨浏览器一致性/增强功能（原生不覆盖）。
- 原则：不与平台竞争，跟着平台走——元素是「过渡 + 增强」层。

```javascript
// dialog 原生化：元素内部换 <dialog>，对外 API 不变
class DsDialog extends HTMLElement {
  connectedCallback() {
    const d = document.createElement('dialog');   // 原生 top layer
    this._wire(d);                                 // 增强：a11y/主题/动画
  }
}
r
```
