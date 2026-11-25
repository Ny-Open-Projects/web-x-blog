---
title: [SCN-1161] SCADA 大屏的设备状态总览（机台状态墙）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1161：SCADA 大屏的设备状态总览（机台状态墙）

**答**：
- 状态墙：机台矩阵（运行/待机/故障/保养），点击进机台详情。
- 颜色标准：绿运行/黄待机/红故障/蓝保养（行业标准色）。
- 点击：机台详情（当前订单/速度/报警）弹出层。

```javascript
// 机台状态墙
function machineWall(machines) {
  const COLOR = { running: 'green', idle: 'yellow', fault: 'red', maint: 'blue' };
  return machines.map(m => ({
    id: m.id, color: COLOR[m.state],
    extra: m.state === 'fault' ? m.faultCode : m.orderNo,
    detail: () => api(`/machine/${m.id}/detail`),
  }));
}
```
