---
title: [HW-115] 手写防抖的边界大全：leading/trailing/cancel/flush/最大等待与异步防抖
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-115：手写防抖的边界大全：leading/trailing/cancel/flush/最大等待与异步防抖
**答**：在 HW-014 基础上补全工程级防抖的六个能力：leading 首次立即执行、trailing 结束后执行、cancel 取消、flush 立即结算、maxWait 最长等待（防长时间连续触发饿死）、异步函数版（等待 promise 完成才允许下一次）。

```javascript
function debounce(fn, wait, { leading = false, trailing = true, maxWait } = {}) {
  let timer = null, lastCall = 0, first = true;
  function invoke(args, thisArg) {
    lastCall = Date.now();
    return fn.apply(thisArg, args);
  }
  function debounced(...args) {
    const now = Date.now();
    const shouldLead = leading && first;
    if (shouldLead) { first = false; invoke(args, this); }
    clearTimeout(timer);
    const sinceFirst = now - (firstInvokeAt ??= now);
    // maxWait：连续触发超过 maxWait 强制结算一次（防饿死）
    const remaining = maxWait != null ? Math.max(0, maxWait - sinceFirst) : wait;
    timer = setTimeout(() => {
      if (trailing) invoke(args, this);
      first = true; firstInvokeAt = undefined;
    }, remaining);
  }
  debounced.cancel = () => { clearTimeout(timer); first = true; firstInvokeAt = undefined; };
  debounced.flush = function (...args) {          // 立即结算（不等 wait）
    this.cancel();
    return invoke(args, this);
  };
  return debounced;
}
// 异步版：前一次 promise 未完成则忽略/排队
function debounceAsync(fn, wait, { mode = 'drop' } = {}) {   // drop | queue
  let timer = null, running = false, queued = null;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(async () => {
      if (running) { if (mode === 'queue') queued = args; return; }
      running = true;
      try { await fn.apply(this, args); }
      finally {
        running = false;
        if (queued) { const q = queued; queued = null; fn.apply(this, q); }
      }
    }, wait);
  };
}
// 用法：输入联想防抖 + maxWait 2s（持续输入每 2s 至少搜一次）+ 组件卸载 cancel
```

**评分点**：
- 六能力齐备：leading/trailing/cancel/flush/maxWait/异步模式。
- maxWait 饿死防护的语义与实现（连续输入每 maxWait 至少执行一次）。
- 异步版 drop/queue 两种模式的差异说清。
- flush 立即结算并重置状态；cancel 后状态复位。
