---
title: [WCN-729] 用 Signals 管理超大列表的虚拟滚动状态，怎么设计才不掉帧？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-729：用 Signals 管理超大列表的虚拟滚动状态，怎么设计才不掉帧？

**答**：
- 结论：把 scrollTop 放进 signal，用 computed 派生可见区间 start/end 与偏移 transform；列表项数据用细粒度 signal，滚动只更新偏移，不重建整列表。
- 对 scroll 事件做 rAF 节流，避免每帧多次写入；行高固定时用查表 O(1) 算索引，不定高用前缀和缓存。
- 追问钩子：滚动时每一项都订阅了全局 scrollTop signal 会怎样？考察「订阅粒度」——应让每行只订阅自己的是否可见派生值。

```javascript
const scrollTop = signal(0);
const ROW = 40, VIEWPORT = 600, TOTAL = 100000;
const start = computed(() => Math.max(0, Math.floor(scrollTop.value / ROW) - 2));
const count = computed(() => Math.ceil(VIEWPORT / ROW) + 4);
const offsetY = computed(() => start.value * ROW);
let ticking = false;
window.addEventListener('scroll', () => {
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => { scrollTop.value = window.scrollY; ticking = false; });
}, { passive: true });
// 仅渲染 [start, start+count) 的行，并用 offsetY 做 transform
console.log('可见区间:', start.value, count.value, '偏移:', offsetY.value);
```
