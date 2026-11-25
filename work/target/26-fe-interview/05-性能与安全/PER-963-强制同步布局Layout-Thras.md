---
title: [PER-963] 强制同步布局（Layout Thrashing）的成因与批处理修复
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-963：强制同步布局（Layout Thrashing）的成因与批处理修复

**答**：
- 成因：在同一帧里交替"读布局属性（offsetWidth/getBoundingClientRect）"与"写样式"，每次读都迫使浏览器执行尚未失效的布局，N 次循环 = N 次布局。
- 修复一：FastDom 模式——读写分离，先批量读、再批量写。
- 修复二：避免读触发属性——用缓存、IntersectionObserver、ResizeObserver 替代每帧读取。
- 追问点：为什么 rAF 里读写交替仍会抖动——rAF 回调后浏览器布局还没执行，读操作会同步触发。

```javascript
// 批处理读写：防布局抖动
function layoutThashingFix(items) {
  const reads = items.map(el => el.getBoundingClientRect().top);  // 批量读
  items.forEach((el, i) => {                                     // 批量写
    el.style.transform = `translateY(${reads[i]}px)`;
  });
}
// 反模式对照：
// items.forEach(el => { const t = el.getBoundingClientRect().top;
//   el.style.transform = `translateY(${t}px)`; });  // 每轮一次强制布局
// 验证：DevTools Performance 中 Layout 出现 N 次连续紫块即中招
```
