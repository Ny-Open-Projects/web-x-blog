---
title: [SCN-1122] IoT 设备的告警风暴抑制（大面积断网场景）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1122：IoT 设备的告警风暴抑制（大面积断网场景）

**答**：
- 场景：园区断电→千台设备同时离线告警——风暴抑制（聚合为一条"区域离线"事件）。
- 实现：按空间/网关聚合离线告警（根因是网关/电源），恢复后自动解除。
- 值班：风暴期间只推根因告警（网关级），设备级静默。

```javascript
// 风暴抑制
function alarmStormSuppress(alarms, gateways) {
  const offline = alarms.filter(a => a.type === 'offline');
  const byGw = groupBy(offline, a => a.gatewayId);
  return Object.entries(byGw).map(([gwId, list]) => ({
    root: gateways.find(g => g.id === gwId)?.offline ? 'gateway-offline' : 'device',
    count: list.length,
    notify: gateways.find(g => g.id === gwId)?.offline
      ? { text: `网关 ${gwId} 离线，影响 ${list.length} 台设备` }
      : list.map(a => a.deviceId),
  }));
}
function groupBy(arr, fn) { const m = {}; arr.forEach(x => { const k = fn(x); (m[k] ??= []).push(x); }); return m; }
```
