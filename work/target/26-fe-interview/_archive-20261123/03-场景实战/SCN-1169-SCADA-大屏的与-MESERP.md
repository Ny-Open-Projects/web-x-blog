---
title: [SCN-1169] SCADA 大屏的与 MES/ERP 的数据一致性
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1169：SCADA 大屏的与 MES/ERP 的数据一致性

**答**：
- 一致性：SCADA 产量 vs MES 报工 vs ERP 结算数据一致性校验（口径差异标注）。
- 差异：差异清单（超 1% 生成核对任务）。
- 时区：班次定义统一（跨系统班次口径一致）。

```javascript
// 系统对账
function crossSystemCheck(scada, mes, erp) {
  const diff = { 'scada-mes': scada.output - mes.reported,
    'mes-erp': mes.reported - erp.settled };
  return { diff,
    task: Object.entries(diff).some(([, d]) => Math.abs(d) > scada.output * 0.01)
      ? { action: '生成核对任务', fields: Object.keys(diff) } : null,
    note: '班次口径需一致（班次定义表共享）' };
}
```
