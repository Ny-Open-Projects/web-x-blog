---
title: [JS-070] 如何手写节流 throttle？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-070：如何手写节流 throttle？

**答**：
- 核心思路：一段时间内只执行一次，时间戳版首沿触发、定时器版尾沿触发。
- 完整实现两者结合：首次立即执行 + 停止触发后再补一次。
- 典型场景：scroll 监听、按钮防重复点击、拖拽位置同步。
- 与防抖的区别：防抖“等停止”，节流“控频率”。

```javascript
function throttle(fn, interval = 200) {
  let last = 0;
  let timer = null;
  return function (...args) {
    const now = Date.now();
    const remaining = interval - (now - last);
    if (remaining <= 0) {
      clearTimeout(timer);
      timer = null;
      last = now;
      fn.apply(this, args);           // 时间戳命中：立即执行
    } else if (!timer) {
      timer = setTimeout(() => {      // 尾沿兜底：最后一次也执行
        last = Date.now();
        timer = null;
        fn.apply(this, args);
      }, remaining);
    }
  };
}

window.addEventListener('scroll', throttle(() => {
  console.log('scroll pos:', window.scrollY);
}, 300)); // 滚动期间最多每 300ms 输出一次，停止后补一次
```
