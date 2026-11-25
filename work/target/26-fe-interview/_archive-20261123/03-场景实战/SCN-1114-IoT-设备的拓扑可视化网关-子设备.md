---
title: [SCN-1114] IoT 设备的拓扑可视化（网关-子设备层级）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1114：IoT 设备的拓扑可视化（网关-子设备层级）

**答**：
- 拓扑：网关→子设备树形展示（子设备经网关接入），离线传播（网关离线子设备全离线标注）。
- 交互：节点点击进入详情，网关重启影响范围预览。
- 渲染：节点 < 200 SVG 树，大拓扑 Canvas。

```javascript
// 设备拓扑
function deviceTopology(gateways, devices) {
  return gateways.map(gw => ({
    gateway: gw.id, online: gw.online,
    children: devices.filter(d => d.gatewayId === gw.id).map(d => ({
      id: d.id, status: gw.online ? d.status : 'offline-by-gateway',
    })),
    impact: gw.online ? 0 : devices.filter(d => d.gatewayId === gw.id).length,
  }));
}
```
