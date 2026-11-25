---
title: [SCN-1153] 工业 SCADA 大屏的整体架构（PLC 数据到前端呈现）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1153：工业 SCADA 大屏的整体架构（PLC 数据到前端呈现）

**答**：
- 链路：PLC/传感器 → OPC UA/MQTT 采集 → 时序库（TDengine/InfluxDB）→ 后端聚合 → 前端（WS 推送）。
- 前端职责：工艺流程图（组态图）+ 实时数据绑定 + 报警窗口 + 趋势曲线。
- 要求：数据新鲜度（< 2s）、界面 7×24 不间断（内存稳定）。

```javascript
// 组态数据绑定
function scadaBinding(tagId, element) {
  return wsSubscribe(`tag/${tagId}`, (v, q) => {      // q: 质量戳
    element.text = formatValue(v, element.unit);
    element.quality = q;                               // good/uncertain/bad
    if (q === 'bad') element.stale = true;             // 数据质量差标灰
  });
}
```
