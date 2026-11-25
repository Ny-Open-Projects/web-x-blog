---
title: [SCN-1104] IoT 设备列表的状态实时刷新（万级设备）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1104：IoT 设备列表的状态实时刷新（万级设备）

**答**：
- 策略：列表页只订阅"状态变化"事件（不做全量刷新），状态变更 patch 更新行。
- 聚合：头部计数（在线 x/离线 y/告警 z）由服务端聚合推送。
- 筛选：状态/类型/分组筛选条件下推（服务端过滤）。

```javascript
// 状态 patch 更新
function deviceListWS(ws) {
  ws.on('device-state', ({ id, status, lastSeen }) => {
    const row = virtualList.find(id);
    if (row) patchRow(row, { status, lastSeen });      // 只更新行
    counters[id === 'alert' ? 'alert' : status]++;
  });
}
// 计数由服务端聚合推送，前端不做全表扫描
```
