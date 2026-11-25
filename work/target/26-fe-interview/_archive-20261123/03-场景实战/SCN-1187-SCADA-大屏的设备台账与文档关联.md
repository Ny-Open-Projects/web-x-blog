---
title: [SCN-1187] SCADA 大屏的设备台账与文档关联
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1187：SCADA 大屏的设备台账与文档关联

**答**：
- 台账：设备台账（型号/参数/图纸/手册）关联展示，故障时一键查看手册。
- 搜索：台账搜索（设备名/位号/图纸编号）。
- 版本：图纸/手册版本管理（旧版归档标注）。

```javascript
// 设备台账
function deviceLedger(device) {
  return {
    specs: device.specs, drawings: device.drawings,
    manual: device.manualUrl,
    search: (kw) => searchLedger(kw),
    drawingVersion: device.drawVersion,                // 图纸版本
    note: '旧版图纸归档可查',
  };
}
function searchLedger(kw) { return []; }
```
