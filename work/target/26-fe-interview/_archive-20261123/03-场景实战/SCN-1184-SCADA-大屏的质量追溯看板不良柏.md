---
title: [SCN-1184] SCADA 大屏的质量追溯看板（不良柏拉图）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1184：SCADA 大屏的质量追溯看板（不良柏拉图）

**答**：
- 柏拉图：不良类型分布（帕累托排序 + 累计占比线），Top3 不良专项。
- 下钻：不良类型 → 班次/设备/原料批次下钻。
- 改善：改善措施跟踪（措施上线后不良率变化对比）。

```javascript
// 不良柏拉图
function defectPareto(defects) {
  const counts = {};
  defects.forEach(d => counts[d.type] = (counts[d.type] ?? 0) + 1);
  const sorted = Object.entries(counts).sort((a, b) => b[1] - a[1]);
  const total = defects.length;
  let acc = 0;
  return sorted.map(([type, c]) => {
    acc += c;
    return { type, count: c, pct: +(c / total * 100).toFixed(1) + '%',
      cumPct: +(acc / total * 100).toFixed(1) + '%' };
  });
}
```
