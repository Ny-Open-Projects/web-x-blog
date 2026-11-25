---
title: [SCN-1174] SCADA 大屏的批次质量追溯（正反向追溯）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1174：SCADA 大屏的批次质量追溯（正反向追溯）

**答**：
- 追溯：批次 → 原料供应商/设备/工艺参数/操作员（正向：产品到原料；反向：原料到产品）。
- 展示：追溯链路图（批次关系树），召回范围圈定（受影响批次）。
- 性能：追溯查询走图数据库（服务端），前端展示关系树。

```javascript
// 批次追溯
async function batchTrace(batchNo, direction) {
  const r = await api('/trace', { batchNo, direction });   // forward/backward
  return {
    tree: r.tree,                                      // 批次关系树
    affected: direction === 'backward' ? r.batches : null,   // 召回范围
    params: r.processParams,                           // 工艺参数
    export: () => exportTraceReport(r),
  };
}
```
