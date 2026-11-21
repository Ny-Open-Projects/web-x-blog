---
title: [JS-160] 事件流三阶段与 stopPropagation 的深解？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-160：事件流三阶段与 stopPropagation 的深解？

**答**：
- 三阶段：捕获（window → target）→ 目标阶段 → 冒泡（target → window）；addEventListener 第三参 true 表示捕获阶段监听。
- 目标阶段的监听按注册顺序执行，此时捕获/冒泡标记不参与排序。
- `stopPropagation` 阻断事件继续传播（向上/向下），但同层后注册的监听仍会执行。
- `stopImmediatePropagation` 更狠：连同层后续监听一起拦掉。
- 应用：捕获阶段适合做全局埋点/兜底拦截，冒泡阶段适合事件委托。

```javascript
const box = document.getElementById('box');
const btn = document.getElementById('btn');

// 事件流演示
document.addEventListener('click', () => console.log('1 document 捕获'), true);
box.addEventListener('click', () => console.log('2 box 捕获'), true);
btn.addEventListener('click', () => console.log('3 btn 目标阶段（按注册顺序）'));
box.addEventListener('click', () => console.log('4 box 冒泡'));
document.addEventListener('click', () => console.log('5 document 冒泡'));
// 点击 btn 输出：1 → 2 → 3 → 4 → 5（捕获 window 向下，冒泡 target 向上）

// stopPropagation：阻断传播，同层不拦
btn.addEventListener('click', (e) => {
  e.stopPropagation();   // box/document 的冒泡监听不再收到
});
btn.addEventListener('click', () => console.log('我还会执行')); // 同层仍执行

// stopImmediatePropagation：同层也拦
const el = document.createElement('button');
el.addEventListener('click', (e) => e.stopImmediatePropagation());
el.addEventListener('click', () => console.log('不会执行'));   // 被同层拦截
el.click();
```
