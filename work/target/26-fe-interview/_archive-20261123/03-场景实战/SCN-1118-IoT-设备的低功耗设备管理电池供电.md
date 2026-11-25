---
title: [SCN-1118] IoT 设备的低功耗设备管理（电池供电传感器）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1118：IoT 设备的低功耗设备管理（电池供电传感器）

**答**：
- 特性：电池设备低频上报（1h 级）——在线判定阈值放宽（24h 内上报即在线）。
- 电量：电池电量上报曲线，低电量（< 20%）告警换电池。
- 策略：数据缓冲（设备本地缓存多次数据一次上报）。

```javascript
// 低功耗设备
function lowPowerDevice(device) {
  return {
    onlineDef: device.lastSeen > Date.now() - 24 * 3600_000,   // 24h 内算在线
    battery: device.batteryPct,
    alert: device.batteryPct < 20 ? 'low-battery' : null,
    buffer: device.bufferedRecords,                    // 本地缓存条数
  };
}
```
