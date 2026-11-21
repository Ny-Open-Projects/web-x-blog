---
title: [ALG-127] 滚动埋点既要首屏一滚就记（leading），也要用户停在最底部时补记一次（trailing）。如何实现完整版 throttle？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-127：滚动埋点既要首屏一滚就记（leading），也要用户停在最底部时补记一次（trailing）。如何实现完整版 throttle？
**答**：throttle 用"上次执行时间 + 定时器"双状态：剩余时间 <= 0 直接执行（leading）；否则若无挂起定时器且允许 trailing，就 setTimeout 在静默期末补一次。要点：trailing 执行后要重置 last，避免与下一次 leading 重复过近；`leading: false` 时把初始 last 对齐为 now，使第一次不立即触发。时间 O(1) 每次触发。

```javascript
function throttle(fn, wait, { leading = true, trailing = true } = {}) {
  let timer = null, last = leading ? 0 : Date.now(); // leading 为 false 首次不触发
  return function (...args) {
    const now = Date.now();
    const remain = wait - (now - last);
    if (remain <= 0) {
      last = now;
      if (timer) { clearTimeout(timer); timer = null; }
      fn.apply(this, args);                 // 时间窗到了：直接执行
    } else if (trailing && !timer) {
      timer = setTimeout(() => {            // 静默期末补最后一次
        timer = null;
        last = leading ? Date.now() : 0;
        fn.apply(this, args);
      }, remain);
    }
  };
}
// 滚动埋点：leading 保证进入即记，trailing 保证停在底部也被记录
```
