---
title: [WCN-217] Qwik 的 resumability 模型与自定义元素结合的可能性与冲突？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-217：Qwik 的 resumability 模型与自定义元素结合的可能性与冲突？
**答**：
- Qwik 按需恢复（不预执行）——自定义元素的 define 在客户端注册时机与 Qwik 恢复模型冲突（元素注册是全局副作用）。
- 可行方向：Qwik loader 顺带执行元素注册（把 define 纳入恢复流）。
- DSD 与 Qwik 兼容好：首屏内容 HTML 直出，交互时才恢复元素逻辑。
- 结论：静态内容用 DSD 无缝；强交互元素需 Qwik 生态适配层。

```javascript
// Qwik 中延迟注册元素
import { $ } from '@builder.io/qwik';
export const ensureGoodsCard = $(async () => {
  await import('./goods-card');   // define 在此时执行
  await customElements.whenDefined('goods-card');
});
r
```
