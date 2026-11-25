---
title: [MFW-836] 笔试：手写 revalidate 去抖合并器（tag 维度 trailing debounce）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-836：笔试：手写 revalidate 去抖合并器（tag 维度 trailing debounce）

**答**：
- 结论：同一 tag 在时间窗口内的多次调用只触发一次真实失效（trailing debounce），按 tag 隔离互不影响。
- 关键：每次调用刷新计时；窗口结束清理定时器，避免内存泄漏。
- 追问钩子：窗口大小与业务陈旧度如何权衡？——越短越新鲜但回源越多；强时效场景应关闭去抖。

```javascript
function createDebouncedRevalidate(fn, windowMs = 300) {
  const timers = new Map();
  return function revalidate(tag) {
    if (timers.has(tag)) clearTimeout(timers.get(tag)); // 刷新计时
    const t = setTimeout(() => {
      timers.delete(tag);                               // 清理，防泄漏
      fn(tag);
    }, windowMs);
    timers.set(tag, t);
  };
}

// 自测：同 tag 三次 → 一次；不同 tag 各自一次
const calls = [];
const r = createDebouncedRevalidate(t => calls.push(t), 50);
r('stock'); r('stock'); r('stock');
r('price');
setTimeout(() => console.log(calls.sort().join(',')), 90); // price,stock
```

**评分点**：
- 同 tag 在窗口内合并为一次（trailing debounce 语义正确）
- 按 tag 隔离定时器，不同 tag 互不影响
- 窗口触发后从 Map 删除定时器，避免内存泄漏
- 能讨论窗口大小与业务陈旧度容忍的权衡（加分）
