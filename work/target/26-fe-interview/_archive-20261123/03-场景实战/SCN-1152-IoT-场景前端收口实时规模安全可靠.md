---
title: [SCN-1152] IoT 场景前端收口（实时/规模/安全/可靠）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1152：IoT 场景前端收口（实时/规模/安全/可靠）

**答**：
- 实时：影子订阅（1103）/遥测曲线（1107）/风暴抑制（1122）。
- 规模：万级列表（1104）/聚合地图（1119）/表格优化（1141）。
- 安全：证书（1113）/权限（1116）/幂等（1121）。
- 可靠：断线重连（1138）/边缘自治（1111）/OTA 回滚（1133）。

```javascript
// IoT 场景检查清单
const IOT_CHECK = [
  { id: 'shadow', test: s => s.shadowSyncRate > 0.99 },
  { id: 'ota', test: s => s.otaFailRate < 0.05 },
  { id: 'cert', test: s => s.certExpiring === 0 },
  { id: 'storm', test: s => s.alarmStormSuppressed },
  { id: 'latency', test: s => s.cmdAckP75 < 3000 },
];
function iotAudit(signals) {
  return IOT_CHECK.filter(c => !c.test(signals)).map(c => c.id);
}
```
