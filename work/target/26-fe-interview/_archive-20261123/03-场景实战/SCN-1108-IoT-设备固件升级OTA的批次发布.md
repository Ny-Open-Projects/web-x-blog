---
title: [SCN-1108] IoT 设备固件升级（OTA）的批次发布与进度
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1108：IoT 设备固件升级（OTA）的批次发布与进度

**答**：
- 发布：固件灰度批次（1%→10%→50%→100%），失败率超标自动暂停批次。
- 前端：批次进度（升级中/成功/失败设备数）、失败原因分布（下载失败/校验失败/升级崩溃）。
- 安全：固件签名校验（设备端），升级窗口（低峰时段执行）。

```javascript
// OTA 批次
function otaBatch(firmware, batches) {
  return batches.map(b => ({
    pct: b.pct, devices: b.count,
    failRate: +(b.failed / b.count * 100).toFixed(1) + '%',
    pause: b.failed / b.count > 0.05,                  // 失败率超 5% 暂停
    window: '02:00-05:00',                             // 升级窗口
  }));
}
// 暂停批次：otaPause(batchId) -> 未升级设备停止拉取
```
