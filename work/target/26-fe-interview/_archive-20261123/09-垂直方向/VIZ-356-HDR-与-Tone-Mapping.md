---
title: [VIZ-356] HDR 与 Tone Mapping：为什么超过 1.0 的颜色要压缩
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## VIZ-356：HDR 与 Tone Mapping：为什么超过 1.0 的颜色要压缩

**答**：
- 光照累加可以超 1.0（HDR），显示设备只有 [0,1]——Tone Mapping 压缩动态范围同时保对比。
- 常用曲线：Reinhard（x/(1+x) 简单压平）、ACES（电影感，暗部/高光滚降）。
- 顺序：HDR 渲染 → tone map → gamma 校正；顺序错则对比度崩坏。

```javascript
// Tone mapping
function aces(x) {
  const a = 2.51, b = 0.03, c = 2.43, d = 0.59, e = 0.14;
  return Math.min(1, Math.max(0,
    (x * (a * x + b)) / (x * (c * x + d) + e)));
}
function reinhard(x) { return x / (1 + x); }
// 验证：HDR 值 2.5
console.log(aces(2.5).toFixed(3), reinhard(2.5).toFixed(3));
// aces 保高光层次，reinhard 压平——引擎默认选 ACES
```
