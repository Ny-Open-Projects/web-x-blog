---
title: [DP-312] 笔试题：手写 Table 合计行与列冻结计算？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-312：笔试题：手写 Table 合计行与列冻结计算？
**答**：实现 Table 冻结列布局计算：1) freeze: 'left'|'right' 列偏移计算（含 sticky offset 累加）；2) 合计行聚合（sum/avg/custom，跳过非数值）；3) 列宽总和与滚动宽度；4) 冻结列阴影条件（存在横向溢出时）。
**评分点**：
- sticky 偏移累加正确（冻结列 offset = 前序冻结列宽和）。
- 聚合器策略接口（sum/avg/custom）。
- 阴影判定（scrollLeft > 0 左侧 / 不足右侧）。
- 数值聚合对 null/NaN 的处理。
```javascript
function layout(columns, data) {
  const widths = columns.map(c => c.width ?? 120);
  const total = widths.reduce((a, b) => a + b, 0);
  let leftOffset = 0;
  const cells = columns.map((c, i) => {
    const cell = { ...c, width: widths[i], sticky: c.freeze ? c.freeze : undefined,
      offset: c.freeze === 'left' ? leftOffset : undefined };
    if (c.freeze === 'left') { cell.offset = leftOffset; leftOffset += widths[i]; }   // 1) 累加
    return cell;
  });
  let rightOffset = 0;
  for (let i = columns.length - 1; i >= 0; i--) {
    if (columns[i].freeze === 'right') { cells[i].offset = rightOffset; rightOffset += widths[i]; }
  }
  const summary = columns.map(c => {                       // 2) 合计
    if (!c.summary) return '';
    const nums = data.map(r => r[c.key]).filter(v => typeof v === 'number' && !Number.isNaN(v));
    if (!nums.length) return '';
    if (c.summary === 'sum') return nums.reduce((a, b) => a + b, 0);
    if (c.summary === 'avg') return nums.reduce((a, b) => a + b, 0) / nums.length;
    return c.summary(nums, data);                          // custom
  });
  return { cells, total, summary, needsScroll: total > containerWidth,   // 3)
    shadowLeft: needsScroll, shadowRight: needsScroll };   // 4)
}
```
