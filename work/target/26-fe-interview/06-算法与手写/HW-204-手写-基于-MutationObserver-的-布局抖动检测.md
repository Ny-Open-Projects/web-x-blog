---
title: [HW-204] 手写布局抖动运行时检测——MutationObserver 标记写 + 布局读取 API patch 检测交错
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-204：手写布局抖动运行时检测——MutationObserver 标记写 + 布局读取 API patch 检测交错
**答**：PER-404 运行时检测的完整实现：MutationObserver 检测 style/class 写（标记本帧"有写"）→ patch 布局读取 API（offsetWidth 系/getBoundingClientRect/getComputedStyle）——帧内有写又读 = 抖动嫌疑（输出调用栈）→ rAF 每帧重置。

```javascript
if (import.meta.env.DEV) {
  let wroteThisFrame = false;
  // 1. 写检测：style 属性变更
  new MutationObserver(() => { wroteThisFrame = true; })
    .observe(document.documentElement, { attributes: true, subtree: true, attributeFilter: ['style', 'class'] });
  // 2. 读检测：patch 布局读取
  const reads = ['offsetWidth', 'offsetHeight', 'offsetTop', 'offsetLeft', 'clientWidth', 'scrollWidth'];
  for (const prop of reads) {
    const desc = Object.getOwnPropertyDescriptor(HTMLElement.prototype, prop);
    Object.defineProperty(HTMLElement.prototype, prop, {
      get() {
        if (wroteThisFrame) {
          console.warn('[layout-thrashing] 本帧已有 DOM 写操作，此次布局读取将强制同步布局', new Error().stack?.split('\n').slice(1, 4).join('\n'));
          window.__thrashCount = (window.__thrashCount ?? 0) + 1;
        }
        return desc.get.call(this);
      },
      configurable: true,                                 // 可恢复（生产构建自动剥离）
    });
  }
  // 3. 帧重置 + 计数上报
  requestAnimationFrame(function reset() {
    if (window.__thrashCount > 10) report?.({ type: 'layout-thrashing', count: window.__thrashCount });
    window.__thrashCount = 0; wroteThisFrame = false;
    requestAnimationFrame(reset);
  });
}
// 仅 DEV 运行（patch 有开销）；report 阈值 10 次（单次误报不告警）
// 输出调用栈前 3 帧（定位交错代码点）；修复后 thrashCount 归零
```

**评分点**：
- MutationObserver 写标记 + patch 读取的双侧检测——本题核心。
- 帧重置（rAF 每帧清零）与阈值上报（>10 次防误报）。
- 调用栈定位（交错点）。
- DEV-only 与 configurable 恢复的工程纪律。
