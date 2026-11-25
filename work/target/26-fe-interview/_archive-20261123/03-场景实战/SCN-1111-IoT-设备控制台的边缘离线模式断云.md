---
title: [SCN-1111] IoT 设备控制台的边缘离线模式（断云自治）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1111：IoT 设备控制台的边缘离线模式（断云自治）

**答**：
- 场景：云断连时边缘网关自治（本地规则继续执行），恢复后状态补同步。
- 前端：边缘状态标识（自治中/云端同步），离线期间数据缓存标记（延迟数据）。
- 一致性：恢复后影子对账（本地状态 vs 云端差异合并）。

```javascript
// 边缘自治标识
function edgeStatus(edge) {
  return {
    mode: edge.cloudConnected ? 'cloud' : 'autonomous',
    note: edge.cloudConnected ? null : '云端断连，边缘规则自治中',
    buffered: edge.bufferedOps,                        // 待补同步操作数
    reconcile: () => api('/edge/reconcile', { id: edge.id }),
  };
}
```
