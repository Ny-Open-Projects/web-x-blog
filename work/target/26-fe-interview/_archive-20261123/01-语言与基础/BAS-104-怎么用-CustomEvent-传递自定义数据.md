---
title: [BAS-104] 怎么用 CustomEvent 传递自定义数据？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-104：怎么用 CustomEvent 传递自定义数据？
**答**：
- `new CustomEvent(type, { detail, bubbles })`：detail 携带任意数据，bubbles 让事件向上冒泡被外层捕获。
- 配合 dispatchEvent 实现同页面模块解耦，等于浏览器原生的发布订阅。
- 事件名加命名空间前缀防冲突；监听要在 dispatch 之前注册。

```javascript
// 发布方：任何地方
document.dispatchEvent(new CustomEvent('cart:added', {
  detail: { id: 42, count: 1 },
  bubbles: true,
}));
// 订阅方
document.addEventListener('cart:added', (e) => {
  console.log(e.detail.id, e.detail.count);  // 42 1
});
```

## 十二、网络与浏览器补充
