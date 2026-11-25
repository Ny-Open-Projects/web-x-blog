---
title: [SCN-1175] SCADA 大屏的备件库存联动（故障时备件查询）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1175：SCADA 大屏的备件库存联动（故障时备件查询）

**答**：
- 联动：设备故障 → 备件库存查询（有货/缺货/在途），缺货采购预警。
- 展示：故障详情页嵌入备件信息（库位/数量/领用）。
- 效率：维修等待时间统计（备件缺货导致的停机时长）。

```javascript
// 备件联动
async function sparePartCheck(fault) {
  const part = fault.sparePart;
  const stock = await api('/spare', { sku: part.sku });
  return {
    inStock: stock.qty > 0, location: stock.location,
    eta: stock.qty === 0 ? stock.leadTimeDays + ' 天采购' : null,
    downtimeCost: stock.qty === 0 ? fault.stopLossPerHour * stock.leadTimeDays * 24 : 0,
  };
}
```
