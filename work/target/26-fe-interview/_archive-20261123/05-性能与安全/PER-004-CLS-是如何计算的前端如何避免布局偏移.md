---
title: [PER-004] CLS 是如何计算的？前端如何避免布局偏移？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-004：CLS 是如何计算的？前端如何避免布局偏移？

**答**：
- 单次偏移分数 = 影响面积比例（impact fraction）× 距离比例（distance fraction），CLS 是所有非用户输入导致的偏移分数**累加**。
- `hadRecentInput` 为 true 的偏移（用户点击后 500ms 内）不计入 CLS。
- 常见诱因：图片/视频不设宽高、动态插入横幅、字体闪替（FOUT）、广告位未占位。
- 修复手段：所有媒体写死 `width/height` 或 `aspect-ratio`、预留广告位尺寸、`font-display: swap` + 尺寸接近的 fallback 字体。

```javascript
let cls = 0;
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    // hadRecentInput 为 true 表示刚发生用户输入，该次偏移不计入 CLS
    if (!entry.hadRecentInput) {
      cls += entry.value;
    }
  }
  console.log('当前 CLS', cls.toFixed(3)); // 良好小于 0.1
}).observe({ type: 'layout-shift', buffered: true });
```
