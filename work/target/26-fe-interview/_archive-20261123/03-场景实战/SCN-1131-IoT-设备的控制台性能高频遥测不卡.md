---
title: [SCN-1131] IoT 设备的控制台性能（高频遥测不卡界面）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1131：IoT 设备的控制台性能（高频遥测不卡界面）

**答**：
- 问题：百台设备 1s 遥测——图表/列表高频更新卡界面。
- 方案：更新节流（图表 1s 合帧、列表 patch）、数据聚合后渲染（不逐点）、离屏不更新。
- 度量：控制台帧率与内存（长时间运行无泄漏）。

```javascript
// 高频更新节流
class ThrottledUpdater {
  constructor(interval = 1000) { this.interval = interval; this.pending = null; }
  update(fn, data) {
    this.pending = data;
    if (this.timer) return;
    this.timer = setTimeout(() => {
      fn(this.pending); this.pending = null;
      this.timer = null;
    }, this.interval);
  }
}
```
