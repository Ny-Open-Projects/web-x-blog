---
title: [SCN-1127] IoT 设备控制台的数据大屏（设备总览）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1127：IoT 设备控制台的数据大屏（设备总览）

**答**：
- 总览：设备总数/在线率/告警数/指令成功率——四象限大屏布局。
- 下钻：点击指标下钻设备列表（过滤条件预置）。
- 轮播：多园区轮播（每 30s 切换）。

```javascript
// 总览大屏
function deviceOverview(parks) {
  const cur = parks[0];
  return {
    park: cur.name,
    total: cur.devices, onlineRate: +(cur.online / cur.devices * 100).toFixed(1) + '%',
    alerts: cur.alerts, cmdSuccess: +(cur.cmdAck / cur.cmdSent * 100).toFixed(1) + '%',
    drill: (kpi) => filterDevices({ park: cur.id, kpi }),
    rotate: () => shiftPark(parks),                    // 30s 轮播
  };
}
function shiftPark(parks) { parks.push(parks.shift()); }
```
