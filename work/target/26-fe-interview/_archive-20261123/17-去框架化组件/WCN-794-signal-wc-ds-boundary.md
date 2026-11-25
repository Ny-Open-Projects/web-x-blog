---
title: [WCN-794] Signals + WC + 设计系统融合时，状态与样式边界如何划分？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-794：Signals + WC + 设计系统融合时，状态与样式边界如何划分？

**答**：
- 结论：职责分层——设计系统管「样式与 token」（CSS 变量、::part），WC 管「DOM 封装与 API 契约」，Signals 管「跨组件状态与派生逻辑」；三者通过薄适配层连接，避免互相侵入。
- 状态边界：Signals 在 WC 外持有状态，通过 property 注入 WC；WC 内部事件回写 signal，不直接在 WC 内引入框架信号库（保持 WC 框架无关）。样式边界：WC 消费 CSS 变量，不感知 token 来源。
- 追问钩子：WC 内部也需要响应式（如内部计数器）怎么办？考察「WC 内部用极简本地状态，复杂状态上提到 signal 层」。

```javascript
// 状态在 signal 层，WC 只消费 property + 派发事件
const count = signal(0);
const btn = document.querySelector('ds-button');
count.subscribe?.(() => {});
function sync() { btn.count = count.value; }        // property 注入
btn.addEventListener('ds-change', (e) => { count.value = e.detail; }); // 事件回写
// WC 内部样式只认 CSS 变量，不关心 token 来源
btn.attachShadow?.({ mode: 'open' });
console.log('三层各司其职：token 样式 / WC 封装 / signal 状态');
```
