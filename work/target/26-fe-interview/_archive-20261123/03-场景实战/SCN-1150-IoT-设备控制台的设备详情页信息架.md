---
title: [SCN-1150] IoT 设备控制台的设备详情页信息架构
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1150：IoT 设备控制台的设备详情页信息架构

**答**：
- 信息架构：概览（状态/遥测最新值）→ 遥测曲线 → 告警历史 → 指令历史 → 配置/固件。
- 懒加载：Tab 懒加载（切换才拉数据），详情页首屏只拉概览。
- 一致：各 Tab 数据时间范围统一（全局时间选择器）。

```javascript
// 详情页信息架构
function deviceDetail(deviceId) {
  return {
    tabs: ['overview', 'telemetry', 'alarms', 'commands', 'config'],
    lazy: true,                                        // Tab 懒加载
    globalTime: { default: '1h', syncAcrossTabs: true },
    load: (tab, range) => api(`/device/${deviceId}/${tab}`, { range }),
  };
}
```
