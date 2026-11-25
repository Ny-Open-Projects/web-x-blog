---
title: [SCN-1145] IoT 设备控制台的暗色模式与工控屏适配
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1145：IoT 设备控制台的暗色模式与工控屏适配

**答**：
- 工控屏：监控室大屏常亮——暗色模式（护眼+省电），高对比告警色。
- 适配：低分辨率工控屏（1024×768）降级布局（列裁剪）。
- 久坐：界面自动轮播（值班室自动切换视图）。

```javascript
// 工控屏适配
function industrialScreen(screen) {
  return {
    theme: 'dark',
    cols: screen.w < 1280 ? REDUCED_COLS : FULL_COLS,
    contrast: 'high',
    autoRotate: { views: ['overview', 'alarms'], intervalMs: 30_000 },
  };
}
```
