---
title: [JS-163] 被动事件 passive 是什么原理？为什么能提升滚动性能？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-163：被动事件 passive 是什么原理？为什么能提升滚动性能？

**答**：
- 问题根源：浏览器在滚动前必须等待 touch/wheel 监听器执行完——因为你可能在里面 `preventDefault()` 阻止滚动。
- `{ passive: true }` 向浏览器承诺「绝不调用 preventDefault」，浏览器不必等监听器就能立即滚动，掉帧明显减少。
- Chrome 56+ 对 document 级的 touchstart/touchmove 默认 passive；wheel 需要显式声明。
- 需要阻止滚动的场景（弹层锁滚动）必须显式 `{ passive: false }`，否则 preventDefault 无效并报警告。
- 优先用 CSS（`overflow: hidden` / `overscroll-behavior`）解决滚动锁，性能与语义都更好。

```javascript
const body = document.body;

// passive 监听：只观察，不阻止 → 滚动零阻塞
body.addEventListener('wheel', (e) => {
  reportScroll(e.deltaY);          // 埋点/视差等只读场景
}, { passive: true });

// 需要阻止滚动的场景必须显式非 passive
let locked = false;
body.addEventListener('wheel', (e) => {
  if (locked) e.preventDefault();  // passive: false 才生效
}, { passive: false });

function lockScroll(on) {
  locked = on;
  // 更推荐 CSS 方案：不占监听器，浏览器原生处理
  document.documentElement.style.overflow = on ? 'hidden' : '';
}

// passive 写法速记：
// 1. 只读事件的监听器一律加 { passive: true }
// 2. touchstart/touchmove/wheel 默认是否 passive 因浏览器而异，别依赖默认值
// 3. passive 里调 preventDefault 不会报错，但会被忽略并在控制台告警
```
