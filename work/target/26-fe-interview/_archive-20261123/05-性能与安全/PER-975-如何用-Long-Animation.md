---
title: [PER-975] 如何用 Long Animation Frames API（LoAF）归因 INP
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-975：如何用 Long Animation Frames API（LoAF）归因 INP

**答**：
- INP 只给数值不给原因；LoAF（PerformanceObserver long-animation-frame）提供慢帧明细：脚本来源、样式/layout 耗时、强制布局次数。
- 分析路径：找 INP 交互对应帧 → LoAF 的 scripts 数组定位慢脚本（URL+函数）→ 切片或移出主线程。
- 结合第三方案：LoAF + 交互 trace 组合上报，平台侧聚合出"慢交互 Top 场景"。
- 注意采样：LoAF 全开开销可控但量大，按 5%~10% 采样慢帧即可。

```javascript
new PerformanceObserver(list => {
  for (const frame of list.getEntries()) {
    if (frame.duration < 50) continue;
    report({
      dur: frame.duration,
      render: frame.renderStart, style: frame.styleDuration,
      forced: frame.forcedStyleAndLayoutDuration,      // 强制布局时间
      scripts: frame.scripts.map(s => ({
        src: s.sourceURL, fn: s.sourceFunctionName, dur: s.duration })),
    });
  }
}).observe({ type: 'long-animation-frame', buffered: true });
// 归因：forced 大 -> 布局抖动；scripts 集中在单文件 -> 拆任务
```
