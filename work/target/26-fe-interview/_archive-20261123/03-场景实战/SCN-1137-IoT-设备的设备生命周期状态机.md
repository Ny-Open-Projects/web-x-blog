---
title: [SCN-1137] IoT 设备的设备生命周期状态机
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1137：IoT 设备的设备生命周期状态机

**答**：
- 状态：未激活→在线→离线→停用→报废；各状态允许操作不同（报废前数据归档）。
- 前端：状态时间轴 + 状态转换操作按钮（按状态显隐）。
- 回收：报废设备数据保留期（合规）后清除。

```javascript
// 设备生命周期
const DEVICE_FSM = {
  inactive: ['activate'],
  online: ['deactivate', 'scrap'],
  offline: ['activate', 'scrap'],
  scrapped: [],
};
function deviceActions(device) {
  const ops = DEVICE_FSM[device.state] ?? [];
  return {
    ops,
    archiveBeforeScrap: device.state !== 'inactive',
    dataRetention: device.state === 'scrapped' ? '合规保留期后清除' : null,
  };
}
```
