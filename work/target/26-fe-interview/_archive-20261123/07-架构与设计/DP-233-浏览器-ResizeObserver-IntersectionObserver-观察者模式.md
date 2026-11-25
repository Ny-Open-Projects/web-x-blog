---
title: [DP-233] 源码识别：浏览器 Observer 三兄弟的观察者模式？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-233：源码识别：浏览器 Observer 三兄弟的观察者模式？
**答**：
- 观察者模式的标准实现：MutationObserver/ResizeObserver/IntersectionObserver/PerformanceObserver 全是"注册回调 → 浏览器事件源通知"——Subject 是浏览器内部（渲染管线/合成器），比手写 pub-sub 多了**批处理**（微任务合并回调）。
- 观察粒度策略：observe(target, options) 的 options（attributes/childList/rootMargin/threshold）是订阅过滤策略。
- 解绑纪律：disconnect + takeRecords——观察者泄漏检测（无断开的 observer 引用目标即内存泄漏）。
- 识别要点：能说清 IO 的通知时机（渲染后异步，非同步）与 RO 的循环防护（resize 回调里再改尺寸 → 同帧合并/跳过）。

```javascript
// 观察者批处理：回调在同一微任务里拿到所有变更
const mo = new MutationObserver(mutations => {     // 被通知方
  for (const m of mutations) { /* type: 'attributes'|'childList' */ }
});
mo.observe(document.body, { attributes: true, childList: true, subtree: true });
// IntersectionObserver 的 threshold 策略：
const io = new IntersectionObserver(entries => {
  entries.forEach(e => e.isIntersecting && lazyLoad(e.target));
}, { threshold: [0, 0.5, 1], rootMargin: '100px' });   // 订阅过滤策略
io.observe(img);
// 循环防护：RO 回调里设置 width 又触发 resize → 浏览器同帧去重；自己改尺寸要判断来源
```
