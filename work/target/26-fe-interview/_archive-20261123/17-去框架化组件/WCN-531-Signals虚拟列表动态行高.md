---
title: [WCN-531] Signals + 虚拟列表：如何实现「仅渲染视口内行」且行高动态变化的细粒度更新？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-531：Signals + 虚拟列表：如何实现「仅渲染视口内行」且行高动态变化的细粒度更新？

**答**：
- 结论：每行一个 signal（含测量高度），列表维护前缀和数组作为「位置索引」，视口变化只更新可见行。
- 动态高度：测量后更新行 signal，增量修正前缀和，不重算全部。
- 细粒度：行高变化只影响其后行的偏移，通过前缀和差分定位需要重绘的窗口。
- 追问：滚动到底部时如何避免抖动？（答：预测量缓冲区 + rAF 合帧更新前缀和）

```javascript
const rows = data.map(d => ({ h: signal(estimatedHeight), el: signal(null) }));
const prefix = signal(buildPrefix(rows));          // 前缀和
function measure(i, h) {
  rows[i].h.set(h);                                 // 只改一行
  const diff = h - prefix.get()[i + 1] + prefix.get()[i];
  prefix.set(prefix.get().map((p, k) => k > i ? p + diff : p)); // 增量修正
}
function visible(scrollTop, viewport) {
  const ps = prefix.get();
  let lo = binarySearch(ps, scrollTop), hi = binarySearch(ps, scrollTop + viewport);
  return [lo, hi];                                  // 只渲染这个区间
}
```
