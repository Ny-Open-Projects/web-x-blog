---
title: [SCN-1202] 工业 SCADA 前端收口（实时/可靠/安全/合规）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1202：工业 SCADA 前端收口（实时/可靠/安全/合规）

**答**：
- 实时：组态绑定（1154）/新鲜度（1157）/越限预警（1173）。
- 可靠：断电恢复（1171）/长期运行（1190）/断点续传（1193）。
- 安全：IT/OT 隔离（1170）/双人复核（1159）/等保（1194）。
- 合规：批次追溯（1174）/监管报送（1186）/审计报表（1146）。

```javascript
// SCADA 检查清单
const SCADA_CHECK = [
  { id: 'fresh', test: s => s.staleTagRate < 0.01 },
  { id: 'alarm', test: s => s.alarmAckRate > 0.99 },
  { id: 'oee', test: s => s.oeeDataReady },
  { id: 'security', test: s => s.mlpsPass },
  { id: 'uptime', test: s => s.screenUptime > 0.999 },
];
function scadaAudit(signals) {
  return SCADA_CHECK.filter(c => !c.test(signals)).map(c => c.id);
}
```
