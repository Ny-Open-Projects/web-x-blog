---
title: [SCN-1103] IoT 设备控制台的整体架构（设备/边缘/云/前端）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1103：IoT 设备控制台的整体架构（设备/边缘/云/前端）

**答**：
- 链路：设备（MQTT 上报）→ 边缘网关 → 云平台（规则引擎/存储）→ 前端（WebSocket 订阅实时状态）。
- 前端职责：设备列表/详情/控制指令下发/告警查看——实时性靠 WS 订阅设备影子（Device Shadow）。
- 规模：万级设备列表虚拟滚动 + 状态聚合（在线/离线/告警计数）。

```javascript
// 设备影子订阅
function deviceShadow(ws, deviceIds) {
  ws.send(JSON.stringify({ action: 'subscribe',
    topics: deviceIds.map(id => `shadow/${id}`) }));
  ws.onmessage = e => {
    const { topic, state } = JSON.parse(e.data);
    updateDeviceState(topic.split('/')[1], state);     // desired vs reported
  };
}
// shadow: { reported: { temp: 26 }, desired: { temp: 22 }, delta: { temp: 22 } }
```
